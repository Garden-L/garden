---
name: skill-design
description: Use when adding or revising skills in this library to choose a name, decide shared versus domain scope, compose instructions, and verify discoverability.
---

# Skill Design

Name the one small judgment or outcome the skill helps an agent make. Use a short, memorable kebab-case name. Prefer a broad principle name when the method survives a change of domain (`why`, `verification`, `decision`); use a domain name when the input, constraints, or output genuinely depend on that domain. Avoid names that merely repeat a document type, technology, or fashionable metaphor without distinguishing when to invoke the skill.

Keep one small concept per skill. A skill should explain the purpose and use of one named thing, like `how` focuses on making a path from intent to action clear. Do not combine neighboring concepts because they often appear in the same task. If the purpose needs an “and” joining independent jobs, split the skills and compose them through a router or workflow. See the repository's [Skill Authoring Principles](../../docs/skill-authoring-principles.md) for the governing rule and examples.

Before creating a skill, check whether an existing skill already owns the principle. Extend it when the new rule changes the same decision. Create a separate skill when it has a distinct trigger, decision, and reusable outcome. Put a project-specific format, terminology, standard, approval gate, or artifact path in that project's profile. Promote a method into `skills/` when it works in other projects without importing the original project's vocabulary or files; keep examples in the originating profile.

Write `SKILL.md` as an agent decision guide: when to use it, what to decide or preserve, and what evidence makes the result credible. Keep it short. Link to a format as a reference unless the shape is itself a correctness requirement. Do not repeat another skill's rules; invoke it by name and add only the difference. A deterministic check belongs in a script when it is more reliable than prose.

When adding a skill, check its frontmatter name and description, links, invocation path from a router or README, and an example of a task it should and should not attract. Run [the library check](scripts/validate-library.py) for mechanical errors; it cannot judge whether the skill's advice is good. Mirror the human-readable instructions into the ignored Korean tree with matching relative layout; English remains canonical. Use the host's skill-creation tooling when available. This skill states the library's placement and naming philosophy, not the mechanics of a particular agent runtime.
