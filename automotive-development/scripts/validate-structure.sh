#!/usr/bin/env bash
set -euo pipefail

package_dir="$(cd "$(dirname "$0")/.." && pwd -P)"
repo_dir="$(cd "$package_dir/.." && pwd -P)"

required_files=(
  "$package_dir/README.md"
  "$package_dir/docs/architecture.md"
  "$package_dir/agents/README.md"
  "$package_dir/scripts/README.md"
  "$package_dir/skills/automotive-development-pipeline/SKILL.md"
  "$package_dir/skills/automotive-development-pipeline/playbooks/requirements-to-srs.md"
)

for file in "${required_files[@]}"; do
  test -f "$file" || { echo "missing: ${file#$repo_dir/}" >&2; exit 1; }
done

for file in "$package_dir"/skills/automotive-development-pipeline/playbooks/*.md "$package_dir"/skills/*/SKILL.md "$repo_dir"/skills/shared/*/SKILL.md; do
  test -f "$file" || { echo "missing skill/playbook file: ${file#$repo_dir/}" >&2; exit 1; }
  sed -n '1,8p' "$file" | rg -q '^name:|^# ' || { echo "missing readable header: ${file#$repo_dir/}" >&2; exit 1; }
done

echo "automotive-development package structure: OK"
