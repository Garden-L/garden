# 스킬 라이브러리 분류 설계

## 의도

스킬이 지원하는 사고 종류와 실제 작업 영역을 기준으로 라이브러리를 묶는다. 도메인 패키지가 반복되는 파일 경로에 의존하지 않으면서 목록을 탐색하기 쉽게 한다.

## 목표

- 프레임, 빌드, 증명, 전달, 유지라는 목적 중심 범주를 사용한다.
- 자동차 개발 같은 도메인 흐름은 조합된 패키지로 유지한다.
- 파일을 옮기되 스킬 이름과 내용을 보존한다.
- 목차와 자동차 스킬 등록부를 새 위치로 갱신한다.

## 제외 범위

- 스킬 지침을 다시 쓰거나 호출 의미를 바꾸지 않는다.
- 에이전트 제품별 어댑터를 만들지 않는다.
- 새 스킬을 추가하거나 기존 스킬을 삭제하지 않는다.

## 제안 구조

```text
skills/
  frame/       # architect, input-review, change-impact
  build/       # software/tdd; automation/pattern-to-tool
  prove/       # verification, verification-evidence, traceability
  communicate/ # requirements, testing, learning/coursebook authoring
  sustain/     # git-hygiene
garden-beam/ # 도메인 작업 패키지
```

자동차 수명주기 스킬은 `garden-beam/skills/`에 두고 공용 스킬은 `skills/`의 목적별 하위 디렉터리로 옮긴다. 자동차 라우터가 이름·파일 등록부를 관리하며 플레이북은 스킬 이름만 사용한다.

## 대응표

- `frame`: architect, input-review, change-impact
- `build/software`: tdd
- `build/automation`: pattern-to-tool
- `prove`: verification, verification-evidence, traceability
- `communicate/requirements`: input-review는 frame에 유지하고 자동차 SRS는 도메인 전용으로 둔다.
- `communicate/testing`: 자동차 STS는 도메인 전용으로 둔다.
- `communicate/learning`: programming-coursebook-authoring
- `sustain`: git-hygiene

## 열린 구현 사항

자동차 전용 요구사항·시험 문서 스킬은 자동차 가정을 포함하므로 도메인 패키지에 남긴다. 중립적인 공용 목록으로 옮기지 않고 자동차 패키지 문서의 communicate 항목에서 안내한다.
