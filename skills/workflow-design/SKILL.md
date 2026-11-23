---
name: workflow-design
description: Place a checkable result at each handoff that later work depends on, and connect it to its input and decision owner. Use when designing a multi-stage flow with uncertain decisions or evidence gaps.
---

# Workflow Design

Choose stage boundaries where an output or decision must be checked before later work can rely on it. For each boundary, identify the input, result, decision owner, and check. Carry the result and its origin into the next stage.

Keep one authoritative source for each fact or decision. The calling playbook sets artifact paths, approvals, and the amount of detail needed.
