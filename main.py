#!/usr/bin/env python3
"""Write one dad joke to /output/entry.txt.

Deterministic, stdlib only, no network. One line, at most 200 characters.
"""

import os

JOKE = (
    "My family staged an intervention about my dad jokes. "
    "I said, 'This is pun-ishment enough.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
