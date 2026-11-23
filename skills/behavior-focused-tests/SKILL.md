---
name: behavior-focused-tests
description: Assert outputs, state changes, errors, or side effects a caller can observe. Use when writing or revising a test that should keep passing through behavior-preserving refactoring.
---

# Behavior-Focused Tests

Assert what a caller or user can observe: outputs, state changes, errors, side effects, or externally visible timing. Choose inputs that distinguish correct behavior from the regression or requirement being guarded.

Avoid coupling a test to private helpers, incidental call order, or internal data layout unless that detail is itself part of the contract. A useful test fails when the behavior breaks and continues to pass through a behavior-preserving refactor.
