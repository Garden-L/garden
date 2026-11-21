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

The package composes shared engineering and specification skills with automotive profiles. Shared `spec-requirements` and `spec-tests` own SRS/STS principles, IDs, test design, and reference formats. The automotive profiles add vehicle context, source applicability, target considerations, and review flows without requiring a second document template. The router maps skill names to their library locations; playbooks name only the profiles needed at each stage.

## External prerequisites

Repository access, Git credentials, CI, test runners, ECU/HIL environments, simulators, and project-specific standards are external prerequisites. This package documents workflows for them but does not install or provide those systems.
