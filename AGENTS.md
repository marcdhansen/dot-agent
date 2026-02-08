# 🤖 Universal Agent Protocol

**Scope**: **UNIVERSAL** — This is the ONLY location for cross-agent Standard Operating Procedure (SOP) procedures (Initialization, Execution, Finalization) and shared agent memories.
**Purpose**: Single entry point for all agents working across any provider or project.

> [!CAUTION]
> **COLLABORATIVE ENVIRONMENT**: All work happens in shared workspaces.  
> **Before starting ANY work**, read the [Collaboration Protocol](docs/sop/COLLABORATION.md).  
> Key rules: One task per agent, branch isolation, explicit git staging, session registration.

## 🚀 **Quick Start** (< 30 seconds)

**New to system?** → [**FIRST_TIME_SETUP.md**](docs/ONBOARDING.md)  
**Returning agent?** → [**DAILY_START.md**](docs/quick/DAILY_START.md)

> **Golden Path**: 3 commands to productive work
>
> ```bash
> ./scripts/smart-init.sh --task-id <id> --task-desc "desc"
> bd ready  # Highly recommended (optional for planning)
> # Work...
> # MANDATORY: Ensure beads issue exists before implementation
> ./scripts/agent-end.sh
> ```

---

## ⚡ Session Mode (Default: Turbo)

**All sessions start in Turbo Mode** for minimal overhead. Escalate to Full Mode when:

| Trigger | Example |
| :--- | :--- |
| Working on Beads issue | `bd ready` shows active task |
| Deep research | Multi-doc analysis |
| Any Code Changes | Even 1 line of code requires Full Mode |
| User requests planning | Explicit plan review |
| CI/CD or Infrastructure | Workflow or config changes |

- **Turbo Mode**: Direct action, minimal protocol. (e.g., creating issues, Q&A, minor doc edits)
- **Full Mode**: Complete 7-phase SOP with validation. (e.g., implementation, research)

---

---

## 📋 **Session Type Detector**

**What kind of session are you starting?**

| Session Type | Quick Start | Enhanced Services | Multi-Agent |
| :--- | :--- | :--- | :--- |
| **Simple Development** | ✅ Daily Start | ❌ Not needed | ❌ Single agent |
| **Complex Task** | ✅ Daily Start | 🤖 Auto-detect | ❌ Single agent |
| **Collaborative Work** | ✅ Daily Start | 🤖 Auto-detect | ✅ Coordination |
| **First Time Here** | ❌ Skip to Setup | 🤖 Auto-detect | ❌ Single agent |

→ [**Let system auto-detect**](scripts/smart-init.sh)

---

## 🏁 Standard Operating Procedure (SOP)

> **Source of Truth**: [**SOP Compliance Checklist**](docs/SOP_COMPLIANCE_CHECKLIST.md)
>
> The SOP Compliance Checklist defines all mandatory phases and is validated by the Orchestrator.

### Session Phases Overview

| Phase | Status | Description |
| ----- | ------ | ----------- |
| [1. Session Context](docs/phases/01_session_context.md) | **MANDATORY** | Session context, friction capture setup |
| [2. Initialization](docs/phases/02_initialization.md) | **MANDATORY** | Tools, context, approvals verification |
| [3. Planning](docs/phases/03_planning.md) | **MANDATORY** | Blast radius, implementation plan, approval |
| [4. Execution Phase](docs/phases/04_execution.md) | Ongoing | TDD execution, decision recording |
| [5. Finalization](docs/phases/05_finalization.md) | **MANDATORY** | Quality gates, git sync, closure notes |
| [6. Retrospective](docs/phases/06_retrospective.md) | **MANDATORY** | Reflection, handoff, strategic analysis |
| [7. Clean State](docs/phases/07_clean_state.md) | **MANDATORY** | Clean repo state confirmation |

### Orchestrator Validation

The **Orchestrator** validates SOP compliance at each phase:

```bash
# Phase validation commands
python ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --init          # Initialization
python ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --finalize      # Finalization
python ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --retrospective   # Retrospective
python ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --clean         # Clean State
```

> [!IMPORTANT]
> **Orchestrator Coordination**: Validates SOP compliance and gates progression between phases. Failed checks block advancement.

## 📚 Reference Documentation

| Topic | Summary | Details |
| ----- | ------- | ------- |
| **Planning Strategy** | 3-tier: ROADMAP → ImplementationPlan → Beads | [Planning Phase](docs/phases/03_planning.md) |
| **TDD Protocol** | Red → Green → Refactor cycle | [Execution Phase](docs/phases/04_execution.md) |
| **Beads Manual** | Task management with `bd` (Optional for planning, MANDATORY for implementation) | [HOW_TO_USE_BEADS.md](docs/sop/HOW_TO_USE_BEADS.md) |
| **Markdown Standards** | Checkboxes, linting, relative paths | [Project rules](rules/) |
| **Self-Evolution** | Capture preferences, log anti-patterns | [SELF_EVOLUTION_GLOBAL.md](docs/sop/SELF_EVOLUTION_GLOBAL.md) |

### 🧠 Universal Memories

- **Testing**: Automated tests pass ONLY when automatically run and passed
- **Timeouts**: Local LLM tests need 120-300s (not default 30s)
- **WTU**: "Wrap this up" = verify full Finalization checklist before ending
- **Harness**: **LangGraph-native (v2.0)** — Durable checkpointing, multi-agent subgraphs. See [**HARNESS_ARCHITECTURE.md**](docs/architecture/HARNESS_ARCHITECTURE.md)

## 🧠 Cross-Session Memory (MANDATORY)

To ensure cross-session continuity and self-evolution, the following systems are **MANDATORY** for all sessions:

1. **AutoMem**: Local knowledge graph for long-term skill and preference storage.
2. **OpenViking**: Temporal state persistence and multi-agent coordination.

*Session initialization will fail if these services are not verified healthy.*

---

**Need specific information?**

### **Immediate Action Items**

- **Task Discovery**: → [GLOBAL_INDEX.md](docs/GLOBAL_INDEX.md) (Master hub)
- **Available Skills**: → [skills/](skills/) (Agent capabilities)
- **Active Projects**: → [GLOBAL_INDEX.md#projects](docs/GLOBAL_INDEX.md#projects)

### **Reference & Learning**

- **Complete Protocols**: → [rules/](rules/) (Full standards)
- **Troubleshooting**: → [docs/troubleshooting/](docs/troubleshooting/) (When things break)
- **Advanced Features**: → [docs/advanced/](docs/advanced/) (Power user features)

---

## 🔒 **Collaboration Protocol**

→ **[COLLABORATION.md](docs/sop/COLLABORATION.md)** — One task per agent, branch isolation, explicit staging

---

## 🎯 **Quick Commands**

```bash
./scripts/smart-init.sh --task-id <id> --task-desc "desc"  # Session start
./scripts/agent-end.sh                                       # Session end
```

---

## 🔗 **Provider-Specific Links**

**Provider-specific configurations and capabilities:**

- **[Gemini Configuration](~/.gemini/GEMINI.md)** (Google/Gemini specific)
- **[Claude Configuration](~/.claude/README.md)** (Claude specific)
- **[VS Code Integration](~/.antigravity/README.md)** (VS Code specific)

---

## 📚 **Complete Documentation Index**

**For comprehensive exploration:**
→ **[Master Navigation Hub: docs/GLOBAL_INDEX.md](docs/GLOBAL_INDEX.md)**

*This document contains every link in the system, organized by context and use case.*

---

*Last Updated: 2026-02-02*  
*Universal Protocol - Works across all providers and projects*
