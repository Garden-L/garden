# Feature

Use when adding or changing software behavior with an accepted goal and a decision source for expected behavior.

If `change-impact-check` reveals cross-component impact, shared-interface changes, or redesign, complete [Architecture Change](architecture-change.md) before editing the affected code.

1. State the outcome, user-visible behavior, acceptance conditions, scope, and source of truth. If a consequential product or domain decision is missing, resolve it before coding.
2. Apply `change-impact-check` to trace the affected subsystem, callers, data, tests, and dependent work. Apply `architecting` for consequential design choices. Apply `domain-model-first` before stateful or branching logic, and `boundary-discipline` where data crosses a trust or representation boundary.
3. Apply `work-decomposition`. Record blocking first steps, independent workstreams, shared mutable state, and the smallest safe decomposition. Keep one owner for a small or tightly coupled change. Split only independently checkable units with explicit boundaries and non-overlapping write ownership.
4. For every split unit, name its owner, files or interface, inputs, output, dependency, and check. Keep one owner responsible for integration and review. If delegation is unavailable, execute the units sequentially using the same checkpoint.
5. Apply `minimal-change`. Use `behavior-focused-tests` to select or write an observable behavior check before production changes when practical, and confirm it exposes the missing behavior. Implement only the agreed scope; use the accepted requirement or decision as the expected-result source.
6. Integrate the complete change and inspect its diff. Run focused checks, then relevant regression and integration checks on the same revision. Apply `prove-real-result` and `verification` on the real behavior and target surface; label unavailable checks as pending.
7. Update the work record with changed scope, revision, checks, evidence, and deviations. Apply `review` to the completed diff before handoff or release.

Output: a bounded feature, the reason for its work split (including why one owner was chosen), behavior evidence, and a reviewable change record.

## Automotive application

- Use the approved SRS requirements, STS expectations, and `WORK` acceptance criteria as the behavior source. Identify the affected source IDs and revision before coding.
- Bound the change by the selected `WORK` package. Keep unrelated cleanup, formatting, renaming, and redesign in separate work. If acceptance criteria depend on one of these changes, record why and update the package and traceability.
- Connect implementation and checks to the same `REQ`, `TC`, and `WORK` IDs. Record actual evidence and leave unavailable integration, ECU, HIL, or vehicle checks pending.
- If the accepted requirement, interface, test expectation, or acceptance criterion must change, follow [Baseline Change Control](change-control.md) before continuing affected work.
