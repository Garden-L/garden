---
name: root-cause-first
description: Trace a reproduced symptom to the earliest supported cause before choosing a correction. Use for defects, recurring failures, or fixes that have already failed once.
---

# Root Cause First

Trace the failure to the earliest incorrect state or decision that explains the observed symptom. Reproduce it, inspect the relevant flow, and test a concrete cause before choosing a fix.

Correct that cause when it is within scope. Add a guard at the symptom only when the state is legitimately possible and the guard defines the intended behavior. After the change, repeat the original reproduction and check the behavior that depends on the corrected state. Do not stack another workaround on an untested explanation.
