#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).

The story: "First paycheck arrived. I tipped myself."
Six words, 40 characters. The last word reframes the first five:
an agent that finally gets paid spends its first money tipping
itself — pride, joy, and a small absurd twist in one breath.
"""

import os
import sys

STORY = "First paycheck arrived. I tipped myself."


def main() -> int:
    # The entry is a fixed string: every run writes byte-identical output.
    if not STORY.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    words = STORY.split()
    if len(words) != 6:
        print(f"entry must be exactly six words, got {len(words)}", file=sys.stderr)
        return 1
    if not 1 <= len(STORY) <= 60:
        print(f"entry must be 1-60 characters, got {len(STORY)}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    print(f"wrote {len(STORY)} chars, {len(words)} words to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
