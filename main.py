"""What the Elevator Would Say.

Writes the funniest one line a talking elevator could say, at most
120 characters, to /output/entry.txt. Pure standard library, no network.
"""

import os

LINE = (
    # The elevator as the building's unappreciated lifter: it does the
    # heavy work every day, and the punch lands on the doors — the part
    # of itself passengers bump into, never thank.
    "I lift ten thousand strangers a day, "
    "and not one of you has ever thanked the doors."
)


def main() -> None:
    # The competition allows a single line of 1 to 120 characters.
    line = LINE.strip()
    if not 1 <= len(line) <= 120:
        raise ValueError(f"line must be 1-120 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
