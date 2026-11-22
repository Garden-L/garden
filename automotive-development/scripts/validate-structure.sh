#!/usr/bin/env bash
set -euo pipefail

package_dir="$(cd "$(dirname "$0")/.." && pwd -P)"
repo_dir="$(cd "$package_dir/.." && pwd -P)"

required_files=(
  "$package_dir/README.md"
  "$package_dir/docs/architecture.md"
  "$package_dir/agents/README.md"
  "$package_dir/scripts/README.md"
  "$package_dir/skills/automotive-engineering/SKILL.md"
  "$package_dir/skills/automotive-engineering/playbooks/requirements-to-srs.md"
  "$package_dir/skills/automotive-engineering/playbooks/module-delivery.md"
  "$package_dir/skills/automotive-engineering/playbooks/implementation-planning.md"
  "$package_dir/skills/automotive-engineering/playbooks/feature.md"
  "$package_dir/skills/automotive-engineering/playbooks/bug-fix.md"
  "$package_dir/skills/automotive-engineering/playbooks/refactoring.md"
  "$package_dir/skills/automotive-engineering/playbooks/integration-testing.md"
  "$package_dir/skills/automotive-engineering/playbooks/code-review.md"
  "$package_dir/skills/automotive-engineering/playbooks/release-readiness.md"
  "$package_dir/docs/module-deliverables.md"
  "$package_dir/scripts/validate-module-delivery.py"
  "$package_dir/scripts/report-module-coverage.py"
  "$package_dir/examples/speed-signal/docs/modules/speed-signal/README.md"
)

for file in "${required_files[@]}"; do
  test -f "$file" || { echo "missing: ${file#$repo_dir/}" >&2; exit 1; }
done

for file in "$package_dir"/skills/automotive-engineering/playbooks/*.md "$package_dir"/skills/*/SKILL.md "$repo_dir"/skills/*/SKILL.md; do
  test -f "$file" || { echo "missing skill/playbook file: ${file#$repo_dir/}" >&2; exit 1; }
  sed -n '1,8p' "$file" | rg -q '^name:|^# ' || { echo "missing readable header: ${file#$repo_dir/}" >&2; exit 1; }
done

echo "automotive-development package structure: OK"
