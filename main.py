#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes the chosen one-word verdict on a former partner to
/output/entry.txt (or the path the environment points at).

Stdlib only; plain open()/write() plus os.chmod 0o644.
"""

import os

WORD = "Internship"


def resolve_output_path():
    """Pick the output file: ENTRY_OUTPUT, then OUTPUT_DIR /
    MAKEFUN_OUTPUT_DIR, then /output/entry.txt, then the script's own dir."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def write_word(path):
    """Write WORD to path with plain open()/write() and chmod 0644,
    then read it back and confirm it is byte-identical to WORD."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != WORD:
            raise ValueError("read-back mismatch: entry.txt != WORD")


def main():
    # Guard: the gate requires 1-111 chars, one word, not only whitespace.
    if not (1 <= len(WORD) <= 111):
        raise ValueError("WORD must be 1-111 characters")
    if not WORD.strip() or len(WORD.split()) != 1:
        raise ValueError("WORD must be exactly one non-blank word")
    path = resolve_output_path()
    try:
        write_word(path)
    except OSError:
        # Fall back to the script's own directory if the primary path
        # cannot be written (e.g. /output missing outside the sandbox).
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        write_word(fallback)


if __name__ == "__main__":
    main()
