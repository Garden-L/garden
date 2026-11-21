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

## Reusable skills

The package composes domain-neutral skills from the repository's top-level `skills/` directory, including architecture, TDD, verification, Git hygiene, input review, traceability, impact analysis, and evidence recording. Playbooks name only the reusable skills needed at each stage.

## External prerequisites

Repository access, Git credentials, CI, test runners, ECU/HIL environments, simulators, and project-specific standards are external prerequisites. This package documents workflows for them but does not install or provide those systems.
