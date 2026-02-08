#!/usr/bin/env python3
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from ledger_schemas import TaskLedger, ProgressLedger, TaskEntry, ProgressStep, Checkpoint

LEDGER_DIR = Path(__file__).parent
TASK_LEDGER_PATH = LEDGER_DIR / "task_ledger.json"
PROGRESS_LEDGER_PATH = LEDGER_DIR / "progress_ledger.json"

def load_json(path):
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)

def init_ledgers(mission_id, description, goals):
    task_ledger = TaskLedger(
        mission_id=mission_id,
        mission_description=description,
        goals=goals,
        tasks=[]
    )
    progress_ledger = ProgressLedger(
        mission_id=mission_id,
        steps=[]
    )
    save_json(TASK_LEDGER_PATH, task_ledger.model_dump())
    save_json(PROGRESS_LEDGER_PATH, progress_ledger.model_dump())
    print(f"✅ Initialized ledgers for mission: {mission_id}")

def add_task(task_id, description, priority="P2", dependencies=None):
    data = load_json(TASK_LEDGER_PATH)
    if not data:
        print("❌ Task ledger not initialized.")
        return
    ledger = TaskLedger(**data)
    task = TaskEntry(
        id=task_id,
        description=description,
        priority=priority,
        dependencies=dependencies or []
    )
    ledger.tasks.append(task)
    save_json(TASK_LEDGER_PATH, ledger.model_dump())
    print(f"✅ Added task: {task_id}")

def add_step(task_id, action, outcome, status="success"):
    # Update progress
    p_data = load_json(PROGRESS_LEDGER_PATH)
    if not p_data:
        print("❌ Progress ledger not initialized.")
        return
    p_ledger = ProgressLedger(**p_data)
    step = ProgressStep(
        index=len(p_ledger.steps),
        task_id=task_id,
        action=action,
        outcome=outcome,
        status=status
    )
    p_ledger.steps.append(step)
    p_ledger.current_step_index = step.index
    save_json(PROGRESS_LEDGER_PATH, p_ledger.model_dump())
    
    # Also update task status in task ledger if completed
    if status == "success" and "completed" in outcome.lower():
        update_task_status(task_id, "completed")
    
    print(f"✅ Recorded step for task: {task_id}")

def update_task_status(task_id, status):
    data = load_json(TASK_LEDGER_PATH)
    if not data:
        return
    ledger = TaskLedger(**data)
    for task in ledger.tasks:
        if task.id == task_id:
            task.status = status
            task.updated_at = datetime.utcnow()
            break
    save_json(TASK_LEDGER_PATH, ledger.model_dump())

def complete_task(task_id):
    update_task_status(task_id, "completed")
    print(f"✅ Task marked as completed: {task_id}")

def create_checkpoint(reason="manual"):
    t_data = load_json(TASK_LEDGER_PATH)
    p_data = load_json(PROGRESS_LEDGER_PATH)
    if not t_data or not p_data:
        print("❌ Ledgers not initialized.")
        return
    
    t_ledger = TaskLedger(**t_data)
    p_ledger = ProgressLedger(**p_data)
    
    checkpoint_id = f"cp_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
    checkpoint = Checkpoint(
        checkpoint_id=checkpoint_id,
        task_ledger=t_ledger,
        progress_ledger=p_ledger,
        reason=reason
    )
    
    cp_path = LEDGER_DIR / f"checkpoints/{checkpoint_id}.json"
    cp_path.parent.mkdir(exist_ok=True)
    save_json(cp_path, checkpoint.model_dump())
    print(f"✅ Created checkpoint: {checkpoint_id}")

