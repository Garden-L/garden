# Automotive Development Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Expand `automotive-development` into a project-style domain package that composes reusable shared skills with automotive-specific playbooks and leaf skills.

**Architecture:** Keep `automotive-development/SKILL.md` as the Codex entry point, preserve the existing automotive leaf skills under `automotive-development/skills/`, and add reusable, domain-neutral skills under `skills/shared/`. Project-level playbooks compose shared skills with automotive-specific skills; the router selects one playbook and instructs the agent to read only the relevant skills.

**Tech Stack:** Markdown skill files, YAML agent metadata, shell scripts; no runtime dependencies.

**Spec:** `docs/superpowers/specs/2026-11-22-automotive-development-package-design.md` (the design is captured by the approved conversation; no separate spec was requested).

## Global Constraints

- Preserve existing automotive leaf-skill behavior and references.
- Keep the package usable from Codex through `automotive-development/SKILL.md`.
- Shared skills must not depend on automotive terminology, standards, or artifacts.
- Do not introduce external runtime dependencies.
- Do not modify unrelated untracked files under `docs/`.

## Review Focus

- A request that matches one workflow must not cause every leaf skill to be loaded; verify explicit routing language.
- Relative references from the router and playbooks must resolve from the package directory.
- Existing leaf-skill names and paths must remain stable.
- The package should explain that external ECU/HIL, CI, repository, and credential prerequisites are not bundled skills.

### Task 1: Add reusable shared skills

**Files:**
- Create: `skills/shared/architect/SKILL.md`
- Create: `skills/shared/tdd/SKILL.md`
- Create: `skills/shared/verification/SKILL.md`
- Create: `skills/shared/git-hygiene/SKILL.md`

- [ ] Define each shared skill by capability, inputs, outputs, and boundaries rather than by automotive workflow.
- [ ] Keep each skill independently usable by future domain packages such as web development.

### Task 2: Package scaffolding and project documentation

**Files:**
- Create: `automotive-development/README.md`
- Create: `automotive-development/.gitignore`
- Create: `automotive-development/docs/architecture.md`
- Create: `automotive-development/agents/README.md`
- Create: `automotive-development/scripts/README.md`

- [ ] Add the package purpose, installation/use model, directory map, workflow list, and external prerequisites to `README.md`.
- [ ] Add conservative ignores for generated reports, local logs, and temporary artifacts.
- [ ] Document the router → playbook → leaf-skill architecture in `docs/architecture.md`.
- [ ] Document reserved locations for future author/reviewer agents and scripts without inventing executable behavior.

### Task 3: Add project-level playbooks

**Files:**
- Create: `automotive-development/playbooks/requirements-to-srs.md`
- Create: `automotive-development/playbooks/srs-to-sts.md`
- Create: `automotive-development/playbooks/readiness-review.md`
- Create: `automotive-development/playbooks/implementation.md`
- Create: `automotive-development/playbooks/verification.md`
- Create: `automotive-development/playbooks/change-control.md`

- [ ] Define each playbook's trigger, required inputs, leaf skills to read, gates, outputs, and stop conditions.
- [ ] Keep the existing pipeline's approval and baseline-change boundaries intact.
- [ ] Make each playbook independently readable and avoid duplicating the detailed rules owned by leaf skills.

### Task 4: Refactor the package entry point

**Files:**
- Modify: `automotive-development/SKILL.md`
- Modify: `automotive-development/agents/openai.yaml`

- [ ] Turn the top-level skill into a project router that classifies the request and selects one playbook.
- [ ] Require the selected playbook and only its referenced leaf skills to be read.
- [ ] Preserve direct routing for SRS, STS, readiness, backlog, bounded implementation, verification, and change-control requests.
- [ ] Update the agent-facing display text to describe the package as a staged automotive development workflow.

### Task 5: Validate package structure and references

**Files:**
- Test: shell-based structural checks run from the repository root

- [ ] Verify all listed playbooks and referenced leaf `SKILL.md` files exist.
- [ ] Verify every skill frontmatter has a `name` and `description`.
- [ ] Verify no existing leaf skill or unrelated file was modified.
- [ ] Review the final diff and run the repository's available checks, noting that no application test runner exists for this Markdown-only package.
