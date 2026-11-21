# Personal Codex Skills

Reusable skills for building programming coursebooks and engineering workflows.

## Shared skill library

- [`shared`](skills/shared/) — domain-neutral architecture, TDD, verification, and Git hygiene skills that can be composed by multiple project packages.

## Skills

- [`programming-coursebook-authoring`](skills/programming-coursebook-authoring/SKILL.md) — creates a complete programming coursebook, hands-on project structure, purpose-named staged files, learner checkpoints, and Notion chapter pages.

## Automotive development skill set

[`automotive-development`](automotive-development/README.md) is a project-style package. Its pipeline skill and playbooks compose the shared skills above with automotive-specific requirements, testing, readiness, implementation, verification, and baseline-change skills.

Install these sub-skills together when using the automotive pipeline on another system, in this order:

1. [`software-requirements-specification`](automotive-development/skills/software-requirements-specification/SKILL.md)
2. [`software-test-documentation`](automotive-development/skills/software-test-documentation/SKILL.md)
3. [`implementation-readiness-review`](automotive-development/skills/implementation-readiness-review/SKILL.md)
4. [`implementation-backlog-traceability`](automotive-development/skills/implementation-backlog-traceability/SKILL.md)
5. [`bounded-implementation-execution`](automotive-development/skills/bounded-implementation-execution/SKILL.md)
6. [`implementation-verification-review`](automotive-development/skills/implementation-verification-review/SKILL.md)

The orchestration entry point is [`automotive-development-pipeline`](automotive-development/skills/automotive-development-pipeline/SKILL.md). TDD, verification, code-review, and debugging skills are optional helpers. Git credentials, repository remotes, CI, test runners, and HIL/ECU environments are external prerequisites, not installable skills.

Install [`baseline-change-control`](automotive-development/skills/baseline-change-control/SKILL.md) when approved requirements, tests, or interfaces may change during implementation. It is used only when such a change is proposed.

Each skill is kept in its own directory so more personal skills can be added without coupling them to a specific programming language or project.
