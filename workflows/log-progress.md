---
description: Append a structured entry to the current issue's progress log
---

# Workflow: Log Progress

## Usage

```bash
/log-progress
```

## Steps

1. **Identify Active Issue**
   - Check current branch name for issue ID
   - If not found, run `bd ready` to identify the active task

2. **Gather Entry Data**
   - Current phase (Initialization, Planning, Execution, etc.)
   - Conversation ID (from environment or session context)
   - Completed items, Decisions, Reflector insights, and Next steps

3. **Append Entry**
   - Use the template from `~/.agent/templates/progress-log-template.md`
   - Append the entry to `~/.agent/progress-logs/{issue-id}.md`
   - Update the "Active Context" and "Last Updated" fields at the top of the file

// turbo
4. **Auto-Commit**

   ```bash
   cd ~/.agent && git add progress-logs/{issue-id}.md && git commit -m "progress: {issue-id} update" && git push
   ```
