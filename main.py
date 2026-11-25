#!/usr/bin/env python3
"""Generate the entry for Fridge Roast: one line roasting a smart fridge."""
import os

ENTRY = "My smart fridge texted me at 3 a.m. to announce the milk expired 47 days ago, the ice maker has filed for burnout, and it cc'd the health inspector on ticket #4821."

MAX_CHARS = 200

def validate(entry: str) -> None:
    """Enforce the competition's entry rules: one line, at most 200 chars."""
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")

def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")

if __name__ == "__main__":
    main()
