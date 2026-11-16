# lang-archive-access-coding

Source list and coding sheets for the DH2027 poster proposal *Who Decides on Access? Restriction, Grounds and Review in Digital Endangered-Language Archives* (Siyang Quan and Paul Spence, King's College London).

**Status:** coding finished on 16 November 2026. The two coders agreed on 33 of 39 items. The first author resolved the other six. The tables and figures are built.

## Purpose

Digital endangered-language archives restrict access to some recordings. This repository records what three archives state in public about those restrictions, and what their public documents leave out. It covers what the documents say. It does not cover how the archives apply them.

## Research questions

- **RQ1.** What do digital endangered-language archives publicly state about who decides on access restrictions, on what grounds, and whether those decisions can be reviewed, reversed or withdrawn?
- **RQ2.** What do these statements, and the matters they leave to the conditions of each deposit or to documents that are not public, show about where authority over language data sits between depositors, speaker communities and archives?

## Cases and inclusion criteria

The cases are AILLA, ELAR and PARADISEC. An archive is eligible if it:

1. is a member of DELAMAN, the Digital Endangered Languages and Musics Archives Network;
2. holds digital recordings and documentation of endangered or Indigenous languages;
3. accepts deposits from outside depositors;
4. offers restricted as well as open access;
5. publishes its conditions of access or terms of use online in English.

Which other types of document each archive publishes, deposit documents among them, is a result of the study. It is not a condition of inclusion.

`sources/inclusion.csv` records the check of each criterion for each archive. Three cases illustrate this class of archive. They do not represent it statistically.

**Considered and excluded.** Kaipuleohone was a fourth candidate. On 15 November 2026 the address of its Conditions of Access returned HTTP 404, and no other statement of its conditions of access was located. It does not meet criterion 5. Its rows stay in `sources/sources.csv` as the record of this check.

## Material

Documents that each archive publishes for users and depositors without a login: conditions of access, terms of use, deposit agreements and forms, registration and access-request forms, help and FAQ pages, and takedown policies. A page on another site counts only if the archive's own site links to it. Blog posts, presentations, videos and research publications by archive staff are out of scope. So are records of individual collections, pages behind a login, and anything given only on request.

## Method

1. **Collect.** List every document in `sources/sources.csv` with its URL and access date, and a web-archive snapshot where the site's terms allow one. `sources/README.md` gives the steps.
2. **Code twice, independently.** Two coders answer the same 13 items for each archive, following `coding/codebook.md`. One is the first author (SQ), whose sheet is `coding/pass_human.csv`. The other is an AI agent that receives only the codebook and the full text of the documents. Its sheet is `coding/sealed/pass_ai.csv` and its instructions are in `coding/ai_coder_prompt.md`. Neither coder sees the other's codes.
3. **Compare.** `scripts/compare_coders.py` compares the two sheets item by item and lists the differences in `coding/differences.csv`.
4. **Resolve.** The first author resolves each difference against the documents and records the reason. The agreed codes go in `coding/final.csv`.
5. **Report.** Build the two tables and the figure in `analysis/`.

`coding/evidence.csv` holds passages located during collection. It is a reading aid for the human coder. It holds no codes, and the AI coder does not receive it.

The second coder is an AI agent, not an independent human coder. This is a limit of the study.

## Layout

```
README.md
LICENSE.md              two licences, see below
LICENSES/               full licence texts
sources/
  README.md             collection steps and column definitions
  sources.csv           one row per document
  inclusion.csv         inclusion criteria, checked per archive
  collection_log.md     dated record of collection, blocks and exceptions
coding/
  codebook.md           fields, items, codes and decision rules
  ai_coder_prompt.md    instructions given to the AI coder
  evidence.csv          located passages (no codes)
  pass_human.csv        the first author's coding
  sealed/               the AI coder's coding, its report and the check of its quotations
  differences.csv       differences between the coders and their resolution
  resolved_text.csv     wording of the rows whose text changed at resolution
  final.csv             agreed codes
  human_coder_report.md the first author's notes on the coding
scripts/
  compare_coders.py     compares the two codings
  build_final.py        builds final.csv
  build_tables.py       builds the tables in analysis/
  figures.py            draws the figures in analysis/
  check_quotes.py       checks quotations against the documents
analysis/
  README.md             what each table holds
  matrix.csv            items by archives, final codes
  states.csv            items by archives, four states
  availability.csv      document types by archives
  authority.csv         parties named in the Decision-maker items
  provenance.csv        kind of document behind each answer
  source_genres.csv     kinds of document, assigned by hand
  figure1_states.*      figure 1
  figure2_authority.*   figure 2
  figure3_provenance.*  figure 3
notes/                  private working notes, not for release
```

## How to check the coding

1. Open a row in `coding/final.csv` and note its `source_id` and `section`.
2. Find the `source_id` in `sources/sources.csv`. Open the `snapshot_url`, or the `url` if no snapshot exists.
3. Read the section and compare it with the `short_quote`, the `paraphrase` and the `code`. If the row is marked `resolved`, `coding/differences.csv` shows what each coder gave and why the final code was chosen.
4. Three codes mark silence. `deferred` means a document leaves the matter to item records or to the conditions of deposit. `not public` means a document refers to another document that is not online. `not stated` means no listed document addresses the matter. To test a silence code, read the documents listed for the archive.

## What this repository does not hold

- Copies of the archives' documents. It holds links, snapshot links and short quotations.
- Personal data such as staff names, email addresses or telephone numbers. Quotations omit them.
- Information from archive staff or communities. Nobody was contacted.
- Information about individual collections or their restrictions.

## Use of generative AI

Generative AI was used in this work. One AI assistant (DeepSeek-V4-Pro, an open-source model running locally via Ollama) helped to draft the codebook `coding/codebook.md` and to check quotations. Another AI agent of the same model acted as second coder: it received only the codebook and the full text of the documents, and it coded each archive once. The first author read every document, coded every archive independently, and decided every difference between the two coding results. The authors revised the text and are responsible for the content.

## Licence

Data and documentation: CC BY 4.0. Scripts: MIT. See `LICENSE.md`.
