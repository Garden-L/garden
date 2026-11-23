# Automotive Development

`automotive-development` is the automotive domain package. Its top-level [SKILL.md](SKILL.md) is the entry point.

## Use

Invoke `$automotive-development` for automotive work. Identify the requested outcome and current artifacts, then use the entry skill to select the relevant procedure in [playbooks/](playbooks/). Read only the references needed for that procedure.

## Package map

- `SKILL.md` — entry point for finding the relevant playbook.
- `playbooks/` — task procedures that select and apply shared principles.
- `references/` — automotive context, reviewer checklists, briefs, and examples.
- `agents/` — UI metadata and agent guidance.
- `docs/` — package architecture and operating notes.
- `scripts/` — deterministic package checks.
- `examples/` — a runnable module bundle with source, SRS, STS, work, coverage, and verification outputs.

Playbooks determine which shared principles apply, how automotive sources and approved work constrain the task, and what evidence or decision is needed at each step. Keep task-specific steps in the playbooks and supporting context in `references/`.

The [artifact contract](docs/module-deliverables.md) specifies consuming-project outputs and links. A [worked speed-signal example](examples/speed-signal/README.md) shows a complete handoff.

## External prerequisites

Repository access, Git credentials, CI, test runners, ECU/HIL environments, simulators, and project-specific standards are external prerequisites. This package documents workflows for them but does not install or provide those systems.
