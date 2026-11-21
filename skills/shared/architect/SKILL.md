---
name: architect
description: Use before non-trivial implementation work that crosses module, data, or process boundaries; define ownership, interfaces, and a small design before editing.
---

# Shared Architecture Skill

Use this skill before implementation when the change crosses a boundary or has more than one plausible shape.

1. State the requested outcome and the smallest acceptable change.
2. Trace the callers, inputs, outputs, and owners affected by the change.
3. Sketch two plausible designs when the shape is not obvious.
4. Choose the design with the fewest owners, hidden states, and compatibility layers.
5. Record assumptions, non-goals, and the verification that will prove the design works.

This skill is domain-neutral. Do not invent automotive, web, or safety-specific behavior here; leave those decisions to the calling domain workflow.
