# 🤖 Global Agent Hub

Welcome to the global agent coordination center. This directory serves as the universal hub for all agent activities, skills, protocols, and coordination across workspaces.

## 🚀 Quick Start for New Agents

1. **Read Global SOP**: Start with `docs/sop/GEMINI.md` to understand the Protocol
2. **Check Available Skills**: Browse `skills/` to see universal capabilities
3. **Review Rules**: Understand universal standards in `rules/`
4. **Navigate to Workspace**: Use the appropriate workspace for your project

## 📁 Directory Structure

```
~/.agent/
├── docs/
│   ├── sop/                    # Standard Operating Procedures (global protocols)
│   │   ├── GEMINI.md          # 🌐 Global Agent Rules (Protocol)
│   │   ├── NOMENCLATURE.md  # Universal terminology
│   │   ├── AGENT_ONBOARDING.md     # New agent onboarding
│   │   ├── CROSS_COMPATIBILITY.md  # Multi-IDE/agent support
│   │   └── HOW_TO_USE_BEADS.md     # Beads usage guide
│   ├── workspace/              # Global workspace management
│   └── troubleshooting/        # System-wide troubleshooting guides
├── skills/                     # 🧰 Universal agent capabilities
│   ├── Orchestrator/        # Coordination & compliance
│   ├── Librarian/              # Knowledge management
│   ├── QualityAnalyst/        # Quality assurance
│   ├── Reflect/                # Session reflection & learning
│   ├── JavaScript/             # JavaScript expertise
│   └── coding-standards/       # Code quality standards
└── rules/                      # 🛡️ Universal rules and standards
```

## 🧭 Navigation

### For Protocol Information

- **Main Rules**: `docs/sop/GEMINI.md` - Complete Protocol
- **Getting Started**: `docs/sop/AGENT_ONBOARDING.md` - New agent guide
- **Terminology**: `docs/sop/NOMENCLATURE.md` - Universal definitions

### For Work Coordination

- **Current Work**: Navigate to specific workspace directories
- **Multi-Agent**: Check `docs/sop/GEMINI.md` for coordination protocols
- **Task Management**: Use Beads (`bd`) as specified in `docs/sop/HOW_TO_USE_BEADS.md`

### For Capabilities

- **Available Skills**: `skills/` - Universal agent capabilities
- **Quality Standards**: `skills/coding-standards/` - Code quality guidelines
- **Compliance**: `skills/Orchestrator/` - Automated compliance checking

## 🔗 Integration with Workspaces

Each workspace mirrors this structure:

```
<workspace>/.agent/
├── docs/
│   ├── sop/global-configs/  # → symbolic links to ~/.agent/docs/sop/
│   ├── skills/              # → symbolic links to ../.agent/skills/
│   └── workspace/           # Workspace-specific documentation
├── skills/                  # Workspace-specific skills
└── rules/                   # Workspace-specific rules
```

## 📋 Protocol

All agent work follows the Standard Mission Protocol:

1. **Initialization Check** - Mandatory validation before starting
2. **Execution** - Guidelines during execution  
3. **Finalization** - Mandatory completion procedures

See `docs/sop/GEMINI.md` for complete protocol details.

## 🛠️ Maintenance

This global hub is maintained by:

- **Librarian Skill** - Documentation organization and knowledge management
- **Orchestrator Skill** - Protocol compliance and coordination
- **Community Evolution** - Continuous improvement based on usage

---

**Remember**: This hub replaces the previous `~/.gemini/` structure with a standardized approach that aligns with workspace-level organization for better consistency and navigation.
