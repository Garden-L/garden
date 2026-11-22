# Feature Development

Use when adding behavior defined by an approved requirement and an eligible `WORK-###` packet.

1. Confirm readiness, packet ID, acceptance behavior, changed interfaces, and out-of-scope items.
2. Apply `engineering-design` for changes crossing module or function boundaries; settle the data shape and ownership before coding.
3. Apply `implementation` and `bounded-implementation-execution` to implement only the packet.
4. Write or select a behavior-level test before production changes when a practical test path exists. Establish the failing or missing behavior, then implement the smallest passing change.
5. Run focused tests first, then relevant regression, integration, and static checks. Keep test results tied to the same revision.
6. Update the packet and traceability links with changed files, checks, evidence, and deviations.
7. Route the completed change to [Code Review](code-review.md) and [Implementation Verification](verification.md).

Output: one bounded feature change with behavior evidence and updated traceability.
