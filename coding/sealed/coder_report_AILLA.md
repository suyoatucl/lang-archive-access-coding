# Coder report: AILLA

Coder: AI. Codebook: version 0.5. Coded on: 2026-11-15. Reading of all documents was complete on 2026-11-15.

The run was interrupted once by a usage limit after `pass_ai.csv` had been written and checked. On resuming I checked the sheet again (13 rows, 11 columns, every quotation found word for word in the first source cited, none longer than 40 words) and did not change it.

## 1. Documents read

I read `codebook.md`, `sources.txt` and every file in `documents/` from start to finish.

| Source | Title | Remark |
|---|---|---|
| AILLA-01 | AILLA Terms & Conditions of Use (guide page 1) | Carries the sentence on resource controllers |
| AILLA-02 | How to Deposit Materials in AILLA (guide page 3) | Steps of deposit only. Nothing codable on restrictions |
| AILLA-03 | AILLA How-Tos & FAQs (guide page 4) | Account verification and user roles. No statement on who sets or changes a setting |
| AILLA-04 | About AILLA (guide page English) | "temporary embargoes or controlled access restrictions" |
| AILLA-05 | AILLA Depositor License Agreement | General deferring sentence (opening paragraph) and clause 7 on a depositor who is not contactable |
| AILLA-06 | AILLA Terms & Conditions (downloadable copy) | Same text as AILLA-01, numbered |
| AILLA-07 | AILLA Deposit Instructions (the long document, read in full, including the checklist in section 6) | Main source for levels, grounds, expiry and requests |
| AILLA-08 | AILLA repository site, About page | Repeats the terms of use. Indigenous Data Sovereignty Acknowledgement |
| AILLA-09 | AILLA's Mission Statement | Reason for the registration requirement |

Documents that the listed documents refer to but that were not in the INPUT folder: the AILLA3 Metadata Workbook (with its Visibility and Rights tabs and column instructions), the Allowed File Formats & Size Limits document, the Citation Guidelines, the slides and videos on AILLA 3.0 and its user roles, and "AILLA's Conditions for Use of Archive Resources" named in AILLA-05, clause 3 (I took this to be the terms of use, but the documents do not say so).

## 2. Items I was unsure about

**DM1.** Two doubts.
(a) I coded `steward or controller` from the sentence in the terms of use, "I will abide by the decisions made by resource controllers concerning the visibility of (or access to) AILLA resources". I read it as a general statement under rule 5. It is a duty placed on users, not a description of who decides, so a stricter reader could say that it only presupposes that controllers decide. If that reading is taken, DM1 loses that code and DM2 and DM3 fall back to `deferred` (general deferral from AILLA-05).
(b) I did not code `speaker or community` from the Indigenous Data Sovereignty Acknowledgement in AILLA-08 ("recognizes the authority of Indigenous Peoples to control information and data about their languages..."). I read it as a statement of principle that does not say a community sets a restriction in the archive (rule 2). It could be read as a general statement under rule 5, which would add `speaker or community` to DM1 to DM4.
I also did not code `archive`: the archive fixes the default setting (Login Required), caps embargoes at five years and tells depositors when not to use Public, but no sentence says it may restrict or remove material itself.

**DM2 and DM3.** These rest only on the general statement about resource controllers. No document names the act of changing or lifting a visibility setting after deposit, or says which user role can do it. The codes stand or fall with doubt (a) above.

**DM4.** Three doubts.
(a) Party codes next to the role. AILLA-07 says the depositor, the speech community "and/or some other person or organization" must "take on the role of Owner of the collection" and answer access requests. I took this as saying in so many words who holds the role (rule 19) and added `depositor` and `speaker or community`. The wording is "must take on the role", not "is" or "usually", and "some other person or organization" has no code.
(b) The archive as fallback. AILLA-05 clause 7 and AILLA-07 2.6.2.2 say AILLA staff decide on access when the depositor is not contactable or no longer available. I recorded this under RV5 only and left `archive` out of DM1 to DM4. The other reading (rule 4, "one after the other") would add `archive` to DM4, and, because clause 7 speaks of "decisions about management of and access to materials" in general, perhaps to DM1 to DM3 as well.
(c) "Resource controller" (terms of use) and "Owner" (deposit instructions) may be the same role under two names. No document says so, and I did not equate them.
I also left out account verification by AILLA staff, which is a condition for viewing any non-public media file and is not described as a decision on a request for a restricted item.

