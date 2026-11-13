#!/usr/bin/env python3
"""Module to generate the AI joke submission entry for the make.fun bounty."""

import os
from pathlib import Path


def main():
    # The joke highlights the ultimate minimalism in debugging: removing the problematic feature entirely.
    joke = "My AI coding agent fixed the bug by deleting the feature \u2014 zero lines of code, zero bugs, zero users."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    entry_file = out_path / "entry.txt"
    entry_file.write_text(joke, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
