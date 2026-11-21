---
name: software-requirements-specification
description: Use when supplied automotive requirements need to be drafted or reviewed as a Software Requirements Specification (SRS).
---

# Automotive SRS profile

Apply `spec-requirements` for general SRS principles, IDs, and a reference format. This profile adds only [automotive considerations](references/automotive-context.md). The [automotive example](references/example.md) illustrates how source wording, vehicle states, flows, and open decisions can appear in an SRS; it is not a required layout.

Preserve the supplied wording alongside derived requirements so a reviewer can trace each obligation to its source. Check whether vehicle mode, ignition/power state, driving/parked state, signal validity, timing, faults, and recovery affect the behavior. Include a condition only when supported by the source or confirmed by the owner. For standards and external documents, record which provisions apply and why; do not claim compliance from a citation alone.

Show a flow only when it clarifies a sequence, branch, or state change. Link its nodes to the relevant `REQ` IDs and mark unknown behavior as open. If a question changes behavior, scope, safety, or verification, identify the affected `REQ` IDs, explain the impact, offer a recommendation, and leave the decision with its owner. Apply `why` and `how` through the shared `specification` skill; do not duplicate their rules here.

For a substantial SRS, use separate author and independent reviewer roles when available: [author brief](references/author-agent.md) and [review brief](references/review-agent.md). Review against the source, resolve confirmed decisions in both requirements and affected flows, then recheck the changed parts. If separate agents are unavailable, perform those roles sequentially.
