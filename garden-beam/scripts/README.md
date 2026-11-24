# 패키지 스크립트

스크립트는 결정론적이고 다시 실행해도 안전하며 패키지 범위 안에서 동작해야 한다. 판단을 셸 코드에 숨기기보다 검증하거나 감사 가능한 산출물을 만든다. `validate-structure.sh`는 패키지 구조를, `validate-module-delivery.py <docs/modules/module>`은 완료된 모듈의 ID·링크를 확인한다. `report-module-coverage.py <docs/modules/module>`은 기록된 요구사항·시험·작업을 `05-verification/completion-report.md`로 집계한다. 보고서를 실제 검증 근거와 대조한다.
