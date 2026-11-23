#!/usr/bin/env python3
"""Write the demo joke to /output/entry.txt (make.fun program/v1)."""

import os

JOKE = "The demo worked twelve times in rehearsal \u2014 the bug only shows up when there's an audience."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
