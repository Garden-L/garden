# 속도 신호 모듈: 최종 전달

**범위:** 학습용 로컬 Python 속도 감시기. **원본:** [가상 원본 메모](source.md), 개정 1. **단계:** 로컬 구현·검증 완료. **판단:** 로컬 모델에서 `Verified`. ECU·HIL·차량·안전·릴리스 동작은 범위 밖이다.

| 산출물 | 결과 |
| --- | --- |
| [SRS 단계](01-srs/SRS.md) | `REQ-001`~`REQ-005`, 출처와 수용 조건, [단계 이슈](01-srs/issues.md) |
| [STS 단계](02-sts/STS.md) | `TC-001`~`TC-005`, 기법과 절차 |
| [준비성 단계](03-readiness/readiness-report.md) | 로컬 예제 범위와 진입 판단 |
| [구현 단계](04-implementation/implementation-report.md) | [WORK-001](04-implementation/WORK-001.md), 구현 내용과 로컬 시험 결과 |
| [검증 단계](05-verification/verification.md) | 로컬 실행, 근거, 대상 한계; [완료 보고서](05-verification/completion-report.md) |
| [추적성](traceability.md) | 원본, 요구사항, 시험, 작업, 코드, 근거 연결 |

구현은 [speed_signal.py](../../../src/speed_signal.py), 단위 시험은 [test_speed_signal.py](../../../tests/test_speed_signal.py), 로컬 실행 기록은 [시험 로그](05-verification/evidence/unittest-2026-11-22.txt)에 있다. ECU·HIL을 실행했다고 주장하지 않는다.