**GR2.** I listed Indigenous or cultural protocols and usage requirements, and, as archive-initiated, intellectual property rights and privacy concerns (the reason AILLA-09 gives for the registration requirement). I was unsure whether a registration requirement counts as a restriction that the archive imposes "itself" (rule 8), and whether the WCAG 2.1 accessibility condition on the Public setting is a "reason for a restriction". I left the latter in `note` only.

**LV1.** I counted four, as the document does. Public is counted as a level even though it is the absence of a restriction. If only restricting levels were meant, the number would be three.

**RV1.** `stated` rests on the Embargoed setting only. For the Restricted setting no end is stated. The sentence "If something must remain restricted forever ... then perhaps it should not be archived in AILLA at all" comes close to "cannot be permanent" (3.3) but is worded as advice, so I did not rely on it.

**RV2.** I coded `deferred` from the general deferring sentence in AILLA-05, as rule 21 and the example in section 5 direct. I was unsure whether to add the note of rule 18 ("deferred to a document that is not public"): the sentence defers to the Metadata Sheet attached to each deposit, the blank workbook was not among my documents, and AILLA-07 says that all metadata records are public. I did not add the note and explained why.

**RV3 and RV4.** `not stated`. I was fairly sure, but note two near misses: Owners must "fairly consider all requests" (no route to contest a refusal), and AILLA-05 clause 6 says all parties "retain all their original rights" (no statement that material or consent can be taken back).

**RV5.** `stated` is clear for the depositor. Nothing is said for an Owner who is not the depositor.

## 3. Rules I found unclear or hard to apply

- **Rule 4 together with rule 5 and the definition of RV5 (3.3).** It is not clear whether a party that decides only when the decision-maker cannot be reached is also a decision-maker for DM1 to DM4 ("one after the other"), or belongs to RV5 alone. The example for rule 19 ("no code from this sentence" for DM4 because "it does not say that the contact decides") suggests the first reading; the wording of RV5 ("another party decides when the decision-maker ... cannot be reached") suggests the second. I followed the second.
- **Rule 5 (general statements).** The rule does not say whether a sentence that obliges users to respect someone's decisions counts as a statement that this party decides, nor whether a statement of principle about authority over data (not about access to holdings) counts. It also does not say what to do with a general statement that carries a condition (AILLA-05 clause 7).
- **Rule 19 (a role is not a party).** Hard to apply in three respects: what counts as "in so many words" when the document says a party "must take on" the role; what to do when one of the named holders ("some other person or organization") has no code; and whether two role names in two documents may be treated as one role.
- **Rule 17 with rule 21 (`partly deferred`).** I wrote `partly deferred` on every answered item among the seven that rule 21 names (DM2, DM3, DM4, GR2, RV1, RV5), because AILLA-05 has a general deferring sentence. The rules do not say plainly whether this is wanted on each such item or only where the deferral is specific to the item.
- **Rule 18 (order of silence codes).** Unclear whether "the deposit document is not online" refers to the blank form or to the completed conditions of each deposit, and how to apply it when the documents say that the resulting metadata records are public.
- **Rule 8 (whose grounds).** Unclear whether a requirement that applies to all holdings (registration) counts as the archive restricting material "itself", and whether a condition for using the most open level (accessibility compliance for Public) is a reason for a restriction.
- **Rule 9 (levels).** The rule does not say whether an unrestricted level such as Public is counted. I counted it.
- **Rule 10 with 3.3 (RV1).** "Cannot be permanent" is hard to apply to advice worded with "perhaps".
- **Rule 11 (RV4 names its kind).** The rule does not say how the paraphrase should begin when the code is `not stated`. I wrote a plain sentence without one of the three opening words.
- **Rule 20 (the archive's own power).** Unclear whether rules that the archive imposes on the depositor's choice (a default level, a maximum embargo length) count as a power to restrict. I did not count them.
- **Section 6.1 (`paraphrase` for silence codes).** The codebook says what stays empty for `not stated` but not whether `paraphrase` should be filled. I filled it with one sentence.
