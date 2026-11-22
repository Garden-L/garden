# Package architecture

`automotive-development` has three layers:

```text
automotive-development/skills/automotive-engineering/SKILL.md
        ↓ selects and coordinates
automotive-development/skills/automotive-engineering/playbooks/*.md
        ↓ resolves names through the central skill registry and reads only those needed
skills/* + automotive-development/skills/*
```

The engineering skill owns request classification and workflow selection. Its co-located `playbooks/` directory owns stage sequencing, inputs, and outputs. Shared skills own reusable SRS/STS principles and reference formats; automotive leaf skills add vehicle context, applicable sources, target considerations, and lifecycle gates.

The [module-delivery playbook](../skills/automotive-engineering/playbooks/module-delivery.md) composes the focused stages. The [module artifact contract](module-deliverables.md) defines the consuming project's deliverable paths and cross-links. Shared `decision` preserves reasoning across those artifacts; the automotive package chooses the concrete `ISSUE`, `REQ`, `TC`, and `WORK` links. Structural checking lives in `scripts/validate-module-delivery.py` and cannot substitute for review of meaning or target behavior.

After SRS/STS readiness, focused development playbooks cover implementation planning, feature work, bug fixes, refactoring, integration testing, code review, implementation verification, and release readiness. Existing shared skills remain the source of reusable engineering methods; the automotive package adds vehicle-specific constraints and gates.
