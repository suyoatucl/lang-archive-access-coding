# Coder report: PARADISEC (AI coder)

Coded on 2026-11-15 with codebook version 0.4. Output: `pass_ai.csv`, 13 rows (DM1 to RV5).

Only the files in the input folder were used: `codebook.md`, `sources.txt` and the eight files in `documents/`. No web access, no other file and no outside knowledge was used.

## 1. Documents read

All eight documents were read from start to finish on 2026-11-15. Navigation menus, footers and the blog feed were ignored.

| source_id | Title | Used in the coding |
|---|---|---|
| PARADISEC-01 | Access Conditions (page heading: Conditions of Access) | Notes to LV1 and LV2 only. The page sets conditions of use for people who obtain data. It says that "Specific restrictions accompany each item" |
| PARADISEC-02 | Deposit of Material (deposit form) | DM1 to DM4, GR1, GR2, LV1, LV2, RV1, RV5 |
| PARADISEC-03 | Deposit | DM1, DM2, DM4, GR2, LV2, RV4 |
| PARADISEC-04 | How to administer your account | DM2, DM3, DM4, LV1, LV2 |
| PARADISEC-05 | Getting Started with PARADISEC (PARADISEC Workflows) | DM2, DM3, DM4, LV1, LV2 |
| PARADISEC-06 | Our Collections | Notes to LV1 and LV2 (metadata, deferral to the catalogue) |
| PARADISEC-07 | Metadata | Not used for a code. It lists a `rights` field, "Access conditions specific to this item", with no fixed values |
| PARADISEC-08 | Privacy Notice for EU Users of PARADISEC | Notes to RV3 and RV4 only (decision 4 in section 8 of the codebook) |

## 2. Items I was unsure about

**DM1 to DM4, the code `archive`.** For DM3 and DM4 the archive is coded only from Explanatory Note 4 of the deposit form ("you empower PARADISEC to decide over questions of access to, and use of, the material"). I read this as a general statement under rule 5. It can also be read as tied to the moment of signing, in which case it would count for DM1 only. For DM1 and DM2 there is a second basis in PARADISEC-03 (the archive "enforces access restrictions whenever we are made aware of such issues"), so those two are firmer. No document says how the depositor and the archive share the decision or which one prevails. I did not write `conflict`, because the two statements can both hold.

**DM4, the code `steward or controller`.** The deposit form asks a Closed Access depositor to "nominate an alternate contact for if you are unavailable" and gives the example "Files can be accessed with permission from the depositor or [a nominated contact]". Section 3.1 lists "a nominated contact" as a role, so I coded it. The doubt is that the contact's power to give permission stands in an example condition, not in a rule of the archive. A stricter reading of rule 2 would give `depositor; archive`.

**RV5.** Coded `stated` on the same passage as above. The instruction says to nominate a contact for when the depositor is unavailable but does not itself say that the contact decides. The example line does. If the example is not accepted as an explicit statement, the code would be a silence code with the implication described in the note. DM4 and RV5 should be resolved together.

**RV1.** Coded `stated`. Rule 10 asks whether the mechanism is required or optional. The form words it as an instruction ("please specify a time period for Closed Access"), but no document says that a period is compulsory, that Closed Access cannot be permanent, or what happens when no period is given. I described this in the paraphrase and did not choose between "required" and "optional".

**GR1.** Coded `free text` from question C.3 of the form, which asks for "special conditions" with examples. The form never asks in so many words for the reason for a restriction. The Closed Access option asks for conditions, a time period and a contact, not a reason. If C.3 is not accepted as a place where reasons are given, GR1 would be `not stated`.

**GR2.** The depositor reasons are examples on the form. The other reasons listed are archive-initiated (PARADISEC-03). I listed the grounds of the takedown request (rights, privacy law, defamation, copyright) with the archive-initiated reasons, although they are reasons that a third party gives.

**LV1.** Coded `2` (Open Access, Closed Access). Closed Access holds whatever conditions the depositor writes (permission, a year, community membership), so the real number of settings is open-ended, but the documents name two levels only. PARADISEC-06 also says that some digitised fieldnotes are "publicly available through this website"; I did not count this as a third level because no document presents it as an access level. PARADISEC-06 and PARADISEC-01 say that conditions are specified for each collection or item, so I wrote `partly deferred`.

**RV3.** Coded `not stated`. The takedown request in PARADISEC-03 could be read as a route for a person who disagrees with material being accessible. I kept it under RV4 only.

**RV4.** Coded `stated` as takedown only. The privacy notice lists a right of erasure "in certain conditions" for individuals in the EEA. I did not code this as withdrawal, because it concerns personal data and the notice also says that personal data in archived records may be retained indefinitely.

## 3. Rules I found unclear or hard to apply

- **Rule 5 (general statements).** The rule separates a statement "tied to the moment of deposit" from a statement "with no moment given". Explanatory Note 4 of the deposit form is made at signing but describes a standing power of the archive. The rule does not say which side such a statement falls on.
- **Rule 2 with rule 10 (explicit statements, options count).** It is not clear whether an example condition printed on a deposit form ("For example: ...") is an explicit statement or an option that counts. Rule 7 says that examples are not a closed list for grounds, but no rule says how examples count for DM4, RV1 and RV5.
- **Rule 19 and section 3.1 (roles).** Section 3.1 names "a nominated contact" as a role, but says to use the code "when a document gives the decision to the role". The form asks for a nominated contact without stating a rule that the contact decides. The rule does not say whether asking for a nomination is enough.
- **Rule 4 (several decision-makers).** The paraphrase must say how the parties share the decision. The documents name two or three parties and do not say how they share it. I wrote that the documents do not say. A fixed wording for this case would help.
- **Rule 8 and GR1 (whose grounds).** GR1 assumes that the archive asks for reasons. The rule does not say what to code when a form asks for "special conditions" or for the conditions of a restriction, without asking for reasons.
- **Rule 9 (levels).** The rule does not say how to count a level whose content is set freely by the depositor, or material that is described as public outside the two named levels.
- **Rule 13 (conflict).** It is not clear whether two statements that give the same decision to different parties (the depositor in PARADISEC-03, the archive in the form) are a conflict or a case of several decision-makers under rule 4. I treated them under rule 4.
- **Rule 17 (partly deferred).** PARADISEC-06 and PARADISEC-01 defer the content of the conditions to each collection or item. The rule does not say whether that deferral applies to every item or only to the items it touches most closely. I wrote `partly deferred` for LV1, LV2 and DM4 only.
- **Rule 12 with RV3 and RV4.** A takedown request contests the fact that material is accessible. The rules do not say whether it can count for RV3 as well as RV4.
- **Section 6.1, `short_quote`.** The PDF text of the deposit form breaks sentences across lines. To keep quotations character for character, I took every quotation from a single line of the source file. For GR1, GR2 and RV1 this gives part of a sentence, and for RV5 it led me to quote the example line instead of the instruction. The notes say so in each case.

## 4. Other remarks

- Silence codes: RV2 and RV3 are `not stated`. No item was coded `deferred` or `not public`.
- The deposit form's Explanatory Notes refer to "access to the material (part C)", although access is part D of the form. This did not affect a code.
- Email addresses appear in the documents as "[email address removed]". No quotation contains a personal name, an email address or a telephone number.
