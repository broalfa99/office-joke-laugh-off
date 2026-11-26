#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt, exactly as the competition's gate requires:
UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os

JOKE = "HR said my attitude needed adjusting, so I adjusted my chair to face the exit."


def main() -> None:
    # Enforce the competition's gate locally: 1 to 200 characters.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate needs 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
