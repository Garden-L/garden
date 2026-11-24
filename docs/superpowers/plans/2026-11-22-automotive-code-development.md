# 자동차 코드 개발 흐름 계획

> **작업 에이전트:** 이 세션에서 실행한다. 기존 공용 스킬과 SRS/STS 작성·전문 검토 파일을 보존한다.

**목표:** 자동차 패키지가 준비성 검토와 작업 계획부터 구현, 시험, 코드 검토, 검증, 릴리스까지 실제 코드 개발을 지원하게 한다.

**구조:** `automotive-engineering`을 간결한 라우터로 유지한다. pstack의 피처·버그 수정·리팩토링·검토·배포 흐름을 참고한 작업별 플레이북을 추가한다. 기존 공용·자동차 스킬을 이름으로 조합하고 승인된 SRS/STS 결과를 코드 개발 단계에 연결한다.

**기술:** Markdown 스킬과 플레이북, 기존 패키지 검사 스크립트.

**범위:** SRS/STS 작성 스킬과 도메인 검토 파일을 제외한 자동차 패키지 변경. 공용 스킬 본문은 유지한다.

## 작업

1. [x] 라우터가 기존 문서 단계와 코드 개발 흐름을 함께 선택하게 한다.
2. [x] 피처, 버그 수정, 리팩토링, 통합·시스템 시험, 코드 검토, 릴리스 준비 플레이북을 추가한다.
3. [x] SRS/STS 세부 절차를 바꾸지 않고 준비성, 백로그, 범위가 정해진 구현, 검증, 모듈 인계를 연결한다.
4. [x] 패키지 문서와 구조 검사를 전체 수명주기에 맞게 수정한다.
5. [x] 링크, 스킬 이름, 패키지 구조를 확인하고 SRS/STS와 공용 스킬이 바뀌지 않았는지 diff를 검토한다.

## 검증 근거

- `bash garden-beam/scripts/validate-structure.sh` — 통과.
- `python3 garden-beam/scripts/validate-module-delivery.py garden-beam/examples/speed-signal/docs/modules/speed-signal` — 통과.
- `python3 garden-beam/scripts/report-module-coverage.py ... --output /tmp/automotive-module-coverage-check.md` — 보고서 생성 성공.
- `python3 -m unittest discover -s garden-beam/examples/speed-signal/tests -v` — 시험 5개 통과.
- `python3 skills/skill-design/scripts/validate-library.py` — 통과. 당시 활성 스킬 20개.
- 영어·한국어 플레이북의 상대 링크 검사 — 통과.
- `git diff --check` — 통과.
