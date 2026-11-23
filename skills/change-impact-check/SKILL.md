---
name: change-impact-check
description: Before writing code, locate the proposed change in the existing architecture and trace the work it affects.
---

# Change Impact Check

Before coding, locate the proposed change in the current architecture and trace the callers, interfaces, state, tests, and dependent work that the change can affect.

Decide whether the change remains local and its affected work is understood. Carry those impacts into the change. If the scan reveals broad changes, unclear ownership, or a redesign, flag that the work exceeds a local edit.
