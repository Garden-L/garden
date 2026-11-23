# Requirements to SRS

Use when supplied automotive requirements must become an SRS.

1. Confirm the source revision, module scope, target context, and relevant boundaries.
2. Apply `spec-requirements` for general requirement quality and traceability. Preserve source wording and location for each derived `REQ`; do not treat a citation as proof of standards compliance.
3. Apply the [automotive SRS context](../references/automotive-srs-context.md) to consider vehicle mode, ignition/power, driving state, signal validity, timing, faults, and recovery only when supported by the source or owner.
4. Record assumptions, conflicting sources, and unresolved behavior as issues linked to affected `REQ` IDs. Do not invent safety levels, standards decisions, interfaces, limits, or architecture.
5. Use flows only when they clarify a sequence, branch, or state change. Keep unknown branches open and link nodes to `REQ` IDs. Keep test procedures and evidence in the STS.
6. For substantial or consequential SRS work, use separate author and reviewer roles when available. Read the [SRS author brief](../references/srs-author-brief.md) and [reviewer brief](../references/srs-reviewer-brief.md) at those steps. Apply shared `review` and resolve confirmed findings in the SRS and affected flows.

Output: an SRS with stable requirement IDs, source links, explicit open decisions, and only the flows that clarify behavior. The shared SRS format is a reference, not a required layout; the [automotive example](../references/automotive-srs-example.md) is illustrative.
