---
name: bounded-implementation-execution
description: Use when one approved implementation work package must be implemented, tested, and committed within its defined scope.
---

# Bounded Implementation Execution

Implement exactly one approved `WORK-###` from its implementation packet. Do not expand the task, repair baselined requirements, or push/merge without the required approvals.

Keep the process proportional: reuse existing packet, test, and matrix artifacts; do not create duplicate documents or demand heavyweight review for a low-risk, small change. Add a check or approval only when the work's risk, scope, or repository policy requires it.

## Preconditions

Confirm the packet contains:

- work ID, SRS/STS IDs, readiness conditions, and acceptance criteria;
- base revision, affected components or files, and out-of-scope items;
- contract impact, verification method, and any project-specific change limit.

If any item is missing or a readiness condition is unsatisfied, stop and report it. Preserve unrelated working-tree changes; use an isolated worktree or branch when available.

## Execute the slice

1. Reconcile the packet with the current repository and record any mismatch.
2. For a behavior change, run an existing relevant test or establish a failing test/observable baseline where practical. For other changes, use the packet's relevant check.
3. Implement the smallest change that satisfies the packet.
4. Run mapped tests, regression tests, and applicable lint/type/build checks.
5. Inspect the complete diff against the base revision. Confirm it stays within the approved boundary and any project-specific limit.
6. Update the traceability matrix with implementation status and evidence.
7. Before committing, inspect the target repository's commit instructions and checks (for example `AGENTS.md`, `CONTRIBUTING.md`, commitlint or Git hooks). Follow every applicable rule; include work/SRS/STS IDs in the form those rules permit. Stage only the approved scope, inspect the staged diff, then make a focused local commit. If a required rule cannot be satisfied, report the conflict instead of bypassing it.

Stop and request a revised packet if the change crosses the approved component or file boundary, changes a public contract, schema/wire behavior, safety/security/diagnostic/timing assumption, acceptance criterion, or exceeds an applicable limit. Do not hide or revert unrelated user changes.

## Completion states

- `BLOCKED`: missing input, failed baseline, scope mismatch, or unmet condition.
- `IN PROGRESS`: implementation or verification remains.
- `READY FOR REVIEW`: tests and diff checks pass; local commit is prepared.
- `PENDING ENVIRONMENT`: local checks pass but integration, HIL, hardware, or release evidence is missing.

Never claim completion from code existence alone. Report commands, results, changed files, commit SHA, remaining risks, and evidence gaps.

## Delivery gates

Prepare the branch and local commit only. Obtain the user's explicit approval for the specific push and PR/MR creation or update before performing them. Obtain a separate explicit approval for merge after review, CI, and required verification pass. A review verdict is not user approval.

## Required output

Report the following information concisely, combining sections when appropriate:

1. **Work and baseline** — IDs, base revision, packet status.
2. **Changes** — files changed and scope check.
3. **Verification** — commands, results, and pending environments.
4. **Traceability update** — SRS/STS/work/status/evidence links.
5. **Commit** — local SHA and message, or why no commit was made.
6. **Next gate** — review, push/MR approval, or blocker.
