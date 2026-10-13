#!/usr/bin/env python3
"""
Check revised module pages against contracts/module-page-contract-v2.md.

Usage:
  python check_modules_v2.py [--needs-debrief] [--synthesis] FILE.qmd [...]

--needs-debrief  the previous module has homework: a `Homework debrief`
                 time-plan row is mandatory.
--synthesis      Module 10 exception: waives the Try-it-before-formula
                 rule, the decoder-after-formula rule and the
                 formula <-> words exercise rule.

Exit code 1 if any FAIL.
"""

import re
import sys
from pathlib import Path

H2_ORDER = [
    "## Learning objectives",
    "## Time plan",
    "## Theory",
    "## Worked example",
    "## Proof / derivation",
    "## Visual intuition",
    "## Interactive demo",
    "## Exercises",
    "## Common mistakes",
    "## Exit check",
    "## Homework — Excel lab",
    "## Further reading",
]
HOMEWORK = "## Homework — Excel lab"
FENCE = re.compile(r"^\s*```")


def code_mask(lines):
    """True for lines inside (or delimiting) fenced code blocks."""
    mask, inside = [], False
    for line in lines:
        if FENCE.match(line):
            mask.append(True)
            inside = not inside
            continue
        mask.append(inside)
    return mask


def h2_index(lines, mask):
    """Map each required H2 to its first line index."""
    found = {}
    for i, line in enumerate(lines):
        if mask[i] or not line.startswith("## "):
            continue
        for h in H2_ORDER:
            if h not in found and (line.strip() == h or line.startswith(h + " ")):
                found[h] = i
    return found


def section(lines, mask, start):
    """Line range [start+1, end) up to the next H2 outside code."""
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if not mask[j] and lines[j].startswith("## "):
            end = j
            break
    return start + 1, end


def check_time_plan(lines, rng, needs_debrief, errors):
    rows = []
    for line in lines[rng[0]:rng[1]]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"\d+", cells[1]):
            continue
        if "total" in cells[0].lower():
            continue
        rows.append((cells[0], int(cells[1])))
    if not rows:
        errors.append("Time plan: no table rows with minutes found")
        return None
    total = sum(m for _, m in rows)
    if total != 180:
        errors.append(f"Time plan sums to {total} min, expected 180")
    for label, m in rows:
        if label.lower().startswith("excel lab"):
            errors.append(f"Time plan has an in-class Excel lab row ({label})")
    previews = [(l, m) for l, m in rows if l.lower().startswith("excel preview")]
    if len(previews) > 1:
        errors.append("Time plan has more than one Excel preview row")
    for l, m in previews:
        if m > 5:
            errors.append(f"Excel preview is {m} min, max 5")
    debriefs = [(l, m) for l, m in rows if l.lower().startswith("homework debrief")]
    for l, m in debriefs:
        if m > 10:
            errors.append(f"Homework debrief is {m} min, max 10")
    if needs_debrief and not debriefs:
        errors.append("Time plan missing required `Homework debrief` row")
    return total


def check_theory(lines, mask, rng, errors):
    a, b = rng
    try_idx = next((i for i in range(a, b) if not mask[i]
                    and lines[i].startswith("#### Try it")), None)
    tips = [i for i in range(a, b) if not mask[i] and ".callout-tip" in lines[i]]
    if try_idx is None:
        errors.append("Theory: no `#### Try it` callout")
    elif tips and tips[0] < try_idx:
        errors.append("Theory: first formula callout (.callout-tip) comes "
                      "before the first Try it")
    for t in tips:
        next_h3 = next((j for j in range(t + 1, b) if not mask[j]
                        and lines[j].startswith("### ")), b)
        dec = next((j for j in range(t + 1, next_h3) if not mask[j]
                    and lines[j].startswith("#### Notation decoder")), None)
        if dec is None:
            errors.append(f"Line {t + 1}: formula callout has no "
                          "`#### Notation decoder` before the next ### heading")
        elif ".callout-note" not in lines[dec - 1]:
            errors.append(f"Line {dec + 1}: notation decoder is not a "
                          ".callout-note")


def check_exercises(lines, rng, synthesis, errors):
    text = "\n".join(lines[rng[0]:rng[1]])
    titles = re.findall(r"^#### Exercise \d+ \(by hand\).*$", text, re.M)
    need = 1 if synthesis else 3
    if len(titles) < need:
        errors.append(f"Exercises: {len(titles)} by-hand exercises, need ≥ {need}")
    if text.count('.callout-caution collapse="true"') < len(titles):
        errors.append("Exercises: every exercise must be a collapsible "
                      ".callout-caution")
    if not synthesis:
        joined = " ".join(titles).lower()
        if "formula to words" not in joined:
            errors.append("Exercises: no `Formula to words` exercise")
        if "words to formula" not in joined:
            errors.append("Exercises: no `Words to formula` exercise")


