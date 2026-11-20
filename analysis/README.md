# Analysis

Three scripts build everything in this folder from `coding/final.csv`, `sources/sources.csv` and `sources/citations.csv`.

```
python3 scripts/build_tables.py
python3 scripts/figures.py
python3 scripts/build_references.py
```

The second script needs matplotlib. The same data always give the same files.

## Tables

| File | Content |
|---|---|
| `matrix.csv` | The comparison table: one row for each item in the codebook, one column for each archive, the final code in each cell |
| `states.csv` | The same grid with one of four states in each cell: `answered`, `deferred`, `not public`, `not stated`. No item took `not public` |
| `availability.csv` | Which types of document each archive publishes: one row for each document type, one column for each archive. A cell says `public` with the sources, or gives the status recorded in the register |
| `authority.csv` | One row for each party named in a Decision-maker item, marked `stated`, or `fallback` where the party decides only if the decision-maker cannot be reached |
| `provenance.csv` | For each item and archive, the first source cited for the final code and the kind of document it is |
| `parties_by_act.csv` | For each Decision-maker item (set, change, lift, decide on requests) and each party, whether each archive names the party (`stated`, `fallback`, the silence code of the item, or empty), and how many archives name it. The poster's statement that only PARADISEC lets the depositor change or lift a restriction rests on this table |
| `references_archives.md` | APA 7 references for the 24 documents read, from `sources/citations.csv`. ELAR's addresses are left out until ELAR consents to links |
| `citation_keys.csv` | For each document, its in-text citation, such as `AILLA, n.d.-a`, and its reference |
| `documents_by_type.csv` | As `availability.csv`, with the in-text citations of the documents of each type, including `other`. It is Table 2 of the abstract |
| `source_genres.csv` | The assignment of each source, or part of a source, to one of three kinds of document. It is an input, written by hand |

## Figures

Each figure is saved as PNG (300 dpi), SVG and PDF.

| File | Shows | Built from |
|---|---|---|
| `figure1_states` | For each item and archive, whether the public documents answer it, defer it, or do not state it. A white dot marks the six cells on which the two coders differed | `states.csv`, `coding/final.csv` |
| `figure2_authority` | Who decides: the four kinds of party against the four acts, one panel for each archive, with space and a rule between the panels. A hollow mark is a party that decides only if the depositor cannot be reached | `authority.csv`, `states.csv` |
| `figure3_provenance` | The kind of document that carries the quotation behind each answer: a deposit document, terms or a policy for users, or a help or information page | `provenance.csv` |

**How to read figure 3.** It uses the first source cited for each final code. Many codes rest on several sources, so the figure shows where the most direct statement stands, not every place where the matter is mentioned.

**Colour.** Figure 1 uses two steps of one hue for the ordered states and a neutral grey for silence. Figure 2 uses one hue. Figure 3 uses three hues that were checked for colour-blind readers. Every tile that is not a plain answer carries a text label, so no figure depends on colour alone.
