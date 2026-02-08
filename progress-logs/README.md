# Progress Logs

This directory contains ACE-inspired **Evolving Playbooks** for each development issue.

## System Overview

Inspired by the **Agentic Context Engineering (ACE)** framework, these logs serve as a running context that survives agent crashes and provides incremental handoffs.

### Roles and Responsibilities

- **Generator**: Agents create entries documenting tactical progress and decisions.
- **Reflector**: Agents analyze what worked and what failed, extracting strategic insights.
- **Curator**: Agents periodically consolidate older entries and cross-log patterns to prevent context bloat.

## Naming Convention

Logs are named using the **Beads Issue ID**:
`{issue-id}.md` (e.g., `lightrag-ifw.md`)

## Workflow

1. **Creation**: A log is created during the **Initialization** phase of a new issue.
2. **Update**: Use `/log-progress` after significant milestones or at the end of a session.
3. **Curation**: When a log exceeds 50 entries, older entries are summarized into the **Historical Summary** section.
4. **Cleanup**: During the **Clean State** phase (Phase 7), local temporary files are deleted, leaving these logs as the persistent record.

## Maintenance

- **Do not delete logs** unless the issue is archived.
- **Auto-commit** is required after every entry.
