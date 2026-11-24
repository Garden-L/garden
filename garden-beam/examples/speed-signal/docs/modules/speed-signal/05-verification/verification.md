# 속도 신호 검증 — 로컬 예제

**검토 주장:** 로컬 Python 모델이 [REQ-001~REQ-005](../01-srs/SRS.md)를 구현하고 다섯 [STS 사례](../02-sts/STS.md)처럼 동작한다. ECU·HIL·차량·안전·릴리스에 대한 주장이 아니다.

**환경:** 로컬 Python 3와 `unittest`. **명령:** 예제 루트에서 `python3 -m unittest discover -s tests -v`. **관찰:** 다섯 시험이 실행돼 통과했다. [보관한 출력](evidence/unittest-2026-11-22.txt)을 근거로 삼는다.

| 요구사항 | 시험 | 상태 | 관찰 결과 | 근거 |
| --- | --- | --- | --- | --- |
| REQ-001 | TC-001 | Pass | 유효한 양 끝값에서 플래그가 해제 상태 | [로그](evidence/unittest-2026-11-22.txt) |
| REQ-002 | TC-002 | Pass | 양쪽 범위 밖 값에서 플래그 설정 | [로그](evidence/unittest-2026-11-22.txt) |
| REQ-003 | TC-003 | Pass | 100 ms에는 해제, 101 ms에는 설정 | [로그](evidence/unittest-2026-11-22.txt) |
| REQ-004 | TC-004 | Pass | 세 번째 유효 메시지 뒤에만 해제 | [로그](evidence/unittest-2026-11-22.txt) |
| REQ-005 | TC-005 | Pass | 전원 종료가 상태를 지우고 시간 초과를 멈춤 | [로그](evidence/unittest-2026-11-22.txt) |

**결정 확인:** [ISSUE-001](../01-srs/issues.md#issue-001--전원-종료와-시간-초과)에 예시 책임자의 선택과 SRS·STS·구현 연결, 로컬 시험 근거가 있다. `Verified`는 로컬 모델 범위에 한정된다.

**결론:** 선언된 로컬 예제 범위에서 `Verified`. **관찰 밖:** ECU, HIL, 차량 통합, 물리적 시간 정확성, 진단 지속성, 안전, 릴리스. 어느 것도 실행하거나 승인하지 않았다. 제품 모듈이라면 자체 원본 결정과 대상 환경 근거가 필요하다.
