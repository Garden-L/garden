---
name: architecting
description: When a change affects the system structure, choose an architecture that fits its scope and constraints.
---

# Architecting

Use the affected components and boundaries to judge whether the change fits the existing structure or requires a structural change.

For a local change, preserve the surrounding structure. For a broad change, define the target boundaries and interface relationships before implementation. Choose the simplest structure that satisfies the intended behavior and constraints; keep any choice that depends on an unknown condition open.
