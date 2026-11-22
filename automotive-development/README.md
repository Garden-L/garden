# Automotive Development

`automotive-development` is a project-style Codex skill package for staged automotive software work. Automotive workflows live here, while reusable engineering skills live directly under the repository's `skills/` directory.

## Use

Invoke `$automotive-engineering` for automotive work, or invoke an automotive leaf skill directly for a focused task. The engineering skill is the router; this directory is the project package containing playbooks and automotive-specific skills.

## Package map

- `skills/automotive-engineering/SKILL.md` — concise workflow router.
- `skills/automotive-engineering/playbooks/` — task-specific sequences and gates.
- `skills/` — automotive-specific leaf skills.
- `agents/` — future author, reviewer, or worker briefs.
- `docs/` — package architecture and operating notes.
- `scripts/` — deterministic package checks and future helpers.
- `examples/` — a runnable module bundle with source, SRS, STS, issue, work, coverage, and verification outputs.

The code-development flow starts after SRS/STS readiness. Use implementation planning to create bounded work packets, then choose feature, bug-fix, or refactoring playbooks. Integration testing, code review, implementation verification, and release readiness are separate gates with separate evidence.

## Reusable skills

The package composes shared engineering and specification skills with automotive profiles. Shared `spec-requirements` and `spec-tests` own SRS/STS principles, IDs, test design, and reference formats. The automotive profiles add vehicle context, source applicability, target considerations, and review flows without requiring a second document template. The router maps skill names to their library locations; playbooks name only the profiles needed at each stage.

For a module developed from initial requirements through code, use the [module delivery playbook](skills/automotive-engineering/playbooks/module-delivery.md). Its [artifact contract](docs/module-deliverables.md) specifies the consuming project's outputs and their links. A [worked speed-signal example](examples/speed-signal/README.md) shows the complete handoff. `decision` supplies the shared issue-to-outcome principle; the automotive package owns file locations and vehicle-specific fields.

## External prerequisites

Repository access, Git credentials, CI, test runners, ECU/HIL environments, simulators, and project-specific standards are external prerequisites. This package documents workflows for them but does not install or provide those systems.
