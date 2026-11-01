#!/bin/sh
# Usage: check-timetable.sh path/to/planning.qmd
# Sums the "Duration (min)" (3rd) column of rows whose first cell is D<d>-B<n>.
f="${1:?planning.qmd path}"
awk -F'|' '
  $2 ~ /^ *D[1-3]-B[0-9]+ *$/ {
    d = substr($2, index($2, "D") + 1, 1); gsub(/ /, "", $4)
    sum[d] += $4; total += $4
  }
  END {
    bad = 0
    for (d = 1; d <= 3; d++) {
      printf "Day %d: %d min\n", d, sum[d]
      if (sum[d] != 360) bad = 1
    }
    printf "Total: %d min\n", total
    if (total != 1080) bad = 1
    exit bad
  }' "$f"
