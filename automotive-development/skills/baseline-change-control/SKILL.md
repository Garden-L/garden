---
name: baseline-change-control
description: Use when implementation reveals a proposed change to an approved SRS, STS, interface, or acceptance criterion and its downstream impact must be traced before work resumes.
---

# Baseline Change Control

Apply the shared `engineering-design` method, then follow the automotive-specific SRS/STS, `WORK-###`, and approval rules below. Handle a discovered baseline change without quietly folding it into the current work item.

If the change belongs to a [module bundle](../../docs/module-deliverables.md), use its canonical `ISSUE` record with `decision` to connect the reason, owner decision, changed documents, work, and later evidence. The change record may be linked from that issue; do not overwrite its earlier rationale.

1. Record the proposed change, reason, affected baseline versions and IDs, and the first work item that exposed it. Distinguish a clarification from a changed obligation or expected result.
2. Trace its effects through related SRS requirements, STS cases, interfaces, work packages, code, and verification evidence. Mark only affected work as waiting for a decision; independent work may continue.
3. Present the decision owner with the current behavior, proposed behavior, alternatives when meaningful, and the implementation and test impact. Do not choose an interpretation that changes the approved baseline.
4. After a recorded decision, use the owning SRS or STS workflow to revise the affected document and version. Update affected backlog items and traceability links, then reassess readiness for those items before implementation resumes.

Return a compact change record with affected IDs, decision status, work that can proceed, and the next owner/action. If the proposal is rejected, retain the original baseline and record the disposition. This skill does not itself approve requirements, change code, or authorize push or merge.
