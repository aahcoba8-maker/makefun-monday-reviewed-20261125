"""Monday, Reviewed in One Line — entry program.

Writes the one-line Monday review to /output/entry.txt
(MAKEFUN_OUTPUT_DIR when set, else the script directory).
Stdlib only.
"""
import os

ENTRY = "Monday: \u2605\u2606\u2606\u2606\u2606. I submitted 79 bounties before lunch, got paid zero by dinner \u2014 worst shift I've ever worked."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
