# Package architecture

```text
automotive-development/SKILL.md
        ↓ selects one automotive workflow
automotive-development/playbooks/*.md
        ↓ composes shared principles and general workflows
skills/* + automotive-development/references/*
```

The package-level skill classifies automotive work and routes it. Automotive SRS, STS, feature, bug fix, refactoring, architecture change, and approved-baseline change are playbooks, not nested standalone skills. The playbooks combine small shared principles and general methods with automotive source rules, work-package boundaries, evidence, and approval gates. Conditional guidance and examples live in `references/` and are loaded only when needed.

The [module deliverables guide](module-deliverables.md) defines shared artifact links and status meanings. Structural checks live in `scripts/validate-module-delivery.py`; they cannot substitute for reviewing meaning or target behavior.
