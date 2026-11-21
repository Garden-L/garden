---
name: tdd
description: Use when a change has a cheap, focused executable test path; capture the intended behavior with a failing test before changing implementation.
---

# Shared Test-Driven Development Skill

Use the narrowest practical test for the behavior being changed.

1. Identify the intended observable behavior and the smallest reproduction.
2. Write a focused test that expresses the behavior, not the implementation.
3. Run it and confirm it fails for the intended reason.
4. Make the smallest implementation change.
5. Rerun the focused test and nearby checks.

Do not force a new test when the path is expensive, brittle, or unavailable. In that case, use the closest executable check and state the limitation.
