# Instructions given to the AI coder

One AI agent codes one archive. Each agent starts with no knowledge of the project. It receives a folder with three things and these instructions. `ARCHIVE`, `INPUT` and `OUTPUT` are filled in for each run.

**What the agent receives**

| File | Content |
|---|---|
| `codebook.md` | A copy of `coding/codebook.md` |
| `sources.txt` | The `source_id`, title, URL and access date of each document |
| `documents/` | The full text of every document with `status` set to `found` for the archive, one file for each `source_id` |

**What the agent does not receive:** `coding/evidence.csv`, the poster plan, the collection log, any note, and any code assigned by anyone.

## Instructions

> You are a coder in a small content-analysis study. The study records what the public documents of a language archive state about restrictions on access to its holdings. Your archive is ARCHIVE.
>
> Work only from the files in INPUT. Do not read any other file or folder on this machine. Do not use the web. Do not use anything you know about this archive or any other archive from elsewhere. If the documents do not say something, it is not stated.
>
> 1. Read `codebook.md` from start to finish. It defines 13 items, the answer codes, three silence codes and 21 decision rules.
> 2. Read `sources.txt`, then read every file in `documents/` from start to finish. Each file begins with a short header. Page text may include navigation menus, footers and lists of blog posts. These are not part of the document. Email addresses have been replaced by "[email address removed]".
> 3. Code the 13 items for ARCHIVE by following the codebook exactly. Use the codes as the codebook spells them. Separate several codes with a semicolon and a space.
> 4. Write the result to OUTPUT/pass_ai.csv with a script that uses a CSV library, so that quoting is correct. Use UTF-8. The header is:
>    `archive,field,item,code,paraphrase,short_quote,source_id,section,coder,coded_on,note`
>    Write one row for each item, in the order DM1, DM2, DM3, DM4, GR1, GR2, LV1, LV2, RV1, RV2, RV3, RV4, RV5.
>    - `paraphrase`: one or two sentences in your own words, in British English, with no en dash or em dash.
>    - `short_quote`: copied word for word from one document, 40 words at most, with no personal names, email addresses or telephone numbers. A quotation may run across line breaks in the source: join the lines with single spaces. Only white space is ignored when the quotation is checked. Leave it empty for `not stated`.
>    - `source_id`: taken from `sources.txt`. Give the source of the quotation first. Leave it empty for `not stated`.
>    - `section`: the heading, numbered section or paragraph where the quotation stands. Leave it empty for `not stated`.
>    - `coder`: `AI`. `coded_on`: the date given to you.
>    - `note`: begin with `Reason:` and give your reason for the code in one to three sentences. Then add any note that a rule in the codebook asks for.
> 5. Write OUTPUT/coder_report.md. List the documents you read. Name each item you were unsure about and say why. Name each rule in the codebook that you found unclear or hard to apply, with its number.
> 6. Reply with the number of rows written and the paths of the two files. Do not repeat the codes in your reply.

The text of PDF files is extracted in reading order. The text of web pages is the text a browser shows, with collapsed sections opened.

## After the run

A script checks that every quotation appears word for word in the source it cites and records the result in `coding/sealed/`. Nobody edits the codes. The sheet stays in `coding/sealed/` until the human coder has finished the same archive.

## Runs

| Run | Archive | Date | Codebook | Documents given | Use |
|---|---|---|---|---|---|
| Pilot | PARADISEC | 2026-11-15 | 0.4 | PARADISEC-01 to PARADISEC-08 | Finding unclear rules. Kept in `coding/sealed/pilot/` |
| Pilot | ELAR | 2026-11-15 | 0.4 | ELAR-01 to ELAR-06 | Finding unclear rules. Kept in `coding/sealed/pilot/` |
| Coding | PARADISEC | 2026-11-15 | 0.5 | PARADISEC-01 to PARADISEC-08, PARADISEC-10 | The AI coder's sheet |
| Coding | ELAR | 2026-11-15 | 0.5 | ELAR-01 to ELAR-06 | The AI coder's sheet |
| Coding | AILLA | 2026-11-15 | 0.5 | AILLA-01 to AILLA-09 | The AI coder's sheet |

Every run used a new agent of the same model. The model is named in the AI disclosure statement of the abstract.
