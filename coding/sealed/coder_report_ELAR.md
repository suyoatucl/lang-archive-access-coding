# Coder report: ELAR

Coder: AI. Codebook: version 0.5. Coded on: 2026-11-15. Rows written to `pass_ai.csv`: 13.

## Documents read

All were read from start to finish, after `codebook.md` and `sources.txt`. The reading was complete on 2026-11-15.

| source_id | Title | What it holds for the coding |
|---|---|---|
| ELAR-01 | Using ELAR (Terms and Conditions; How to use ELAR; Frequently Asked Questions) | Conditions of Access, the three access levels, who determines them, who grants permission, how to request access |
| ELAR-02 | About (Terms and Conditions and Data Protection Statement; Takedown Policy) | The same Conditions of Access as ELAR-01, and the Takedown Policy |
| ELAR-03 | Legal (Terms of Use and Privacy Policy) | Terms for the website. Nothing on restrictions on deposited material beyond a summary of the user's undertakings |
| ELAR-04 | Registering as an ELAR user (registration form) | Ten numbered terms. Clause 2 defines the Collection Steward. Clause 4 glosses the steward as the speech or signer community |
| ELAR-05 | Access request (form) | First page of the form only. Requests are forwarded to the Collection steward(s). Level name 'S_SubscriberAccess' |
| ELAR-06 | Deposit (Depositing collections) | Invitation to write to the archive about depositing. No deposit form or agreement |

Navigation menus, cookie banners, the team list and the Google Forms furniture were not treated as part of the documents.

## Items I was unsure about

**DM1.** Two doubts. First, the FAQ says the levels are "determined by the person or people who collected or curated the materials". I coded `depositor` because the next FAQ answer says "the depositor marked these materials as restricted", so the page treats that party as the depositor. A reader could hold that the two phrases name different parties. Second, I added `archive` only because rule 20 says that a power to "restrict or remove material, on a complaint" counts for DM1. The Takedown Policy says "protect or remove", not "restrict". The documents do not say how the depositor and the archive share the decision, and I wrote that in the paraphrase.

**DM2.** The only basis is rule 20 and the Takedown Policy. No document says that a depositor or steward can change a level after deposit. The note carries `partly deferred` because the general deferring sentence exists.

**DM3.** Coded `deferred` from the general deferring sentence. I did not extend rule 20 to DM3, although protecting or removing material and lifting a restriction are both changes made after deposit.

**DM4.** The role is clear. The party is not. ELAR-04 clause 4 says "the collection steward, i.e. the speech or signer community", in a clause about artificial intelligence. Rule 19 says a passing gloss counts, so I added `speaker or community`. ELAR-01 describes the steward as "the person who is responsible for the administration of the materials in that collection" and sets the steward beside "the person or people who collected or curated the materials", which sits uneasily with the gloss. I did not treat this as a conflict under rule 13, because ELAR-01 does not say who holds the role.

**GR1.** Coded `not stated`. The FAQ tells users to read the access restrictions "to understand why the depositor marked these materials as restricted". This implies that depositors record reasons with each bundle, but no document asks for reasons or says in what form they are given. A coder could read the same sentence as a deferral of GR1 to the bundle record. I used it for GR2 only, because it speaks of the reasons and not of the form in which the archive accepts them.

**GR2.** Coded `deferred` from the FAQ sentence, which names the matter. The general deferring sentence would give the same code.

**LV2.** The quotation can hold only one of the three names within 40 words. The other two follow in the same FAQ answer.

**RV3.** Coded `not stated`. The Takedown Policy says "taken down or reviewed" twice. A request to have material "reviewed" could be read as a route to have a restriction or an access decision reconsidered. I read it as part of the takedown route, because the only outcome the policy names is to "protect or remove" material, and rule 12 says a takedown request counts for RV4 only.

**RV4.** Coded `stated`, kind `takedown`. The policy speaks of "withdrawn items" and tombstones. I did not code `both`, because no document says that a depositor or a recorded person can take material or consent back.

**RV1, RV2, RV5.** All three are `deferred` on the strength of one sentence, "Specific restrictions accompany each item in ELAR." No document addresses these matters directly.

## Rules I found unclear or hard to apply

**Rule 5 (general statements), with rule 6.** ELAR-04 clause 2 says each collection has a Collection Steward "who is responsible for all matters relating to the collection". This does not speak of deciding on access as such, and rule 6 excludes statements that a party administers or manages a collection, so I did not count it. If it were read as a general statement, `steward or controller` (and, through the gloss in clause 4, `speaker or community`) would be added to DM1, DM2 and DM3, and DM3 would no longer be `deferred`. The rule does not say where "responsible for all matters" falls between "manages" and "decides". The same rule was also hard to apply to "determined by": I read it as an act of setting a level that counts for DM1 only, but the sentence does not mention deposit.

**Rule 19 (a role is not a party).** The rule says a passing gloss counts even when the passage is about another subject. It does not say what to do when another document describes the same role in words that point elsewhere (ELAR-01: "the person who is responsible for the administration"). It also does not say whether a gloss given in one document carries over to a decision that another document gives to the role. I applied it across documents.

**Rule 20 (the archive's own power).** The rule counts a takedown power for DM1 and DM2. It was not clear to me whether the archive then counts as a party that "sets" a restriction alongside the depositor under rule 4, and how to describe the sharing. It is also not clear why the rule stops at DM2 when removal on complaint can follow a decision by the depositor.

**Rules 17 and 21 (partly deferred, general deferral).** I wrote `partly deferred` for DM2 and DM4, where an answer and the general deferring sentence both exist. Rule 21 does not say whether a specific deferring sentence (as for GR2) should also be marked `general deferral` when a general one exists as well. I mentioned both in the note.

**Rule 18 (order of silence codes).** The Conditions of Access refer several times to "the conditions of deposit", and ELAR-06 shows no deposit form or agreement. The sentence I quote for the deferrals points to each item, not to the deposit conditions, so I did not write `deferred to a document that is not public`. The rule does not say which wording to use when one document defers both to item records and to deposit conditions.

**Rule 12 (a request is not an appeal).** See RV3. The rule does not cover a takedown route that also invites a request for "review".

**Rule 11 (RV4 names its kind).** See RV4. The rule does not say whether the archive's use of the word "withdrawn" for items it has taken down is enough for `withdrawal`.

**Rule 9 (levels).** The levels are described as levels of access to files but are set for bundles. I counted them as levels and said so in the paraphrase. The documents say nothing clear on the visibility of metadata, so the note records only that it is not described as a level.

**Section 3.1, `depositor`.** The definition tells the coder to use the code when the document "treats that party as the one who placed the material in the archive". ELAR-01 never says this of "the person or people who collected or curated the materials". I relied on the neighbouring sentence that uses the word "depositor".

## Other remarks

- The clause on artificial intelligence in ELAR-01, ELAR-02 and ELAR-04 requires the consent of "the speaker/signer community or its designated representatives" for one kind of use. I read it as a condition of use that applies to all material, not as a restriction on access to an item, and did not code it under DM1 to DM4 or GR2. It is the source of the gloss used for DM4.
- ELAR-05 shows only the first page of the access request form. Later pages, which the FAQ says ask for the bundles and the reasons for the request, are not in the document.
- ELAR-01 and ELAR-02 carry the same Conditions of Access. Where the quotation stands in both, both are listed in `source_id`, with ELAR-01 first.
- Every quotation was checked by script against the cited document, ignoring white space only.
