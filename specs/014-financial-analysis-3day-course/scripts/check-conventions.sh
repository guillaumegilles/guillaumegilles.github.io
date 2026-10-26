#!/bin/sh
# Convention checks from quickstart section 5 on the French course.
cd "$(dirname "$0")/../../.." || exit 2
FR=fr/teaching/financial-analysis
rc=0
if grep -rnE 'style=|<style' "$FR" --include=*.qmd; then echo "FAIL inline style"; rc=1; fi
# .callout-important must be followed (within 2 lines) by a TODO: title
for f in $(find "$FR" -name '*.qmd'); do
  awk -v F="$f" '
    /callout-important/ { want = NR; next }
    want && NR <= want + 2 && /^## / { if ($0 !~ /TODO:/) { print F ": callout-important without TODO: -> " $0; bad = 1 } want = 0 }
    END { exit bad }' "$f" || rc=1
done
# quests: one caution block each, exercises with folded answers
for f in $(ls "$FR"/modules/0[1-9]-*.qmd | grep -v enseignant); do
  n=$(grep -c 'callout-caution' "$f")
  [ "$n" -ge 1 ] || { echo "$f: no callout-caution derivation"; rc=1; }
  e=$(grep -c '{#exr-' "$f"); a=$(grep -c '<details class="answer">' "$f")
  [ "$e" -ge 1 ] || { echo "$f: no #exr- exercise"; rc=1; }
  [ "$a" -ge 1 ] || { echo "$f: no folded answer"; rc=1; }
done
exit $rc
