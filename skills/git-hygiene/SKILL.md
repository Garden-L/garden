---
name: git-hygiene
description: Use before and after repository changes to protect unrelated work, keep scope reviewable, and avoid destructive Git operations.
---

# Git Hygiene

Before editing, inspect the current branch and working tree. Preserve unrelated user changes. Keep generated artifacts and temporary files out of tracked changes unless the workflow requires them. Before handoff, inspect the diff, status, and affected paths.

Never reset, checkout, clean, force-push, or delete user data without explicit authorization. This skill does not prescribe a branching or release policy.
