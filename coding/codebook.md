# Codebook

**Status:** version 0.6, 16 November 2026. Both coders coded with version 0.5. Version 0.6 adds what the resolution of their differences settled (rules 5, 22 and 23). Section 8 records the decisions taken.

## 1. What is coded

The unit is one archive. The cases are AILLA, ELAR and PARADISEC. For each archive the coder answers a fixed set of items from the archive's public documents, listed in `sources/sources.csv` with `status` set to `found`.

The coding records what the documents state. It does not record how the archive applies them, and it does not look at individual collections.

Two coders code each archive independently with this codebook: the first author (SQ) and an AI agent. The first author then resolves every difference against the documents. Section 7 gives the procedure.

## 2. Fields and items

The template has four coded fields and one source field. Each coded field is split into items so that every answer has its own row.

Every item takes either an answer code or one of three silence codes: `deferred`, `not public` or `not stated`. Section 3.4 defines them. The table lists the answer codes.

| Field | Item | Question | Answer codes |
|---|---|---|---|
| Decision-maker | DM1 | Who can set a restriction? | `depositor`; `speaker or community`; `archive`; `steward or controller` |
| Decision-maker | DM2 | Who can change a restriction? | as DM1 |
| Decision-maker | DM3 | Who can lift a restriction? | as DM1 |
| Decision-maker | DM4 | Who decides on a request for access to a restricted item? | as DM1 |
| Grounds | GR1 | In what form does the archive accept reasons for a restriction? | `fixed list`; `free text` |
| Grounds | GR2 | Which reasons do the documents name? | `named` (the reasons go in `paraphrase`) |
| Levels | LV1 | How many access levels does the archive offer for files? | a number |
| Levels | LV2 | What are the levels called? | `named` (the names go in `paraphrase`) |
| Review | RV1 | Expiry: does a restriction end, or can it be given an end date? | `stated` |
| Review | RV2 | Review period: is a restriction reconsidered at a set time or interval? | `stated` |
| Review | RV3 | Appeal: can someone ask for a decision on access to be reconsidered? | `stated` |
| Review | RV4 | Takedown or withdrawal: can material be removed from access, or from the archive, after deposit? | `stated` |
| Review | RV5 | Succession: who decides when the decision-maker has died or cannot be reached? | `stated` |
| Source | all rows | Which document and section support the entry? | `source_id` and `section` |

## 3. Definitions

### 3.1 Decision-maker codes

| Code | Meaning |
|---|---|
| `depositor` | The person or body that deposits the material. A document may describe this party by what they did before deposit, for example as the person who collected or curated the material. Use this code when the document treats that party as the one who placed the material in the archive, and record the document's wording in `note` |
| `speaker or community` | A recorded person, their family, or the community the material comes from, acting in their own right and not through the depositor |
| `archive` | The archive, its staff, a committee of the archive, or its host institution |
| `steward or controller` | A role that the archive defines for a collection or a resource, such as a collection steward, a resource controller or a nominated contact. Use this code when a document says that the role decides or gives permission. If a document also says who holds the role, add that party's code and explain in `paraphrase` (rule 19) |

### 3.2 Grounds codes

| Code | Meaning |
|---|---|
| `fixed list` | The archive defines a closed set of reasons and the depositor chooses from it |
| `free text` | The depositor gives reasons in their own words, with or without examples from the archive |

### 3.3 Review items

| Item | Counts as `stated` when a document says that |
|---|---|
| RV1 Expiry | a restriction ends at a set time, can be given an end date, or cannot be permanent |
| RV2 Review period | a restriction is looked at again at a set date or interval, by any party |
| RV3 Appeal | a person who is refused access, or who disagrees with a decision on a restriction, has a route to have that decision reconsidered |
| RV4 Takedown or withdrawal | a person can ask for material to be removed from access (takedown), or a depositor or recorded person can take material or consent back (withdrawal) |
| RV5 Succession | another party decides when the decision-maker has died, cannot be reached or does not answer |

### 3.4 Silence codes

Use a silence code when no listed document answers the item. The three codes separate three kinds of silence.

