# 구현 보고서

**작업 항목:** [WORK-001](WORK-001.md). **베이스라인:** [SRS](../01-srs/SRS.md), [STS](../02-sts/STS.md), [ISSUE-001](../01-srs/issues.md). **결과:** 로컬 구현 완료, 로컬 시험 5개 통과.

## 변경 내용

- [speed_signal.py](../../../../src/speed_signal.py)에 범위 수용, 잘못된 값, 엄격한 시간 초과, 세 메시지 복구, 결정된 로컬 전원 종료 초기화를 구현했다.
- [test_speed_signal.py](../../../../tests/test_speed_signal.py)에 `TC-001`~`TC-005` 동작 시험을 추가했다.
- ECU 통합, 제품 코드, 커밋, MR은 이 예제에 포함되지 않는다.

## 검사

예제 루트에서 `python3 -m unittest discover -s tests -v`를 실행했다.

**관찰 결과:** 시험 5개 통과. [저장한 출력](../05-verification/evidence/unittest-2026-11-22.txt)을 참조한다. 로컬 예제 실행에 한정된 결과다.

## 차이와 남은 작업

로컬 예제에서 `WORK-001`과 다른 점은 없다. ECU/HIL 적용, 물리적 시간, 진단, 안전, 릴리스 작업은 표현하거나 검증하지 않았다.
