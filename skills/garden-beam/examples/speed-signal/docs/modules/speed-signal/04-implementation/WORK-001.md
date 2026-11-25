# WORK-001 — 로컬 속도 감시기

**베이스라인:** [SRS 개정 1](../01-srs/SRS.md), [STS 개정 1](../02-sts/STS.md), [ISSUE-001 결정](../01-srs/issues.md#issue-001--전원-종료와-시간-초과). **상태:** 로컬 구현·시험 검증. **책임자:** 예시 구현 담당자. **리비전:** 이 예제 패키지. 특정 커밋 SHA나 MR을 주장하지 않는다.

**범위:** 작은 Python 모델에서 `REQ-001`~`REQ-005`와 `TC-001`~`TC-005`를 구현한다. **허용 파일:** `src/speed_signal.py`, `tests/test_speed_signal.py`, 예제 문서. **범위 밖:** ECU 인터페이스, 버스 인코딩, 하드웨어 시간, 안전 적합성, 제품 릴리스.

**의존성과 결정:** `REQ-005`·`TC-005` 구현 전에 로컬 모델에 대한 `ISSUE-001`을 결정한다. SRS의 0.1 km/h 단위 정수와 정수 ms를 사용한다. 다른 공개 인터페이스나 스키마 변경은 없다.

**구현:** [소스](../../../../src/speed_signal.py), [단위 시험](../../../../tests/test_speed_signal.py). **검사 명령:** 예제 루트에서 `python3 -m unittest discover -s tests -v`. **수용:** 연결된 사례 다섯 개가 모두 통과한다. **관찰 결과:** 다섯 개 통과. [로그](../05-verification/evidence/unittest-2026-11-22.txt)와 [검증 기록](../05-verification/verification.md)을 참조한다.

**롤백:** 이 예시 모듈만 제거한다. ECU 통합이나 배포 산출물은 없다. **전달 게이트:** push, MR, merge, 릴리스를 주장하지 않는다.
