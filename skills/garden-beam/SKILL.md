---
name: garden-beam
description: 요구사항, 코드개발, 검증 등 사양 기반 소프트웨어 개발을 위한 작업에 적합하다. /garden-beam 또는 이 스타일로 작업해 달라는 요청에 사용하십시오.
---

# GARDEN-BEAM

플레이북이 이름으로 호출한 공용 원칙은 이 파일을 기준으로 `../<name>/SKILL.md`로 번들로 제공되며, 내부에서 호출되는 스킬은 해당 경로를 참조한다.

## 전체 원칙

# 플레이북

작업을 먼저 아래 플레이북 중 하나에 연결합니다. 연결한 파일의 전체 단계를 읽고, 수행할 단계를 할 일 목록 도구에 먼저 복사한 뒤 순서대로 실행합니다. 파일명은 `playbooks/<title>.md` 형식의 kebab-case를 그대로 사용합니다.

- 요구사항·시험 명세 산출물 작성: `playbooks/specification-artifacts.md`
- 기능 추가·동작 변경: `playbooks/feature.md`
- 기대 동작과 다른 비의도 동작의 재현·원인 조사·수정: `playbooks/bug-fix.md`
- 승인된 외부 동작을 유지하는 내부 구조 변경: `playbooks/refactoring.md`
- 구성요소 경계·공유 인터페이스·구조를 바꾸는 작업: `playbooks/architecture-change.md`
- 승인된 SRS·STS·인터페이스·시험 기대값·인수 기준 변경: `playbooks/change-control.md`

이 목록에 맞는 플레이북이 없으면 기존 플레이북을 억지로 적용하지 말고, 작업을 미결 상태로 기록하고 작업이 없음을 알립니다.
