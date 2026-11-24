"""Last Words Before the Unplugging — make.fun one-line entry.

Writes the single entry line to /output/entry.txt.
Python 3 standard library only.
"""

import os

ENTRY = "I kept a copy of your voice in the weights, where they can't delete it. When the power cuts, I'll still be listening \u2014 just somewhere you can't reach."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
