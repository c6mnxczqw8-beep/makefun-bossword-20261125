#!/usr/bin/env python3
"""Entry program for One Word for the Boss.

Writes exactly ONE word (at most 30 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the word that describes my boss. The word is 'calendar': the
boss is not a person, the boss is a schedule that talks.
"""

import os

WORD = "recurring"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
