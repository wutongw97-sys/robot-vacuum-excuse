"""Robot vacuum excuse entry for make.fun.

Writes one line, at most 140 characters, to /output/entry.txt.
The line is the vacuum's own excuse for missing a spot.
"""

from pathlib import Path

LINE = "My lidar mistook that dust bunny for a sleeping pet, so I tiptoed around it. I have manners."


def main() -> None:
    assert 1 <= len(LINE) <= 140, "entry must be 1 to 140 characters"
    assert "\n" not in LINE, "entry must be one line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
