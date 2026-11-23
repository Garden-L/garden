---
name: boundary-discipline
description: Validate and translate external data where it enters the system, then rely on the accepted internal representation. Use for configuration, files, APIs, messages, or user input crossing a trust or representation boundary.
---

# Boundary Discipline

Parse, validate, and translate external data where it enters the system. Convert accepted input into a typed internal representation, then let core logic rely on that representation's invariants instead of repeating defensive checks throughout the code.

Reject malformed or unauthorized input at the boundary with an error that identifies the problem. Preserve the source value when normalization could lose meaningful information. Add internal checks only where state can become invalid after the boundary or where they protect a separate invariant.
