# 완성된 모듈 예제: 속도 신호

배포용 차량 소프트웨어가 아닌 학습용 로컬 Python 모델이다. 원본, SRS, STS, 이슈 결정, 작업 패킷, 코드, 시험 결과, 최종 전달이 어떻게 연결되는지 보여준다. 최종 진입점은 [모듈 목차](docs/modules/speed-signal/README.md)다.

이 디렉터리에서 `python3 -m unittest discover -s tests -v`를 실행할 수 있다. `garden-beam/scripts/report-module-coverage.py docs/modules/speed-signal --lang ko`로 [완료 보고서](docs/modules/speed-signal/05-verification/completion-report.md)를 다시 만들고, `validate-module-delivery.py docs/modules/speed-signal`로 구조를 확인한다. 이 예제의 필수 검증 환경은 로컬 Python 모델뿐이다. ECU·HIL·차량·안전·릴리스 판단은 범위 밖이다.

[스킬·결과 점검](skill-audit.md)에 각 스킬이 예제의 어떤 산출물로 나타났는지와 실행하지 못한 게이트를 기록했다.
