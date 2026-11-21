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

Reusable skills are in the repository's top-level `skills/` directory. Read only those referenced by the selected playbook and needed by the current stage.

## Package and environment

Before running on another system, verify the selected playbook's required skills are available. If one is missing, report the exact skill and stage it blocks. Optional skills such as TDD or Git hygiene are loaded only when the selected playbook calls for them.

Do not treat a missing Git provider connection, repository remote, test runner, hardware/HIL environment, or project policy as a missing skill. Report those as environment prerequisites separately.

For a project with no repeatable way to exercise its real target behavior, add a project-specific verification recipe or skill that records how to start, drive, observe, and clean up the target. Reuse an existing harness when one exists; this is not a required generic automotive skill.

If no playbook fits, choose the narrowest automotive skill available and state any missing workflow coverage. Keep the response focused on current stage, decisions or blockers, produced artifact, and next step.
