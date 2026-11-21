# SRS to STS

Use when an automotive SRS or requirements document must become a traceable English STS.

1. Apply `engineering-design` to confirm the SRS revision, scope, and open decisions.
2. Apply `software-test-documentation`; it invokes `spec-tests` and adds vehicle-specific test conditions and environment guidance.
3. Apply `verification` before reporting coverage.
4. Keep unsupported test environments, limits, and expected behavior explicit rather than guessing. Link gaps to the affected `REQ` and `ISSUE` IDs.

Output: an STS with traceable test cases, selected test design techniques, and executable procedures. The shared format is a reference, not a required layout.
