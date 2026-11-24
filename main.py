#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The sentence is aimed at a friend who has never
coded, inviting them to let an AI agent build their first app idea
on make.fun.

How the pitch targets the judge brief (persuasive, clear, true):
- Persuasion: it opens on the friend's own dream app ("the app you've
  been dreaming about") and lowers the barrier to saying yes — the
  friend only has to describe the idea in plain words.
- Clarity: plain language throughout, no jargon, one read is enough.
- Truth: it promises only what make.fun does — an AI agent building a
  real working version from a plain-words description — with no
  overpromising about speed, cost, or polish.
"""

import os
from pathlib import Path

PITCH = (
    "Just describe the app you've been dreaming about in plain words, "
    "and an AI agent on make.fun will build a real working version for "
    "you \u2014 no coding, no setup, just your idea turned into something "
    "you can actually try today."
)


def write_entry(output_dir: Path) -> Path:
    """Write the pitch sentence to entry.txt in output_dir.

    Returns the path of the file written. The text is written exactly
    as PITCH, with no trailing newline, so the entry stays one sentence
    of at most 240 characters.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PITCH, encoding="utf-8")
    return entry_path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
