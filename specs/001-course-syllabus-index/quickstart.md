# Quickstart: Course Syllabus Index Pages

How to implement and verify this feature locally.

## Prerequisites

```sh
source .venv/bin/activate        # Python env for computational cells
quarto --version                 # Quarto CLI available
```

## Implement (per course)

For each course in `teaching/`, edit its `index.qmd` to match
`contracts/syllabus-template.md`:

1. **Front matter** — ensure `title`, `lang` (`fr`/`en`), `date-modified`.
   Remove any per-file `format:`/`theme:` override.
2. **Session outline** — add a `| # | Session | Topics Covered |` table whose
   Session cells link to the course's session files (use the exact paths from
   the matching `_quarto.yml` sidebar block).
3. **Recommended Literature** — add a table. Books:
   `| Author(s) | Title | Edition | Publisher/Source |`. Papers (ai-papers):
   `| Author(s) | Title | Year | Publication Venue |`. ≥1 row required.

Special cases:
- `ece-proba`: fix `_quarto.yml` so the block lists
  `teaching/ece-proba/index.qmd` (NOT the missing `statistics-probability/...`).
- `essca-stat`: drop the `cosmo` theme override; use `date-modified`.
- `inseec-finance`: add a full YAML front-matter block (none exists today).
- `ai-papers`: clean the stray draft placeholder block; add front matter.

## Bilingual counterpart stubs

For each **EN-authored** course (`essca-stat`, `ai-papers`, `ai-dev`), create a
French stub at `fr/teaching/<course>/index.qmd` per the stub contract, and
register it in `_quarto.yml`. Do **not** create an `en/` tree — the three
FR-authored courses (`inseec-finance`, `ece-proba`, `mathematical-analysis`)
are handled by the separate language-normalization feature.

## Verify

```sh
# Per-file spot check (fast)
quarto render teaching/essca-stat/index.qmd --quiet

# Full render gate (MUST exit 0 before commit)
quarto render
echo "exit: $?"
```

Structural checks (no new tooling — plain grep):

```sh
for f in teaching/*/index.qmd; do
  echo "== $f =="
  grep -qE '^lang:' "$f"            && echo "  lang ok"        || echo "  MISSING lang"
  grep -qE '^date-modified:' "$f"   && echo "  date ok"        || echo "  MISSING date-modified"
  grep -qiE '^##.*(Literature|Bibliograph)' "$f" && echo "  literature heading ok" || echo "  MISSING literature"
  grep -qE '^\| *# *\|' "$f"        && echo "  outline table ok" || echo "  MISSING outline table"
  grep -qE '^(format|theme):' "$f"  && echo "  WARN per-file theme override" || true
done
```

## Definition of Done

- [ ] All 6 `teaching/*/index.qmd` pass the structural checks above.
- [ ] `quarto render` exits 0.
- [ ] `ece-proba` sidebar points to the real `index.qmd`.
- [ ] Each syllabus is the first entry in its sidebar block.
- [ ] A French stub exists for every EN-authored course (`essca-stat`,
      `ai-papers`, `ai-dev`) and renders (no 404). FR-authored courses deferred.
- [ ] `docs/` and `_freeze/` committed alongside the source changes.
