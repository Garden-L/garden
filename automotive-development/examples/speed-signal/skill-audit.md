# Skill-to-output audit for this example

This audit checks the authored example against the skill library. It is not evidence that an independent agent will always produce the same quality. The scenario was authored in this repository, then its code and structural checks were run locally.

The completed [SRS](docs/modules/speed-signal/01-srs/SRS.md) follows the shared SRS reference's document information, purpose/scope, context, scenarios, requirements, interfaces/data, constraints, issues, references, and revision history. The completed [STS](docs/modules/speed-signal/02-sts/STS.md) follows the shared STS reference's document information, purpose/scope, basis/traceability, environment, strategy, cases/procedures, results/issues, and revision history. These examples model the formats; the skills allow other clear layouts.

The structural validator accepted the complete example and rejected deliberate copies with a broken `TC` link, a broken heading anchor, or a stale completion report. The coverage generator marked a deliberately removed evidence file as a gap. These checks exercise the output contract, not the agent's reasoning.

| Skill or contract | Expected decision/output | Example evidence | Result |
| --- | --- | --- | --- |
| `workflow-design` | Checkable stage handoffs from source to verified local result | [module index](docs/modules/speed-signal/README.md), [work packet](docs/modules/speed-signal/04-implementation/WORK-001.md), [verification](docs/modules/speed-signal/05-verification/verification.md) | Present for this narrow scope |
| `specification` + `spec-requirements` | Sourced, evaluable `REQ` obligations; acceptance conditions near claims | [SRS](docs/modules/speed-signal/01-srs/SRS.md) and [source](docs/modules/speed-signal/source.md) | Present |
| Automotive SRS playbook + `spec-requirements` | Vehicle/power context; unsupported behavior visible | [REQ-005](docs/modules/speed-signal/01-srs/SRS.md) and [ISSUE-001](docs/modules/speed-signal/01-srs/issues.md) | Present for local model |
| Automotive STS playbook + `spec-tests` | `REQ`→`TC`, applicable technique, executable steps, expected results | [STS](docs/modules/speed-signal/02-sts/STS.md), [tests](tests/test_speed_signal.py) | Present |
| `decision` | One issue record with observation, why, options, owner choice, application, proof | [issues.md](docs/modules/speed-signal/01-srs/issues.md) | Present; owner choice is fictional |
| Automotive feature playbook + shared principles | Bounded implementation with behavior evidence | [WORK-001](docs/modules/speed-signal/04-implementation/WORK-001.md), [traceability](docs/modules/speed-signal/traceability.md) | Present; no commit or MR |
| `verification` + automotive review | Real run, environment limit, supported final verdict | [test output](docs/modules/speed-signal/05-verification/evidence/unittest-2026-11-22.txt), [verification](docs/modules/speed-signal/05-verification/verification.md) | Five local tests passed; no target run |
| Module artifact contract | Required files and valid ID links | `validate-module-delivery.py` output; [completion report](docs/modules/speed-signal/05-verification/completion-report.md) | Structural check passed; counts are derived |

## Limits and next agent-level check

No separate author/reviewer agents ran, no actual stakeholder authorized a decision, no ECU/HIL was used, and no commit or MR was created for the example. Those gates are **not verified** by this audit. The final `Verified` verdict in the module README applies only to the deliberately narrow local Python model.

To test the package behavior with a new agent, provide only [source.md](docs/modules/speed-signal/source.md), a target-project location, and the `$automotive-development` entry point. Ask the agent to draft an SRS and STS from the source without showing the completed example. Check whether it leaves `SRC-5` unresolved for a real owner, applies suitable test techniques, and limits claims to the available evidence. Compare that result to the [artifact contract](../../docs/module-deliverables.md); a successful structural check alone is insufficient.
