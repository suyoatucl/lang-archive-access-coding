"""Build coding/final.csv from the human coder's sheet and the record of resolutions.

Usage:
    python3 scripts/build_final.py

Inputs:
    coding/pass_human.csv     the first author's coding
    coding/differences.csv    each difference between the coders, with the final code
    coding/resolved_text.csv  the wording of rows whose text changed at resolution
    sources/sources.csv       the source register, for addresses, dates and snapshots

A row is marked `resolved` if the coders differed on its code, and `agreed` otherwise.
The script stops if a difference has no final code.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLS = ["archive", "field", "item", "code", "paraphrase", "short_quote", "source_id", "section",
        "agreement", "source_url", "access_date", "snapshot_url", "note"]


def read(path):
    with open(ROOT / path, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    human = read("coding/pass_human.csv")
    diffs = {(r["archive"], r["item"]): r for r in read("coding/differences.csv")}
    text = {(r["archive"], r["item"]): r for r in read("coding/resolved_text.csv")}
    sources = {r["source_id"]: r for r in read("sources/sources.csv")}

    out = []
    for row in human:
        key = (row["archive"], row["item"])
        final = dict(row)
        if key in diffs:
            if not diffs[key]["final_code"].strip():
                raise SystemExit(f"no final code for {key}")
            final["code"] = diffs[key]["final_code"]
            final["agreement"] = "resolved"
        else:
            final["agreement"] = "agreed"
        if key in text:
            for column in ("paraphrase", "short_quote", "source_id", "section", "note"):
                final[column] = text[key][column]
        ids = [part.strip() for part in final["source_id"].split(";") if part.strip()]
        unknown = [sid for sid in ids if sid not in sources]
        if unknown:
            raise SystemExit(f"unknown source for {key}: {unknown}")
        final["source_url"] = "; ".join(sources[sid]["url"] for sid in ids)
        final["access_date"] = "; ".join(sources[sid]["access_date"] for sid in ids)
        final["snapshot_url"] = "; ".join(sources[sid]["snapshot_url"] for sid in ids)
        out.append({column: final.get(column, "") for column in COLS})

    with open(ROOT / "coding" / "final.csv", "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(out)
    agreed = sum(1 for row in out if row["agreement"] == "agreed")
    print(f"wrote {len(out)} rows: {agreed} agreed, {len(out) - agreed} resolved")


if __name__ == "__main__":
    main()
