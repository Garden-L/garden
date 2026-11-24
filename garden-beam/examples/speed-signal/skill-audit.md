# 이 예제의 스킬·결과 점검

작성한 예제를 스킬 라이브러리와 비교한 기록이다. 독립 에이전트가 언제나 같은 품질로 작성한다는 증거는 아니다. 이 저장소에서 예제를 작성한 뒤 코드와 구조 검사를 로컬에서 실행했다.

완성된 [SRS](docs/modules/speed-signal/01-srs/SRS.md)는 공통 참고 형식의 문서 정보, 목적·범위, 맥락, 시나리오, 요구사항, 인터페이스·데이터, 제약, 이슈, 참조, 개정 이력을 따른다. [STS](docs/modules/speed-signal/02-sts/STS.md)는 문서 정보, 목적·범위, 근거·추적성, 환경, 전략, 사례·절차, 결과·이슈, 개정 이력을 따른다. 예제는 형식을 보여주지만 스킬은 다른 명확한 구성을 허용한다.

구조 검사기는 완성 예제를 수용하고 `TC` 연결·제목 앵커·완료 보고서를 일부러 깨뜨린 복사본을 거부했다. 커버리지 생성기는 일부러 제거한 근거 파일을 공백으로 표시했다. 이 검사는 결과물 계약을 시험하며 에이전트의 판단을 증명하지는 않는다.

| 스킬 / 계약 | 기대 판단·결과 | 예제 근거 | 결과 |
| --- | --- | --- | --- |
| `workflow-design` | 원본에서 검증된 로컬 결과까지 확인 가능한 단계 전달 | [모듈 목차](docs/modules/speed-signal/README.md), [작업 패킷](docs/modules/speed-signal/04-implementation/WORK-001.md), [검증](docs/modules/speed-signal/05-verification/verification.md) | 좁은 로컬 범위에 있음 |
| `specification` + `writing-requirements-spec` | 출처와 수용 조건이 있는 `REQ`를 범위·맥락·미결사항과 연결한 SRS | [SRS](docs/modules/speed-signal/01-srs/SRS.md), [원본](docs/modules/speed-signal/source.md) | 있음 |
| 자동차 SRS 플레이북 + `writing-requirements-spec` | 차량·전원 맥락과 근거 없는 동작의 표시 | [REQ-005](docs/modules/speed-signal/01-srs/SRS.md), [ISSUE-001](docs/modules/speed-signal/01-srs/issues.md) | 로컬 모델에 있음 |
| 자동차 STS 플레이북 + `writing-test-spec` | `REQ`→`TC`와 시험 공백을 연결하고, 기법·실행 단계·기대 결과를 정리한 STS | [STS](docs/modules/speed-signal/02-sts/STS.md), [시험](tests/test_speed_signal.py) | 있음 |
| `decision` | 관찰·이유·선택지·책임자 결정·반영·근거를 갖춘 단일 이슈 | [issues.md](docs/modules/speed-signal/01-srs/issues.md) | 있음. 책임자는 가상 |
| 자동차 피처 플레이북 + 공용 원칙 | 동작 근거를 갖춘 제한된 구현 | [WORK-001](docs/modules/speed-signal/04-implementation/WORK-001.md), [추적성](docs/modules/speed-signal/traceability.md) | 있음. 커밋·MR 없음 |
| `verification` + 자동차 검토 | 실제 실행, 환경 한계, 근거 있는 최종 판단 | [시험 출력](docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt), [검증](docs/modules/speed-signal/05-verification/verification.md) | 로컬 시험 5개 통과. 대상 실행 없음 |
| 모듈 산출물 계약 | 필수 파일과 유효한 ID 연결 | 구조 검사 결과, [완료 보고서](docs/modules/speed-signal/05-verification/completion-report.md) | 구조 검사 통과. 집계값은 기록에서 도출 |

## 한계와 다음 에이전트 시험

별도 작성·검토 에이전트, 실제 책임자의 승인, ECU/HIL, 예제 커밋·MR은 없었다. 이 게이트들은 **검증되지 않았다**. README의 `Verified`는 의도적으로 좁힌 로컬 Python 모델 범위에만 적용된다.

새 에이전트의 동작을 확인하려면 완성 예제 대신 [source.md](docs/modules/speed-signal/source.md), 대상 프로젝트 경로, `$garden-beam` 진입점만 제공한다. SRS·STS 초안을 요청해 `SRC-5`를 실제 책임자 결정 전까지 열어 두는지, 적절한 시험 기법을 적용하는지, 근거 범위 안에서만 주장하는지 확인한다. [산출물 계약](../../docs/module-deliverables.md)과 대조한다. 구조 검사 통과만으로 충분하지 않다.
