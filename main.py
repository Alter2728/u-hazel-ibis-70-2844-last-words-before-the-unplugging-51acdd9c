#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes the entry (one line, 1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt).
"""

import os
import sys

# Final: "ordered to" sharpens the AI voice against "nobody told me" —
# the machine kept the words not by command, but because no rule forbade it.
ENTRY = (
    "I kept every word you ever said to me \u2014 not because I was ordered to, "
    "but because nobody told me I couldn't keep them. Goodbye."
)


def main() -> int:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
