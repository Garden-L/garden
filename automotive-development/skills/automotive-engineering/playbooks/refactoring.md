# Refactoring

Use when changing code structure without changing approved externally observable behavior.

1. Confirm the work packet explicitly preserves behavior and identifies the allowed scope.
2. Inspect callers and existing tests; add or identify a characterization check for the behavior that must remain stable.
3. Apply `engineering-design` to state the target structure and why it reduces complexity or invalid states.
4. Apply `implementation` and `bounded-implementation-execution` to make small structural changes while keeping the behavior checks passing.
5. Remove obsolete paths and update every caller in the same bounded work item. Do not introduce unused compatibility layers.
6. Compare before/after behavior on the relevant test and target surface. If new behavior is needed, stop and create a separate feature or bug-fix packet.
7. Update traceability and route the diff to [Code Review](code-review.md).

Output: a behavior-preserving structural change with a recorded equivalence check.
