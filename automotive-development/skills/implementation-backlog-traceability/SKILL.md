---
name: implementation-backlog-traceability
description: Use when an approved or readiness-reviewed SRS and STS must be converted into small, reviewable implementation work packages with bidirectional traceability to tests, commits, and merge requests.
---

# Implementation Backlog and Traceability

Convert a baselined SRS/STS and readiness result into small implementation units. This skill plans and controls the work; it does not silently change requirements or write production code.

## 1. Apply the readiness gate

Record the SRS, STS, readiness-review, and repository revisions.

- `NOT READY`: stop; report blockers.
- `READY WITH CONDITIONS`: plan only work whose conditions are satisfied; carry the other conditions into the affected work items and MRs.
- `READY`: continue while preserving open decisions and coverage gaps.

Never guess a requirement, interface, test oracle, safety constraint, or owner. Create an `ISSUE-###`/decision record and block affected work when the answer could change code or tests.

## 2. Create bounded work packages

Keep original SRS and STS IDs. Split the scope into the smallest independently observable vertical slices, not broad layer tasks. Make prerequisite interfaces or infrastructure explicit.

Each `WORK-###` must state:

```text
purpose / observable behavior
SRS IDs and STS IDs
readiness conditions, decisions, and dependencies
in-scope components/files/interfaces
out-of-scope behavior and refactors
acceptance criteria and verification evidence
branch, commit, MR, and rollback plan
```

Before implementation, publish an implementation packet with exact files, API/data/schema effects, tests, diff estimate, and stop conditions. Use project limits when supplied; otherwise treat 5–10 files and roughly 300 changed lines as review triggers. Split or explicitly justify larger work.

Stop and request approval if the work would expand its boundary, change a baselined SRS/STS or public contract, alter schema/wire behavior, change safety/security/diagnostic/timing assumptions, or revise acceptance criteria.

## 3. Execute one unit at a time

```text
select eligible WORK-ID
→ publish packet and create branch/draft MR
→ run mapped behavior tests
→ make the smallest in-scope change
→ run mapped and regression checks
→ update matrix with commit, MR, CI, and evidence
→ review and merge only after gates pass
```

Code existing is not completion. Mark a work item complete only when its tests and required reviews have evidence. Keep integration, HIL, hardware, or release checks as `Pending environment` until they run.

## 4. Maintain bidirectional traceability

Use one row per relationship:

| SRS ID | STS ID | WORK-ID | Component/interface | Branch/MR | Commit | Status | Evidence | Gap/decision |
|---|---|---|---|---|---|---|---|---|

Check for requirements without tests/work, tests without requirements, work without requirement/test links, and commits/MRs missing from the matrix. Keep gaps visible. Valid statuses are `Planned`, `In progress`, `Verified`, `Pending environment`, `Blocked`, and `Rejected`.

## 5. Delivery approvals

After each bounded unit, the agent may create a local branch, commit only the approved scope, and prepare the MR title/body and evidence. Treat these as separate external gates:

1. **Push/MR approval** — obtain explicit approval immediately before pushing the branch or creating/updating the draft MR. Then record branch, commit, MR, CI, and evidence in the matrix.
2. **Merge approval** — obtain a separate explicit approval after required reviews, tests, and CI pass. Never merge on the basis of push/MR approval alone.

Use the connected Git provider when available. If a requested push or MR action fails, report the exact failure and never claim success. Never push out-of-scope changes.

## Required output

Return, in this order:

1. **Baseline and gate** — versions, repository revision, scope, verdict.
2. **Conditions and decisions** — blockers, owners, affected work.
3. **Implementation backlog** — ordered packages, dependencies, boundaries.
4. **Traceability matrix** — SRS ↔ STS ↔ work ↔ branch/MR/commit ↔ evidence.
5. **First implementation packet** — files, tests, limits, stop conditions.
6. **Delivery plan** — local commit, push/MR approval gate, CI, and separate merge approval gate.

Do not pass the entire SRS/STS to an implementer without a selected work ID and explicit boundary. Do not claim tests, CI, push, or MR creation without evidence.
