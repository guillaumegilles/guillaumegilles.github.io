#!/bin/sh
# Every FR page needs an EN counterpart; EN pages other than index/planning
# must be stubs.
cd "$(dirname "$0")/../../.." || exit 2
FR=fr/teaching/financial-analysis
EN=teaching/financial-analysis
rc=0
for f in $(cd "$FR" && find . -name '*.qmd' | sort); do
  if [ ! -f "$EN/$f" ]; then echo "MISSING $EN/$f"; rc=1; continue; fi
  case "$f" in
    ./index.qmd|./planning.qmd) ;;
    *) grep -qi "Translation in progress" "$EN/$f" || { echo "NOT A STUB $EN/$f"; rc=1; } ;;
  esac
done
exit $rc
