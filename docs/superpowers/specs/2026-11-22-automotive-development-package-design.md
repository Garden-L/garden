# Automotive Development Package Design

## Intent

Make `automotive-development` a project-style Codex skill package while allowing future domain packages, such as web development, to reuse domain-neutral skills.

## Structure

- `skills/shared/` contains independently usable skills for architecture, TDD, verification, and Git hygiene.
- `automotive-development/SKILL.md` is the automotive package router.
- `automotive-development/playbooks/` contains automotive workflow compositions.
- `automotive-development/skills/` remains the home of automotive-specific leaf skills.
- Package documentation, agent briefs, and validation scripts live under the automotive package.

## Goals

- Keep existing automotive skill paths stable.
- Load only the shared and automotive skills required by the selected workflow.
- Make shared skills usable without automotive context.
- Provide a documented extension point for future domain packages.

## Non-goals

- Do not create a web-development package yet.
- Do not move or rewrite existing automotive leaf skills.
- Do not add runtime dependencies or automate external ECU/HIL environments.

## Routing

The top-level automotive skill classifies the request, selects one playbook, and instructs the agent to read the playbook plus only its referenced skills. Direct invocation of an existing leaf skill remains valid.
