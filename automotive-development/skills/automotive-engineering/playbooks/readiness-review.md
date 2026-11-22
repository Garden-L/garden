# Implementation Readiness Review

Use before production code or automated tests begin when an SRS and/or STS exists.

1. Apply `engineering-design` for the shared readiness method.
2. Apply `implementation-readiness-review` for automotive SRS/STS, safety, target, and HIL gates.
3. Apply `verification` to inspect the actual source artifacts and evidence.
4. Inspect repository state when existing artifacts are part of the review.
5. Stop at unresolved implementation-changing decisions; do not silently approve them.

Output: a readiness decision, actionable issues, and proposed first TDD slices. After readiness, use [Implementation Planning](implementation-planning.md) to prepare bounded code work.
