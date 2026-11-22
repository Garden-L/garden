---
name: bounded-implementation-execution
description: Use when one approved implementation work package must be implemented, tested, and committed within its defined scope.
---

# Bounded Implementation Execution

Apply the shared `implementation` method, then enforce the automotive work-packet, traceability, safety, and delivery gates below. Implement exactly one approved `WORK-###` from its implementation packet. Do not expand the task, repair baselined requirements, or push/merge without the required approvals.

For a [module bundle](../../docs/module-deliverables.md), update the same `WORK` packet with actual code/test paths, checks, results, and revision; link evidence in its `traceability.md` and `05-verification/verification.md`. A decision is only `Applied` when the affected artifacts and code actually changed.

Keep the process proportional: reuse existing packet, test, and matrix artifacts; do not create duplicate documents or demand heavyweight review for a low-risk, small change. Add a check or approval only when the work's risk, scope, or repository policy requires it.

## Preconditions

Confirm the packet contains:

- work ID, SRS/STS IDs, readiness conditions, and acceptance criteria;
- base revision, allowed files/components, and out-of-scope items;
- API/data/schema impact, test plan, diff limit, and rollback plan.

If any item is missing or a readiness condition is unsatisfied, stop and report it. Preserve unrelated working-tree changes; use an isolated worktree or branch when available.

## Execute the slice

1. Reconcile the packet with the current repository and record any mismatch.
2. Run the mapped behavior tests before changing production code; capture the baseline.
3. Implement the smallest change that satisfies the packet.
4. Run mapped tests, regression tests, and applicable lint/type/build checks.
5. Inspect the complete diff against the base revision. Confirm every changed file is allowed and the diff is within the packet limit.
   For stateful or safety-related code, inspect state transitions, time boundaries, duplicate events, and repeated calls. If one function accumulates unrelated rules or nested transitions, split by responsibility before the slice grows harder to review; keep the behavior tests as the guard.
6. Update the traceability matrix with implementation status and evidence.
7. Prepare one focused local commit containing only the approved scope. Include the work, SRS, and STS IDs in the message.

Stop and request a revised packet if the change needs an unlisted file, public contract, schema/wire behavior, safety/security/diagnostic/timing assumption, acceptance criterion, or larger scope. Do not hide or revert unrelated user changes.

## Completion states

- `BLOCKED`: missing input, failed baseline, scope mismatch, or unmet condition.
- `IN PROGRESS`: implementation or verification remains.
- `READY FOR REVIEW`: tests and diff checks pass; local commit is prepared.
- `PENDING ENVIRONMENT`: local checks pass but integration, HIL, hardware, or release evidence is missing.

Never claim completion from code existence alone. Report commands, results, changed files, commit SHA, remaining risks, and evidence gaps.

## Delivery gates

Prepare the branch and local commit only. Push and draft-MR creation require a separate explicit approval. Merge requires another separate approval after review, CI, and required verification pass.

## Required output

Return:

1. **Work and baseline** — IDs, base revision, packet status.
2. **Changes** — files changed and scope check.
3. **Verification** — commands, results, and pending environments.
4. **Traceability update** — SRS/STS/work/status/evidence links.
5. **Commit** — local SHA and message, or why no commit was made.
6. **Next gate** — review, push/MR approval, or blocker.
