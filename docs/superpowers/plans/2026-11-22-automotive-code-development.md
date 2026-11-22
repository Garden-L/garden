# Automotive Code Development Workflow Plan

> **For agentic workers:** Execute in this session. Preserve existing shared skill contents and all SRS/STS authoring and specialist review files.

**Goal:** Make the automotive package support practical code development from readiness and work planning through implementation, testing, code review, verification, and release.

**Architecture:** Keep `automotive-engineering` as a concise router. Add task-specific playbooks inspired by pstack's feature, bug-fix, refactoring, review, and shipping flows. Compose existing shared skills and automotive skills by name; keep SRS/STS stages intact and connect their approved outputs to the code-development stages.

**Tech Stack:** Markdown skills and playbooks; existing package validation scripts.

**Scope:** Automotive package changes excluding SRS/STS authoring skills and their domain review files. Shared skill contents remain unchanged.

## Tasks

1. [x] Update router to select code-development workflows in addition to the existing document stages.
2. [x] Add playbooks for feature, bug fix, refactoring, integration/system testing, code review, and release readiness.
3. [x] Connect readiness, backlog, bounded implementation, verification, and module-delivery stages without changing SRS/STS-specific steps.
4. [x] Update package documentation and structural validation to describe/check the full lifecycle.
5. [x] Validate links, skill names, and package structure; review the diff to confirm SRS/STS and shared skill content are untouched.

## Verification evidence

- `bash automotive-development/scripts/validate-structure.sh` — passed.
- `python3 automotive-development/scripts/validate-module-delivery.py automotive-development/examples/speed-signal/docs/modules/speed-signal` — passed.
- `python3 automotive-development/scripts/report-module-coverage.py ... --output /tmp/automotive-module-coverage-check.md` — generated the report successfully.
- `python3 -m unittest discover -s automotive-development/examples/speed-signal/tests -v` — 5 tests passed.
- `python3 skills/skill-design/scripts/validate-library.py` — passed (20 active skills).
- English and Korean playbook-relative-link checks — passed.
- `git diff --check` — passed.