def resume_mission():
    t_data = load_json(TASK_LEDGER_PATH)
    p_data = load_json(PROGRESS_LEDGER_PATH)
    if not t_data or not p_data:
        print("❌ Ledgers not initialized.")
        return
    
    t_ledger = TaskLedger(**t_data)
    p_ledger = ProgressLedger(**p_data)
    
    print(f"🔄 Resuming Mission: {t_ledger.mission_id}")
    
    # Identify last successful step
    last_step = p_ledger.steps[-1] if p_ledger.steps else None
    if last_step:
        print(f"📍 Last successful step: {last_step.index} (Task: {last_step.task_id})")
        print(f"   Action: {last_step.action}")
        print(f"   Outcome: {last_step.outcome}")
    else:
        print("📍 No progress recorded yet. Starting from initial state.")
    
    # Identify next pending tasks
    pending = [t.id for t in t_ledger.tasks if t.status == "open"]
    if pending:
        print(f"📋 Next pending task(s): {', '.join(pending)}")
    else:
        print("📋 All currently tasks marked as completed or in progress.")

def rollback_to_checkpoint(checkpoint_id):
    cp_path = LEDGER_DIR / f"checkpoints/{checkpoint_id}.json"
    if not cp_path.exists():
        print(f"❌ Checkpoint not found: {checkpoint_id}")
        return
    
    cp_data = load_json(cp_path)
    checkpoint = Checkpoint(**cp_data)
    
    save_json(TASK_LEDGER_PATH, checkpoint.task_ledger.model_dump())
    save_json(PROGRESS_LEDGER_PATH, checkpoint.progress_ledger.model_dump())
    print(f"✅ Rolled back to checkpoint: {checkpoint_id}")

def main():
    parser = argparse.ArgumentParser(description="Manage SOTA Harness Ledgers")
    subparsers = parser.add_subparsers(dest="command")

    # Init
    init_p = subparsers.add_parser("init")
    init_p.add_argument("mission_id")
    init_p.add_argument("description")
    init_p.add_argument("--goals", nargs="+", required=True)

    # Add Task
    task_p = subparsers.add_parser("add-task")
    task_p.add_argument("id")
    task_p.add_argument("description")
    task_p.add_argument("--priority", default="P2")
    task_p.add_argument("--deps", nargs="+")

    # Add Step
    step_p = subparsers.add_parser("add-step")
    step_p.add_argument("task_id")
    step_p.add_argument("action")
    step_p.add_argument("outcome")
    step_p.add_argument("--status", default="success")

    # Complete Task
    comp_p = subparsers.add_parser("complete-task")
    comp_p.add_argument("task_id")

    # Status
    subparsers.add_parser("status")

    # Checkpoint
    cp_p = subparsers.add_parser("checkpoint")
    cp_p.add_argument("--reason", default="manual")

    # Resume
    subparsers.add_parser("resume")

    # Rollback
    rb_p = subparsers.add_parser("rollback")
    rb_p.add_argument("checkpoint_id")

    args = parser.parse_args()

    if args.command == "init":
        init_ledgers(args.mission_id, args.description, args.goals)
    elif args.command == "add-task":
        add_task(args.id, args.description, args.priority, args.deps)
    elif args.command == "add-step":
        add_step(args.task_id, args.action, args.outcome, args.status)
    elif args.command == "complete-task":
        complete_task(args.task_id)
    elif args.command == "checkpoint":
        create_checkpoint(args.reason)
    elif args.command == "resume":
        resume_mission()
    elif args.command == "rollback":
        rollback_to_checkpoint(args.checkpoint_id)
    elif args.command == "status":
        t_data = load_json(TASK_LEDGER_PATH)
        p_data = load_json(PROGRESS_LEDGER_PATH)
        if t_data:
            print(f"Mission: {t_data['mission_id']}")
            print(f"Description: {t_data['mission_description']}")
            print("\nTasks:")
            for t in t_data['tasks']:
                print(f"  [{t['status']}] {t['id']}: {t['description']}")
        if p_data:
            print("\nProgress:")
            if p_data['steps']:
                last = p_data['steps'][-1]
                print(f"  Last step: {last['action']} -> {last['outcome']}")

if __name__ == "__main__":
    main()
