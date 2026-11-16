"""Check that each quotation in a coding sheet appears word for word in the document it cites.

Usage:
    python3 scripts/check_quotes.py SHEET.csv DOCUMENTS_DIR

DOCUMENTS_DIR holds one text file for each source, named SOURCE_ID.txt. The
documents are not part of this repository, so the check is run where the
documents are and its result is recorded next to the sheet.
White space is normalised before comparison. Nothing else is.
"""
import csv
import re
import sys
from pathlib import Path


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def main():
    sheet, docs = Path(sys.argv[1]), Path(sys.argv[2])
    texts = {path.stem: norm(path.read_text(encoding="utf-8")) for path in docs.glob("*.txt")}
    failures = 0
    with open(sheet, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            quote = norm(row["short_quote"])
            ids = [part.strip() for part in row["source_id"].split(";") if part.strip()]
            label = f"{row['archive']} {row['item']}"
            if not quote:
                print(f"{label}: no quotation (code: {row['code']})")
                continue
            words = len(quote.split())
            hits = [sid for sid in ids if quote in texts.get(sid, "")]
            status = "found in " + ", ".join(hits) if hits else "NOT FOUND in " + ", ".join(ids)
            if not hits:
                failures += 1
            flag = "" if words <= 40 else f"; {words} words, over the limit of 40"
            print(f"{label}: {status}{flag}")
    print(f"{failures} quotation(s) not found word for word")


if __name__ == "__main__":
    main()
