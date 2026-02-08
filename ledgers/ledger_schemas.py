from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field

class TaskEntry(BaseModel):
    id: str
    description: str
    status: str = "open"  # open, in_progress, completed, failed, blocked
    priority: str = "P2"
    dependencies: List[str] = Field(default_factory=list)
    facts: List[str] = Field(default_factory=list)
    guesses: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskLedger(BaseModel):
    mission_id: str
    mission_description: str
    goals: List[str]
    tasks: List[TaskEntry]
    metadata: dict = Field(default_factory=dict)

class ProgressStep(BaseModel):
    index: int
    task_id: str
    action: str
    outcome: str
    status: str = "success"  # success, failure, stall
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    observed_state: dict = Field(default_factory=dict)

class ProgressLedger(BaseModel):
    mission_id: str
    steps: List[ProgressStep]
    current_step_index: int = 0
    stalls_detected: int = 0
    replan_history: List[str] = Field(default_factory=list)

class Checkpoint(BaseModel):
    checkpoint_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    task_ledger: TaskLedger
    progress_ledger: ProgressLedger
    reason: str = "manual"
