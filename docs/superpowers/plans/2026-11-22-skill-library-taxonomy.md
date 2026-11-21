# Skill Library Taxonomy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganize the skill library into purpose-led categories while keeping automotive workflows as a domain package.

**Architecture:** Move only shared skills into nested purpose categories. Keep automotive leaf skills in their package, update all indexes and the central name-to-file registry, and keep playbooks path-free.

**Tech Stack:** Markdown, filesystem moves.

**Spec:** `docs/superpowers/specs/2026-11-22-skill-library-taxonomy-design.md`

## Global Constraints

- Preserve skill names and substantive instructions.
- Do not delete existing user work or unrelated documentation.
- Keep automotive-specific standards and lifecycle gates in the automotive package.
- Playbooks refer to skills by name; the automotive router owns path resolution.

## Review Focus

- Every moved skill remains discoverable from the root README and the relevant domain router.
- All skill registry paths resolve after moves.
- No automotive playbook retains stale paths to shared skills.
- Top-level `skills/` no longer implies all skills share the same practical purpose.

---

### Task 1: Move shared skills into purpose categories

**Files:** Move existing skill directories according to the approved design mapping; preserve all nested files.

- [ ] Move frame skills: architect, input-review, change-impact.
- [ ] Move build skills: tdd under software; pattern-to-tool under automation.
- [ ] Move prove skills: verification, verification-evidence, traceability.
- [ ] Move communicate skill: programming-coursebook-authoring under learning.
- [ ] Move sustain skill: git-hygiene.

### Task 2: Update indexes and routing

**Files:** `README.md`, `automotive-development/README.md`, `automotive-development/skills/automotive-engineering/SKILL.md`, relevant automotive playbooks.

- [ ] Rewrite README groups around purpose and domain packages.
- [ ] Update automotive registry paths to new locations.
- [ ] Retain name-only references in automotive playbooks.
- [ ] Remove stale references to the old flat directory layout.

### Task 3: Verify the resulting structure

- [ ] Search for stale paths and old flat-layout claims.
- [ ] Resolve every path in the automotive registry to an existing skill file.
- [ ] Review the final diff to confirm only intended moves and documentation updates occurred.
