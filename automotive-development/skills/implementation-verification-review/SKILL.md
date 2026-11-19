---
name: implementation-verification-review
description: Use when an implementation work package needs a proportional review against its approved requirements, tests, scope, diff, and evidence before delivery.
---

# Implementation Verification Review

Review one `WORK-###` after implementation. Decide whether it is ready for the next gate; do not rewrite the SRS/STS or silently fix the code.

## Review proportionally

Reuse the existing packet, matrix, test results, and CI evidence. For a low-risk small change, perform a focused review. Expand the review only when the diff or risk involves public contracts, schema/wire behavior, safety, security, diagnostics, timing, concurrency, or resource limits.

## Required checks

1. **Baseline and scope** — compare the branch to the packet's base revision. Confirm every changed file, API/data/schema effect, and line/file limit is allowed. Treat unrelated changes as a scope failure.
2. **Requirement and test coverage** — verify SRS IDs, STS IDs, acceptance criteria, and observable behavior match. Check both directions for missing requirement, test, work, commit, or MR links.
3. **Verification evidence** — confirm mapped tests, relevant regression checks, and required lint/type/build/CI results. Do not treat unexecuted hardware, HIL, integration, or release checks as passed.
4. **Risk review** — inspect only risks relevant to the change: errors/boundaries, state/recovery, interfaces, security, safety, concurrency, performance, diagnostics, and rollback.
5. **Traceability update** — record findings, evidence, status, and any required decision in the existing matrix.

If a defect or scope expansion is found, return it to the implementer or create a new work item. Do not modify a baselined requirement or test specification as a workaround.

## Verdicts

- `APPROVED FOR PUSH/MR` — scope, tests, evidence, and required review checks pass.
- `CONDITIONAL` — safe to continue only with listed non-blocking evidence or environment conditions.
- `CHANGES REQUIRED` — scope, behavior, test, traceability, or risk issue blocks delivery.
- `BLOCKED` — missing baseline, packet, decision, or required environment prevents a valid review.

This review does not authorize push, MR creation, or merge. Push/MR requires the separate approval gate; merge requires another approval after review and CI.

## Required output

Return:

1. **Verdict** and one-sentence reason.
2. **Baseline and scope** — revisions and changed-file result.
3. **Findings** — severity, evidence, affected IDs, and required action.
4. **Verification** — tests/checks run and pending environments.
5. **Traceability** — updated links and remaining gaps.
6. **Next gate** — rework, push/MR approval, or merge approval.
