# Universal Agent Bootstrap

> [!IMPORTANT]
> All agents MUST execute session initialization before any work.

## Required First Action

Before responding to ANY user request, execute:

```bash
python3 ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --init --turbo
```

This is **NON-NEGOTIABLE** - run before any other work.

## Session Requirements

1. **Initialization Gate**: Run Orchestrator `--init` before any work
2. **Finalization Gate**: Run Orchestrator `--finalize` before session end  
3. **Git Operations**: All commits MUST go through feature branches and PRs
4. **No Direct Main Commits**: Branch protection is enforced via pre-commit hooks

## Compliance Verification

After completing any task, verify compliance:

```bash
python3 ~/.gemini/antigravity/skills/Orchestrator/scripts/check_protocol_compliance.py --summary
```

## External Documentation

All agents MUST read these files as they are relevant to ALL workflows:

- `~/.agent/AGENTS.md` - Universal protocols and collaboration guidelines
- `~/.agent/docs/SOP_COMPLIANCE_CHECKLIST.md` - Complete SOP compliance requirements
- `~/.gemini/antigravity/skills/Orchestrator/SKILL.md` - Orchestrator skill documentation

## Enforcement Mechanisms

- **Pre-commit hooks** will block non-compliant commits
- **Session locks** track compliance status
- **Audit trails** log all session activity
- **Cross-provider coordination** ensures universal compliance

## Bypass Prevention

- Sessions cannot start without passing initialization checks
- Commits cannot be made without passing finalization checks
- Hook tampering is detected and reported
- All enforcement is external to agent control

---

*This bootstrap documentation is referenced by all provider-specific configurations to ensure universal SOP compliance.*