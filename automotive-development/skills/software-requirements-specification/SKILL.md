---
name: software-requirements-specification
description: Use when supplied automotive requirements need to be drafted or reviewed as a Markdown Software Requirements Specification (SRS).
---

# Automotive Software Requirements Specification

Turn the supplied requirement sentences into a readable Markdown SRS using the [output format](references/srs-output-format.md). This single skill owns authoring, independent review, user decisions, and final updates. By default, run the author and reviewer roles below as separate sub-agents when multi-agent support is available.

## Default sub-agent workflow

1. Send the supplied requirements and context to the **author sub-agent** using [author-agent.md](references/author-agent.md). It creates the SRS draft, requirement IDs, and Mermaid flows.
2. Send the source requirements and the draft independently to the **review sub-agent** using [review-agent.md](references/review-agent.md). It returns only actionable findings, resolution options, and recommendations; it does not edit the draft.
3. Present the review findings to the user. Ask the user to choose a recommended option, choose another option, or provide an additional requirement.
4. Send the user's decision back to the author sub-agent. Update the affected requirement, issue status, decision record, and Mermaid flows together.
5. Repeat review only for the changed or newly affected parts unless the user requests a full review.

If sub-agent tools are unavailable, perform the same author-then-review sequence in the main agent and clearly keep the two roles separate.

The author and reviewer are separate roles inside this skill. The reviewer returns findings only; the author applies user-approved decisions.

- Start with a short clarification pass. If an ambiguity, conflict, missing condition, actor, threshold, or scope decision would change the SRS or its flow, ask the user a focused question before finalizing that part.
- For each important ambiguity, give a recommended interpretation or a small set of concrete options, explain the practical effect, and let the user choose or add a different requirement.
- Ask only the highest-impact questions first, group related questions, and wait for the user's answers before treating the affected wording or flow as confirmed.
- Accept additional user requirements after the recommendation and merge them into the affected requirement, source note, open item, and Mermaid flow.
- If the user asks for a draft before answering, label the affected requirements and Mermaid nodes as `Confirmation needed` or `TBD`; never silently choose an assumption.
- Give each requirement a unique ID and quote its source sentence verbatim alongside it. Use “shall” for obligations and make small wording edits only when the meaning is clear.
- Perform a lightweight quality check for each requirement: actor, trigger, condition, single obligation, measurable wording, terminology consistency, and consistency with related requirements.
- Send only failed or questionable checks to Issues and open items with resolution options; do not create a long checklist when no problem is found.
- Flag unclear, conflicting, or incomplete wording under Issues and open items. For each issue, list practical resolution options, recommend one, and ask the user to choose an option or provide a custom resolution.
- When the user chooses or supplies a resolution, mark the issue `Resolved`, apply the decision to the requirement and Mermaid flow, and keep the decision record in the SRS.
- Create a small Mermaid flow for an individual requirement when it has multiple steps, a condition, or a state change; omit a flow for a simple standalone statement.
- When multiple requirements have clear dependencies or a shared sequence, add one integrated Mermaid flow that connects their IDs. Do not force unrelated requirements into the same chart.
- Label unknown steps or decisions as `TBD` instead of inventing behavior.
- Ground the SRS in the supplied material. Leave unsupported values, standards compliance, safety levels, and architecture open. Keep implementation and test code outside the SRS.

See the [worked example](references/example.md) for vague timing, a missing condition, and a scope conflict.
