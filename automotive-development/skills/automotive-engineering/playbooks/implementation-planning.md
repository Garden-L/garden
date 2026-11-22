# Implementation Planning

Use when an approved SRS/STS and readiness result need to become executable code work.

1. Apply `workflow-design` to order work by dependencies and reviewable outputs.
2. Apply `implementation-backlog-traceability` to preserve `REQ` → `TC` → `WORK` links and create bounded vertical slices.
3. Apply `engineering-design` where a work item changes an interface, shared state, or module boundary.
4. For each `WORK-###`, state intended behavior, allowed and excluded scope, exact acceptance checks, dependencies, rollback, and stop conditions.
5. Sequence prerequisite interfaces and infrastructure before dependent behavior. Keep one implementation owner per work item and avoid overlapping file ownership when parallelizing.
6. Confirm the first eligible packet satisfies readiness conditions before implementation begins.

Output: ordered work packets, dependency order, traceability updates, and the first eligible implementation packet.
