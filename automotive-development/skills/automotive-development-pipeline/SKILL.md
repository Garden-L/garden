---
name: automotive-development-pipeline
description: Use when automotive requirements must be processed as a staged workflow from SRS through STS and implementation-readiness review.
---

# Automotive Development Pipeline

Coordinate the existing automotive document skills without replacing their authoring or review rules. The pipeline is a gated workflow: do not silently resolve decisions or treat the existence of a document as approval.

## Determine the entry point

- Raw or sentence-level requirements → start with [Software Requirements Specification](../software-requirements-specification/SKILL.md).
- An existing SRS without an approved/complete STS → continue with [Software Test Documentation](../software-test-documentation/SKILL.md).
- An existing SRS and STS → continue with [Implementation Readiness Review](../implementation-readiness-review/SKILL.md).
- A completed readiness review → continue with [Implementation Backlog and Traceability](../implementation-backlog-traceability/SKILL.md) before production implementation.
- If the required source document, version, scope, or context is missing, stop and report the missing input.

## Run the gated workflow

### 1. SRS gate

Invoke the SRS skill when requirements are not yet captured as an SRS. Preserve source sentences, requirement IDs, issues, decisions, and affected Mermaid flows. Run its author/reviewer workflow.

Stop and ask the user to resolve any ambiguity, conflict, missing condition, or scope choice that could change the SRS. Mark affected content as `Confirmation needed` or `TBD`; never infer approval from a plausible assumption.

Treat the SRS as approved only when the user explicitly confirms it in the current workflow or the document records an explicit approval status, owner, and date. Do not infer approval from a filename, formatting, or the absence of comments.

Proceed to STS only when the SRS is approved for test-documentation work, or when the user explicitly asks to continue with unresolved items that remain clearly marked. Carry those unresolved items into the STS and readiness handoffs.

### 2. STS gate

Invoke the STS skill from the current SRS. Preserve all SRS requirement IDs and carry unresolved requirement decisions into `ISSUE-###` records. Create the traceability summary and run the independent STS review required by that skill.

Stop for user input when an expected result, test scope, procedure, or test technique depends on an unresolved requirement decision. If a `Must Fix` review finding changes the test design, revise and review the affected STS before continuing.

Treat the STS as complete for readiness review only when no unresolved issue can change the test design, or when the user explicitly authorizes continuation with those issues recorded. Do not treat unresolved `Must Fix` findings as complete.

Proceed to readiness review only when the STS is available with its review findings and remaining decisions explicitly recorded.

### 3. Implementation-readiness gate

Invoke the Implementation Readiness Review skill with the SRS, STS, versions, target scope, and available code/build/test/simulator/ECU/HIL context. Do not author or silently repair the SRS or STS during this stage.

Return exactly one readiness verdict from that skill:

- `READY`
- `READY WITH CONDITIONS`
- `NOT READY`

Do not write production code or automated tests as part of this pipeline. A `NOT READY` verdict returns the work to the owning SRS or STS stage; a `READY WITH CONDITIONS` verdict carries its conditions into the next implementation plan.

`READY WITH CONDITIONS` authorizes planning or explicitly scoped work only; it is not blanket approval to implement beyond the listed conditions.

### 4. Implementation backlog and delivery gate

Invoke [Implementation Backlog and Traceability](../implementation-backlog-traceability/SKILL.md) with the approved SRS, STS, readiness report, repository revision, and delivery preferences. It must create ordered vertical-slice work packages, an implementation packet for the first eligible slice, and a bidirectional SRS → STS → work → branch/MR/commit → evidence matrix.

Do not pass the entire SRS/STS to an implementer without a selected work ID and explicit in-scope/out-of-scope boundary. A `READY WITH CONDITIONS` result limits backlog eligibility to work whose conditions are satisfied.

Each approved bounded work package may be committed locally and prepared for delivery. Require a separate explicit approval immediately before pushing or creating/updating its draft merge request, then require another explicit approval before merge. Record the remote, branch, commit, MR, CI, and verification evidence in the matrix. If the Git provider or remote is unavailable, report that fact instead of claiming that push or MR creation succeeded.

## Required handoff

At every stage, report:

1. Current stage and gate status.
2. Input documents and versions.
3. Output artifacts and paths, when the user supplied or requested a location.
4. Decisions needed before the next stage.
5. Traceability or review gaps that remain.
6. Branch, commit, push, MR, and CI status when implementation delivery has begun.

At completion, include the final readiness verdict, backlog status, delivery status, and next allowed action. Do not claim the pipeline is complete if a required gate is waiting for a user decision or if a promised push/MR action lacks evidence.
