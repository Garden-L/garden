# Baseline Change Control

Use when implementation reveals a proposed change to an approved SRS, STS, interface, or acceptance criterion.

1. Trace the affected approved artifacts, interfaces, behavior, tests, and downstream work.
2. Use the automotive [SRS](requirements-to-srs.md) and [STS](srs-to-sts.md) playbooks to assess affected behavior and tests; use `decision` for the choice and rationale.
3. Apply `verification` to confirm the proposed change against the actual artifacts.
4. Preserve unrelated work while recording the change.
5. Pause the affected implementation until the change decision and downstream impact are recorded.

Output: a change-control record, impact analysis, and an explicit resume condition.
