# Architecture Change

Use when `change-impact-check` shows that the work crosses component boundaries, changes shared interfaces, or requires redesign. Complete this before code changes in the affected area.

1. Map the affected modules, callers, interfaces, state, `REQ`/`TC` links, and `WORK` packages. Separate confirmed impacts from unknowns.
2. Apply `architecting`: choose the target boundaries and responsibilities. Sketch the relevant types, signatures, module layout, and interface relationships only as far as needed to settle the change.
3. Compare the current and target structures. Identify migration steps, dependencies, shared files, and checks that can demonstrate each step preserves or changes the approved behavior as intended.
4. Apply `work-decomposition` to make bounded work packages with one integration owner and explicit checks. If an approved SRS, STS, interface, or acceptance criterion must change, use [Baseline Change Control](change-control.md) before affected implementation.
5. Resume the [Feature](feature.md), [Bug Fix](bug-fix.md), or [Refactoring](refactoring.md) playbook with the chosen structure, work boundaries, and verification path.

Output: the affected scope, target structure, migration order, work boundaries, and unresolved decisions.
