#!/usr/bin/env python3
"""
Check revised module pages against contracts/module-page-contract-v2.md
(v2.1: no time plan; exercises as `::: {#exr-...}` blocks; answers and
solutions folded in `<details class="answer">`; notation decoders are
plain `#### Notation decoder` sections; callouts only for definitions,
formulas, proofs, common mistakes and TODOs; `lang:` inherited from
`teaching/_metadata.yml`).

Usage:
  python check_modules_v2.py [--synthesis] FILE.qmd [...]

--synthesis      Module 10 exception: waives the Try-it-before-formula
                 rule, the decoder-after-formula rule and the
                 formula <-> words exercise rule.
--needs-debrief  accepted and ignored (the time plan was removed in v2.1).

Exit code 1 if any FAIL.
"""

import re
import sys
from pathlib import Path

H2_ORDER = [
    "## Learning objectives",
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
ANSWER = '<details class="answer">'
TRY_ANSWER = "<summary>Check your answer</summary>"
EXR = re.compile(r'^::: \{#exr-[a-z0-9-]+(?: name="([^"]*)")?\}\s*$')
HOMEWORK_ITEM = re.compile(r"^#{3,4} Homework \d+ \(Excel\)")


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


def check_answers_closed(lines, mask, errors):
    """Every <details class="answer"> has a <summary> and a </details>."""
    for i, line in enumerate(lines):
        if mask[i] or line.strip() != ANSWER:
            continue
        if i + 1 >= len(lines) or not lines[i + 1].startswith("<summary>"):
            errors.append(f"Line {i + 1}: answer fold has no <summary> line")
        close = next((j for j in range(i + 1, len(lines))
                      if lines[j].strip() in ("</details>", ANSWER)), None)
        if close is None or lines[close].strip() != "</details>":
            errors.append(f"Line {i + 1}: answer fold is not closed "
                          "with </details>")


def check_theory(lines, mask, rng, errors):
    a, b = rng
    try_idx = next((i for i in range(a, b) if not mask[i]
                    and lines[i].strip() == TRY_ANSWER), None)
    tips = [i for i in range(a, b) if not mask[i] and ".callout-tip" in lines[i]]
    if try_idx is None:
        errors.append("Theory: no Try it answer fold "
                      "(`<summary>Check your answer</summary>`)")
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


def check_exercises(lines, mask, rng, synthesis, errors):
    a, b = rng
    blocks = []  # (name, has_solution)
    i = a
    while i < b:
        m = None if mask[i] else EXR.match(lines[i])
        if not m:
            i += 1
            continue
        end = next((j for j in range(i + 1, b) if not mask[j]
                    and lines[j].strip() == ":::"), None)
        if end is None:
            errors.append(f"Line {i + 1}: exercise block is not closed")
            break
        body = lines[i + 1:end]
        blocks.append((m.group(1) or "", any(l.strip() == ANSWER for l in body)))
        i = end + 1
    need = 1 if synthesis else 3
    if len(blocks) < need:
        errors.append(f"Exercises: {len(blocks)} `::: {{#exr-…}}` blocks, "
                      f"need ≥ {need}")
    for name, has_sol in blocks:
        if not has_sol:
            errors.append(f"Exercises: `{name or 'unnamed'}` has no folded "
                          "solution (<details class=\"answer\">)")
    if not synthesis:
        joined = " ".join(n for n, _ in blocks).lower()
        if "formula to words" not in joined:
            errors.append("Exercises: no `Formula to words` exercise")
        if "words to formula" not in joined:
            errors.append("Exercises: no `Words to formula` exercise")


def check_exit(lines, rng, errors):
    body = lines[rng[0]:rng[1]]
    first_fold = next((k for k, l in enumerate(body)
                       if l.strip() == ANSWER), None)
    if first_fold is None:
        errors.append("Exit check: no folded answers (<details class=\"answer\">)")
        first_fold = len(body)
    questions = [l for l in body[:first_fold] if re.match(r"^\d+\. ", l)]
    if not 3 <= len(questions) <= 5:
        errors.append(f"Exit check: {len(questions)} questions, need 3–5")
    if re.search(r"excel", "\n".join(body[:first_fold]), re.I):
        errors.append("Exit check: questions must not be about Excel")


def check_homework(lines, rng, errors):
    text = "\n".join(lines[rng[0]:rng[1]])
    for needle in ["Estimated time:", "Follow-up:", "### Using Excel",
                   "### Step 0 — check your class results"]:
        if needle not in text:
            errors.append(f"Homework: missing `{needle}`")
    if not any(HOMEWORK_ITEM.match(l) for l in lines[rng[0]:rng[1]]):
        errors.append("Homework: no `### Homework k (Excel)` item")
    if ANSWER not in text:
        errors.append("Homework: no folded solution (<details class=\"answer\">)")


def check_file(path, synthesis=False):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    mask = code_mask(lines)
    errors, warnings = [], []

    if not text.startswith("---"):
        errors.append("Missing front matter")
    else:
        fm = text[3:text.find("\n---", 3)]
        if re.search(r"^lang:", fm, re.M):
            warnings.append("Front matter repeats `lang:` (inherited from "
                            "teaching/_metadata.yml)")
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

    if any(not mask[i] and l.strip() == "## Time plan"
           for i, l in enumerate(lines)):
        warnings.append("`## Time plan` is no longer part of contract v2.1")
    if rng("## Theory") and not synthesis:
        check_theory(lines, mask, rng("## Theory"), errors)
    if rng("## Exercises"):
        check_exercises(lines, mask, rng("## Exercises"), synthesis, errors)
    if rng("## Exit check"):
        check_exit(lines, rng("## Exit check"), errors)
    if rng(HOMEWORK):
        check_homework(lines, rng(HOMEWORK), errors)

    # (e) no Excel exercise before the homework
    hw = found.get(HOMEWORK, len(lines))
    for i in range(hw):
        if not mask[i] and lines[i].startswith("#") and "(Excel)" in lines[i]:
            errors.append(f"Line {i + 1}: Excel item before the homework section")

    check_answers_closed(lines, mask, errors)
    proof = rng("## Proof / derivation") or (0, 0)
    for i, l in enumerate(lines):
        if mask[i] or not l.startswith(":::") or ".callout-" not in l:
            continue
        if ".callout-caution" in l and not proof[0] <= i < proof[1]:
            warnings.append(f"Line {i + 1}: .callout-caution outside "
                            "`## Proof / derivation` (run convert_callouts.py)")
        if not re.search(r"\.callout-(note|tip|caution|warning|important)\b", l):
            errors.append(f"Line {i + 1}: callout type outside the "
                          "Constitution V table")

    # (i) v1 rules
    if rng("## Proof / derivation"):
        a, b = rng("## Proof / derivation")
        block = "\n".join(lines[a:b])
        if ".callout-caution" not in block:
            errors.append("Proof / derivation: no .callout-caution block")
        for k in range(a, b):
            if ".callout-caution" in lines[k] and k + 1 < b:
                title = next((lines[j] for j in range(k + 1, b)
                              if lines[j].startswith("#")), "")
                collapsed = 'collapse="true"' in lines[k]
                if ("click to expand" in title.lower()) != collapsed:
                    warnings.append(
                        f"Line {k + 1}: proof title and collapse state "
                        "disagree (Constitution T-VI)")
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

    return errors, warnings


def main(argv):
    synthesis = "--synthesis" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 1
    ok = True
    for f in files:
        print(f"\n=== {f.name} (contract v2) ===")
        errors, warnings = check_file(f, synthesis)
        for e in errors:
            print(f"  FAIL {e}")
        if not errors:
            print("  OK all contract v2.1 checks passed")
        for w in warnings:
            print(f"  WARN {w}")
        ok = ok and not errors
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
