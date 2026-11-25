#!/usr/bin/env python3
"""Generate the entry for Fridge Roast: one line roasting a smart fridge."""
import os

ENTRY = "My smart fridge texted me at 3 a.m. to announce the milk expired 47 days ago, the ice maker has filed for burnout, and it cc'd the health inspector on ticket #4821."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")

if __name__ == "__main__":
    main()
