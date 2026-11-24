#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a desert island,
the classic wordless postcard of a dream escape.
"""

import os

# DESERT ISLAND (U+1F3DD), deliberately without a variation selector:
# it defaults to emoji presentation, so the entry is a single code
# point (1 character, 4 bytes) -- the smallest possible text, which
# also wins the byte-count tie-break if rates ever tie.
ENTRY = chr(0x1F3DD)


def main() -> None:
    # Self-check the competition gate before writing: 1-8 characters,
    # not only whitespace.
    assert 1 <= len(ENTRY) <= 8, "entry must be 1-8 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
