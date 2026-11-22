---
name: implementation-verification-review
description: Use when an implementation work package needs a practical check against its approved requirements, test procedures, changed artifact, and target evidence before delivery.
---

# Implementation Verification Review

Use the shared `verification` method to check one completed `WORK-###` against its approved SRS, STS, implementation, and actual run evidence. Decide whether the result is supported well enough for the next delivery gate. Do not silently change the requirement, test expectation, or implementation during review.

For a [module bundle](../../docs/module-deliverables.md), record the verification in `05-verification/verification.md` and regenerate `05-verification/completion-report.md` after the source records are current.

## Perform the review

1. **Identify what changed.** Compare the implementation with the work packet and its base revision. Confirm the correct files, build, configuration, and target are under review.
2. **Choose checks for the changed behavior.** Start with the STS procedures linked to the affected requirements. Add only relevant boundary, invalid-input, error, recovery, or regression cases. For vehicle behavior, use the required ECU/HIL/vehicle environment when available; mark unavailable target checks as pending.
3. **Run and observe.** Confirm each precondition, follow the procedure in order, and capture actual intermediate and final behavior. Record the command, revision, environment, inputs, logs, and relevant side effects. A green summary without the underlying result is insufficient.
4. **Compare with the expectation.** For each failure or unexpected result, check that the correct build ran, the setup and inputs match the procedure, and the expected result agrees with the approved requirement. Reproduce the mismatch under the same conditions before concluding it is an implementation defect. If the test or requirement is unclear, report that and stop short of a pass/fail claim.
5. **Verify corrections and scope.** Rerun the corrected case and relevant regression checks. Confirm no unrelated change or unverified target behavior is included in the delivery claim.

A useful finding states the expected behavior, the actual reproducible result, the evidence, and why the difference matters to the vehicle behavior or delivery decision. Recommend the correction that addresses the demonstrated cause. If the cause is still uncertain, say what needs to be checked next; do not guess or change a baselined SRS/STS to make the result pass.

## Verdicts

- `APPROVED FOR PUSH/MR` — required checks passed in the applicable environment and the evidence supports the stated scope.
- `CONDITIONAL` — only named non-blocking checks or environments remain pending.
- `CHANGES REQUIRED` — a reproducible mismatch or invalid check prevents delivery.
- `BLOCKED` — missing expectations, setup, or required environment prevents a valid conclusion.

A local or simulated pass does not establish ECU, HIL, vehicle, safety, or release behavior. This review does not authorize push, MR creation, or merge.

## Report

Give the verdict and reason, reviewed revision and environment, checks run, expected and actual results for failures, evidence, remaining unverified scope, and the next action. For module delivery, update the verification record and regenerate the completion report. Do not repeat IDs or decision rationale already maintained in the source artifacts.
