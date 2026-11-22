---
name: review
description: Use when assessing a change, document, design, implementation, or other deliverable before acceptance, handoff, or release.
---

# Review

Produce an evidence-based judgment about whether the work meets its stated intent and is ready for its next use. Apply the relevant domain or artifact-specific criteria supplied by the caller; this skill provides the review method, not every domain checklist.

## 0. Set the review scope

Identify the intended outcome, review boundary, intended users, relevant baseline or source material, and decision the review must support. If scope or a necessary source is missing, state the limit before drawing conclusions.

## 1. Inspect the actual work

Read or run the deliverable itself and compare it with the request, approved requirements, design, or other governing material. Follow important references and changed behavior to their evidence. Do not treat a summary, successful build, or author's claim as proof of correctness.

## 2. Look for consequential failures

Check correctness, omissions, contradictions, unsupported assumptions, boundary and failure behavior, consistency with surrounding work, and effects outside the immediate change. Apply only the checks relevant to this review. Prioritize issues by real impact and likelihood; distinguish confirmed defects from risks that still need evidence.

## 3. Verify findings

For each potential finding, capture the exact location and supporting evidence. Reproduce or independently verify it when practical. Drop speculative findings that do not affect the stated intent or next decision. Keep unresolved questions distinct from confirmed defects and optional improvements.

## 4. Report a decision-ready review

- Verdict: ready, ready with conditions, changes required, or blocked.
- Findings ordered by severity, each with location, evidence, impact, and recommended action.
- Checks performed and their results.
- Risks, assumptions, and areas not verified.
- The next action needed to proceed.

Do not silently make changes while acting as reviewer. When independent review matters, use a fresh reviewer context if available; otherwise identify the result as self-review. Add domain-specific criteria from the calling skill, such as SRS or STS checklists, without replacing this method.
