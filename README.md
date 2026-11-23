# Development Skills Library

Reusable skills for software and systems development, organized by the kind of work they support. Domain packages compose these skills into workflows for areas such as automotive development.

## Skills

- [`architecting`](skills/architecting/SKILL.md) — choose the simplest structure that meets the intended behavior and constraints.
- [`specification`](skills/specification/SKILL.md) — keep each obligation tied to its source and judgment condition.
- [`spec-requirements`](skills/spec-requirements/SKILL.md) — state one traceable, clear, verifiable obligation.
- [`spec-tests`](skills/spec-tests/SKILL.md) — connect a test case to its requirement and observable expected result.
- [`review`](skills/review/SKILL.md) — judge actual work against its intent and relevant criteria.
- [`work-decomposition`](skills/work-decomposition/SKILL.md) — choose direct, sequential, or parallel execution based on dependencies, ownership, and checks.
- [`verification`](skills/verification/SKILL.md) — compare actual results with explicit expectations under stated conditions.
- [`decision`](skills/decision/SKILL.md) — compare meaningful options, recommend a choice, and connect important decisions to follow-through.
- [`workflow-design`](skills/workflow-design/SKILL.md) — connect stage inputs, outputs, decisions, and checks to a reviewable result.
- [`skill-design`](skills/skill-design/SKILL.md) — name, scope, compose, and check skills added to this library.

## Small engineering principles

Use these focused skills when a specific judgment is needed; they complement broader workflows above.

- [`minimal-change`](skills/minimal-change/SKILL.md) — keep a change limited to what the intended result requires.
- [`change-impact-check`](skills/change-impact-check/SKILL.md) — inspect architectural fit and affected work before writing code.
- [`domain-model-first`](skills/domain-model-first/SKILL.md) — settle the core data shape and invariants before implementing logic.
- [`boundary-discipline`](skills/boundary-discipline/SKILL.md) — validate and translate external input at system boundaries.
- [`root-cause-first`](skills/root-cause-first/SKILL.md) — trace a reproduced failure to its cause before adding a guard or workaround.
- [`behavior-focused-tests`](skills/behavior-focused-tests/SKILL.md) — test observable behavior so tests survive internal refactoring.
- [`prove-real-result`](skills/prove-real-result/SKILL.md) — inspect the actual outcome and evidence before claiming completion.

## Reasoning skills

- [`why`](skills/why/SKILL.md) — explain causes, consequences, and the evidence behind a judgment.
- [`how`](skills/how/SKILL.md) — show actionable options, tradeoffs, and a checkable path forward.

## Parked skills

These skills are retained outside the active library for now:

- `programming-coursebook-authoring`
- `git-hygiene`

## Automotive development package

[`automotive-development`](automotive-development/SKILL.md) is the automotive domain entry skill. Its package-level playbooks compose shared principles and general engineering methods with automotive requirements, test artifacts, work packages, target evidence, and baseline gates.

Automotive requirements, test documentation, feature, bug fix, refactoring, architecture change, and baseline changes are playbooks under the [automotive package](automotive-development/README.md), not nested standalone skills. The [module deliverables guide](automotive-development/docs/module-deliverables.md) defines shared links; the [speed-signal example](automotive-development/examples/speed-signal/README.md) shows one complete layout.

The automotive package's orchestration entry point is [`automotive-development`](automotive-development/SKILL.md). Its playbooks select the shared principles needed for each automotive task. Git credentials, repository remotes, CI, test runners, and HIL/ECU environments are external prerequisites, not installable skills.

Each shared principle has its own directory directly under `skills/`. Domain packages have their own entry `SKILL.md` and compose the shared principles with domain-specific context and gates.

## Install the skill bundle

This repository is organized as one skill bundle: shared skills and domain packages such as automotive development live together. Register the repository using the bundle mechanism supported by your agent. Once registered, invoke skills by name; workflow documents refer to shared skills by name rather than depending on this repository's directory layout.

English skill files are the canonical, version-controlled source. Matching Korean translations are kept locally under `skills-ko/` and `automotive-development-ko/` with the same instructional layout; both Korean directories and `trash/` are ignored by Git and are not committed.

## Skill placement

### Shared principle skills

A shared principle skill owns one reusable engineering judgment. Its title and instructions name that principle, say when it applies, and give only the rules needed to apply it. Keep it concise and independent of any one project's standards, artifact paths, workflow gates, or tools. Do not turn a principle skill into an implementation workflow.

Dependency points downward from playbooks to principles: a shared principle must not name a domain playbook, enumerate its use cases, or choose the next workflow. It states its own judgment and result; the playbook decides when to invoke it and what to do next.

For example, `minimal-change` says to identify the intended outcome, choose the smallest change that achieves it, preserve what lies outside that change, and expand scope only when needed. It does not prescribe project-specific file limits, cleanup policy, or approval steps.

Write a skill’s frontmatter `description` with a concrete action and a discriminating trigger. Name the signals that distinguish it from neighboring skills, but keep workflow steps and handoff rules in playbooks. For example, `architecting` says: “Sketch the affected modules, types, signatures, and interface boundaries before choosing the simplest structure that meets the intended behavior. Use for ‘architect this’, ‘design this’, or structural changes where coding first could lock in the wrong shape.”

### Domain playbooks apply principles

A domain package such as `automotive-development/` composes shared principles into concrete work for that domain. The playbook supplies applicable artifacts, boundaries, sequence, evidence, and decision gates. It translates a general principle into domain-specific steps without copying the whole shared skill.

For automotive code changes, the feature, bug fix, and refactoring playbooks bind `minimal-change` to an approved `WORK` package: they define how files and acceptance criteria bound the work, where unrelated cleanup belongs, how traceability is updated, and when an approved baseline change must be routed. Those are automotive workflow rules, so they live in the automotive package rather than the shared principle.

When creating a skill, apply [`skill-design`](skills/skill-design/SKILL.md): check existing ownership, choose a shared principle versus a domain playbook, and ensure guidance fits its intended scope. Shared principles go in `skills/`; standards, project terms, artifact paths, and lifecycle gates go in the relevant domain package. Link a shared principle from the domain playbook at the point where it changes a decision.

Do not generalize a skill based only on a possible future use. Identify at least one concrete use outside its originating project and confirm that the core guidance still works there without importing domain-specific assumptions. If that test is not met, keep the skill with its project. When a shared skill is useful to a project package, link it from that package's README and from the relevant router or playbook so agents can discover and load it at the point of use.

For the repository-wide rules on entrypoint size, routing versus execution, progressive disclosure, placement, composition, discoverability, and validation, see [Skill Authoring Principles](docs/skill-authoring-principles.md).
