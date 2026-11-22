# Speed signal traceability

This map uses the [source notes](source.md), [SRS](01-srs/SRS.md), [STS](02-sts/STS.md), [issue record](01-srs/issues.md), [work packet](04-implementation/WORK-001.md), [code](../../../src/speed_signal.py), [tests](../../../tests/test_speed_signal.py), and [verification](05-verification/verification.md). Every evidence claim below refers to the local Python run only.

| Source | Requirement | Test | Decision | Work | Code / test | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | REQ-001 | TC-001 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | Local verified |
| SRC-2 | REQ-002 | TC-002 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | Local verified |
| SRC-3 | REQ-003 | TC-003 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | Local verified |
| SRC-4 | REQ-004 | TC-004 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | Local verified |
| SRC-5 | REQ-005 | TC-005 | ISSUE-001 | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | Local verified |

`SRC-5` is the documented gap; `REQ-005` is the illustrative decision's resulting obligation. For actual target delivery, replace the local-only evidence with relevant ECU/HIL/vehicle results and reassess the verdict.
