---
name: automotive-development
description: For automotive software work, find the relevant procedure in playbooks and apply its needed principles and references.
---

# Automotive Development

Identify the requested outcome and current artifacts. Match the task to a file in [playbooks/](playbooks/), open its full steps, and carry those steps through to their stated output. If several playbooks apply, follow their dependencies and use each only for the work it owns. The playbooks select shared principles and task-specific references.

## Governing principles

- Ground every behavior and expected result in an identified source, approved decision, or observed evidence. Keep assumptions and open questions visible.
- Preserve traceability across source requirements, SRS, STS, work packages, code changes, and verification. Identify the applicable artifact revisions before acting.
- Treat an approved baseline as a boundary. Assess and resolve a proposed change to requirements, interfaces, expected results, or acceptance criteria before dependent work proceeds.
- Keep work and claims proportional to the evidence. Distinguish planned checks from executed checks and local results from integration, ECU, HIL, vehicle, and release results.
- Never infer approval or invent safety levels, compliance claims, interfaces, limits, or expected behavior.

Task steps, outputs, and handoff conditions belong to the selected playbook. Shared principles named there live at `../skills/<name>/SKILL.md` relative to this file; read a named leaf skill when applying it. Report the result, evidence, and remaining limits.
