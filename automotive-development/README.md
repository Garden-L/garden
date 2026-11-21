# Automotive Development

`automotive-development` is a project-style Codex skill package for staged automotive software work. It is a domain package, not a universal engineering mode: automotive workflows live here, while reusable engineering capabilities live in the repository's `skills/shared/` library.

## Use

Invoke `$automotive-development-pipeline` for an end-to-end automotive workflow, or invoke an automotive leaf skill directly for a focused task. The pipeline is the workflow entry point; this directory is the project package that contains the pipeline, supporting playbooks, automotive-specific skills, and shared-skill connections.

## Package map

- `skills/automotive-development-pipeline/SKILL.md` — workflow entry point and orchestrator.
- `skills/automotive-development-pipeline/playbooks/` — pipeline-specific workflow compositions and gates.
- `skills/` — automotive-specific leaf skills.
- `agents/` — future author, reviewer, or worker briefs.
- `docs/` — package architecture and operating notes.
- `scripts/` — deterministic package checks and future helpers.

## Shared skills

The package composes domain-neutral skills from `../skills/shared/`, including architecture, TDD, verification, and Git hygiene. Playbooks name the shared skills used at each stage. Shared skills must remain free of automotive assumptions so future packages such as web development can reuse them.

## External prerequisites

Repository access, Git credentials, CI, test runners, ECU/HIL environments, simulators, and project-specific standards are external prerequisites. This package documents workflows for them but does not install or provide those systems.
