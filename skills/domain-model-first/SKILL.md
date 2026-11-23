---
name: domain-model-first
description: Use before implementing logic whose behavior depends on domain entities, states, relationships, or invariants.
---

# Domain Model First

Make the central data shape reflect the domain before distributing behavior across conditionals.

Identify the relevant entities, states, relationships, allowed transitions, and invariants. Choose types and ownership that make those rules visible and make invalid states difficult to represent. Then implement behavior against that model. Use a simpler representation when the problem is genuinely simple; do not add layers or abstractions without a domain need.

Check the model against representative valid, invalid, and boundary cases before expanding the implementation.
