#!/usr/bin/env bash
# validate-all.sh — run validators across all four sub-repos.
#
# Usage:
#   ./validate-all.sh           # default mode
#   ./validate-all.sh --strict  # gate-quality mode
#
# Exits non-zero on any failure.
set -euo pipefail

STRICT=""
if [ "${1:-}" = "--strict" ]; then
  STRICT="--strict"
fi

ROOT="$(cd "$(dirname "$0")" && pwd)"
FAILED=0

run() {
  local name="$1"; shift
  echo "=== $name ==="
  if "$@"; then
    echo "  PASS"
  else
    echo "  FAIL"
    FAILED=1
  fi
  echo
}

run "corpus"  python3 "$ROOT/corpus/tools/validate.py"  "$ROOT/corpus/corpus.jsonl"      $STRICT
run "cad"     python3 "$ROOT/cad/tools/validate.py"     "$ROOT/cad/designs.jsonl"        $STRICT
run "fab"     python3 "$ROOT/fab/tools/validate.py"     "$ROOT/fab/recipes.jsonl"        $STRICT
run "control" python3 "$ROOT/control/tools/validate.py" "$ROOT/control/instruments.jsonl" $STRICT

if [ "$FAILED" -ne 0 ]; then
  echo "One or more sub-repos failed validation."
  exit 1
fi
echo "All sub-repos validated cleanly."
