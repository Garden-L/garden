# Bug Fix

Use when an automotive software defect can be reproduced or investigated against a defined expected behavior.

1. Confirm the affected requirement, test procedure, work scope, target, and reported symptom.
2. Reproduce the failure on the closest relevant surface and preserve the command, inputs, environment, revision, and observed result.
3. Compare the observed behavior with the approved expectation. If the expectation is absent or contradictory, route to [Baseline Change Control](change-control.md) or the owning SRS/STS workflow before changing code.
4. Trace candidate causes and eliminate them with targeted evidence. Do not add guards for causes that have not been demonstrated.
5. Apply `implementation` and `bounded-implementation-execution`. Add a focused failing regression check when the test path is practical, then fix the demonstrated cause.
6. Rerun the original reproduction on the same surface and relevant regression checks. Record any unavailable target or HIL test as pending.
7. Update the work packet and traceability record, then route to [Code Review](code-review.md) and [Implementation Verification](verification.md).

Output: symptom, demonstrated cause, focused correction, reproduction evidence, and remaining environment checks.
