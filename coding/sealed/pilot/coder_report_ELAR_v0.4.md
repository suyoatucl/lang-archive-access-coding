# Coder report: ELAR

Coder: AI. Coded on: 2026-11-15. Codebook: version 0.4.

Output: `pass_ai.csv` in this folder, 13 rows (DM1 to RV5), written with Python's `csv` module in UTF-8. Before writing, the script checked that every quotation is a character-for-character substring of the first source cited and has 40 words or fewer.

## 1. Documents read

All were read from start to finish, after `codebook.md` and `sources.txt`. Reading was complete on 2026-11-15.

| source_id | Title | What it holds for this coding |
|---|---|---|
| ELAR-01 | Using ELAR (Terms and Conditions; How to use ELAR; Frequently Asked Questions) | The main source. The FAQ part "Access" gives the three levels, who determines them, who grants permission, and how to request access |
| ELAR-02 | About (Terms and Conditions and Data Protection Statement; Takedown Policy) | The same Conditions of Access as ELAR-01, and the Takedown Policy |
| ELAR-03 | Legal (Terms of Use and Privacy Policy) | Terms for the website. Nothing on restrictions on deposited material beyond a summary of the user's undertaking |
| ELAR-04 | Registering as an ELAR user (registration form) | Defines the Collection Steward (clause 2) and glosses the steward as "the speech or signer community" (clause 4) |
| ELAR-05 | Access request (form) | Only the first page of the form. Says the request is forwarded to the Collection steward(s) and names the setting 'S_SubscriberAccess' |
| ELAR-06 | Deposit (Depositing collections) | Three short paragraphs. Asks prospective depositors to write to the archive. No deposit form, agreement or conditions |

No deposit agreement, deposit form or depositor guidance is among the documents. Most of the silence codes follow from this.

## 2. Items I was unsure about

**DM1 (coded `depositor`).** The code rests on "why the depositor marked these materials as restricted". Two other readings were possible and I did not code them:
- The steward. The levels "are administered by the Collection Steward", and the steward "is responsible for all matters relating to the collection" (ELAR-04, clause 2). I treated both as implying, not stating, a power to set a restriction (rule 2).
- The archive. Under the Takedown Policy, ELAR can "protect or remove" material after a justified request. I coded this under RV4 only. The codebook example "The archive may restrict any item at its discretion" gives `archive` for DM1 and DM2, so another coder could add `archive` here.

**DM2 and DM3 (coded `depositor`).** These are the least secure codes. No sentence speaks of changing or lifting a restriction. I applied rule 5 to the sentence "These are determined by the person or people who collected or curated the materials in the collection and are administered by the Collection Steward", which gives no moment. Two doubts:
- The sentence does not say "depositor". I mapped "the person or people who collected or curated the materials" to `depositor` because the same FAQ part uses "depositor" for the party who marked materials as restricted. This is a step of interpretation. A stricter reading of rule 2 would give `not stated`.
- "administered by the Collection Steward" may mean that the steward is the one who changes the setting in the catalogue (rule 6). The document does not say so, and I did not code it.

**DM4 (coded `speaker or community; steward or controller`).** The role code is secure: permission is "granted ... by the collection steward". The added party code is doubtful. It rests on one gloss in ELAR-04, clause 4: "the collection steward, i.e. the speech or signer community". That clause concerns artificial intelligence, not access requests, and the FAQ calls the steward "the person who is responsible for the administration of the materials in that collection". I added the code because 3.1 and rule 19 say to add a party code when a document says who holds the role. A coder who reads the gloss as limited to its clause would code `steward or controller` alone.

**GR1 (coded `not stated`) and GR2 (coded `deferred`).** The FAQ sentence "Read the access restrictions to understand why the depositor marked these materials as restricted" shows that reasons are recorded in each bundle. I used it to code GR2 as `deferred`, because the reasons themselves are left to the bundle records. For GR1 the same sentence only implies that depositors give reasons and says nothing about the form, so I coded `not stated`. `deferred` for GR1 would also be arguable. `not public` did not fit either item: the Terms and Conditions mention "the conditions of deposit" but do not say that they cover reasons.

