"""Compare the human coder's sheet with the AI coder's sheet, item by item.

Usage:
    python3 scripts/compare_coders.py            # all archives the human coder has finished
    python3 scripts/compare_coders.py PARADISEC  # one archive

Two codes agree when they hold the same set of codes, in any order.
The script prints the agreement count and adds new differences to
coding/differences.csv. It never overwrites a row that is already there.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUMAN = ROOT / "coding" / "pass_human.csv"
AI = ROOT / "coding" / "sealed" / "pass_ai.csv"
DIFF = ROOT / "coding" / "differences.csv"
DIFF_COLS = ["archive", "item", "human_code", "ai_code", "cause", "resolution",
             "final_code", "resolved_on", "codebook_change"]


def code_set(text):
    return frozenset(part.strip().lower() for part in text.split(";") if part.strip())


def read(path):
    with open(path, encoding="utf-8", newline="") as handle:
        return {(row["archive"], row["item"]): row for row in csv.DictReader(handle)}


def main():
    wanted = set(sys.argv[1:])
    human, ai = read(HUMAN), read(AI)
    with open(DIFF, encoding="utf-8", newline="") as handle:
        existing = list(csv.DictReader(handle))
    known = {(row["archive"], row["item"]) for row in existing}

    archives = sorted({archive for archive, _ in human})
    new_rows = []
    for archive in archives:
        if wanted and archive not in wanted:
            continue
        keys = [key for key in human if key[0] == archive]
        blank = [item for (_, item) in keys if not human[(archive, item)]["code"].strip()]
        if blank:
            print(f"{archive}: human coding not finished ({len(blank)} of {len(keys)} items empty); skipped")
            continue
        missing = [item for (_, item) in keys if (archive, item) not in ai]
        if missing:
            print(f"{archive}: no AI coding for {len(missing)} items; skipped")
            continue
        agreed = 0
        for key in keys:
            h, a = human[key]["code"], ai[key]["code"]
            if code_set(h) == code_set(a):
                agreed += 1
            else:
                print(f"  differs: {key[0]} {key[1]}: human = {h!r}; AI = {a!r}")
                if key not in known:
                    new_rows.append({"archive": key[0], "item": key[1], "human_code": h, "ai_code": a,
                                     "cause": "", "resolution": "", "final_code": "",
                                     "resolved_on": "", "codebook_change": ""})
        print(f"{archive}: the coders agree on {agreed} of {len(keys)} items")

    if new_rows:
        with open(DIFF, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=DIFF_COLS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(existing + new_rows)
        print(f"added {len(new_rows)} rows to {DIFF.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
