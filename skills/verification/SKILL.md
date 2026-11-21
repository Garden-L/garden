---
name: verification
description: Use before declaring work complete; verify the real artifact and report direct evidence rather than relying on compilation, self-report, or file presence.
---

# Verification

Verify the artifact the user will actually consume.

- Read the final diff and confirm the scope.
- Run the narrowest relevant test, checker, or real workflow.
- Inspect the produced document, value, or runtime behavior directly.
- Check the failure path when the workflow has a gate or approval boundary.
- Report the exact command and result, including limitations.

The calling project workflow owns domain-specific approval decisions.
