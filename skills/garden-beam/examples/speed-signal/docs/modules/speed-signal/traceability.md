# 속도 신호 추적성

[원본 메모](source.md), [SRS](01-srs/SRS.md), [STS](02-sts/STS.md), [이슈 기록](01-srs/issues.md), [작업 패킷](04-implementation/WORK-001.md), [코드](../../../src/speed_signal.py), [시험](../../../tests/test_speed_signal.py), [검증](05-verification/verification.md)을 연결한다. 아래 근거는 모두 로컬 Python 실행에만 해당한다.

| 출처 | 요구사항 | 시험 | 결정 | 작업 | 코드 / 시험 | 근거 | 상태 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | REQ-001 | TC-001 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | 로컬 검증 |
| SRC-2 | REQ-002 | TC-002 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | 로컬 검증 |
| SRC-3 | REQ-003 | TC-003 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | 로컬 검증 |
| SRC-4 | REQ-004 | TC-004 | — | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | 로컬 검증 |
| SRC-5 | REQ-005 | TC-005 | ISSUE-001 | WORK-001 | `src/speed_signal.py` / `tests/test_speed_signal.py` | `docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt` | 로컬 검증 |

`SRC-5`는 기록된 공백이고 `REQ-005`는 예시 결정으로 생긴 의무다. 실제 대상 개발에서는 로컬 근거를 관련 ECU·HIL·차량 결과로 보완하고 판단을 다시 내려야 한다.
