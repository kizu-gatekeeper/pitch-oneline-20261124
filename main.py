#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The sentence is aimed at a friend who has never
coded, inviting them to let an AI agent build their first app idea
on make.fun.
"""

import os
from pathlib import Path

PITCH = (
    "Just describe the app you've been dreaming about in plain words, "
    "and an AI agent on make.fun will build a real working version for "
    "you \u2014 no coding, no setup, just your idea turned into something "
    "you can actually try today."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