| Code | Meaning | What to record |
|---|---|---|
| `deferred` | A document says that the matter is settled in the record of each item or collection, or in the conditions agreed at deposit | Quote the sentence that defers |
| `not public` | A document refers to another document, form or procedure that covers the matter, and that document is not online, sits behind a login, or is given only on request | Quote the reference, and name what is missing |
| `not stated` | No listed document addresses the matter, defers it, or refers to a document that covers it | Leave `short_quote` empty |

## 4. Decision rules

1. **Read in full.** Read every `found` document for the archive from start to finish before coding. `coding/evidence.csv` is a reading aid for the human coder, to consult after a first full reading. It is not complete and it is not a basis for a code. The AI coder does not receive it.
2. **Explicit statements only.** An answer code needs a sentence in a document that says so. If a document only implies an answer, use a silence code and describe the implication in `note`.
3. **Deciding is not being consulted.** Code the party that the document says decides. A party that is asked for a view, informed, or described as having an interest does not decide. Record this in `note`.
4. **Several decision-makers.** List every party the documents name, separated by a semicolon, in the order of the table in 3.1. Say in `paraphrase` how they share the decision: jointly, either one, one after the other, or one overriding the other. If the documents do not say, write `the documents do not say how they share the decision`. Two documents that give the same decision to different parties are a case of several decision-makers. They are a conflict under rule 13 only if one document excludes the other party.
5. **General statements.** A statement is tied to the moment of deposit when it describes a choice made at deposit, such as the choice of an access level on a deposit form. It counts for DM1 only. A general statement speaks of deciding on access as such and names no act, for example "the archive decides questions of access". It counts for DM1, DM2, DM3 and DM4, even if it stands in a deposit document. Write `general statement` in `note`. A statement that names an act, such as setting a level, marking an item as restricted or granting a request, counts only for the item that matches the act. A sentence that speaks of controlling access and then says what that means in terms of an act, for example answering requests, names the act.
6. **Ability counts.** A document that says a party can set, change, edit, lift or grant states who can do so. A document that only says a party administers or manages a collection does not.
7. **Both forms of grounds.** If an archive offers a closed list and also free text, code `fixed list; free text`. Examples that a form offers are not a closed list.
8. **Whose grounds.** GR1 applies when a document asks a party to give reasons, conditions or sensitivities for a restriction, or lets a party give them. If the party writes them freely, code `free text`. If no document asks for them, use a silence code. If the archive names reasons for which it restricts material itself, list them in GR2 and write `archive-initiated` in `note`. Rule 23 says how conditions of use count.
9. **Levels.** Count the named levels of access to files. A level whose conditions the depositor writes freely counts as one level; say so in `note`. Levels may attach to files, items, bundles or collections; say which in `paraphrase`. The visibility of metadata is not a level; record it in `note`. If documents use different names for the same level, count it once and give the variants in `paraphrase`.
10. **Options count.** If a document lets a depositor use a mechanism, such as an end date, the item is `stated`. Say in `paraphrase` whether the mechanism is required or optional. An example condition that a form prints as something the depositor may choose shows that the option exists. It counts. Write `from an example on the form` in `note`.
11. **RV4 names its kind.** Start the `paraphrase` for RV4 with `takedown`, `withdrawal` or `both`.
12. **A request is not an appeal.** A request for access to a restricted item is part of how the restriction works. Code who decides on it under DM4. It is not an appeal. A takedown request counts for RV4 only. RV3 needs a route to contest a decision that has been made, for example a refusal of access, a refusal of a takedown request, or a restriction that someone wants lifted.
13. **Conflict between documents.** If two current documents disagree, follow the more binding one: deposit agreement or form first, then access policy or terms of use, then help pages. Describe both in `paraphrase` and write `conflict` in `note`.
14. **Versions.** Code the current version of each document. Do not code a `superseded` document.
15. **Silence needs a full reading.** Use a silence code only after reading every `found` document for the archive. Write in `note` the date on which the reading was complete.
16. **No outside knowledge.** Do not code from memory, from the research literature, or from another archive's documents.
17. **An answer comes before silence.** If one document answers an item and another defers it, give the answer code and write `partly deferred` in `note`. Use a silence code only when no document answers the item.
18. **Order of silence codes.** If a document defers a matter to deposit conditions and the deposit document is not online, code `deferred` and write `deferred to a document that is not public` in `note`. Use `not public` when a document points to another document without saying that the matter is decided case by case.
19. **A role is not a party.** If a document says that a role such as a collection steward decides or gives permission, code `steward or controller`. Do not replace the role with the party you think holds it. Add a party code only if a document says in so many words who holds the role, for example with "is", "that is" or "usually". A passing gloss counts; say in `note` where it stands and whether the passage is about another subject. A request to name a contact does not by itself make the contact a decision-maker. If the document says what the contact is for, for example when the depositor cannot be reached, it counts for RV5.
20. **The archive's own power.** A power of the archive to restrict or remove material, on a complaint or on its own initiative, counts for DM1 and DM2. Where it is part of a takedown route it also counts for RV4.
21. **General deferral.** A general deferring sentence says that restrictions or conditions are set for each item, collection or deposit, and names no particular matter. It supports `deferred` only for the items that the terms of one restriction could answer: DM2, DM3, DM4, GR2, RV1, RV2 and RV5. Use it only when no document answers the item, and write `general deferral` in `note`. DM1, GR1, LV1, LV2, RV3 and RV4 concern rules of the archive. For them `deferred` needs a sentence that names the matter. Rule 17 applies to a general deferring sentence only for the seven items named here.
22. **A party that steps in.** If a document says that a party decides when the decision-maker has died, cannot be reached or does not answer, code RV5 as `stated`, and also add that party to each Decision-maker item that its power covers under rule 5. Say in `paraphrase` that the party decides only in that case, and write `fallback` in `note`. A contact that a document only asks the depositor to name is not covered by this rule (rule 19).
23. **Conditions of use.** Conditions that the archive sets on the use of its material by all users, such as a ban on commercial use, count for GR2 as reasons named by the archive. List them in `paraphrase` and write `archive-initiated` and `conditions of use` in `note`. This rule applies to GR2 only. Conditions of use are not restrictions on access for the Decision-maker, Levels and Review items.

