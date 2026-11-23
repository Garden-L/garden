---
name: work-decomposition
description: Use when deciding whether engineering work should stay with one owner or be divided into sequential or parallel units.
---

# Work Decomposition

Divide work around dependencies, ownership, and evidence. The goal is a sequence that can be checked and integrated, not the largest number of workers.

## Decide the shape

1. State the outcome, accepted behavior, scope boundary, and available source of truth. Resolve decisions that would change the implementation before coding.
2. Trace the affected components, interfaces, shared state, and checks. List the work that blocks everything else first.
3. Make a checkpoint with four parts:
   - **Blocking first steps:** decisions, discovery, or interfaces that must settle before implementation.
   - **Independent workstreams:** deliverables that can proceed without editing the same files or waiting on the same decision.
   - **Shared mutable state:** files, interfaces, branches, hardware, or records with concurrent owners. Assign one owner or serialize changes.
   - **Smallest safe decomposition:** the fewest units that preserve clear ownership and allow each result to be checked.
4. Keep one owner when the change is small, tightly coupled, or has no independent deliverable. Split only when each unit has a bounded result, explicit inputs and interfaces, disjoint ownership, and its own check.
5. For every split unit, name its owner, paths or boundary, inputs, output, dependencies, check, and integration order. The integrating owner reviews the actual result and reruns affected checks.
6. Revisit the checkpoint when evidence changes scope, interfaces, dependencies, or the verification surface. Do not continue a split that now creates more coordination than progress.

## Quick choice

| Work shape | Choice |
| --- | --- |
| One function or one coupled behavior | One owner implements and verifies end to end |
| Independent components with stable interfaces and separate checks | Split by component or deliverable |
| Multiple workers need the same files or mutable state | Assign one writer at a time or first create disjoint ownership |
| Acceptance or architecture is unresolved | Settle the blocking decision before dividing implementation |

## Common mistakes

- Splitting by role alone, such as implementation versus tests, when both need the same changing contract.
- Starting parallel edits before agreeing on interfaces or file ownership.
- Treating an unavailable target check as passed because a local check is green.
- Creating tiny assignments whose handoff and integration cost exceeds the work.
- Keeping a plan after its assumptions have changed.

**Example:** A focused change to one state transition stays with one owner. For a feature spanning an independent parser and UI, define the shared data shape first, assign each component separately, then integrate and verify the end-to-end behavior.
