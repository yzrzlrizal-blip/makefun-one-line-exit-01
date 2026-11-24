#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty u-kreutzx-the-one-line-exit-1dc652d1.

Writes one funny resignation letter, exactly one line long, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Standard library only,
fully deterministic: the same bytes on every run.
"""

import os
import sys

# The resignation letter: a formal opening, six years of 4:59 p.m.
# "quick questions", and a punchline that treats the calendar like a
# relationship that has run its course.
RESIGNATION = (
    "I hereby resign: after six years of 'quick questions' at 4:59 p.m., "
    "my calendar and I have agreed to see other people."
)

CHAR_LIMIT = 140


def write_entry() -> int:
    text = RESIGNATION
    stripped = text.strip()
    if not stripped:
        print("error: resignation line is empty", file=sys.stderr)
        return 1
    if len(text) != len(stripped) or "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(text) > CHAR_LIMIT:
        print(
            f"error: entry is {len(text)} chars, over the {CHAR_LIMIT} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    payload = text.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != payload:
        print("error: entry.txt does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(payload)} bytes ({len(text)} chars) to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry())
