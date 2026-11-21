# Development Skills Library

Reusable skills for software and systems development, organized by the kind of work they support. Domain packages compose these skills into workflows for areas such as automotive development.

## Skills

- [`engineering-design`](skills/engineering-design/SKILL.md) — frame inputs, architecture, readiness, and proposed baseline changes.
- [`specification`](skills/specification/SKILL.md) — create requirements and test specifications with traceability.
- [`spec-requirements`](skills/spec-requirements/SKILL.md) — create an SRS with stable IDs and traceable requirements; its format and example are references.
- [`spec-tests`](skills/spec-tests/SKILL.md) — create an STS with traceable cases and suitable test design techniques; its format and example are references.
- [`implementation`](skills/implementation/SKILL.md) — implement bounded work with TDD and reusable tooling.
- [`verification`](skills/verification/SKILL.md) — review changes, evidence, risk, and traceability before delivery.

## Reasoning skills

- [`why`](skills/why/SKILL.md) — explain causes, consequences, and the evidence behind a judgment.
- [`how`](skills/how/SKILL.md) — show actionable options, tradeoffs, and a checkable path forward.

## Parked skills

These skills are retained outside the active library for now:

- [`programming-coursebook-authoring`](trash/skills/programming-coursebook-authoring/SKILL.md)
- [`git-hygiene`](trash/skills/git-hygiene/SKILL.md)

## Automotive development package

[`automotive-development`](automotive-development/README.md) is a project-style package. Its pipeline skill and playbooks compose reusable skills above with automotive-specific requirements, testing, readiness, implementation, verification, and baseline-change skills.

The automotive package is included in this bundle. Its orchestration entry point is [`automotive-engineering`](automotive-development/skills/automotive-engineering/SKILL.md); domain-specific skills are selected by that router. Git credentials, repository remotes, CI, test runners, and HIL/ECU environments are external prerequisites, not installable skills.

Each active skill has its own directory directly under `skills/`. Domain packages compose the shared skills with domain-specific context and gates.

## Install the skill bundle

This repository is organized as one skill bundle: shared skills and domain packages such as automotive development live together. Register the repository using the bundle mechanism supported by your agent. Once registered, invoke skills by name; workflow documents refer to shared skills by name rather than depending on this repository's directory layout.

English skill files are the canonical, version-controlled source. Matching Korean translations are kept locally under `skills-ko/` with the same directory layout; `skills-ko/` and `trash/` are ignored by Git and are not committed.

## Skill placement

When creating a skill, first check whether its method applies beyond the project or domain that prompted it. Place reusable methods in the appropriate shared skill in `skills/`. Keep domain-specific context, standards, and lifecycle gates inside the relevant package, such as `automotive-development/skills/`.

Do not generalize a skill based only on a possible future use. Identify at least one concrete use outside its originating project and confirm that the core guidance still works there without importing domain-specific assumptions. If that test is not met, keep the skill with its project. When a shared skill is useful to a project package, link it from that package's README and from the relevant router or playbook so agents can discover and load it at the point of use.
