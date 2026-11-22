# Release Readiness

Use before packaging or releasing an implementation after code review and required verification.

1. Confirm the release candidate revision, included work items, approved baseline, target configuration, and release scope.
2. Apply `review` and `verification` to inspect release evidence; use `implementation-verification-review` for automotive work-item criteria.
3. Confirm required unit, integration, regression, and target/HIL/vehicle checks have evidence for this exact candidate. List deferred checks and their owners; do not imply they passed.
4. Check unresolved issues, deviations, traceability gaps, known defects, calibration/configuration, rollback or recovery information, and required approvals against project policy.
5. Return `READY`, `READY WITH CONDITIONS`, or `NOT READY`. Conditions must be explicit and must not authorize work beyond their scope.
6. Prepare release notes and evidence links. Perform deployment, publication, or irreversible release actions only when separately authorized.

Output: release-readiness verdict, evidence and conditions, known gaps, and the next authorized delivery action.
