---
name: boundary-discipline
description: Use when data crosses a trust or representation boundary such as configuration, files, APIs, network messages, or user input.
---

# Boundary Discipline

Parse, validate, and translate external data where it enters the system. Convert accepted input into a typed internal representation, then let core logic rely on that representation's invariants instead of repeating defensive checks throughout the code.

Reject malformed or unauthorized input at the boundary with an error that identifies the problem. Preserve the source value when normalization could lose meaningful information. Add internal checks only where state can become invalid after the boundary or where they protect a separate invariant.