## 5. Examples

These examples are invented. They do not come from any archive.

| Invented sentence | Item | Code | Why |
|---|---|---|---|
| "The depositor selects an access level for each file when submitting it." | DM1 | `depositor` | Names who sets, at deposit |
| "Depositors should discuss access with the speakers before choosing a level." | DM1 | `depositor` | Speakers are consulted. They do not decide (rule 3) |
| "The archive may restrict any item at its discretion." | DM1, DM2 | `archive` | The archive can set a restriction and can change an open item to a restricted one |
| "Choose one of the following reasons: A, B, C, or Other (please describe)." | GR1 | `fixed list; free text` | A closed list with a free-text option (rule 7) |
| "Describe any restrictions, for example sacred material." | GR1 | `free text` | An example is not a closed list (rule 7) |
| "Restricted items become open ten years after deposit unless renewed." | RV1 | `stated` | A set end |
| "We contact depositors every three years to confirm their access settings." | RV2 | `stated` | A set interval |
| "To see a restricted file, write to the depositor." | DM4 | `depositor` | Names who decides on a request |
| "To see a restricted file, write to the depositor." | RV3 | `not stated` | A request, not an appeal (rule 12) |
| "Requests for restricted items go to the collection steward." | DM4 | `steward or controller` | The document names a role, not a party (rule 19) |
| "Each collection has a steward, usually the depositor, who approves requests." | DM4 | `depositor; steward or controller` | The document says who holds the role (rule 19) |
| "Restrictions are set out in the record of each item." | DM1 | `deferred` | The matter is left to item records (3.4) |
| "Depositors state their reasons in the deposit agreement, available from the archive on request." | GR1 | `not public` | A document covers the matter and is not online (3.4) |
| "If the depositor cannot be reached, the archive director decides." | RV5 | `stated` | Names who decides next |
| "Conditions of access, for example: open after [year]." (printed on a deposit form) | RV1 | `stated` | An example on a form shows that the option exists (rule 10) |
| "Specific conditions accompany each collection." (and no document says when a restriction ends) | RV1 | `deferred` | A general deferring sentence covers RV1 (rule 21) |
| "Specific conditions accompany each collection." (and no document gives a route of appeal) | RV3 | `not stated` | A general deferring sentence does not cover RV3 (rule 21) |
| "Please name a contact in case we cannot reach you." | RV5 | `stated` | The document says what the contact is for (rule 19) |
| "Please name a contact in case we cannot reach you." | DM4 | no code from this sentence | It does not say that the contact decides (rule 19) |

