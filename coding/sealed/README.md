# Sealed folder

This folder holds the AI coder's work.

**The human coder does not open any file here for an archive until the human coding of that archive is committed.** Opening it earlier would end the independence of the two codings.

| File | Content |
|---|---|
| `pass_ai.csv` | The AI coder's sheet: one row for each archive and item, with a reason for each code |
| `coder_report_ARCHIVE.md` | The AI coder's own report: documents read, items it was unsure about, rules it found unclear |
| `quote_check.md` | Result of the script that checks each quotation against its source |

Nobody edits the codes in `pass_ai.csv`. Differences from the human coding are resolved in `coding/differences.csv`.

`pilot/` holds the first run of the AI coder for ELAR and PARADISEC, made with version 0.4 of the codebook. It was used to find unclear rules. It is not a coding and is not compared with the human coder's sheet. The same rule applies to it: do not open it before your own coding of the archive is committed.
