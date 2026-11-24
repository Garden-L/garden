#!/usr/bin/env bash
set -euo pipefail

package_dir="$(cd "$(dirname "$0")/.." && pwd -P)"
repo_dir="$(cd "$package_dir/.." && pwd -P)"

if [[ -d "$package_dir/skills" ]]; then
  echo "패키지 안에 skills/ 디렉터리를 두지 않는다" >&2
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
  test -f "$file" || { echo "누락: ${file#$repo_dir/}" >&2; exit 1; }
done

for playbook in "$package_dir"/playbooks/*.md; do
  playbook_name="${playbook##*/}"
  case "$playbook_name" in
    requirements-to-srs.md|srs-to-sts.md|feature.md|bug-fix.md|refactoring.md|change-control.md|architecture-change.md) ;;
    *) echo "예상하지 못한 자동차 플레이북: $playbook_name" >&2; exit 1 ;;
  esac
done

for file in "$package_dir/SKILL.md" "$package_dir"/playbooks/*.md "$repo_dir"/skills/*/SKILL.md; do
  test -f "$file" || { echo "스킬/플레이북 파일 누락: ${file#$repo_dir/}" >&2; exit 1; }
  sed -n '1,8p' "$file" | rg -q '^name:|^# ' || { echo "읽을 수 있는 제목 없음: ${file#$repo_dir/}" >&2; exit 1; }
done

echo "garden-beam 패키지 구조: 정상"