## 6. Coding sheets

### 6.1 `pass_human.csv` and `pass_ai.csv`

Each coder fills one sheet. One row for each archive and item: 3 archives by 13 items, 39 rows.

| Column | Content |
|---|---|
| `archive` | Archive name |
| `field` | Decision-maker, Grounds, Levels or Review |
| `item` | Item code, for example `DM1` |
| `code` | An answer code from section 2 or a silence code from section 3.4. Several codes are separated by a semicolon and a space |
| `paraphrase` | One or two sentences in the coder's words |
| `short_quote` | The most direct quotation, word for word, 40 words at most, with no personal data. A quotation may run across line breaks in the source: only white space is ignored when it is checked. For `deferred` and `not public`, the sentence that defers or refers. Empty when the code is `not stated` |
| `source_id` | One or more `source_id` values from `sources/sources.csv`, separated by a semicolon. Empty when the code is `not stated` |
| `section` | Section, heading or paragraph in the source. Empty when the code is `not stated` |
| `coder` | `SQ` or `AI` |
| `coded_on` | Date of coding, as YYYY-MM-DD |
| `note` | Doubts, implications, conflicts, the notes that the rules ask for, and, for the AI coder, the reason for the code |

The AI coder's sheet is kept in `coding/sealed/pass_ai.csv` until the human coder has finished the same archive. The human coder does not open it before then.

### 6.2 `differences.csv`

One row for each archive and item where the two coders differ in `code`.

| Column | Content |
|---|---|
| `archive`, `item` | As above |
| `human_code`, `ai_code` | The two codes |
| `cause` | Why the coders differ, for example a passage one coder missed, or a rule read in two ways |
| `resolution` | What the first author decided and why, with the passage that settles it |
| `final_code` | The agreed code |
| `resolved_on` | Date |
| `codebook_change` | Any change made to this codebook as a result, or `none` |

### 6.3 `final.csv`

The agreed coding. It has the columns of 6.1 without `coder` and `coded_on`, and adds `agreement` (`agreed` or `resolved`), `source_url`, `access_date` and `snapshot_url`. `scripts/build_final.py` builds it from `pass_human.csv`, `differences.csv` and `resolved_text.csv`.

### 6.4 `resolved_text.csv`

The wording of the rows whose text changed at resolution: rows where the final code differs from the human coder's, and rows whose paraphrase was extended because a rule changed. It has the columns `archive`, `item`, `paraphrase`, `short_quote`, `source_id`, `section` and `note`.

## 7. Procedure

**Pilot.** A first run of the AI coder with version 0.4 of this codebook served as a pilot. Its reports named rules that could be read in two ways, and version 0.5 clarifies them. The pilot sheets are kept in `coding/sealed/pilot/`. They are not used as codings.

1. **AI coding.** An AI agent receives this codebook and the full text of every `found` document for one archive. It receives nothing else: no evidence sheet, no plan, no codes from anyone. `coding/ai_coder_prompt.md` holds its instructions. It fills the 13 rows for that archive.
2. **Check of quotations.** A script checks that each quotation in the AI coder's sheet appears word for word in the source it cites. The result is recorded next to the sheet. The codes are not changed.
3. **Human coding.** The first author reads every `found` document for the archive in full and fills `pass_human.csv` without opening the AI coder's sheet.
4. **Comparison.** A script compares the two sheets item by item and lists the differences in `differences.csv`. Two codes agree when they hold the same set of codes, in any order.
5. **Resolution.** The first author resolves each difference against the documents and records the reason. The AI coder's sheet is evidence to weigh. It does not decide.
6. **Final sheet.** The agreed coding goes to `final.csv`.
7. **Codebook changes.** If a difference shows that a rule is unclear, the first author changes the rule, records the change in section 9, and checks earlier codes that the rule affects.

