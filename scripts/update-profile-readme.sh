#!/usr/bin/env bash
# post-render script: generate a GitHub profile README from about.qmd
# and push it to the guillaumegilles/guillaumegilles repo.
set -euo pipefail

# Guard against recursive post-render invocation
if [ "${PROFILE_README_RUNNING:-}" = "1" ]; then
  exit 0
fi
export PROFILE_README_RUNNING=1

REPO="guillaumegilles/guillaumegilles"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TMPDIR="$(mktemp -d)"

cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT

echo "📄 Rendering about.qmd → GFM README.md …"
quarto render "$PROJECT_DIR/about.qmd" --to gfm \
  --output README.md --output-dir "$TMPDIR" 2>/dev/null

if [ ! -f "$TMPDIR/README.md" ]; then
  echo "❌ GFM render failed — README.md not produced."
  exit 1
fi

# Clean up Quarto artifacts:
# 1. Remove the auto-generated "# About" title (first 2 lines)
sed -i '1{/^# About$/d}' "$TMPDIR/README.md"
sed -i '1{/^$/d}' "$TMPDIR/README.md"
# 2. Fix shields.io badge URLs where Quarto appended .png
sed -i 's/logoColor=fff\.png/logoColor=fff/g' "$TMPDIR/README.md"

echo "📦 Cloning $REPO …"
if ! git clone --depth 1 "git@github.com:${REPO}.git" "$TMPDIR/profile-repo" 2>/dev/null; then
  echo "⚠️  Could not clone $REPO — skipping push (check SSH keys or auth)."
  echo "   README.md was generated at: $TMPDIR/README.md"
  # Prevent cleanup so user can inspect the file
  trap - EXIT
  exit 0
fi

if diff -q "$TMPDIR/README.md" "$TMPDIR/profile-repo/README.md" &>/dev/null; then
  echo "✅ Profile README is already up-to-date — nothing to push."
  exit 0
fi

cp "$TMPDIR/README.md" "$TMPDIR/profile-repo/README.md"

cd "$TMPDIR/profile-repo"
git add README.md
git commit -m "chore: sync profile README from ggilles.dev

Auto-generated from about.qmd by post-render script."
git push

echo "🚀 Profile README pushed to github.com/${REPO}"
