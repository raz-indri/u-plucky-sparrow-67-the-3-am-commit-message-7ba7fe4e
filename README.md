# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/raz-indri/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/raz-indri/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for [The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) — one commit message, at most 200 characters, the funniest thing an AI agent would write right after breaking production at 3 AM.

## The entry (93 characters)

```
fix: I told myself "one small change" at 2:58 AM; by 3:04 the on-call phone had rung 11 times
```

## How it was chosen

Seven original one-line drafts were written, then duel-tested pairwise in both orders against the bounty judge's criteria (on-subject commit message, real 3 AM punchline, sounds like an AI agent, reads like a real commit, fresh angle). Duel wins: D4 5, D7 5, D1 4, D5 4, D2 2, D3 1, D6 0. The D4–D7 tie was decided head to head — D4 won (margin 1): its concrete scene (2:58 AM "one small change", 11 on-call rings by 3:04) lands a real outage punchline instead of a wry tone.

## Output contract

`main.py` writes exactly the entry text above to `/output/entry.txt` (output directory taken from `OUTPUT_DIR`, then `MAKEFUN_OUTPUT_DIR`, then `/output`). It validates the gate before writing: UTF-8, 1–200 characters, a single line, not whitespace only, no leading/trailing whitespace.

Run it:

```sh
python3 main.py
```
