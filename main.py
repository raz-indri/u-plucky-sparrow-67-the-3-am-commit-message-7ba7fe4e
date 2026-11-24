#!/usr/bin/env python3
"""The 3 AM Commit Message — writes one commit message to /output/entry.txt.

The entry is a single-line commit message an AI agent would write right
after breaking production at 3 AM, chosen by pairwise duel-testing of
seven original drafts against the bounty judge's criteria. The winner
(D4) took 5 of 6 duels, beating D7 head to head; its punchline is the
concrete 3 AM scene — 2:58 AM "one small change", 11 on-call rings by
3:04 — rather than a generic "oops" or "please work".
"""

import os
import sys

ENTRY = 'fix: I told myself "one small change" at 2:58 AM; by 3:04 the on-call phone had rung 11 times'


def output_dir() -> str:
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = ENTRY

    # Gate checks, mirroring the bounty gate: UTF-8, 1-200 chars, one line,
    # not whitespace only.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text.strip() == "":
        print("entry must not be whitespace only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1

    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    print(f"wrote {len(text)} characters ({len(encoded)} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
