---
name: change-impact-check
description: Locate a proposed change in the existing architecture and trace affected callers, interfaces, state, tests, and dependent work before coding. Use before code changes to determine whether the work stays local or crosses architectural boundaries.
---

# Change Impact Check

Before coding, locate the proposed change in the current architecture and trace the callers, interfaces, state, tests, and dependent work that the change can affect.

Decide whether the change remains local and its affected work is understood. Carry those impacts into the change. If the scan reveals broad changes, unclear ownership, or a redesign, flag that the work exceeds a local edit.
