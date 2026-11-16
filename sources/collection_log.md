# Collection log

Dated record of what was collected, how, and what could not be collected. Dates are UTC.

## 2026-11-14

### DELAMAN membership (criterion 1)

The members page of DELAMAN (https://www.delaman.org/members/) lists AILLA, ELAR, Kaipuleohone and PARADISEC as Full Members. Recorded in `inclusion.csv`.

### PARADISEC

**Method.** The AI assistant retrieved public pages of www.paradisec.org.au and paradisec-archive.github.io with a headless browser, and two PDF forms by direct download. The main site has no `robots.txt` (HTTP 404). Nothing was saved to the repository.

**Registered.** Eleven rows in `sources.csv` (PARADISEC-01 to PARADISEC-11). Thirty passages in `coding/evidence.csv`. A script checked 29 quotations word for word against the retrieved text. One quotation (PARADISEC-E11) is set in two columns in the PDF and was checked by eye.

**Pages read with no passage on access restriction located.** They are not in `sources.csv`. The coder may want to confirm.

- Home page
- About us
- Advisory Committee
- Contact Us
- Principles for data management
- Do you own your records? (concerns ownership of intellectual property)
- Catalog Structure & File Naming
- Costing a deposit
- File formats
- Editing metadata
- Technical Guides & Downloads
- PARADISEC Workflows: Overview; Metadata & Data Management

**Not read.** Blog posts and the publications list (out of scope). Pages in other languages. Other pages of the PARADISEC Workflows guide (digitising, audio and video processing, ingest, training).

**Could not be reached.**

- The catalogue, https://catalog.paradisec.org.au/, returned HTTP 403 from a web application firewall. Registered as PARADISEC-10 with `status` set to `not reachable`. No attempt was made to work around the block. SQ to check in a browser.

**Two versions of the deposit form.**

- Current: PARADISEC-02, file name version v20261013, linked from the Deposit page and the downloads page.
- Earlier: PARADISEC-09, PDF created in 2015 and modified in 2018, still online and linked from the Getting Started guide (PARADISEC-05).
- The earlier form says the archive "will not hold material on permanent closed access" and offers an option to keep metadata out of public view. The current form has neither. Following the scope rule on versions, only the current form is coded.

**Items for which the assistant located no passage.** Review period (RV2) and appeal (RV3). This is not a code. The coder decides after reading the documents in full.

**Outside the template.** The Conditions of Access (PARADISEC-01) has a paragraph on commercial use and on uploading data to AI services. It is recorded in `evidence.csv` as `context only` and is not coded.

### AILLA

**Repository site: not collected.** Automated access is not permitted.

- The site's `robots.txt` (https://ailla.utexas.org/robots.txt) disallows `/about` and most other paths for all user agents.
- The site's bot protection returned "Access Denied" to the headless browser.

No attempt was made to work around either. SQ to read the About page in a browser (AILLA-08). The sitemap named in `robots.txt` lists https://ailla.lib.utexas.edu/about as the About page.

**Guide on LibGuides: pages collected.** AILLA's information for users and depositors is a guide at https://guides.lib.utexas.edu/ailla, last updated on 29 October 2026 according to the guide. It names ailla.utexas.org as the repository. That site's `robots.txt` allows the guide pages with a crawl delay of 10 seconds. The assistant read six English pages with a headless browser, 11 seconds apart.

- Registered: Terms & Conditions of Use, Deposit with AILLA, How-Tos and FAQs, About AILLA (AILLA-01 to AILLA-04). Nine passages in `coding/evidence.csv`, all checked word for word by script.
- Read with no passage on access restriction located: Mission & History; Citation Guidelines.
- Not read: the Spanish and Portuguese pages; Technology Stack; Grants, Letter of Consultation; the slides and videos linked from the FAQ page.
- SQ to confirm that the repository site links to this guide.

**Files on the guide: not read.** The guide links the Depositor License Agreement, the Deposit Instructions and copies of the Terms & Conditions as downloadable files (AILLA-05 to AILLA-07). The same `robots.txt` disallows the download path (`/ld.php`). SQ to download them in a browser.

**Error by the assistant.** The assistant downloaded four of these files before it had read the `/ld.php` rule: the check of `robots.txt` and the downloads ran in one command. The files were deleted unread. Nothing in this repository comes from them. The scope rule on automated access in `README.md` now says to read `robots.txt` before any other request.

**Gap.** The guide pages mention resource controllers, user roles, visibility settings, embargoes and controlled access. No page read so far defines them or sets out access levels.

**Other AILLA hosts, for comparison only.** An earlier site (islandora-ailla.lib.utexas.edu) and the legacy site (ailla-legacy.lib.utexas.edu) are still online according to a web search. The assistant did not read them. The legacy site could not be reached from the assistant's environment because of a certificate error.

### Web-archive snapshots

None saved yet. With SQ's consent, the assistant tried to submit the PARADISEC documents to the Wayback Machine (Save Page Now). The connection failed for the first three and the attempt stopped. No request was accepted. SQ to save PARADISEC-01 to PARADISEC-09 in a browser and add the links to `sources.csv`.

### First reachability checks for the other two archives

- ELAR (https://www.elararchive.org/) returned HTTP 403 to a command-line request. The home page opened in the headless browser. Not yet collected.
- Kaipuleohone is hosted on ScholarSpace (https://scholarspace.manoa.hawaii.edu/), which answered on the second attempt. Not yet collected.

## 2026-11-15

### Kaipuleohone

**Method.** The assistant read `robots.txt` for ScholarSpace and for Google Sites first. Both allow the pages requested.

**Registered.** One page, the archive's page on the LAELabs site of the University of Hawai'i (Kaipuleohone-01). Two passages in `coding/evidence.csv`, checked word for word by script.

**Could not be reached.** The Kaipuleohone community page on ScholarSpace (Kaipuleohone-02) returned "Access denied" from the site's automated-traffic filter. No attempt was made to work around it. SQ to read it in a browser.

**Not found.** A deposit form (Kaipuleohone-03). The archive's page mentions one, links none, and refers enquiries to the director by email. A web search found none. This is provisional until SQ has checked ScholarSpace.

**Inclusion criteria at risk.** Criterion 5 asks for an access policy and deposit documents online in English. Neither has been located for Kaipuleohone so far. See `inclusion.csv`.

### ELAR

**Method.** www.elararchive.org has no `robots.txt` (the address redirects to the login page) and the blog has none (HTTP 404). The site returned HTTP 403 to command-line requests and admitted the headless browser. The assistant read six pages 5 seconds apart: home, About, Using ELAR, Legal, Register, and Request access.

**Stopped.** Two statements on those pages bear on how this study may collect and cite ELAR's documents.

- The Conditions of Access prohibit automated collection of the archive's materials by crawlers or scrapers, and prohibit use of the materials for AI or machine learning without community consent. The clause names recordings, transcriptions, translations, annotations and metadata. It does not name the policy pages.
- The website's terms of use do not allow storing pages of the website on a networked server or device, or creating links to the website from another website without written consent.

The assistant made no further request to ELAR after reading these and asked SQ how to proceed.

**Resumed on SQ's decision.** SQ decided that the assistant should go on reading policy and help pages, that SQ would review the result, and that SQ would delete it and collect by hand if the review found a problem. Snapshots and links are handled as for the other archives for now, and the question goes to the co-author before any public release. The assistant then read the Using ELAR page again to capture the collapsed FAQ answers, the Deposit page, and the two public forms embedded in the Register and Request access pages. The forms were read and not submitted. One search of the blog for deposit pages returned blog posts only, which are out of scope.

**Never requested.** The catalogue, the list of collections, the map, any item or recording, any metadata record, and any page behind the login.

**Registered.** Eight rows in `sources.csv` (ELAR-01 to ELAR-08). Twenty-four passages in `coding/evidence.csv`, all checked word for word by script. The temporary copies of the pages were deleted after the check. No copy of a page is in this repository.

**Not found.** A deposit agreement, deposit form or deposit instructions (ELAR-07). The Deposit page asks prospective depositors to write to the archive. This bears on inclusion criterion 5.

**Not read.** Later pages of the access request form, which appear only after answering questions. The second host of the portal (ELAR-08), which could not be reached.

**Outside the template.** The conditions of access and the registration terms restrict AI use of the archive's materials. Recorded in `evidence.csv` as `context only`.

**Shared wording.** Much of ELAR's Conditions of Access matches PARADISEC's, with the archive's name changed.

### PARADISEC, addition

A web search listed further copies of the deposit form on the PARADISEC site (file names dated 2026-06-04 and a copy uploaded in 2025-08). The assistant did not retrieve them. They suggest that several superseded versions remain online besides PARADISEC-09.

### Decisions on 2026-11-15

**Inclusion criteria revised.** Criterion 3 no longer assumes that an archive which accepts deposits issues public deposit documents. Criterion 5 now asks for conditions of access or terms of use online in English, and no longer for deposit documents. Which other document types an archive publishes is recorded as a result.

**Kaipuleohone excluded.** SQ found the address of the archive's Conditions of Access (Kaipuleohone-04) and reported that it returned HTTP 404. The assistant confirmed the status at 13:55 UTC after reading the host's `robots.txt`, which allows the request. No other statement of conditions of access was located. The case does not meet the revised criterion 5 and is excluded. The cases are now AILLA, ELAR and PARADISEC. The decision goes to the co-author with the draft.

**Codebook 0.3.** Silence is coded as `deferred`, `not public` or `not stated`. `steward or controller` replaces `named controller`. The coding sheets now hold three archives.

### The Language Archive, checked and not collected (2026-11-15)

The co-author suggested The Language Archive (Max Planck Institute for Psycholinguistics) as a possible replacement for ELAR, subject to a check of its terms. The assistant read `robots.txt` for archive.mpi.nl, which allows the pages with a crawl delay of 10 seconds, then the home page and the Terms of Use (effective 26 October 2026). The terms do not allow access to the service by any automatic means for any purpose without prior written consent. The assistant made no further request. Nothing from this archive is registered, and the temporary copies were deleted. ELAR was not replaced.

### Collection completed by SQ (2026-11-15)

**AILLA.** SQ downloaded the Depositor License Agreement, the Terms & Conditions, the Deposit Instructions and the Mission Statement from the guide in a browser, and printed the About page of the repository site (AILLA-05 to AILLA-09). The About page links to the guide, which confirms the guide as the archive's current documentation. The row AILLA-09, which had recorded that no separate access policy page was located, now registers the Mission Statement.

**PARADISEC.** SQ opened the catalogue in a browser and printed its home page (PARADISEC-10). It is now registered as found and is part of the material for coding.

**ELAR.** The second host (ELAR-08) returned HTTP 404.

**Snapshots.** SQ saved web-archive snapshots for every document registered as found or superseded, in a browser. Whether the snapshot links for ELAR can appear in a public release is an open point, because ELAR's website terms restrict storing its pages.

**Document sets for coding.** AILLA-01 to AILLA-09; ELAR-01 to ELAR-06; PARADISEC-01 to PARADISEC-08 and PARADISEC-10.

### Coding by the AI coder (2026-11-15)

**Pilot.** One new AI agent for PARADISEC and one for ELAR coded with version 0.4 of the codebook. Their reports named rules that could be read in two ways. SQ reviewed 14 proposed clarifications, accepted 13 as proposed and widened the reach of the rule on general deferral to seven items. The codebook is now at version 0.5. The pilot sheets are kept in `coding/sealed/pilot/` and are not used as codings.

**Coding run.** Three new AI agents, one for each archive, coded with version 0.5. Each received the codebook and the full text of the documents listed above, and nothing else. For ELAR the assistant read the six policy pages again for this purpose and deleted the copies afterwards. For AILLA the agent read the files that SQ had saved.

**Sealed.** The AI coder's sheet for the three archives is in `coding/sealed/pass_ai.csv` (39 rows). A script found every quotation word for word in the document it cites. Two of the three agents were interrupted by a usage limit after writing their sheets and were resumed; both reported that they changed nothing in their sheets after resuming. SHA-256 of the sealed sheet: `483ab755d3a3b52bce2f80b5df51261514047dfee9937668c541e3436bf394b5`. The hash lets anyone confirm later that the sheet was not altered after the human coding began.

## 2026-11-16

### Materials given to the AI coder

At SQ's request the folders that the three AI agents received and wrote on 15 November were copied unchanged from the assistant's temporary area into the private notes, with checksums and the exact instructions. The input folder for ELAR no longer existed, because the assistant had deleted its copies of ELAR's pages after the coding run. On SQ's decision the assistant read the six ELAR policy documents again at 11:20 UTC with the same method and rebuilt the folder. The rebuilt texts have the same length, page by page and in total, as those of 15 November, and every quotation in the AI coder's sheet for ELAR is found in them word for word. The rebuilt folder is a reconstruction and is marked as one. These folders hold full copies of the archives' documents and are not part of any public release.
