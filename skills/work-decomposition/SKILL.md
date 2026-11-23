---
name: work-decomposition
description: Separate work only where each part has a clear boundary, owner, dependency, and check. Use when a change spans components or workers and the smallest safe division is uncertain.
---

# Work Decomposition

Identify blocking decisions, independent results, shared mutable state, and the integration point. Keep tightly coupled work with one owner. Split only where each part has a clear boundary, owner, dependency, and way to check its result.

Reconsider the split when interfaces or dependencies change. The calling playbook decides the work record and execution sequence.
