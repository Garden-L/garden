# Refactoring

Use when changing internal structure while preserving accepted externally observable behavior.

If `change-impact-check` reveals cross-component impact, shared-interface changes, or redesign, complete [Architecture Change](architecture-change.md) before editing the affected code.

1. State the behavior contract and scope that must remain unchanged. Apply `change-impact-check` to trace callers and affected work; identify or add a characterization check before moving structure.
2. Apply `architecting` to name the target structure and the complexity, invalid states, or coupling it removes. Use `domain-model-first` if the refactor reshapes state or domain relationships. If new behavior is needed, route it to Feature or Bug Fix.
3. Apply `work-decomposition` for multi-component changes. Keep coupled API and caller migrations under one integration owner; divide only disjoint changes with a pinned contract and independent checks.
4. Apply `minimal-change`. Make small structural changes while keeping the behavior pin green. Remove obsolete paths and update callers in the same bounded change; avoid speculative compatibility layers.
5. Apply `prove-real-result` and `verification` to compare before and after behavior on the relevant tests and real target surface. For larger changes, use an equivalence check or replay where available.
6. Review the complete diff and confirm the change improves the stated structure without changing behavior. Record the contract, checks, revision, and any unavailable evidence; apply `review` before handoff.

Output: the structural change, behavior contract held, equivalence evidence, and reviewable change record.

## Automotive application

- Identify the approved SRS/STS revision, affected `REQ` and `TC`, and the behavior contract to preserve.
- Bound structural changes by the selected `WORK` package. Record any necessary caller or interface migration and update traceability. Keep unrelated cleanup and redesign in separate work.
- Compare behavior before and after on the relevant target surface; record actual evidence and mark unavailable integration, ECU, HIL, or vehicle checks pending.
- If the change needs a revised requirement, interface, test expectation, or acceptance criterion, follow [Baseline Change Control](change-control.md). Route intended new behavior to [Feature](feature.md) and a defect correction to [Bug Fix](bug-fix.md).
