---
name: architecting
description: Sketch the affected modules, types, signatures, and interface boundaries before choosing the simplest structure that meets the intended behavior. Use for “architect this”, “design this”, or structural changes where coding first could lock in the wrong shape.
---

# Architecting

Use the affected components and boundaries to judge whether the change fits the existing structure or requires a structural change.

For a local change, preserve the surrounding structure. For a broad change, sketch the target modules, types, signatures, and interface relationships before implementation. Choose the simplest structure that satisfies the intended behavior and constraints; keep any choice that depends on an unknown condition open.
