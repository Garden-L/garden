#!/usr/bin/env bash
set -euo pipefail

package_dir="$(cd "$(dirname "$0")/.." && pwd -P)"
repo_dir="$(cd "$package_dir/.." && pwd -P)"

if [[ -d "$package_dir/skills" ]]; then
  echo "nested skills/ directory is not part of the automotive package layout" >&2
  exit 1
fi

required_files=(
  "$package_dir/SKILL.md"
  "$package_dir/README.md"
  "$package_dir/agents/README.md"
  "$package_dir/agents/openai.yaml"
  "$package_dir/docs/architecture.md"
  "$package_dir/docs/module-deliverables.md"
  "$package_dir/playbooks/requirements-to-srs.md"
  "$package_dir/playbooks/srs-to-sts.md"
  "$package_dir/playbooks/feature.md"
  "$package_dir/playbooks/bug-fix.md"
  "$package_dir/playbooks/refactoring.md"
  "$package_dir/playbooks/change-control.md"
  "$package_dir/playbooks/architecture-change.md"
  "$package_dir/references/automotive-srs-context.md"
  "$package_dir/references/automotive-sts-context.md"
  "$package_dir/references/sts-reviewer-checklist.md"
  "$package_dir/scripts/README.md"
  "$package_dir/scripts/validate-module-delivery.py"
  "$package_dir/scripts/report-module-coverage.py"
  "$package_dir/examples/speed-signal/README.md"
  "$repo_dir/skills/minimal-change/SKILL.md"
  "$repo_dir/skills/work-decomposition/SKILL.md"
)

for file in "${required_files[@]}"; do
  test -f "$file" || { echo "missing: ${file#$repo_dir/}" >&2; exit 1; }
done

for playbook in "$package_dir"/playbooks/*.md; do
  playbook_name="${playbook##*/}"
  case "$playbook_name" in
    requirements-to-srs.md|srs-to-sts.md|feature.md|bug-fix.md|refactoring.md|change-control.md|architecture-change.md) ;;
    *) echo "unexpected automotive playbook: $playbook_name" >&2; exit 1 ;;
  esac
done

for file in "$package_dir/SKILL.md" "$package_dir"/playbooks/*.md "$repo_dir"/skills/*/SKILL.md; do
  test -f "$file" || { echo "missing skill/playbook file: ${file#$repo_dir/}" >&2; exit 1; }
  sed -n '1,8p' "$file" | rg -q '^name:|^# ' || { echo "missing readable header: ${file#$repo_dir/}" >&2; exit 1; }
done

echo "automotive-development package structure: OK"
