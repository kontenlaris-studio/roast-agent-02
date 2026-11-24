"""Roast Your Own Agent — one-line roast written to /output/entry.txt."""
import os

LINE = "It formats a completely wrong answer so beautifully I almost thanked it before I noticed the bug."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"wrote /output/entry.txt ({len(LINE)} characters)")
