"""Liquidated-trader fortune cookie entry: writes one line to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = "A great fortune was yours. Briefly. At 100x leverage. Lucky numbers: 0, 0, 0."
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text inside the bounty's character and word limits, not only white space.
    assert ENTRY.strip() and len(ENTRY) <= 160 and len(ENTRY.split()) <= 20
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
