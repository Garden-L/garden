---
name: git-hygiene
description: Use before and after repository changes to protect unrelated work, keep scope reviewable, and avoid destructive Git operations.
---

# Shared Git Hygiene Skill

Before editing, inspect the current branch and working tree. Preserve unrelated user changes. During work, keep generated artifacts and temporary files out of the tracked change unless the workflow explicitly requires them. Before handoff, inspect the diff, status, and affected paths.

Never reset, checkout, clean, force-push, or delete user data without explicit authorization. This skill is repository-neutral and does not prescribe a branching or release policy.
