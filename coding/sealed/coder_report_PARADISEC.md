# Coder report: PARADISEC

Coder: AI. Coded on 2026-11-15. Codebook version 0.5.

I worked only from the files in the INPUT folder. I read `codebook.md` and `sources.txt` in full, then every file in `documents/` from start to finish. The reading was complete on 2026-11-15. I wrote 13 rows to `pass_ai.csv`. A script checked that each quotation appears word for word (white space ignored) in the first source cited and has 40 words or fewer.

## 1. Documents read

| source_id | Title | Remark |
|---|---|---|
| PARADISEC-01 | Access Conditions (page heading: Conditions of Access) | Read in full |
| PARADISEC-02 | Deposit of Material (deposit form), with Explanatory Notes and Appendix 1 | Read in full |
| PARADISEC-03 | Deposit | Read in full |
| PARADISEC-04 | How to administer your account | Read in full |
| PARADISEC-05 | Getting Started with PARADISEC (PARADISEC Workflows) | Read in full |
| PARADISEC-06 | Our Collections | Read in full |
| PARADISEC-07 | Metadata | Read in full. Only the field "rights: Access conditions specific to this item" touches access. I did not base a code on it |
| PARADISEC-08 | Privacy Notice for EU Users of PARADISEC | Read in full. Treated under decision 4: codable only where a statement concerns access to deposited material. I did not base a code on it |
| PARADISEC-10 | PARADISEC catalogue, home page | Read in full |

`sources.txt` lists no PARADISEC-09. I coded the nine documents that were supplied.

Navigation menus, footers and the list of blog posts were ignored.

## 2. Items I was unsure about

**DM1.** The codes are clear, but the way the two parties share the decision is not. The depositor chooses at deposit. Explanatory Note 4 of the form says that by signing "you empower PARADISEC to decide over questions of access". This could be read as the archive overriding the depositor. No document says so in so many words, so I wrote that the documents do not say how they share the decision.

**DM3.** `depositor` rests on a help page that addresses "you" as a person who has "a collection in PARADISEC". I read that party as the depositor. `archive` rests only on the general statement in Explanatory Note 4. No document describes the archive lifting a restriction.

**DM4.** This is the item I am least sure about. I coded three parties.
- `depositor`: clear from PARADISEC-03 ("permission (specified by the depositor)") and the form's example.
- `steward or controller`: from the form's example condition "Files can be accessed with permission from the depositor or [a nominated contact]". Section 3.1 names a nominated contact as such a role, and the example says the contact gives permission. But it is only an example of a condition a depositor may write, and it is in square brackets. A coder could reasonably leave this code out.
- `archive`: only from the general statement in Explanatory Note 4.
PARADISEC-05 uses the word "collector" for the party whose catalogue page gives instructions for requests. It does not say that the collector decides. I treated this as a partial deferral to the catalogue page.

**GR1.** Question C.3 of the form asks for "special conditions ... when handling this material". It does not use the word "reasons" and does not tie the answer to the Open or Closed choice in part D. I coded `free text` because rule 8 includes conditions and sensitivities. The form does not say whether an answer is required.

**GR2.** I listed the form's examples and the archive's own reasons. The takedown passages name privacy, copyright, defamation and cultural sensitivity as grounds for a takedown request. I included them with the archive's own reasons, though they are strictly grounds for a request by a third party.

**LV1 and LV2.** The form names two levels. PARADISEC-04 mentions one option of a "Data access conditions" field in the catalogue and does not list the other options, so the catalogue may offer more than the documents state. PARADISEC-01 mentions "password-protected data" and PARADISEC-06 mentions field notes that are "publicly available through this website". I did not count either as a level, because neither is named as an access level for deposited files.

**RV1.** The form says "please specify a time period for Closed Access". I coded `stated`. I was unsure whether to call the mechanism required or optional. The wording reads as a requirement for anyone choosing Closed Access, but no document says that a restriction cannot be permanent or that a form without a period is refused.

**RV2.** No document states a review. I coded `deferred` under rule 21 from the sentence "Specific restrictions accompany each item in PARADISEC". Without rule 21 I would have coded `not stated`.

**RV3.** Coded `not stated`. PARADISEC-08 gives a right to complain to a supervisory authority, but about the processing of personal data. I did not count it.

**RV4.** Coded as takedown only. Two passages made me hesitate about withdrawal. The right to erasure in PARADISEC-08 concerns personal data of people in the EEA, and the same notice says that personal data in archived records may be kept indefinitely. Part E of the form has the depositor "revoke any previous conditions of restricted access", which is about conditions, not about taking material back. I counted neither as withdrawal.

**RV5.** The form asks for "an alternate contact for if you are unavailable". Rule 19 and the last examples in section 5 make this `stated`. The form does not say in that sentence that the contact decides. The section "Fieldworkers need to make a Will" in PARADISEC-03 is about depositing material after death, and I did not count it.

## 3. Rules I found unclear or hard to apply

**Rule 4 (several decision-makers).** The rule asks how the parties share a decision. Here one party acts at deposit and the other is "empowered" to decide in general. It is not clear whether an empowering clause of this kind should be read as "one overriding the other" or as "the documents do not say". I chose the second.

**Rule 5 (general statements).** Explanatory Note 4 is close to the rule's own example, so I applied it to DM1 to DM4. The result is that `archive` appears in DM3 and DM4 on the strength of one sentence in the notes to a deposit form. The rule does not say whether a general statement should still count for an item when other documents give a specific answer for that item that names a different party.

**Rule 6 (ability counts) and section 3.1 (`depositor`).** The help pages address "you". PARADISEC-04 defines "you" only as someone who has a collection in PARADISEC, and PARADISEC-05 says "collector" in one place. Section 3.1 covers a party described by what they did before deposit. It does not clearly cover a second-person address in a help page. I coded `depositor` and recorded the wording.

**Rule 8 (whose grounds).** It is not clear whether a question about "special conditions ... when handling this material" in a rights section counts as asking for reasons for a restriction, when the form does not link that question to the access choice.

**Rule 9 (levels).** The rule does not say what to do when a help page shows that a catalogue field has options and names only one of them. I counted only the named levels.

**Rules 10 and 19 together.** Rule 10 says an example condition on a form shows that an option exists, and speaks of mechanisms. Rule 19 says a request to name a contact does not make the contact a decision-maker. The form's example "permission from the depositor or [a nominated contact]" falls between them: it is an example, and it says the contact gives permission. I coded `steward or controller` for DM4 and noted `from an example on the form`. The rules do not say clearly whether an example can support a decision-maker code.

**Rules 17 and 21 (`partly deferred`).** Rule 21 says rule 17 applies to a general deferring sentence for seven items. I read this to mean that every answered item among the seven gets the note `partly deferred` whenever such a sentence exists. That applied to DM2, DM3, DM4, GR2, RV1 and RV5. The note then says little, because it appears on every answered item of that group. I was not sure this is what the rule intends.

**Rule 20 (the archive's own power).** The rule counts the power for DM1 and DM2 and, within a takedown route, for RV4. The source sentence says the archive "enforces access restrictions". It is not fully clear whether enforcing is the same as setting. I read it as setting, because the sentence follows a statement that online material may be sensitive or unlawful.

**Rule 12 and decision 4 (privacy notice).** The rule on appeals and the decision on privacy notices do not say how to treat a right to complain to an outside authority about personal data in deposit metadata. I did not count it for RV3.

**Rule 11 (RV4 names its kind).** The rule is clear. The difficulty was the boundary of "withdrawal": the codebook does not say whether a data protection right to erasure counts when the notice does not mention deposited recordings.
