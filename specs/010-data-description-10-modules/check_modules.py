#!/usr/bin/env python3
"""
Check module pages against the contract (contracts/module-page-contract.md).
Usage: python check_modules.py [file1.qmd file2.qmd ...]
If no files given, checks all module-*.qmd in teaching/data-description/modules/
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
MODULES_DIR = REPO_ROOT / "teaching" / "data-description" / "modules"

REQUIRED_HEADINGS = [
    "## Learning objectives",
    "## Time plan",
    "## Theory",
    "## Worked example",
    "## Using Excel",
    "## Proof / derivation",
    "## Visual intuition",
    "## Interactive demo",
    "## Exercises",
    "## Common mistakes",
    "## Further reading",
]

def check_file(path):
    """Return (errors, warnings, time_sum) for a module file."""
    text = path.read_text(encoding="utf-8")
    errors = []
    warnings = []

    # 1. Front matter checks
    if not text.startswith("---"):
        errors.append("Missing front matter (---)")
    else:
        fm_end = text.find("\n---", 3)
        if fm_end == -1:
            errors.append("Front matter not closed")
        else:
            fm = text[3:fm_end]
            if "lang: en" not in fm:
                warnings.append("Front matter missing 'lang: en'")
            if "date-modified:" not in fm:
                warnings.append("Front matter missing 'date-modified:'")
            if "date:" in fm and "date-modified:" not in fm:
                warnings.append("Front matter has 'date:' but should use 'date-modified:'")

    # 2. Required headings in order (match at line start, allow suffixes)
    heading_positions = {}
    lines = text.split("\n")
    for i, line in enumerate(lines):
        stripped = line.strip()
        for h in REQUIRED_HEADINGS:
            if stripped == h or stripped.startswith(h + " "):
                # Calculate character position
                pos = len("\n".join(lines[:i])) + (1 if i > 0 else 0)
                if h not in heading_positions:  # first occurrence wins
                    heading_positions[h] = pos
                break

    for h in REQUIRED_HEADINGS:
        if h not in heading_positions:
            errors.append(f"Missing required heading: {h}")

    # Check order
    prev_pos = -1
    for h in REQUIRED_HEADINGS:
        pos = heading_positions.get(h, -1)
        if pos != -1 and pos < prev_pos:
            errors.append(f"Heading order violation: {h} appears before previous heading")
        prev_pos = max(prev_pos, pos)

    # 3. Time plan sums to 180
    time_match = re.search(r"## Time plan\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if time_match:
        time_text = time_match.group(1)
        # Look for pattern like "70 / 60 / 50" or "theory / Excel / exercises"
        nums = re.findall(r"(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", time_text)
        if nums:
            theory, excel, exercises = map(int, nums[0])
            total = theory + excel + exercises
            if total != 180:
                errors.append(f"Time plan sums to {total} min, expected 180 (theory={theory}, excel={excel}, exercises={exercises})")
        else:
            # Table format: sum every block row whose second cell is an
            # integer, except the Total row (tolerates extra rows such as
            # "Homework debrief", added by feature 012).
            table_rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", time_text, re.MULTILINE)
            table_rows = [(label, int(m)) for label, m in table_rows if "total" not in label.lower()]
            if len(table_rows) >= 3:
                total = sum(m for _, m in table_rows)
                if total != 180:
                    detail = ", ".join(f"{label}={m}" for label, m in table_rows)
                    errors.append(f"Time plan sums to {total} min, expected 180 ({detail})")
            else:
                warnings.append("Time plan format not recognized (expected 'X / Y / Z' or table with Theory/Excel lab/Exercises rows)")
    else:
        errors.append("Time plan section missing or empty")

    # 4. At least one collapsible .callout-caution
    if '.callout-caution collapse="true"' not in text:
        errors.append("No collapsible .callout-caution found (needed for derivations/exercises)")

    # 5. Further reading has OpenStax and Khan Academy
    fr_match = re.search(r"## Further reading\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if fr_match:
        fr_text = fr_match.group(1)
        has_openstax = "OpenStax" in fr_text or "openstax" in fr_text.lower()
        has_khan = "Khan Academy" in fr_text or "khanacademy" in fr_text.lower()
        if not has_openstax:
            errors.append("Further reading missing OpenStax reference")
        if not has_khan:
            errors.append("Further reading missing Khan Academy reference")
    else:
        errors.append("Further reading section missing")

    # 6. Demo or TODO callout
    has_demo = "shinylive-python" in text or "{ojs}" in text
    has_todo = 'TODO:' in text or 'TODO :' in text
    if not has_demo and not has_todo:
        errors.append("No interactive demo (shinylive-python or ojs) and no TODO callout")

    # 7. No inline style= or <style> blocks (outside code blocks)
    lines = text.split("\n")
    in_code = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("{shinylive-python}"):
            in_code = True
            continue
        if stripped.endswith("```") or stripped.startswith("{/shinylive-python}"):
            in_code = False
            continue
        if in_code:
            continue
        if re.search(r'style\s*=', line):
            errors.append(f"Line {i}: Found inline style= attribute (forbidden)")
        if "<style" in line.lower():
            errors.append(f"Line {i}: Found <style> block (forbidden)")

    # 8. Line wrapping (outside code blocks)
    lines = text.split("\n")
    in_code = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("{shinylive-python}"):
            in_code = True
            continue
        if stripped.endswith("```") or stripped.startswith("{/shinylive-python}"):
            in_code = False
            continue
        if in_code:
            continue
        if len(line) > 80 and not stripped.startswith("|") and "http" not in line and not stripped.startswith("title:") and not stripped.startswith("subtitle:") and not stripped.startswith("date-modified:") and not stripped.startswith("lang:"):
            warnings.append(f"Line {i} exceeds 80 chars: {line[:100]}...")

    return errors, warnings, total if 'total' in locals() else None

def main():
    if len(sys.argv) > 1:
        files = [Path(f) for f in sys.argv[1:]]
    else:
        files = sorted(MODULES_DIR.glob("module-*.qmd"))

    if not files:
        print("No module files found")
        return 1

    all_ok = True
    total_minutes = 0

    for f in files:
        print(f"\n=== Checking {f.name} ===")
        errors, warnings, time_sum = check_file(f)
        if time_sum:
            total_minutes += time_sum

        if errors:
            all_ok = False
            for e in errors:
                print(f"  FAIL {e}")
        else:
            print("  OK Structure checks passed")

        for w in warnings:
            print(f"  WARN {w}")

    print(f"\n=== Summary ===")
    print(f"Files checked: {len(files)}")
    print(f"Total course minutes (from time plans): {total_minutes}")
    if total_minutes != 1800:
        print(f"  WARN Expected 1800 min (10 × 180), got {total_minutes}")

    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())