# Development Skills Library

Reusable skills for software and systems development, organized by the kind of work they support. Domain packages compose these skills into workflows for areas such as automotive development.

## Skills

- [`engineering-design`](skills/engineering-design/SKILL.md) — frame inputs, architecture, readiness, and proposed baseline changes.
- [`specification`](skills/specification/SKILL.md) — create requirements and test specifications with traceability.
- [`spec-requirements`](skills/spec-requirements/SKILL.md) — create an SRS with stable IDs and traceable requirements; its format and example are references.
- [`spec-tests`](skills/spec-tests/SKILL.md) — create an STS with traceable cases and suitable test design techniques; its format and example are references.
- [`review`](skills/review/SKILL.md) — assess changes and deliverables with evidence, prioritized findings, and a clear verdict.
- [`implementation`](skills/implementation/SKILL.md) — implement bounded work with TDD and reusable tooling.
- [`verification`](skills/verification/SKILL.md) — review changes, evidence, risk, and traceability before delivery.
- [`decision`](skills/decision/SKILL.md) — compare meaningful options, recommend a choice, and connect important decisions to follow-through.
- [`workflow-design`](skills/workflow-design/SKILL.md) — connect stage inputs, outputs, decisions, and checks to a reviewable result.
- [`skill-design`](skills/skill-design/SKILL.md) — name, scope, compose, and check skills added to this library.

## Reasoning skills

- [`why`](skills/why/SKILL.md) — explain causes, consequences, and the evidence behind a judgment.
- [`how`](skills/how/SKILL.md) — show actionable options, tradeoffs, and a checkable path forward.

## Parked skills

These skills are retained outside the active library for now:

- `programming-coursebook-authoring`
- `git-hygiene`

## Automotive development package

[`automotive-development`](automotive-development/README.md) is a project-style package. Its pipeline skill and playbooks compose reusable skills above with automotive-specific requirements, testing, readiness, implementation, verification, and baseline-change skills.

For source requirements through verified code on one module, use its [module delivery playbook](automotive-development/skills/automotive-engineering/playbooks/module-delivery.md), [artifact contract](automotive-development/docs/module-deliverables.md), and [completed local example](automotive-development/examples/speed-signal/README.md). The contract fixes output locations and cross-links; SRS and STS prose remains flexible.

The automotive package is included in this bundle. Its orchestration entry point is [`automotive-engineering`](automotive-development/skills/automotive-engineering/SKILL.md); domain-specific skills are selected by that router. Git credentials, repository remotes, CI, test runners, and HIL/ECU environments are external prerequisites, not installable skills.

After SRS/STS readiness, the automotive code workflow plans bounded work packets and routes each one through feature development, bug fixing, or refactoring. Integration testing, code review, implementation verification, and release readiness have distinct playbooks and evidence gates.

Each active skill has its own directory directly under `skills/`. Domain packages compose the shared skills with domain-specific context and gates.

## Install the skill bundle

This repository is organized as one skill bundle: shared skills and domain packages such as automotive development live together. Register the repository using the bundle mechanism supported by your agent. Once registered, invoke skills by name; workflow documents refer to shared skills by name rather than depending on this repository's directory layout.

English skill files are the canonical, version-controlled source. Matching Korean translations are kept locally under `skills-ko/` and `automotive-development-ko/` with the same instructional layout; both Korean directories and `trash/` are ignored by Git and are not committed.

## Skill placement

When creating a skill, apply [`skill-design`](skills/skill-design/SKILL.md): check whether an existing skill owns the method and whether it works beyond the project that prompted it. Place reusable methods in `skills/`; keep domain-specific context, standards, and lifecycle gates inside the relevant package, such as `automotive-development/skills/`.

Do not generalize a skill based only on a possible future use. Identify at least one concrete use outside its originating project and confirm that the core guidance still works there without importing domain-specific assumptions. If that test is not met, keep the skill with its project. When a shared skill is useful to a project package, link it from that package's README and from the relevant router or playbook so agents can discover and load it at the point of use.
