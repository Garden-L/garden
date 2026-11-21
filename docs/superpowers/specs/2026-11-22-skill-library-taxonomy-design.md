# Skill Library Taxonomy Design

## Intent

Group the skill library by both the kind of thinking a skill supports and the practical work area where it is used. This should make the collection easier to browse without making domain packages depend on repeated file paths.

## Goals

- Use purpose-led categories: frame, build, prove, communicate, and sustain.
- Keep domain workflows such as automotive development as composed packages.
- Preserve skill names and contents while moving files.
- Update indexes and the automotive skill registry to the new locations.

## Non-goals

- Rewriting skill guidance or changing invocation semantics.
- Creating adapters for specific agent products.
- Adding new skills or deleting existing ones.

## Proposed structure

```text
skills/
  frame/       # architect, input-review, change-impact
  build/       # software/tdd; automation/pattern-to-tool
  prove/       # verification, verification-evidence, traceability
  communicate/ # requirements, testing, learning/coursebook authoring
  sustain/     # git-hygiene
automotive-development/ # domain workflow package
```

Automotive-specific lifecycle skills stay in `automotive-development/skills/`. Shared skills move into purpose-based subdirectories under `skills/`. The automotive router owns the name-to-file registry; playbooks refer to skill names only.

## Mapping

- `frame`: architect, input-review, change-impact
- `build/software`: tdd
- `build/automation`: pattern-to-tool
- `prove`: verification, verification-evidence, traceability
- `communicate/requirements`: input-review remains in frame; automotive SRS stays domain-specific
- `communicate/testing`: automotive STS stays domain-specific
- `communicate/learning`: programming-coursebook-authoring
- `sustain`: git-hygiene

## Open implementation detail

The automotive-specific requirements and test-documentation skills remain within their domain package because their content carries automotive assumptions. Their contribution is indexed under communicate in the automotive package documentation rather than moved into the domain-neutral collection.
