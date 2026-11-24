# 패키지 구조

```text
garden-beam/SKILL.md
        ↓ 자동차 작업 흐름 선택
garden-beam/playbooks/*.md
        ↓ 공용 원칙 및 일반 흐름 조합
skills/* + garden-beam/references/*
```

패키지 최상위 스킬은 자동차 작업을 분류하고 연결합니다. 자동차 SRS, STS, 피처, 버그 수정, 리팩토링, 승인 기준선 변경은 중첩 스킬이 아니라 플레이북입니다. 플레이북은 작은 공용 원칙과 일반 방법을 자동차 출처 규칙, 작업 범위, 근거, 승인 게이트와 조합합니다. 조건부 지침과 예제는 `references/`에 두고 필요한 경우에만 읽습니다.

[모듈 산출물 계약](module-deliverables.md)은 대상 프로젝트의 결과물 위치와 연결을 정합니다. 구조 검사는 `scripts/validate-module-delivery.py`가 담당하지만, 의미나 타깃 동작 검토를 대신하지 않습니다.
