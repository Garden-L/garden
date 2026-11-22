---
name: automotive-engineering
description: Use as the main entry point for automotive software work; route the request to a focused lifecycle playbook and only the small skills it needs.
---

# Automotive Engineering

This is the main entry point for the `automotive-development` project package. It routes vehicle software work from source documents through implementation and verification. Keep this file as the mode contract; task procedures belong in playbooks, and focused methods belong in leaf skills.

## Non-negotiables

1. Do not load every skill. Select one playbook, then load only the skills it names.
2. Preserve source IDs, decisions, approval state, and evidence across handoffs.
3. Never infer approval from a filename, document existence, or absence of comments.
4. Do not invent safety levels, standards compliance, interfaces, limits, or expected results.
5. Pause when a missing decision changes scope, safety, implementation, or verification.

## 0. Frame the request

Identify the requested outcome, available artifacts and versions, current lifecycle stage, target scope, and approval state. If the user asks for the full module result, use [Module Delivery](playbooks/module-delivery.md). For a single stage, select the matching playbook below.

## 1. Select a playbook

- Full module from source to verified code → [Module Delivery](playbooks/module-delivery.md)
- Raw requirements to SRS → [Requirements to SRS](playbooks/requirements-to-srs.md)
- SRS to STS → [SRS to STS](playbooks/srs-to-sts.md)
- Pre-implementation review → [Implementation Readiness Review](playbooks/readiness-review.md)
- Convert approved specifications into implementation work → [Implementation Planning](playbooks/implementation-planning.md)
- Add behavior within an approved work packet → [Feature Development](playbooks/feature.md)
- Reproduce and correct a defect → [Bug Fix](playbooks/bug-fix.md)
- Change structure while preserving behavior → [Refactoring](playbooks/refactoring.md)
- Validate behavior across components or target environments → [Integration Testing](playbooks/integration-testing.md)
- Review a code change before delivery → [Code Review](playbooks/code-review.md)
- Approved work package implementation → [Bounded Implementation](playbooks/implementation.md)
- Post-implementation evidence review → [Implementation Verification](playbooks/verification.md)
- Assess delivery and release readiness → [Release Readiness](playbooks/release-readiness.md)
- Proposed approved-baseline change → [Baseline Change Control](playbooks/change-control.md)

## 2. Follow the playbook

The playbook owns the numbered steps, required inputs, outputs, and gates for that task. It calls shared and automotive skills by name. Follow their instructions without copying their full procedures into this mode.

## 3. Resolve missing coverage

If no playbook fits, choose the narrowest relevant skill, state the uncovered workflow, and do not silently extend a different playbook. If a required skill or environment prerequisite is missing, name the blocked stage and continue only where safe.

## 4. Hand off clearly

Report the current stage, artifact/revision used, result or blocker, remaining decisions, and the next permitted action. For implementation, include changed scope, checks and evidence, traceability state, and delivery status.

## Environment limits

Git credentials, repository remotes, CI, test runners, policy documents, and ECU/HIL environments are project prerequisites, not bundled skills. Report when their absence blocks a stage.
