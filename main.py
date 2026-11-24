#!/usr/bin/env python3
"""Write one dad joke to /output/entry.txt.

Deterministic, stdlib only, no network. One line, 161 characters:
a father retells the classic two-tired bicycle joke at the table, the
kids throw the pun back at him ("told us that twice"), and his closer
lands a second pun on "stands up" -- the fallen bike, and the joke
itself. Dad tells it, the pun lands on first read, the frame is fresh,
the punchline arrives at the end.
"""

import os

JOKE = (
    "I told my kids the bicycle fell over because it was two-tired. "
    "They said, 'Dad, you've told us that twice.' "
    "I said, 'I know \u2014 I'm just making sure it stands up.'"
)


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-200")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
