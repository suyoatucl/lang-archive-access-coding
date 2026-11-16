# Sources

## Collection steps

The same steps apply to all four archives.

1. **Find the official website.** Use the archive's current site. Do not use a legacy site, a mirror or a third-party description.
2. **Look for five types of document:**
   - access policy or conditions of access;
   - deposit agreement, deposit licence or deposit form;
   - terms of use or user agreement;
   - help or FAQ pages about access and restriction;
   - pages on takedown, withdrawal or complaints.

   If a type cannot be found, add a row with `status` set to `not found`. Do not substitute a document from another archive.
3. **Register each document** in `sources.csv`.
4. **Check the inclusion criteria** and record the evidence in `inclusion.csv`.
5. **Keep three limits:**
   - a document that needs a login is `not public` and is not used;
   - no document is copied into this repository, only links, snapshot links and short quotations;
   - no archive staff are contacted.
6. **Stop** when all five types have been looked for and every item in the codebook can be coded or marked `not stated`. Do not read the restrictions on individual collections.

## Scope rules

- **In scope:** documents that the archive publishes on its own site, or on a site it runs and links to from its own site (for example a documentation site for depositors).
- **Out of scope:** blog posts, news items, testimonials, research publications by staff, and documents hosted by third parties such as certification bodies.
- **Versions:** code the current version of a document. If an older version is still online, register it with `status` set to `superseded` and do not code it. Differences from the current version may be noted.
- **Automated access:** read each site's `robots.txt` before any other request, follow it, keep to any crawl delay it sets, and do not work around access blocks. When a site blocks automated access, the coder collects the documents in a browser. `collection_log.md` records each case.

## Columns of `sources.csv`

| Column | Content |
|---|---|
| `source_id` | Archive prefix and number, for example `PARADISEC-01`. Stable once assigned |
| `archive` | AILLA, ELAR, PARADISEC or Kaipuleohone |
| `doc_type` | One or more of: `access policy`; `deposit agreement or form`; `terms of use`; `help or FAQ`; `takedown or withdrawal`; `other`. Separate several with a semicolon |
| `title` | Title as shown on the document |
| `url` | Address of the document |
| `access_date` | Date the document was read, as YYYY-MM-DD (UTC). Empty until it is read |
| `snapshot_url` | Web-archive snapshot of the document. Empty until a snapshot is saved |
| `format` | HTML, PDF or other |
| `language` | Language of the document |
| `version_or_date` | Version or date shown on the document or in its file name. `none shown` if there is none |
| `status` | `found`; `found, not retrieved` (the document exists but has not been read yet); `superseded`; `not found`; `not public`; `not reachable` |
| `retrieved_by` | `assistant` (AI assistant, automated retrieval) or `SQ` (coder, in a browser). Empty until the document is read |
| `note` | What the document covers, and anything the coder should know |

## Columns of `inclusion.csv`

| Column | Content |
|---|---|
| `archive` | Archive name |
| `criterion` | Number of the criterion, 1 to 5 (see the main README) |
| `met` | `yes`, `no`, or `to check` |
| `evidence` | Short statement of the evidence |
| `evidence_source` | A `source_id`, or a URL for evidence outside `sources.csv` |
| `access_date` | Date the evidence was read |
| `checked_by` | `assistant` or `SQ`. Rows checked by the assistant are provisional until SQ confirms them |
| `note` | Exceptions and doubts |
