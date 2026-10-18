#!/usr/bin/env python3
"""
Convert collapsible `.callout-caution` blocks of a contract-v2 module page
to the lighter markup of contract v2.1:

- `#### Try it — check your answer`  -> <details class="answer">
- `#### Exercise k (by hand) — T (click for solution)`
                                     -> ::: {#exr-<slug> name="T"} with the
                                        solution folded in <details>
- `#### Exit check — answers`        -> <details class="answer">
- `#### Step 0 — expected results`   -> <details class="answer">
- `#### Homework k (Excel) — T (click for solution)`
                                     -> `### Homework k (Excel) — T` heading,
                                        statement visible, solution folded

Statements and solutions are moved verbatim; only the leading
`**Solution.**` label is dropped (it becomes the fold's summary).
Derivation callouts are left unchanged.

Usage: python convert_callouts.py FILE.qmd [...]   (edits in place)
"""

import re
import sys
import unicodedata
from pathlib import Path

OPEN = '::: {.callout-caution collapse="true"}'
SOL = re.compile(r"^\*\*Solution\.\*\*\s*")


def slug(title):
    t = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    t = re.sub(r"[`$\\{}]", "", t.lower())
    words = re.findall(r"[a-z0-9]+", t)
    stop = {"a", "an", "the", "of", "on", "for", "to", "and", "with", "in"}
    return "-".join(w for w in words if w not in stop)[:40].strip("-")


def details(summary, body):
    body = list(body)
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return [f'<details class="answer">', f"<summary>{summary}</summary>", "",
            *body, "", "</details>"]


def split_solution(body):
    """Return (statement, solution) split at the `**Solution.**` line."""
    for k, line in enumerate(body):
        if SOL.match(line):
            first = SOL.sub("", line)
            sol = ([first] if first else []) + body[k + 1:]
            return body[:k], sol
    return body, []


def convert_block(title, body, used):
    if title.startswith("#### Try it"):
        return details("Check your answer", body)
    if title.startswith("#### Exit check"):
        return details("Answers", body)
    if title.startswith("#### Step 0"):
        return details("Expected results", body)
    m = re.match(r"^#### Exercise \d+ \(by hand\) — (.*?)"
                 r"(?: \(click for solution\))?$", title)
    if m:
        name = m.group(1)
        s = slug(name)
        while s in used:
            s += "-2"
        used.add(s)
        stmt, sol = split_solution(body)
        while stmt and not stmt[-1].strip():
            stmt.pop()
        out = [f'::: {{#exr-{s} name="{name.replace(chr(34), chr(39))}"}}', *stmt]
        if sol:
            out += ["", *details("Solution", sol)]
        return out + [":::"]
    m = re.match(r"^#### (Homework \d+ \(Excel\) — .*?)"
                 r"(?: \(click for solution\))?$", title)
    if m:
        stmt, sol = split_solution(body)
        while stmt and not stmt[-1].strip():
            stmt.pop()
        out = [f"### {m.group(1)}", "", *stmt]
        if sol:
            out += ["", *details("Solution", sol)]
        return out
    return None


def convert(text):
    lines = text.split("\n")
    out, i, used, n = [], 0, set(), 0
    while i < len(lines):
        if lines[i].strip() == OPEN and i + 1 < len(lines):
            end = next(j for j in range(i + 2, len(lines))
                       if lines[j].strip() == ":::")
            new = convert_block(lines[i + 1], lines[i + 2:end], used)
            if new is not None:
                out += new
                i, n = end + 1, n + 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), n


def main(argv):
    for a in argv:
        p = Path(a)
        new, n = convert(p.read_text(encoding="utf-8"))
        p.write_text(new, encoding="utf-8")
        print(f"{p}: {n} blocks converted")


if __name__ == "__main__":
    main(sys.argv[1:])
