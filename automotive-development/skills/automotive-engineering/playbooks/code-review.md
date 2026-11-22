# Code Review

Use when reviewing a completed code change before verification sign-off or delivery.

1. Apply `review` to set scope and inspect the actual diff against the approved work packet and baseline.
2. Check behavior against linked SRS/STS expectations without rewriting them. Assess scope, error paths, state/timing behavior, regressions, interfaces, and traceability as relevant to the change.
3. Report only actionable findings with severity, exact location, evidence, impact, and recommended action. Separate confirmed defects from questions and suggestions.
4. Do not edit the change while acting as reviewer. Return findings to the implementation owner, then review the new revision after fixes.

Output: review verdict, actionable findings, and evidence. Runtime and target evidence belongs to [Implementation Verification](verification.md).