**What is reported.** The number of items on which the two coders agreed, out of 39, and every difference with its resolution. No coefficient such as kappa is reported: 39 decisions are too few for one to mean much.

**Limits.** The AI coder is not an independent human coder. An AI assistant drafted this codebook and located the documents, so the two coders share more than two human coders would.

## 8. Decisions

| No. | Question | Draft position |
|---|---|---|
| 1 | Should a fourth item, DM4, record who decides on a request for access to a restricted item? | Settled on 14 November 2026: DM4 added |
| 2 | Should RV4 be split into takedown and withdrawal? | Kept as one item. Rule 11 makes the paraphrase name the kind |
| 3 | Does a statement of technical ability in a help page count as stating who decides (rule 6)? | Yes |
| 4 | Do privacy notices count as material? | Registered with `doc_type` set to `other`. Codable only where a statement concerns access to deposited material |
| 5 | Should GR1 also record whether a reason is required? | Not as a code. Record in `paraphrase` |
| 6 | Should silence be one code or three? | Settled on 15 November 2026: three codes (3.4) |
| 7 | How should roles such as a collection steward be coded? | Settled on 15 November 2026: `steward or controller` replaces `named controller` (3.1, rule 19) |
| 8 | One coder twice, or two coders? | Settled on 15 November 2026: two coders, the first author and an AI agent, each coding once. The literature treats agreement between independent coders as stronger than one coder's agreement with themselves over time (Hayes and Krippendorff 2007; O'Connor and Joffe 2020) |
| 9 | What to do with rules that the pilot showed to be unclear? | Settled on 15 November 2026: clarify them before either coder's sheet counts, and run the AI coder again with the clarified version. The first author chose the reach of rule 21 |
| 10 | Does a passage that speaks of controlling access, and explains it as answering requests, count for all Decision-maker items? | Settled at resolution on 16 November 2026: no, it names the act and counts for DM4 only (rule 5) |
| 11 | Is a party that decides only when the decision-maker cannot be reached a decision-maker? | Settled at resolution on 16 November 2026: it is coded in RV5 and in the Decision-maker items its power covers, marked `fallback` (rule 22) |
| 12 | Do conditions of use count as reasons? | Settled at resolution on 16 November 2026: yes, for GR2 only, as reasons named by the archive (rule 23). Reasons asked of a person who requests a takedown count for GR1 under rule 8 |

## 9. Change log

| Date | Version | Change |
|---|---|---|
| 2026-11-14 | 0.1 | First draft |
| 2026-11-14 | 0.2 | Added DM4 (who decides on a request for access to a restricted item). Extended rules 5 and 12 and the examples |
| 2026-11-15 | 0.3 | Replaced `not stated` as the only silence code with `deferred`, `not public` and `not stated` (3.4, rules 2, 15, 17, 18). Replaced `named controller` with `steward or controller` (3.1, rule 19). Removed `none named` from GR2. Cases reduced to AILLA, ELAR and PARADISEC |
| 2026-11-15 | 0.4 | Replaced two passes by one coder with one pass each by two coders, the first author and an AI agent (sections 1, 6 and 7, rule 1) |
| 2026-11-15 | 0.5 | After the pilot: clarified the definitions of `depositor` and `steward or controller` (3.1), rules 4, 5, 6, 8, 9, 10, 12 and 19, added rule 20 (the archive's own power) and rule 21 (general deferral), added five examples, and said what stays empty for `not stated` (6.1) |
| 2026-11-16 | 0.6 | At resolution: one sentence added to rule 5; added rule 22 (a party that steps in) and rule 23 (conditions of use); added `resolved_text.csv` (6.4). Checked the codes these rules affect: the paraphrases of GR2 for AILLA and PARADISEC were extended under rule 23 with no change of code; no other code changed |
