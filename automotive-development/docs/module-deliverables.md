# Automotive module deliverables

This contract applies when one automotive module is taken from source requirements through code delivery. It groups outputs by lifecycle stage without imposing a section order on the SRS or STS. Put the bundle in the consuming project's `docs/modules/<module>/` unless that project already has an equivalent location. Keep code and automated tests in the project's normal source tree.

## Artifact set

| Artifact | Purpose | Minimum useful content |
| --- | --- | --- |
| `README.md` | Module index and handoff | Scope, source versions/locations, current stage, links to stage folders, final verdict and remaining gaps |
| `01-srs/SRS.md` | Promised behavior | Stable `REQ` IDs, source for each obligation, observable acceptance condition, assumptions and issue links |
| `01-srs/issues.md` | SRS-stage issues | Source ambiguity, conflict, rationale, options, recommendation, decision state, affected `REQ` IDs |
| `01-srs/review.md` | SRS review results | Source coverage, actionable findings, disposition and unresolved questions |
| `02-sts/STS.md` | Planned verification | Stable `TC` IDs linked to `REQ`, design technique and reason, procedures, expected results and gaps |
| `02-sts/issues.md` | STS-stage issues | Undefined oracle, testability gap, test-scope choice, decision and affected `REQ`/`TC` IDs; state explicitly when none remain |
| `02-sts/review.md` | STS review results | Requirement coverage, test design adequacy, boundary/state/error cases, disposition and remaining gaps |
| `03-readiness/readiness-report.md` | Implementation entry decision | Baselines, readiness verdict, blockers/conditions, eligible first work |
| `04-implementation/WORK-<id>.md` | Bounded implementation packet | Approved baseline, scope, dependencies, code/test locations, commands and acceptance criteria |
| `04-implementation/implementation-report.md` | Work performed | Work IDs, changed code/tests, actual commands and results, commit/revision, deviations and remaining items |
| `05-verification/verification.md` | Evidence-based review | What ran, where, expected versus observed result, evidence, environment limits, conclusion and unverified checks |
| `05-verification/completion-report.md` | Derived coverage view | Per-`REQ` linked `TC`/`WORK`, recorded test status, evidence presence and gaps; generated from source records |
| `traceability.md` | End-to-end map | Source → `REQ` → `TC` → related `ISSUE` → `WORK` → code/test → evidence |
| `issues/` (optional) | Cross-stage issue records | Use when a single issue spans stages; stage folders link to the canonical record |

Keep issue lists beside the stage where they were found. Assign IDs uniquely across the module. When one issue affects multiple stages, retain one canonical record and link it from each affected stage. A stage with no issues can say so briefly. A planned module may not yet have code or executed tests: mark those links and results as pending. A delivered module has at least one implementation report and real verification evidence. Keep actual test logs or traces in `05-verification/evidence/` or another stable location and link them; never replace a result with a plan to run it. Generate `05-verification/completion-report.md` using `scripts/report-module-coverage.py` after updating the source records; do not hand-edit derived counts. It summarizes recorded coverage, not independently verified behavior.

## Decision and status semantics

Use `ISSUE` as the same stable identifier in all artifacts. One issue record owns the rationale. Other documents link the ID and state only. Record when the issue was discovered, the source and observed conflict or gap, why it matters, options and tradeoffs, recommendation, decision owner and decision, affected `REQ`/`TC`/`WORK`, and evidence that the decision was applied and checked. The common `decision` skill owns the selection and follow-through principles. The automotive `baseline-change-control` skill owns changes to an already approved SRS or STS.

Use states with distinct meanings: `Open` means no accepted resolution; `Decided` means the owner chose a response; `Applied` means affected artifacts and code were changed; `Verified` means the result was checked against evidence. Do not advance a state on intent alone. If a decision requires no code, state why and point to the checked affected artifacts. Reopen or supersede a record with an explicit link rather than erasing its earlier decision.

The module's final verdict is `Verified`, `Verified with gaps`, or `Not verified`. `Verified` requires every in-scope `REQ` to have a supported `TC`, implemented `WORK`, and executed evidence at the required environment. `Verified with gaps` names each unresolved or pending requirement and its consequence. `Not verified` means the evidence cannot support a delivery conclusion. A local simulation never proves ECU, HIL, vehicle, or release behavior.

## Stage handoff

| Stage | Exit artifact and check |
| --- | --- |
| Frame | `README.md` names source revisions, boundaries, target, and initial gaps |
| SRS | `01-srs/` contains SRS, stage issues, and review disposition |
| STS | `02-sts/` contains STS, stage issues, and linked test cases; undefined expected behavior remains a gap |
| Readiness | `03-readiness/` records verdict and eligible first `WORK` |
| Implementation | `04-implementation/` contains bounded work packets and an implementation report |
| Verification | `05-verification/` compares actual results to SRS/STS and decisions; regenerate completion report, then update README and traceability |

The [full workflow](../skills/automotive-engineering/playbooks/module-delivery.md) selects the existing stage skills. The [worked example](../examples/speed-signal/README.md) shows the bundle in a small runnable project. `scripts/validate-module-delivery.py` checks structural links and IDs; human review still decides whether requirements, tests, and evidence mean the right thing.
