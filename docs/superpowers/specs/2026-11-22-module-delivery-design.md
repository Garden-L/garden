# Module Delivery Design

## Goal

Give an automotive module a reviewable path from supplied source material through SRS, STS, decisions, bounded implementation, and verified delivery. A completed example must show the actual shape of every output and its links. The skill package defines the method and artifact contract; generated module artifacts live in the consuming project.

## Responsibility split

- Shared `decision`: reusable principle for recording an issue's evidence, why it matters, options, decision authority, affected artifacts, and proof of application. It does not prescribe software IDs or filenames. It composes `why` and `how`.
- Shared `workflow-design`: reusable principle for defining a checkable outcome, stage inputs/outputs, decisions, and checks without owning a domain's artifact paths.
- Shared `skill-design`: repository-specific principles for naming, scope, generalization, composition, and checking a new skill. It guides future skill-writing agents without replacing the host's skill-authoring tool or fixing a document template.
- Existing shared `specification`, `spec-requirements`, `spec-tests`, `engineering-design`, `implementation`, `verification`: retain their current roles. Do not copy their rules into the new skill.
- Automotive `automotive-engineering` full-delivery playbook: apply `workflow-design`, select existing leaf skills in sequence, and define stage outputs and stop conditions.
- Automotive deliverable contract: concrete paths, required information, lifecycle states, and validation for a module. SRS and STS formats remain references; this contract does not force their section layouts.
- Worked example: one invented speed-signal module with complete cross-links and clearly labeled illustrative code and evidence, never claimed as a real ECU/HIL run.

## Module output contract

In a consuming project, use `docs/modules/<module>/` by default, or an existing equivalent location:

```text
README.md                 source versions, scope, stage, artifact index, final verdict
srs.md                    REQ requirements and acceptance conditions
sts.md                    TC cases, chosen techniques, procedures, expected results
issues.md                 canonical ISSUE record, including decision and application evidence
traceability.md           source → REQ → TC → ISSUE when relevant → WORK → code → evidence
completion-report.md      generated per-REQ coverage, recorded status, and gaps
work/WORK-001.md          bounded packet and implementation result per work item
verification.md           commands/runs, observed results, environment gaps, conclusion
```

Code and automated tests remain in the consuming project's normal source tree. A path, revision, and evidence pointer in the module record connect them. The document bundle does not copy code.

## Lifecycle

1. Frame the module and index source versions. Identify unknowns before treating an interpretation as approved.
2. Draft/review SRS. A requirement's source and acceptance condition stay close to it.
3. Draft/review STS. Derive cases and techniques from approved or explicitly provisional requirements. Undefined expected behavior becomes an ISSUE and a coverage gap.
4. Record decisions in one canonical issue record. SRS and STS link to it. Distinguish `Open`, `Decided`, `Applied`, and `Verified`; a decision alone is not completion. Approved baseline changes use the existing change-control skill.
5. Readiness review and bounded WORK packet. Only eligible work proceeds; each unit ends with a checkable state.
6. Implement in the code repository, run relevant checks, preserve evidence, and update traceability. Environment-dependent verification remains pending until executed.
7. Compare the result with the source, SRS, STS, decision record, and actual evidence. Generate a completion report from the recorded links and test statuses; do not treat its counts as independent proof. The module README reports a final verdict and open gaps; it never infers passing from a document's existence.

## Verification of this skill package

- Structural check finds every linked skill, playbook, contract, and example file.
- A deterministic module check validates the example's required files, IDs, references, and evidence pointers without claiming semantic correctness.
- The example's prose and declared results are reviewed against its own requirements and tests.
- The completed SRS/STS example follows the shared reference formats while the skills keep those formats optional for other documents.
- A skill-to-output audit maps the applied skills to example artifacts and names the gates this local example did not exercise.
- Korean read-only mirror adds the same new instructional material under ignored `skills-ko/` and `automotive-development-ko/` paths. The English source stays canonical.

## Potato influence

[Potato PStack](https://github.com/sub4biz/potato-pstack)'s `show-me-your-work` keeps one decision trail; `figure-it-out` sequences auditable phases; `principle-sequence-verifiable-units` and `principle-prove-it-works` require a check per unit and evidence from the real artifact. This design adopts those ideas while keeping this repository's existing `why`, `how`, and `verification` semantics and authorization rules. It does not copy Potato's agent prompts or approval policy.
