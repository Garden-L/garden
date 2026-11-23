# Bug Fix

Use when an unintended behavior can be reproduced or investigated against an established expectation.

If `change-impact-check` reveals cross-component impact, shared-interface changes, or redesign, complete [Architecture Change](architecture-change.md) before editing the affected code.

1. Identify the expected behavior, affected subsystem, reported symptom, and relevant environment. Apply `change-impact-check` before changing code.
2. Reproduce the failure on the closest relevant surface. Record revision, setup, inputs, command or procedure, expected result, and actual result.
3. Apply `root-cause-first`. Trace candidate causes and eliminate them with targeted evidence. Do not code against an unconfirmed cause. If the expected behavior is missing or contradictory, route to its owner before changing the implementation.
4. Apply `work-decomposition` when investigation or correction spans multiple owners or steps. Keep a tightly coupled reproduction and fix with one owner; separate only independent investigations or deliverables with clear handoffs.
5. Apply `minimal-change`. Use `behavior-focused-tests` to add or select a focused regression check before the fix when practical, confirm it exposes the failure, then make the smallest correction supported by evidence.
6. Rerun the original reproduction on the same surface and revision, followed by relevant regression checks. Apply `prove-real-result` and `verification`; record unavailable environments as pending.
7. Update the change record and apply `review` to the completed diff.

Output: the symptom, demonstrated cause, bounded correction, reproduction evidence, and remaining checks.

## Automotive application

- Identify the applicable SRS/STS revision, affected `REQ` and `TC`, observed symptom, and target environment. Reproduce against that expectation before changing code.
- Record the cause and keep the correction within the affected `WORK` package and traceability links. Keep unrelated cleanup, formatting, renaming, and redesign in separate work.
- Repeat the reproduction and relevant regression checks on the corrected revision. Distinguish local evidence from integration, ECU, HIL, and vehicle evidence.
- If the approved expectation is missing, contradictory, or needs revision, follow [Baseline Change Control](change-control.md) before changing the expected behavior.
