# Automotive module deliverables

Use this contract when an automotive task produces requirements, tests, code, or verification evidence for a module. The selected [playbook](../playbooks/) decides which artifacts the task needs and when they are ready for handoff. This document defines the links and status meanings those artifacts share; it does not require every module to produce every document below.

## Shared links

Keep a path from each in-scope source obligation to its derived `REQ`, planned `TC`, applicable `WORK`, changed code or tests, and actual evidence. Use stable IDs and identify source and artifact revisions. An absent link is pending or out of scope with a reason; it is never implied to be complete. Keep one canonical `ISSUE` record for an ambiguity, conflict, or decision and link it from affected artifacts.

| When the task needs it | Artifact and useful content |
| --- | --- |
| Requirements definition | SRS with source-linked `REQ` IDs, observable conditions, assumptions, and open issues |
| Test design | STS with `REQ`-linked `TC` IDs, setup, stimulus, expected result, pass criterion, and test gaps |
| Code change | Bounded `WORK` record or equivalent linking acceptance criteria, affected `REQ`/`TC`, code, and checks |
| Approved baseline change | Decision and impact record linking affected requirements, tests, work, and the condition for resuming dependent work |
| Executed verification | Environment, revision, procedure, expected and observed results, evidence location, and unverified checks |
| Module handoff | Index or traceability view that links the artifacts actually produced and states the supported conclusion and gaps |

The project may use its existing artifact names and locations. Keep code and automated tests in its normal source tree. Store logs or traces at a stable location and link them. A planned check does not count as executed evidence. Distinguish local results from integration, ECU, HIL, vehicle, and release evidence.

## Decisions and conclusions

If an `ISSUE` has a status, use `Open` for no accepted resolution, `Decided` for an owner's choice, `Applied` for the corresponding artifact or code change, and `Verified` only after checking the result against evidence. Preserve earlier decisions when they are superseded.

State a module conclusion only for its declared scope and environment. `Verified` requires supported requirements, linked tests and work where applicable, and executed evidence at the required environment. `Verified with gaps` names pending or unresolved obligations and their consequences. `Not verified` means the evidence cannot support a delivery conclusion. Never promote a local simulation result into an ECU, HIL, vehicle, or release claim.

## Worked layout and checks

The [speed-signal example](../examples/speed-signal/README.md) uses `docs/modules/<module>/` with numbered SRS, STS, readiness, implementation, and verification folders. That layout demonstrates one complete module handoff; use equivalent project locations when appropriate. Its [coverage reporter](../scripts/report-module-coverage.py) generates a derived `completion-report.md` from recorded links, and its [structure checker](../scripts/validate-module-delivery.py) checks that example's full file set and IDs. Neither check proves requirement meaning or target behavior. Follow the selected playbook for the task's actual output and checks.