**LV1 and LV2.** The codes are secure. Two small points: the levels are assigned to bundles and govern the files in them, and no document says in terms whether metadata is visible at each level. I recorded the implication in `note`.

**RV3 (coded `not stated`).** The Takedown Policy opens with "If you believe that material should be taken down or reviewed". A person who thinks an open item should not be open could use this to contest its access level, which is close to "disagrees with a decision on a restriction" in 3.3. I read it as a first request, coded under RV4, by analogy with rule 12. The documents give no route to contest a refused access request or the outcome of a takedown request.

**RV4 (coded `stated`, kind `takedown`).** The policy mentions "withdrawn items" and tombstone citations. I did not code `both`, because no document says that a depositor or a recorded person can take material or consent back.

**RV1, RV2, RV5 (coded `not stated`).** No doubt about the codes. For these rows, and for GR1 and RV3, I listed all six documents in `source_id` and wrote "no relevant passage" in `section`, because the silence rests on the full reading. The codebook does not say what these two columns should hold for `not stated`.

**A passage that fits no item.** The Conditions of Access and the registration terms forbid use of the materials for artificial intelligence or machine learning without the consent of "the speaker/signer community or its designated representatives". This is a restriction on use that covers all holdings, not a restriction on access to files, so I did not code it under any item. It is the only place where the documents give a decision to the community in its own right.

## 3. Rules I found unclear or hard to apply

- **Rule 5 (general statements).** Two difficulties. First, the rule does not say what to do when a general statement and a specific statement both bear on one item. Read literally, the general sentence on who determines the levels also counts for DM4, which would add `depositor` there. I did not add it, because the documents answer DM4 with a specific statement and the general sentence concerns the levels. Second, it is not clear whether a statement about who "determines" access levels is "a statement about decisions on access in general". I treated it as one for DM2 and DM3.
- **Rule 2 with section 3.1 (`depositor`).** The codebook defines the depositor as the party that "deposits the material and signs the deposit document". The ELAR FAQ speaks of "the person or people who collected or curated the materials". The codebook does not say whether such a description may be coded as `depositor` or needs a silence code.
- **Rule 6 (ability counts).** It is unclear whether "administered by the Collection Steward" counts as a statement that the steward can change a setting. I decided that it does not, because no act of setting or changing is named.
- **Rule 19 and section 3.1 (who holds the role).** The rule does not say how strong or how general the statement must be. ELAR-04 gives the holder of the steward role in a single "i.e." gloss, in a clause on another subject, and another document calls the steward "the person". The rule also does not say whether a party code added in this way must meet the definition of `speaker or community` ("acting in their own right").
- **Rule 4 (several decision-makers).** The four ways of sharing a decision do not cover the case where two codes name the same party, once as a role and once as its holder. I explained this in `paraphrase` for DM4.
- **Rule 12 with section 3.3 (RV3 against RV4).** The boundary between a takedown request and an appeal is not drawn. A request to have material "reviewed" contests the current access setting, but it is also the first request made to the archive.
- **Section 3.4 and rule 18 (`deferred` against `not stated`).** ELAR's documents say "Specific restrictions accompany each item in ELAR." It is unclear how far such a sentence defers: only the content of restrictions, or also their grounds, duration and review. I used it to support `deferred` for GR2 only, together with the FAQ sentence, and coded `not stated` for RV1, RV2 and RV5.
- **Rule 9 (levels concern files).** ELAR assigns levels to bundles, not to single files. The rule does not say whether this needs a note. I recorded it in `paraphrase` for LV1.
- **Example row for DM1 and DM2 in section 5 ("The archive may restrict any item at its discretion").** It is unclear whether a takedown power of the archive counts in the same way for DM1 and DM2, or belongs to RV4 alone.
