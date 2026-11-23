# Skill Authoring Principles

This document defines the repository-wide rules for creating and organizing skills. It complements [`skills/skill-design/SKILL.md`](../skills/skill-design/SKILL.md), which describes the decision process for designing an individual skill.

## 1. Keep the top-level skill entrypoint small

The top-level `SKILL.md` is the entrypoint, not the entire manual. It should contain only:

- the skill name and trigger description;
- the skill's purpose and responsibility boundary;
- the minimum decisions the agent must make;
- routing to a child skill or reference when more detail is needed.

Do not put long procedures, domain background, repeated rules, large examples, or every possible edge case in the top-level file.

## 2. Keep one small concept per skill

A skill must focus on one small, named concept, judgment, or action. It should explain the purpose and use of that one thing—not become a collection of related advice.

`skills/how/SKILL.md` is the model: it explains how to choose and describe a path from intent to action. It does not also define requirements, implementation, testing, review, or project management. A new skill named `why` should similarly focus on the purpose of explaining causes and evidence, not become a general reasoning manual.

Use this test before creating a skill:

- Can its purpose be stated in one short sentence without an “and” joining separate jobs?
- Does the name identify the one concept the skill owns?
- Would removing one paragraph change that concept, or only remove an adjacent topic?
- Can a nearby topic be linked as another skill instead of being added here?

If the answer reveals multiple independent concepts, split them into separate skills and compose them through a router or workflow. Do not create a broad “everything for X” skill just because the topics are used in the same project.

Before creating a skill, check whether an existing skill already owns the method. Extend that skill when the new rule changes the same decision. Create a separate skill only when the trigger, responsibility, and outcome are materially different.

## 3. Separate routing from execution

Routers and workers have different responsibilities:

- A router classifies the request, selects the next skill, defines stage order, carries inputs and outputs, and enforces gates.
- A focused skill or playbook performs the work assigned to it and owns only the method and output needed for that work.

Do not duplicate detailed instructions in a router. Link to the focused skill or playbook and state only the handoff conditions that the router owns.

## 4. Use progressive disclosure

Keep the common path in `SKILL.md` and move conditional detail to the narrowest useful resource:

- `references/` for substantial guidance, policies, schemas, and format details;
- `examples/` for representative completed outputs;
- `scripts/` for deterministic checks or repeatable transformations;
- templates or assets for files that belong in generated output.

Read or invoke supporting resources only when the current task needs them. Do not add a reference file merely to make the directory look complete.

## 5. Make boundaries explicit

Every workflow skill should make its boundaries visible:

- required inputs and context;
- produced artifacts or decisions;
- unresolved decisions and how they are recorded;
- conditions that require a stop or user decision;
- work the skill does not perform;
- evidence required before claiming completion.

Do not silently invent missing requirements, approvals, safety claims, interfaces, limits, or acceptance criteria.

## 6. Place skills by reuse scope

- Put domain-independent methods in `skills/`.
- Put project, product, domain, standard, lifecycle, or artifact-specific guidance in the relevant package, such as `automotive-development/`.
- Keep a skill in its originating package unless at least one concrete use outside that package demonstrates that the core guidance survives without importing domain assumptions.

When a shared skill is used by a package, link it from the package README and from the relevant router or playbook.

## 7. Prefer composition over duplication

Keep shared skills small and principle-focused. Compose multiple principles into an engineering workflow or a domain playbook through explicit links and handoffs. A domain package entrypoint routes to its playbooks; it does not absorb the playbooks' detailed procedures.

Do not copy shared principles into domain playbooks or repeat a playbook in its parent entrypoint. If a domain workflow needs to specialize a shared principle, keep the principle general and put only the domain-specific artifacts, constraints, gates, and fields in the package playbook.

For example, `automotive-development/SKILL.md` is the automotive entrypoint. Automotive requirements-to-SRS, SRS-to-STS, feature, bug fix, refactoring, and baseline change procedures live in `automotive-development/playbooks/`; automotive document context, examples, and checklists live in `automotive-development/references/`. The package does not need a nested `skills/` directory.

## 8. Define discoverability and invocation

For every new skill, verify all of the following:

- frontmatter `name` is specific, and `description` gives an imperative instruction with an application trigger and action;
- the skill is reachable from the appropriate README, router, or playbook;
- the name follows lowercase kebab-case;
- UI metadata, when present, matches the skill's actual purpose;
- links resolve from the file that contains them.

Do not rely on a skill existing in the filesystem without providing a discoverable path to it when it is part of a package workflow.

## 9. Validate behavior, not just structure

Run the repository's mechanical checks for frontmatter, links, naming, and structure. Then test the skill with at least:

1. one realistic request it should attract;
2. one nearby request it should not attract;
3. one incomplete or ambiguous request that verifies its stop conditions.

The checks should confirm the output shape, handoff behavior, and refusal to guess—not merely the presence of headings or keywords.

## 10. Keep one canonical source

English skill files are the canonical, version-controlled source. Matching translations may be maintained in the ignored local translation trees, but they must preserve the same instructional structure and links as the canonical files.

When a principle changes, update the canonical document first and then reconcile translations or generated copies.

## 11. Avoid premature generalization

Do not promote a rule to the shared library because it might be useful someday. First identify a concrete second use, remove originating-project assumptions, and confirm that the generalized skill still has a clear trigger and output.

If the rule is only a repository convention, put it here or in the relevant package documentation. If it is a reusable agent method, put it in a skill.
