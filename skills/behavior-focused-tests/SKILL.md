---
name: behavior-focused-tests
description: Use when creating, changing, or assessing tests for a software behavior.
---

# Behavior-Focused Tests

Assert what a caller or user can observe: outputs, state changes, errors, side effects, or externally visible timing. Choose inputs that distinguish correct behavior from the regression or requirement being guarded.

Avoid coupling a test to private helpers, incidental call order, or internal data layout unless that detail is itself part of the contract. A useful test fails when the behavior breaks and continues to pass through a behavior-preserving refactor.
