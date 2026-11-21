"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, 1-280 chars, one line).
Deterministic: no network, no randomness, no input.
"""

import os

JOKE = (
    "The demo crashed, so I asked my agent for a one-line fix. "
    "It rewrote the module, added a framework, "
    "and committed it as 'trust me'."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
