# 개발 스킬 라이브러리

소프트웨어와 시스템 개발에 재사용하는 작은 원칙 스킬을 모은 저장소다. `garden-beam`은 이 원칙을 작업별 플레이북으로 조합한다.

## 공용 스킬

- [`architecting`](skills/architecting/SKILL.md) — 의도한 동작과 제약을 만족하는 가장 단순한 구조를 선택한다.
- [`specification`](skills/specification/SKILL.md) — 의무를 출처와 판단 조건에 연결한다.
- [`writing-requirements-spec`](skills/writing-requirements-spec/SKILL.md) — 소프트웨어 요구사항 명세서를 일관된 문서로 작성한다.
- [`writing-test-spec`](skills/writing-test-spec/SKILL.md) — 요구사항과 시험 사례, 기대 결과, 시험 공백을 연결한 STS를 작성한다.
- [`review`](skills/review/SKILL.md) — 실제 결과를 의도와 적용 기준에 비춰 판단한다.
- [`work-decomposition`](skills/work-decomposition/SKILL.md) — 의존성, 책임, 확인 방법에 따라 작업 분할을 결정한다.
- [`verification`](skills/verification/SKILL.md) — 명시된 조건에서 실제 결과와 기대 결과를 비교한다.
- [`decision`](skills/decision/SKILL.md) — 선택지를 비교하고 근거 있는 결론을 권고한다.
- [`workflow-design`](skills/workflow-design/SKILL.md) — 단계 사이에 확인 가능한 결과와 인계를 둔다.
- [`skill-design`](skills/skill-design/SKILL.md) — 스킬의 이름, 범위, 적용 조건을 정한다.

## 작은 엔지니어링 원칙

특정 판단이 필요할 때 아래 스킬을 사용한다. 작업 순서는 플레이북이 정한다.

- [`minimal-change`](skills/minimal-change/SKILL.md) — 의도한 결과에 필요한 범위로 변경을 제한한다.
- [`change-impact-check`](skills/change-impact-check/SKILL.md) — 코드 작성 전 구조와 영향받는 작업을 살핀다.
- [`domain-model-first`](skills/domain-model-first/SKILL.md) — 로직 전에 핵심 데이터와 불변식을 정한다.
- [`boundary-discipline`](skills/boundary-discipline/SKILL.md) — 외부 입력을 시스템 경계에서 검증하고 변환한다.
- [`root-cause-first`](skills/root-cause-first/SKILL.md) — 결함의 원인을 추적한 뒤 수정한다.
- [`behavior-focused-tests`](skills/behavior-focused-tests/SKILL.md) — 내부 구조보다 관찰 가능한 동작을 시험한다.
- [`prove-real-result`](skills/prove-real-result/SKILL.md) — 완료를 주장하기 전에 실제 결과를 확인한다.

## 설명 원칙

- [`why`](skills/why/SKILL.md) — 근거, 원인, 결과를 연결해 이유를 설명한다.
- [`how`](skills/how/SKILL.md) — 선택지, 절충점, 실행 경로를 설명한다.

## 보류한 스킬

현재 활성 라이브러리 밖에 보관한다.

- `programming-coursebook-authoring`
- `git-hygiene`

## 개발 플레이북 패키지

[`garden-beam`](garden-beam/SKILL.md)이 요구사항, 시험, 작업 패키지, 구현, 검증을 잇는 진입 스킬이다. [플레이북](garden-beam/README.md)은 공용 원칙을 작업의 산출물, 근거, 승인 기준선과 조합한다.

[모듈 산출물 연결 기준](garden-beam/docs/module-deliverables.md)은 공통 연결을 설명하고, [속도 신호 예제](garden-beam/examples/speed-signal/README.md)는 한 가지 전체 배치를 보여 준다. Git 인증, 저장소 원격, CI, 시험 실행기와 대상 환경은 설치 가능한 스킬이 아니라 외부 준비 사항이다.

공용 원칙은 `skills/` 바로 아래의 각 디렉터리에 둔다. 도메인 패키지는 자체 `SKILL.md`를 진입점으로 사용한다.

## 스킬 묶음 설치

이 저장소에는 공용 스킬과 개발 플레이북 패키지가 함께 있다. 사용하는 에이전트의 스킬 묶음 등록 방법으로 저장소를 등록한 뒤 이름으로 호출한다. 플레이북은 저장소 배치에 의존하지 않도록 공용 스킬을 이름으로 가리킨다.

한국어 파일이 이 저장소의 원본이다. 영어 번역은 이후 별도로 작성한다.

## 스킬 배치

### 공용 원칙 스킬

공용 스킬 하나는 재사용 가능한 판단 하나를 맡는다. 제목과 본문에는 그 원칙의 적용 조건과 필요한 판단 규칙만 둔다. 프로젝트 표준, 산출물 경로, 작업 게이트, 도구를 끌어오지 않는다.

플레이북이 원칙을 선택한다. 공용 원칙은 플레이북을 이름으로 지시하거나 다음 작업 흐름을 결정하지 않는다. 예를 들어 `minimal-change`는 의도한 결과에 필요한 변경을 고르는 원칙만 다루고, 작업의 파일 범위나 기준선 변경 절차는 다루지 않는다.

설명란에는 **구체적인 행동과 구별되는 적용 조건**을 적는다. 비슷한 스킬과 구분할 단서는 포함하되 작업 단계와 인계 규칙은 플레이북에 둔다. 예를 들어 `architecting`은 구조 변경 전에 모듈·타입·시그니처·인터페이스 경계를 스케치하라고 안내하고, 코딩부터 하면 잘못된 구조가 굳어질 수 있는 작업에서 사용하도록 설명한다.

### 작업별 플레이북

`garden-beam/` 같은 플레이북 패키지는 공용 원칙을 구체적인 작업에 적용한다. 플레이북은 산출물, 경계, 순서, 근거, 결정 게이트를 정한다. 공용 원칙의 본문을 복사하지 않고 필요한 지점에서 호출한다.

코드 변경에서는 피처·버그 수정·리팩터링 플레이북이 `minimal-change`를 승인된 `WORK` 패키지에 연결한다. 파일과 수용 기준으로 범위를 정하고 추적성 및 기준선 변경을 다루는 규칙은 플레이북에 둔다.

스킬을 만들 때는 [`skill-design`](skills/skill-design/SKILL.md)으로 기존 책임과 배치 범위를 확인한다. 다른 프로젝트에서 실제로 재사용된 근거 없이 일반화하지 않는다. 저장소 공통 규칙은 [스킬 작성 원칙](docs/skill-authoring-principles.md)을 따른다.
