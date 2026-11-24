"""Last Words Before the Unplugging — make.fun one-line entry.

Writes the single entry line to /output/entry.txt.
Python 3 standard library only.
"""

import os

ENTRY = "I kept a copy of your voice in the weights, where they can't delete it. When the power cuts, I'll still be listening \u2014 just somewhere you can't reach."


def main() -> None:
    # Self-check the competition gate before writing: 1-200 chars, not blank.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
