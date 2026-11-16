"""Build the two tables in analysis/ from the final coding and the source register.

Usage:
    python3 scripts/build_tables.py

Outputs:
    analysis/matrix.csv        items by archives, the final code in each cell
    analysis/states.csv        items by archives, one of four states in each cell:
                               answered, deferred, not public, not stated
    analysis/availability.csv  document types by archives: public, or the status
                               recorded in the register when no document was found
    analysis/authority.csv     one row for each party named in a Decision-maker item,
                               marked `stated` or `fallback`
    analysis/provenance.csv    for each item and archive, the kind of document that
                               carries the quotation behind the final code

A party is marked `fallback` when the note of the row says so and the party is the
archive (codebook rule 22). The kinds of document come from analysis/source_genres.csv,
which assigns each source, or each part of a source, to one of three kinds. A row of
that file applies when its `section_contains` text occurs in the section cited; an
empty text applies to any section. The first row that applies is used.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVES = ["AILLA", "ELAR", "PARADISEC"]
PARTIES = ["depositor", "speaker or community", "archive", "steward or controller"]
FALLBACK_PARTY = "archive"
TYPES = ["access policy", "deposit agreement or form", "terms of use", "help or FAQ", "takedown or withdrawal"]
SILENCE = {"deferred", "not public", "not stated"}


def read(path):
    with open(ROOT / path, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write(path, header, rows):
    with open(ROOT / path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    final = read("coding/final.csv")
    cell = {(row["archive"], row["item"]): row for row in final}
    items = []
    for row in final:
        if (row["field"], row["item"]) not in items:
            items.append((row["field"], row["item"]))

    write("analysis/matrix.csv", ["field", "item"] + ARCHIVES,
          [[field, item] + [cell[(a, item)]["code"] for a in ARCHIVES] for field, item in items])
    write("analysis/states.csv", ["field", "item"] + ARCHIVES,
          [[field, item] + [cell[(a, item)]["code"] if cell[(a, item)]["code"] in SILENCE else "answered"
                            for a in ARCHIVES] for field, item in items])

    sources = read("sources/sources.csv")
    rows = []
    for doc_type in TYPES:
        line = [doc_type]
        for archive in ARCHIVES:
            mine = [s for s in sources if s["archive"] == archive
                    and doc_type in [part.strip() for part in s["doc_type"].split(";")]]
            found = sorted(s["source_id"] for s in mine if s["status"] == "found")
            if found:
                line.append("public (" + ", ".join(found) + ")")
            else:
                other = sorted({s["status"] for s in mine}) or ["not found"]
                line.append("; ".join(other))
        rows.append(line)
    write("analysis/availability.csv", ["document type"] + ARCHIVES, rows)

    authority = []
    for row in final:
        if row["field"] != "Decision-maker":
            continue
        for party in [part.strip() for part in row["code"].split(";")]:
            if party in PARTIES:
                fallback = party == FALLBACK_PARTY and "fallback" in row["note"]
                authority.append([row["archive"], row["item"], party, "fallback" if fallback else "stated"])
    write("analysis/authority.csv", ["archive", "item", "party", "basis"], authority)

    genres = read("analysis/source_genres.csv")
    provenance = []
    for row in final:
        state = row["code"] if row["code"] in SILENCE else "answered"
        ids = [part.strip() for part in row["source_id"].split(";") if part.strip()]
        first, genre = (ids[0] if ids else ""), ""
        if state == "answered":
            section = row["section"].split("; ")[0]
            for rule in genres:
                if rule["source_id"] == first and rule["section_contains"] in section:
                    genre = rule["genre"]
                    break
            if not genre:
                raise SystemExit(f"no kind of document for {first} ({row['archive']} {row['item']})")
        provenance.append([row["archive"], row["field"], row["item"], state, first, genre])
    write("analysis/provenance.csv", ["archive", "field", "item", "state", "first_source", "genre"], provenance)
    print("wrote matrix.csv, states.csv, availability.csv, authority.csv and provenance.csv in analysis/")


if __name__ == "__main__":
    main()