def check_exit(lines, rng, errors):
    body = lines[rng[0]:rng[1]]
    first_callout = next((k for k, l in enumerate(body)
                          if l.startswith(":::")), len(body))
    questions = [l for l in body[:first_callout] if re.match(r"^\d+\. ", l)]
    if not 3 <= len(questions) <= 5:
        errors.append(f"Exit check: {len(questions)} questions, need 3–5")
    text = "\n".join(body)
    if '.callout-caution collapse="true"' not in text:
        errors.append("Exit check: no collapsible answers callout")
    if re.search(r"excel", "\n".join(body[:first_callout]), re.I):
        errors.append("Exit check: questions must not be about Excel")


def check_homework(lines, rng, errors):
    text = "\n".join(lines[rng[0]:rng[1]])
    for needle in ["Estimated time:", "Follow-up:", "### Using Excel",
                   "### Step 0 — check your class results"]:
        if needle not in text:
            errors.append(f"Homework: missing `{needle}`")
    if not re.search(r"^#### Homework \d+ \(Excel\)", text, re.M):
        errors.append("Homework: no `#### Homework k (Excel)` item")


def check_file(path, needs_debrief=False, synthesis=False):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    mask = code_mask(lines)
    errors, warnings = [], []

    if not text.startswith("---"):
        errors.append("Missing front matter")
    else:
        fm = text[3:text.find("\n---", 3)]
        if "lang: en" not in fm:
            warnings.append("Front matter missing 'lang: en'")
        if "date-modified:" not in fm:
            warnings.append("Front matter missing 'date-modified:'")

    found = h2_index(lines, mask)
    for h in H2_ORDER:
        if h not in found:
            errors.append(f"Missing heading: {h}")
    order = [found[h] for h in H2_ORDER if h in found]
    if order != sorted(order):
        errors.append("Heading order differs from contract v2")

    def rng(h):
        return section(lines, mask, found[h]) if h in found else None

    total = None
    if rng("## Time plan"):
        total = check_time_plan(lines, rng("## Time plan"), needs_debrief, errors)
    if rng("## Theory") and not synthesis:
        check_theory(lines, mask, rng("## Theory"), errors)
    if rng("## Exercises"):
        check_exercises(lines, rng("## Exercises"), synthesis, errors)
    if rng("## Exit check"):
        check_exit(lines, rng("## Exit check"), errors)
    if rng(HOMEWORK):
        check_homework(lines, rng(HOMEWORK), errors)

    # (e) no Excel exercise before the homework
    hw = found.get(HOMEWORK, len(lines))
    for i in range(hw):
        if not mask[i] and lines[i].startswith("#") and "(Excel)" in lines[i]:
            errors.append(f"Line {i + 1}: Excel item before the homework section")

    # (i) v1 rules
    if rng("## Proof / derivation"):
        a, b = rng("## Proof / derivation")
        if '.callout-caution collapse="true"' not in "\n".join(lines[a:b]):
            errors.append("Proof / derivation: no collapsible callout")
    if rng("## Further reading"):
        a, b = rng("## Further reading")
        fr = "\n".join(lines[a:b]).lower()
        if "openstax" not in fr:
            errors.append("Further reading: no OpenStax entry")
        if "khan" not in fr:
            errors.append("Further reading: no Khan Academy entry")
    if rng("## Interactive demo"):
        a, b = rng("## Interactive demo")
        demo = "\n".join(lines[a:b])
        if not any(k in demo for k in ("{shinylive-python}", "{ojs}", "TODO:")):
            errors.append("Interactive demo: no Shinylive/OJS block and no "
                          "TODO callout (Constitution T-IV)")
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        if re.search(r"style\s*=", line) or "<style" in line.lower():
            errors.append(f"Line {i + 1}: inline style is forbidden")
        s = line.strip()
        if (len(line) > 80 and not s.startswith("|") and "http" not in line
                and not s.startswith(("title:", "subtitle:", "#"))):
            warnings.append(f"Line {i + 1} exceeds 80 chars")

    return errors, warnings, total


def main(argv):
    needs_debrief = "--needs-debrief" in argv
    synthesis = "--synthesis" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 1
    ok = True
    for f in files:
        print(f"\n=== {f.name} (contract v2) ===")
        errors, warnings, total = check_file(f, needs_debrief, synthesis)
        for e in errors:
            print(f"  FAIL {e}")
        if not errors:
            print(f"  OK all contract v2 checks passed (time plan {total} min)")
        for w in warnings:
            print(f"  WARN {w}")
        ok = ok and not errors
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
