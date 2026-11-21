---
name: automotive-engineering
description: Use as the main entry point for automotive software work; route the request to a focused lifecycle playbook and only the small skills it needs.
---

# Automotive Engineering

This is the main entry point for the `automotive-development` project package. Classify the user's request, read the matching playbook in this skill's `playbooks/` directory, and then load only the small skills that playbook names. Do not load every skill for every task. Preserve each skill's approval gates and never infer approval from a document's existence.

## Package workflow links

- Raw requirements to SRS: [Requirements to SRS](playbooks/requirements-to-srs.md)
- SRS to STS: [SRS to STS](playbooks/srs-to-sts.md)
- Pre-implementation review: [Implementation Readiness Review](playbooks/readiness-review.md)
- Approved work package implementation: [Bounded Implementation](playbooks/implementation.md)
- Post-implementation evidence review: [Implementation Verification](playbooks/verification.md)
- Proposed approved-baseline change: [Baseline Change Control](playbooks/change-control.md)

The installed bundle exposes reusable skills by name. Read only those named by the selected playbook and needed by the current stage.

## Skill registry

Resolve skill names through this registry. Playbooks use names so their instructions do not depend on the bundle's folder layout.

### Shared skills

- `engineering-design` — `skills/engineering-design/SKILL.md`
- `spec-requirements` — `skills/spec-requirements/SKILL.md`
- `spec-tests` — `skills/spec-tests/SKILL.md`
- `why` — `skills/why/SKILL.md`
- `how` — `skills/how/SKILL.md`
- `implementation` — `skills/implementation/SKILL.md`
- `specification` — `skills/specification/SKILL.md`
- `verification` — `skills/verification/SKILL.md`

### Automotive skills

- `automotive-baseline-change-control` — `automotive-development/skills/baseline-change-control/SKILL.md`
- `automotive-implementation-profile` — `automotive-development/skills/bounded-implementation-execution/SKILL.md`
- `implementation-backlog-traceability` — `automotive-development/skills/implementation-backlog-traceability/SKILL.md`
- `automotive-readiness-review` — `automotive-development/skills/implementation-readiness-review/SKILL.md`
- `automotive-verification-review` — `automotive-development/skills/implementation-verification-review/SKILL.md`
- `software-requirements-specification` — `automotive-development/skills/software-requirements-specification/SKILL.md`
- `software-test-documentation` — `automotive-development/skills/software-test-documentation/SKILL.md`

The shared `implementation` skill includes the reusable-tool principle for recurring engineering patterns.

## Package and environment

Before running on another system, verify the selected playbook's required skills are available. If one is missing, report the exact skill and stage it blocks. Load only the shared and automotive profile skills named by the selected playbook.

Do not treat a missing Git provider connection, repository remote, test runner, hardware/HIL environment, or project policy as a missing skill. Report those as environment prerequisites separately.

For a project with no repeatable way to exercise its real target behavior, add a project-specific verification recipe or skill that records how to start, drive, observe, and clean up the target. Reuse an existing harness when one exists; this is not a required generic automotive skill.

If no playbook fits, choose the narrowest automotive skill available and state any missing workflow coverage. Keep the response focused on current stage, decisions or blockers, produced artifact, and next step.
