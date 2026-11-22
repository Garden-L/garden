---
name: workflow-design
description: Use when designing a multi-stage workflow whose outputs, decisions, and checks must stay connected from initial input to a reviewable outcome.
---

# Workflow Design

Start with a result that can be checked, the input that supports it, and the boundaries of the claim. Divide the work into stages only where an output or decision can be reviewed before the next stage depends on it. For each stage, name its input, result, responsible decision, and check. Put uncertain, high-impact decisions early enough that downstream work does not silently assume their answers.

Make the handoff between stages explicit: which result becomes the next input, which identifier or link preserves its origin, and what happens when a check fails or evidence is missing. Keep one authoritative record for each fact or decision and link other artifacts to it. Use `decision` for choices whose effects cross stages. A plan or document is not evidence that the later work happened.

Choose only the rigor the result needs. A small task may combine stages in one session; a risky or irreversible task needs narrower units and stronger checks. The calling domain defines its file layout, standards, approval authority, and environment. This skill defines the reasoning for a workflow, not a universal document template.
