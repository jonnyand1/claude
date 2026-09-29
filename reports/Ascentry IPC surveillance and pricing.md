# Ascentry: lab-born infection surveillance, sold with middleware

**Bottom line (research cut-off 2026-09-26).**

1. **IPC tools:** Ascentry (formerly BYG4lab) has one IPC/epidemiology product, **Infection Tracker**. It was called Ynfectio from 2023 and descends from Info Partner's INFECTIO, first released more than 25 years ago. It is lab-fed and provides MDRO/BHRe alerts, readmission and contact alerts, an IPC-team hygiene module, antibiograms and statistics. An AI cross-transmission layer is being piloted with GeodAIsics and CHU Rennes.
2. **AMS:** Ascentry offers only lab-side "AMS support" (antibiograms, resistance trends, reports to pharmacists). No prescription-level AMS, consumption (DDD/DOT) or AMS CDSS was found.
3. **Footprint:** France is CONFIRMED. Belgium is CONFIRMED as an installed base, through official tenders naming BYG4lab middleware and a legacy INFECTIO site in Arlon. Switzerland rests only on an old partner4lab company claim and is unverified.
4. **Pricing:** there is no public price list. Hospitals buy a licence and then sign roughly 4-year maintenance contracts, usually single-source. The IPC module has been bought both on its own (€10,315 over 4 years, CH Nevers) and bundled with Ascentry middleware (€415,155, CHU Caen).
5. **Framing correction:** Ascentry sells **no LIS**, so "LIS upsell" is the wrong frame. The real pattern is a standalone, LIS-agnostic product that is cross-sold into Ascentry middleware accounts and increasingly sold through LIS partners (Inlog covers Infection Tracker; the Technidata TDMind OEM covers middleware). The main open buying window is the **legacy INFECTIO base**, which loses maintenance in June 2027 (internal intelligence). Confirmed or likely legacy sites include GHT Coeur Grand Est, CHU Grenoble, CHU Reims and CHU Dijon (chapter 13).

---

## Confidence labels and research limitations

### Confidence-label legend

| Label | Meaning |
|---|---|
| CONFIRMED | Official, registry, procurement or independent source |
| CONFIRMED (company claim) | Stated by Ascentry/BYG4lab/partner4lab, its partners or its advertorials; not independently verified |
| CONFIRMED (user-provided internal intelligence) | **None exists for this company.** No prior LUMED tender, report or internal context about Ascentry was provided |
| INDICATIVE | Analyst inference; the reasoning is stated |
| UNKNOWN | Searched and not found; where it was searched is stated |

A result of "not found on a portal that was not queried directly" means **unverified, not absent**.

### Research limitations: every blocked or unqueried source and the manual check it implies

| Source | Problem | Manual check implied |
|---|---|---|
| BOAMP, PLACE (marches-publics.gouv.fr), regional platforms (Maximilien, e-marchespublics, AWS-achat, Atexo instances), achatpublic, marchesonline, francemarches | Not queried (interactive search) | Search "BYG", "BYG4LAB", "BIG4LAB", "Ascentry", "Ynfectio", "Infectio", "nYna/NINA", "EVM", "Qualynk", "Info Partner". Download the DCE/CCTP for CHU Caen ref. 2023132 on PLACE |
| data.gouv.fr DECP bulk files; recherche-entreprises API | Connection resets. The data.economie.gouv.fr API did work | Resolved on 26/09/2026 by a direct registry query: SIREN 200011203 is the Centre hospitalier intercommunal Agglomération de Nevers (https://recherche-entreprises.api.gouv.fr/search?q=200011203) |
| UGAP, RESAH, UniHA, CAIH, Helpévia catalogues | Login-walled | Check whether Ascentry or Infection Tracker is listed and at what price |
| TED notice HTML/PDF for 577496-2021, 495457-2021, 583476-2019 | Rendering blocked. One researcher parsed the XML; another could not | Open the PDFs to confirm BYG's role in the UGAP and CHU Caen reagent lots |
| publicprocurement.be, simap.ch, ANAC/BDNCP (IT), PLACSP (ES), Find a Tender / Contracts Finder (UK) | Not queried directly; reached only via TED/web | Search each portal for BYG4lab/Ascentry/Ynfectio/Infection Tracker |
| KBO/BCE (BE), Zefix/moneyhouse (CH), Companies House (UK), YTJ (FI) | Not queried | Confirm or rule out local legal entities |
| Bodacc, Infogreffe, RNE | Not consulted directly | Get the exact date BYG INFORMATIQUE became ASCENTRY FRANCE and the nature of the 10/09/2026 filing |
| EUDAMED, FDA establishment database | Not queried (JavaScript-only UI) | Check CE/IVDR/MDR class, UDI and actor registration for BYG Informatique and Finbiosoft |
| web.archive.org | Blocked (egress / connection reset) | Retrieve archived byg4lab.com Ynfectio page, white paper and case studies |
| byg4lab.com (301 to ascentry.com, content removed), byg-info.com (503), partner4lab.com (DNS/502), professeurs-medecine-nancy.fr (503) | Legacy pages unreadable; some claims rest on search snippets only | Read archived copies |
| LinkedIn | Not fetched | Headcount by function; background of CEO Ludovic d'Apréa; Belgian/Swiss staff |
| Business Wire QuidelOrtho release (403), infonet.fr (403), PitchBook (paywall), CFNEWS, Fusacq, Forbes France BrandVoice (DNS) | Blocked or paywalled | Read the full texts |
| Biologiste365 "Quand les données de biologie…" and "antibiothérapie" articles | Paywalled after the intro | Read the full text. The CHRU Nancy/LUMED point is now settled by internal intelligence: LUMED APSS + ZINC since 2021 |
| Spectra Diagnostic n°35 (Nov 2024) and n°41 (Nov 2025) PDFs | Text extraction failed (font encoding) | Read manually; n°41 "Retours sur les middlewares" may name customers |
| RICAI, ESCMID, EuroMedLab/IFCC, JIB/SFBC, BSIM/BVIKM, Swiss Society for Microbiology abstract books; SF2H 2026 abstract book; Google Scholar | Not full-text searched | Search for Ynfectio/Infection Tracker abstracts (Rennes, Grenoble, Reims authors) |
| JIB, RICAI, Medica, Santexpo, HIMSS Europe 2025–2026 exhibitor lists | Not reached | Confirm event presence |
| DECP publication threshold (chapter 13) | Small maintenance contracts, typical for Infectio, are usually not published, so DECP under-reports the legacy base | Ask each target hospital's purchasing office for its annual list of contracts, or ask Ascentry-exposed labs directly |
| TED XML/PDF downloads for 489752-2024 (September 2026) | HTTP 202 (not generated). Lot winners read through the TED search API instead | Open the notice in a browser to confirm lot-by-lot winners and any co-holders |

---

## Executive summary of key findings

| # | Finding | NEW (since ~Sept 2025)? | Confidence | Source |
|---|---|---|---|---|
| 1 | BYG4lab rebranded as **Ascentry** at ADLM Chicago (July 2025). Ynfectio became **Infection Tracker**, nYna became Lab Composer, Ypoc became POC Controller | No (July 2025) | CONFIRMED (company claim) | [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software); [Biologiste365](https://www.biologiste365.fr/biologiste365-fr/actualites-biologiste365-fr/byg4lab-devient-ascentry/) |
| 2 | Infection Tracker is a lab-fed IPC/AMR epidemiology tool claimed at "90+ sites across Europe". No customer is named on the page | Page published 9 Dec 2025, modified 9 Feb 2026: **NEW** | CONFIRMED (company claim) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| 3 | No prescription-level AMS, antibiotic-consumption or AMS CDSS function was found | — | UNKNOWN (searched product pages, FAQ, trade press) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| 4 | **Inlog** strategic partnership (LIS/transfusion) explicitly covers Infection Tracker. The reference site is Hôpitaux Paris Saint-Joseph / Marie-Lannelongue | **NEW** (2 Oct 2025) | CONFIRMED (company claim) | [Ascentry x Inlog](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |
| 5 | CHU Caen framework (nYna + Ynfectio + Qualynk + EVM-IH, 3 GHT sites, €415,155) modified | **NEW** (modification 17 Dec 2025) | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 6 | Advisory Board of IVD-industry executives launched | **NEW** (22 Jan 2026) | CONFIRMED (company claim) | [Advisory board PR](https://www.ascentry.com/event/ascentry-launches-advisory-board-to-drive-strategic-growth/) |
| 7 | Technidata partnership renewed; new TDMind (Ascentry middleware inside the Technidata LIS) released | **NEW** (Jan–Feb 2026) | CONFIRMED | [Ascentry PR](https://www.ascentry.com/wp-content/uploads/2026/02/Press-Release-Ascentry-x-TechniData-February-2026-1.pdf); [Technidata PR](https://www.technidata-web.com/images/PDF/Press/English/202602_PR_Partnership_TECHNIDATA_x_ASCENTRY.pdf) |
| 8 | Standalone 4-year maintenance contract for "INFECTIO LABO / YNFECTIOLABO" (€10,314.92), no competition, CH intercommunal Agglomération de Nevers | **NEW** (notified 2 Feb 2026) | CONFIRMED (contract and buyer identity via registry) | [DECP 2026S00059](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/); [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| 9 | CEO change: Ludovic d'Apréa became COO (25 Mar 2026), then CEO (1 Jul 2026). Founder-owner Cyril Verhille remains President and leads the Advisory Board | **NEW** | CONFIRMED (company claim) | [CEO announcement](https://www.ascentry.com/event/ascentry_appoints_ludovic_d_aprea_as_new_chief_executive_officer/) |
| 10 | IPC-audience events in 2026: BICS/ABIHH/WIN (Brussels), CPias Bretagne, Sciensano, JNI/SEIMC (Bilbao), **SF2H 2026 session "AI & Infection Tracker: first results at Rennes University Hospital"** | **NEW** | CONFIRMED (company claim) | [News & events](https://www.ascentry.com/news-and-events/); [SF2H 2026](https://www.ascentry.com/event/sf2h-2026/) |
| 11 | Legal entities renamed: holding BYG4lab Group became **Ascentry Group** (16/07/2026). Operating company BYG INFORMATIQUE is now **ASCENTRY FRANCE** (exact date unresolved; see contradiction C1) | **NEW** | CONFIRMED (registry aggregator) | [Pappers Group](https://www.pappers.fr/entreprise/ascentry-group-915233837); [Pappers France](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| 12 | French operating entity revenue €13.7M, net profit €2.88M, 94 staff (2024). Group claims 120 employees | 2025 accounts filed Jul–Aug 2026, figures not retrieved: **NEW** | CONFIRMED | [Pappers France](https://www.pappers.fr/entreprise/byg-informatique-326649407); [About us](https://www.ascentry.com/about-us/) |
| 13 | The peer-reviewed evidence for this product line is historical **VIGI@ct/VIGIguard, sold under the bioMérieux name**. Ascentry says Info Partner designed them. No peer-reviewed evaluation of Ynfectio/Infection Tracker exists | — | CONFIRMED (papers); link CONFIRMED (company claim) | [JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf); [PubMed 17544166](https://pubmed.ncbi.nlm.nih.gov/17544166) |
| 14 | Belgian IVD tenders require connection to existing BYG4lab middleware, including the **HUmani Charleroi antibiogram tender won by bioMérieux Benelux** (€895,143.27) | Award 2025 | CONFIRMED | [TED 180670-2024](https://ted.europa.eu/en/notice/-/detail/180670-2024); [TED 423892-2025](https://ted.europa.eu/en/notice/-/detail/423892-2025) |
| 15 | Legacy INFECTIO loses maintenance in **June 2027**. Known current Infectio customers: **GHT Coeur Grand Est** and **CHU Grenoble Alpes**. No public Ascentry statement of the date was found | **NEW** | CONFIRMED (user-provided internal intelligence) | Internal; chapter 13 |
| 16 | **CHU Reims** still uses **InfectioGlobal V4** for MRSA alerts to its infection-control team. Its LIS vendor Inlog now resells Infection Tracker | **NEW** (2025 thesis) | CONFIRMED | [Reims thesis 2025](https://dumas.ccsd.cnrs.fr/dumas-05322365v1) |
| 17 | CHU Grenoble's Ascentry PILOT MALDI maintenance ends about **25/04/2027**, close to the Infectio cut-off. CHU Dijon's Info Partner contract ended about 03/05/2026 with no published renewal | **NEW** | CONFIRMED (contracts); end dates INDICATIVE | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 18 | RESAH's anti-microbial-resistance framework awarded the IPC/AMS software lots 8–10 to **Nosotech (Nosokos)**, running to about May 2028. Ascentry holds no RESAH framework lot. Relaunched lot 1 (microbiology + surveillance/antibiotherapy software) went to bioMérieux | **NEW** (follow-on contracts 2025–2026) | CONFIRMED | [TED 489752-2024](https://ted.europa.eu/en/notice/-/detail/489752-2024); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 19 | **CHRU Nancy**, the historic INFECTIO site, has used **LUMED APSS and ZINC since 2021**. It is the natural reference for legacy-Infectio prospects | **NEW** (to this report) | CONFIRMED (user-provided internal intelligence) | Internal |
| 20 | Only about 20 of Ascentry's claimed 400+ French middleware sites are publicly identifiable. Six contracts come up for renewal between January and December 2027 (Gonesse, Saint-Étienne, Rouen, Grenoble, Caen, plus the Infectio cut-off), and CH Cannes runs Inlog + nYna, the profile the Inlog–Ascentry partnership targets | **NEW** | CONFIRMED (contracts, hospital documents); end dates INDICATIVE | Chapter 13.7 |

---

## Contradictions between notes, reconciled

| # | Topic | What the notes say | Reconciliation | Confidence |
|---|---|---|---|---|
| C1 | Renaming of the French operating entity | One note says Pappers shows a registry change on **10/09/2026** for SIREN 326 649 407, now "ASCENTRY FRANCE". Another says the **holding** BYG4lab Group became Ascentry Group on **16/07/2026**. A third reads the 10/09/2026 Bodacc entry as an **administration change** (probably the CEO transition). The brand launch was **ADLM, July 2025** | These are three separate events: the brand (July 2025), the holding rename (16/07/2026, CONFIRMED via Pappers) and the operating-company rename (date **not established**). 10/09/2026 is the latest Bodacc filing, but whether it records the rename or a governance change is unverified. Check Bodacc/RNE | Brand and holding: CONFIRMED. Operating-company rename date: UNKNOWN |
| C2 | Company founding date | Pappers gives 01/12/1982. The recherche-entreprises API gives 2003-10-01. The ADLM release says "over two decades" | Treat 1982 as the founding of BYG (company and Keensight both say so). 2003 is probably a registry re-creation or legal-form event, which is unverified | INDICATIVE |
| C3 | €10,315 Infectio Labo / Ynfectio Labo contract | One note (from the Pappers contract listing) names **CH intercommunal Agglomération de Nevers**. The other (raw DECP) gives only **buyer SIRET 20001120300011**, place of performance Nièvre (58), and leaves the buyer unresolved | CONFIRMED: the contract object, €10,314.92, 48 months, no publicity or competition, notified 02/02/2026, place of performance Nièvre. RESOLVED: a direct registry lookup of SIREN 200011203 returns CTRE HOSPITALIER INTERCOMMUNAL AGGLOMERATION DE NEVERS, 1 avenue Patrick Guillot, 58000 Nevers (https://recherche-entreprises.api.gouv.fr/search?q=200011203) | CONFIRMED |
| C4 | Finbiosoft acquisition date | Keensight announced "to acquire" on **14 March 2024**. Ascentry's blog says Finbiosoft "joined" on 14 March 2024. PitchBook shows 14 or 18 March | Use **14 March 2024** (announcement / joining). 18 March may be the closing date, which is unverified | CONFIRMED (14 Mar); 18 Mar UNKNOWN |
| C5 | "Merger" vs acquisition | Brandpie: "Ascentry was born from the merger of BYG4lab and Finbiosoft" | Legally, BYG4lab **acquired** Finbiosoft with Keensight backing. "Merger" is agency brand language | CONFIRMED (acquisition) |
| C6 | Info Partner vs partner4lab | Notes use both names | They are the same business. **Info Partner SAS** (SIREN 349 314 948, Vandoeuvre/Villers-lès-Nancy, founded 1989 per its own claim) traded as **partner4lab**. The JIB 2021 deck says "Février 2020 : Acquisition d'INFO PARTNER". A 2020 advertorial dates the acquisition to 28 Feb 2020 | CONFIRMED (company claim + registry) |
| C7 | CHU Caen contract duration and dates | Pappers/pricing note: 4 years, "notified 17/12/2025". DECP: **44 months**, notified **2024-04-18**, with a modification published **2025-12-17**. TED: award decision 2024-04-15, conclusion 2024-04-17 | The contract started in April 2024. The 17/12/2025 date is the **modification** (amount not shown), not a new award. The duration is **44 months per DECP**; "4 years" is the rounded figure in the Pappers listing. Expected expiry is about **Dec 2027** | CONFIRMED (dates); end date INDICATIVE |
| C8 | Which entity publishes the website | The legal notice names **BYG4lab Group SAS** (SIREN 915 233 837, the holding) as publisher. The ISO 13485 manufacturer is **BYG Informatique SAS / Ascentry France** (SIREN 326 649 407), which is also the party on every public contract | The website is published by the **holding**, whose legal notice still uses the pre-July-2026 name. The medical-device manufacturer and contracting party is the **operating company**. Bidders should expect "BYG INFORMATIQUE" on pre-2026 awards and possibly "ASCENTRY FRANCE" later | CONFIRMED |
| C9 | National surveillance exports on the Infection Tracker page | One note records the page claiming exports to **SPARES, PRIMO, ConsoRes, WHONET, EARS-Net**. Two other notes read the same page as naming no national network, only "comply with national and international guidelines" and multi-format export | The claim is **contested between readings**. Only a legacy byg4lab.com snippet ("automatic reporting for CONSORES/SCIENSANO") and Spectra advertorials ("national surveillance reports") are independently recorded. Re-read the live page before quoting it in a tender | INDICATIVE |
| C10 | UGAP 2021 framework and CHU Caen 2019 reagent tender | One note parsed the TED XML: BYG INFORMATIQUE is a member of the Ortho-Clinical–led winning group on UGAP lot "biochimie immunologie chimie sèche" (TED 495457-2021), and the EVM service was a mandatory supplementary item awarded to Grifols at CHU Caen (TED 583476-2019). The other note could not render these and calls BYG's role unverified | The XML reading is more specific and is adopted, **with the caveat that it came from flattened XML**. Confirm from the PDFs | CONFIRMED (XML), manual check advised |
| C11 | CHR/CHU Orléans | One note: only a 2019 contract (€40,966), renewal unknown. The other: a further Pappers entry, 13/04/2023, €21,000, 2 years (contract no. 238-457) | Both are in the contract table. The 2023 entry comes from the Pappers listing only | CONFIRMED (Pappers/DECP) |
| C12 | "Centre Hospitalier Général" and unnamed CHU rows in Pappers | Pappers shows generic buyer names | The DECP SIRETs resolve them to **CH Beauvais** (EVM/NINA, 2019 and 2025) and **CHU Saint-Étienne** (MALDI connections, €9,120) | CONFIRMED |

---

## 1. Company profile and headcount

Ascentry is a **French lab-software group headquartered in L'Union (31240), near Toulouse, in Occitanie**. A second French site at Villers-lès-Nancy (Grand Est) came from the 2020 purchase of Info Partner/partner4lab, the origin of the IPC product line ([Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407)). BYG was founded in 1982, and Cyril Verhille acquired it in 2012 ([Keensight PR 2022](https://keensight.com/wp-content/uploads/2022/07/PR-BYG4lab-v17.07.2022-FR-KEENSIGHT-ONLY-Final.pdf)). **Keensight Capital took a majority stake in July 2022**, with IRDI Capital Investissement co-investing ([Private Equity Wire](https://www.privateequitywire.co.uk/keensight-capital-acquires-majority-stake-byg4lab/)). The group acquired Finbiosoft (Finland, Validation Manager) in March 2024 and set up a US subsidiary, BYG4lab, Inc. ([Keensight 2024](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/); [ADLM 2025 exhibitor](https://adlm25.myexpoonline.com/co/byg4lab-inc)).

### Legal entities

| Entity | SIREN | Role | Key facts | Confidence | Source |
|---|---|---|---|---|---|
| ASCENTRY FRANCE (formerly BYG INFORMATIQUE) | 326 649 407 | Operating company, ISO 13485 manufacturer, contracting party on all French public contracts | SASU, capital €75k. Sites: L'Union HQ and Villers-lès-Nancy. President: Ascentry Group | CONFIRMED | [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| ASCENTRY GROUP (formerly BYG4lab Group, renamed 16/07/2026) | 915 233 837 | Holding; publishes the website | SAS, capital €49,004,518.56. Created 01/07/2022. President Cyril Verhille. Keensight chairs the Supervisory Board (since 08/11/2022) | CONFIRMED | [Pappers Group](https://www.pappers.fr/entreprise/ascentry-group-915233837); [Legal notice](https://www.ascentry.com/legal-notice/) |
| INFO PARTNER (partner4lab) | 349 314 948 | Former microbiology/epidemiology publisher, acquired Feb 2020. Still an awardee in 2022 (CHU Dijon) | — | CONFIRMED | [Societe.com](https://www.societe.com/societe/info-partner-349314948.html); [DECP augmenté](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| Ascentry Finland (Finbiosoft Oy) | n/a | Validation Manager; ISO 27001 | — | CONFIRMED (company claim) | [Trust Center](https://www.ascentry.com/trust/) |
| BYG4lab, Inc. (USA) | n/a | US sales | — | CONFIRMED | [About us](https://www.ascentry.com/about-us/) |
| Belgian, Swiss or UK entity | — | None found | KBO, Zefix and Companies House not queried | UNKNOWN | — |

### Financials by year

| Entity | Year | Revenue | Net result | Headcount | Confidence | Source |
|---|---|---|---|---|---|---|
| Ascentry France | 2021 | €9.59M | €2.21M | n/a | CONFIRMED | [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| Ascentry France | 2022 | €10.7M | €2.67M | 79 | CONFIRMED | same |
| Ascentry France | 2023 | €13.5M | €2.42M | 83 | CONFIRMED | same |
| Ascentry France | 2024 | €13.73M | €2.88M | 94 | CONFIRMED | same; [Societe.com](https://www.societe.com/societe/byg-informatique-326649407.html) |
| Ascentry France | 2025 | Filed 23/08/2026, figures not retrieved | — | — | UNKNOWN | [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| Ascentry Group (holding) | 2022 / 2023 / 2024 | €14.4K / €1.66M / €1.9M | €415K / €1.04M / €90.2K | band 10–19 (2023) | CONFIRMED | [Pappers Group](https://www.pappers.fr/entreprise/ascentry-group-915233837) |
| Group consolidated | 2024–2025 | Estimated €15–18M | — | 120 (company claim) | INDICATIVE: French entity plus Finbiosoft plus US, minus intercompany fees. No consolidated accounts found | [About us](https://www.ascentry.com/about-us/) |

Revenue grew **about 43% from 2021 to 2024**, but **2023 to 2024 was nearly flat (+1.7%)**. That sits oddly against the company's "double-digit" growth narrative ([Keensight PR 2022](https://keensight.com/wp-content/uploads/2022/07/PR-BYG4lab-v17.07.2022-FR-KEENSIGHT-ONLY-Final.pdf)). The net margin is about 21%, and the company claims R&D spend of 23% of revenue ([About us](https://www.ascentry.com/about-us/)).

**Headcount.** The company claims 120 employees worldwide, "over 110" at the Finbiosoft deal, and about 40% in R&D in 2022 (CONFIRMED, company claim: [About us](https://www.ascentry.com/about-us/); [Ascentry blog](https://www.ascentry.com/articles/finbiosoft-joins-forces-with-byg4lab/)). An INDICATIVE functional split derived from those figures is 45–50 in R&D, 25–35 in customer experience, 10–15 in sales and partnerships, and 3–6 in regulatory/QA. The team dedicated to Infection Tracker is UNKNOWN; the product manager is Wendy van der Linden, listed as based in Brussels in the SF2H 2025 programme ([SF2H 2025](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf)).

**Leadership** (CONFIRMED, company claim, [Leadership](https://www.ascentry.com/leadership-team/)):

| Person | Role |
|---|---|
| Cyril Verhille | President; leads the Advisory Board |
| Ludovic d'Apréa | CEO since 1 Jul 2026 |
| Stéphane Jamin | Deputy CEO & CFO |
| Teemu Qvick | CTO |
| Akseli Virtanen | CMO (Chief *Marketing* Officer) |
| Alexandre Rousseaux | VP Industrial Partnerships (the IVD-partner contact) |
| Tim Bickley | VP Sales USA |

**No medical, ID or IPC clinical lead was found.**

The CEO change, the IVD-industry Advisory Board and the 2026 entity renames are consistent with preparation for a Keensight exit around 2026–2028 (INDICATIVE, reasoning only; no sale process reported).

---

## 2. Product portfolio overview

Ascentry sells **four products and no LIS**. It positions itself as vendor-neutral middleware alongside third-party LIS ([ascentry.com](https://www.ascentry.com); [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software)).

| Product (current) | Legacy names | What it is | IPC/AMS relevance | Confidence | Source |
|---|---|---|---|---|---|
| **Infection Tracker** | Ynfectio (2023); INFECTIO / INFECTIO.GLOBAL / INFECTIO.LABO / InfectioGlobal V4 (Info Partner); earlier BACTERIO, VIGI@ct, VIGIguard (Info Partner-designed per company) | IPC and AMR epidemiology: alerts, contact tracing, hygiene module, antibiograms, statistics | **Core overlap with LUMED IPC** | CONFIRMED (company claim) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/); [Biologiste365](https://www.biologiste365.fr/biologiste365-fr/actualites-biologiste365-fr/byg4lab-devient-ascentry/) |
| **Lab Composer** | nYna (also written NINA), EVM, Yline platform; Pilot NextGen / pYlot / PILOT.4lab (microbiology middleware, probably folded in) | Vendor-neutral multi-site, multi-LIS middleware: autovalidation expert rules, QC, TAT, MDM/ETL add-ons | Indirect: lab data layer; the anchor account for cross-sell | CONFIRMED (company claim); mapping INDICATIVE | [Lab Composer](https://www.ascentry.com/products/lab-composer/) |
| **POC Controller** | pocY / Ypoc | Cloud POCT management | None | CONFIRMED (company claim) | [POC Controller](https://www.ascentry.com/products/poc-controller/) |
| **Validation Manager** | Finbiosoft Validation Manager | Cloud method verification/validation; 18 countries | None; drives the UK/Nordic/German footprint | CONFIRMED (company claim) | [Validation Manager](https://www.ascentry.com/products/validation-manager/) |
| Qualynk, EVM-IH, B.I byBYG, M.D.M byBYG | — | Method validation, immunohaematology bench, BI, master data | None | CONFIRMED (tender/company) | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024); [SF2H 2023 programme](https://www.sf2h.net/k-stock/data/uploads/2023/05/SF2H_2023ProgrammeCompletCongresLille2023.pdf) |
| "Bylis", "Bymanager", "BYG4Epi" | — | Not found; probably not real product names | — | UNKNOWN (ascentry.com, web, HAL) | — |

---

## 3. AMS / CDSS products: what exists and what was not found

**Ascentry has no AMS CDSS.** Its AMS claims are limited to lab-side epidemiology. Infection Tracker "automates antibiogram generation", detects resistance patterns and gives "timely insights into resistance trends" that support "antibiotic prescriptions and … AMS efforts". Users can schedule reports for ID specialists and **pharmacists**, who appear only as report recipients ([Infection Tracker](https://www.ascentry.com/products/infection-tracker/)). Ynfectio offered "automatic reporting to clinicians and prescribers" ([Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/)).

| AMS capability | Status | Confidence | Where searched / source |
|---|---|---|---|
| Cumulative antibiogram generation | Claimed | CONFIRMED (company claim) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| Resistance-phenotype alerts (BHRe/CPE, MDRO) | Claimed | CONFIRMED (company claim) | same; [Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/) |
| Scheduled reports to ID physicians and pharmacists | Claimed | CONFIRMED (company claim) | [Infection Tracker FAQ](https://www.ascentry.com/products/infection-tracker/) |
| Antibiotic consumption (DDD/DOT), pharmacy/dispensing data ingestion | Not found | UNKNOWN | Product page, FAQ, Trust, About, Biologiste365, Newswise |
| Prescription linkage, restricted-antibiotic workflow, prescribing alerts, IV-to-oral, duration alerts | Not found | UNKNOWN | same |
| Antibiogram rules (CLSI M39 / first isolate per patient; EUCAST/CA-SFM expert rules) | Not stated. Lab Composer's "expert rule engine" is for autovalidation | UNKNOWN | [Lab Composer](https://www.ascentry.com/products/lab-composer/) |
| AMS partnership or AMS outcome study | None found | UNKNOWN | Web, PubMed/Europe PMC, HAL |

The ConsoRes/SPARES reporting claim (legacy snippet) probably covers only the **resistance** part, since consumption data come from pharmacy systems that Infection Tracker does not appear to ingest (INDICATIVE; context: [Répia on ConsoRes](https://www.preventioninfection.fr/actualites/spares-nouvelle-version-de-consores-disponible/)).

---

## 4. IPC products: Infection Tracker in depth

### Lineage from Nancy's Bactério to Infection Tracker

The IPC line started at Nancy. The **BACTERIO** software was taken up by Info Partner in 1996, and Info Partner reportedly became a bioMérieux partner through it (INDICATIVE, snippet of a 503 page: [professeurs-medecine-nancy.fr](http://www.professeurs-medecine-nancy.fr/Informatique_medicale.htm)). BYG4lab's 2021 deck calls Info Partner "Editeur et concepteur des solutions BACTERIO – VIGI@ct – VIGIguard – INFECTIO" ([JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf)). BYG bought Info Partner in February 2020, saying microbiology was "la seule brique logiciel manquante" ([Spectra Diagnostic n°8](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD008_Publi-Byg.pdf)). It rebuilt Infectio on Yline as **Ynfectio**, launched in France in February 2023 ([Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/)), and renamed it **Infection Tracker** in 2025. Ynfectio won the **JIB 2021 Innovation Trophy** in the health-data category ([BYG4lab news](https://byg4lab.com/case-studies/byg4lab-remporte-le-trophee-de-linnovation-en-biologie-medicale-%F0%9F%8F%86/)).

### Functions

| Function | Status | Confidence | Source |
|---|---|---|---|
| Real-time alerts: BHRe/CPE, resistance phenotypes, notifiable diseases (MDO) | Claimed | CONFIRMED (company claim) | [Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/) |
| Alert on **readmission of known MDRO carriers and of their contacts**; contact tracing | Claimed | CONFIRMED (company claim) | [Infection Tracker FAQ](https://www.ascentry.com/products/infection-tracker/) |
| Hygiene module for the IPC team (EOH); patient hygiene file; rounds sheets; HAI (IAS) management | Claimed | CONFIRMED (company claim) | [Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/); [JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf) |
| Outbreak ("bouffées épidémiques") detection with de-duplication | Claimed. Appears rule/alert-based; no statistical method (e.g. SaTScan) stated | CONFIRMED (company claim); method INDICATIVE | same |
| Filters by ward, facility, building; multi-site / GHT consolidation | Claimed | CONFIRMED (company claim) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/); [Spectra SD031](https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf) |
| Configurable surveillance questionnaires and forms; statistics module exporting every field in several formats | Claimed | CONFIRMED (company claim) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| Disciplines: bacteriology, virology, parasitology, mycology (culture/ID, AST, blood cultures, molecular, urine cytology) | Claimed | CONFIRMED (company claim) | same |
| Genomic/WGS typing integration | Not found | UNKNOWN | product page, trade press |

### Data sources

The product is fed by the **LIS**: "all data in the LIS system can be sent to Infection Tracker" ([FAQ](https://www.ascentry.com/products/infection-tracker/)). The legacy INFECTIO.GLOBAL collected LIS data "via a HL7 connection" and could connect to patient-movement software ([partner4lab](https://partner4lab.com/shop/infectio-global/), snippet only). Readmission and ward alerts therefore imply an **ADT/HIS feed**, though no message type is named (INDICATIVE). No pharmacy data feed was found (INDICATIVE).

An independent thesis gives a telling detail about the product's historical limits. At CHRU Nancy (2020), InfectioGlobal was only the **data source**. The IPC team ran BHRe carrier/contact follow-up in an **in-house Microsoft Access database**, and the author flagged manual steps and entry errors ([HAL 03298181](https://hal.univ-lorraine.fr/hal-03298181v1)). Ascentry now claims contact-readmission alerts natively.

### National reporting claims

| Network / export | Claim | Confidence | Source |
|---|---|---|---|
| ConsoRes / SPARES (FR) | Legacy snippet: "automatic reporting for CONSORES/SCIENSANO". One reading of the current page lists SPARES and ConsoRes; two readings do not (see C9) | INDICATIVE (contested) | [byg4lab legacy URL](https://byg4lab.com/en/product-ynfectio/); [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| Sciensano (BE) | Legacy snippet only. Ascentry attended "Sciensano 2026" as an event. No formal feed found | INDICATIVE | same; [News & events](https://www.ascentry.com/news-and-events/) |
| PRIMO (FR) | In one reading of the current page only | INDICATIVE (contested) | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| WHONET | In one reading of the current page only | INDICATIVE (contested) | same |
| EARS-Net | In one reading of the current page only | INDICATIVE (contested) | same |
| ANRESIS / Swissnoso (CH) | Not found | UNKNOWN | web, product page |
| Generic "national surveillance reports", "Gestion des MDO", "extraction automatique" | Advertorials and 2021 deck | CONFIRMED (company claim) | [Spectra SD031](https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf); [JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf) |
| Formal agreement with CPias, Santé publique France, e-SIN | Not found | UNKNOWN | web (EN/FR), product pages, Biologiste365 |

### AI via GeodAIsics

On **26 January 2024** BYG4lab signed with **GeodAIsics**, a Grenoble generative-AI start-up led by Arnaud Attyé, to detect cross-transmission of HAI/MDRO and raise cluster alerts earlier from Ynfectio data ([Ascentry PR](https://www.ascentry.com/event/ascentry-signs-a-partnership-agreement-with-geodaisics/); [Spectra SD031](https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf)). The work reached clinical evaluation in two stages:

- A **sponsored** SF2H 2025 innovation session, "L'Intelligence Artificielle pour la détection des contaminations croisées avec Ynfectio", with speakers from CHU Grenoble Alpes and CHU Rennes ([SF2H 2025](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf)).
- An SF2H 2026 session, "**AI & Infection Tracker: First results at Rennes University Hospital**" (4 June 2026, Dr Guillaume Ménard) ([SF2H 2026](https://www.ascentry.com/event/sf2h-2026/)).

No results have been published, and the product pages make **no AI claim** beyond an "Automated intelligence" heading (CONFIRMED, company claim; results UNKNOWN).

### Installed base (claimed and evidenced)

The company claims "**90+ sites across Europe**", with no country split and no named Infection Tracker customer stories. All 11 customer stories concern Validation Manager ([Customer stories](https://www.ascentry.com/customer-stories/)).

| Site | Evidence | Product | Confidence | Source |
|---|---|---|---|---|
| CHU Caen Normandie (3 GHT sites) | 2024 framework | Ynfectio | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024) |
| CH intercommunal Agglomération de Nevers | 2026 maintenance | Infectio Labo / Ynfectio Labo | CONFIRMED | [DECP 2026S00059](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| CHU Reims | 2025 PharmD thesis: MRSA alert forms sent to the EOH "via InfectioGlobal V4® (BYG4Lab)" | InfectioGlobal V4 | CONFIRMED (independent) | [DUMAS 05322365](https://dumas.ccsd.cnrs.fr/dumas-05322365v1) |
| CHRU Nancy | 2020 thesis: InfectioGlobal used as the BHRe data source | InfectioGlobal | CONFIRMED (independent, 2020) | [HAL 03298181](https://hal.univ-lorraine.fr/hal-03298181v1) |
| CH Abbeville | 2019 thesis: INFECTIO.GLOBAL connected to LIS and patient movements | INFECTIO.GLOBAL | CONFIRMED (independent, 2019) | [DUMAS 02884834](https://dumas.ccsd.cnrs.fr/dumas-02884834v1) |
| Arlon (BE) technical platform | partner4lab user-day snippet | INFECTIO.GLOBAL + PILOT.4lab | CONFIRMED (company claim, legacy) | [partner4lab](https://partner4lab.com/feed-back-journee-pilot4lab/) |
| CHU Rennes | AI pilot site (sponsored sessions 2025–2026) | Ynfectio / Infection Tracker | CONFIRMED (company claim) | [SF2H 2026](https://www.ascentry.com/event/sf2h-2026/) |
| CHU Grenoble Alpes | Speaker at SF2H 2025 AI session; PILOT MALDI customer | Possibly Ynfectio | INDICATIVE | [SF2H 2025](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf) |
| Hôpitaux Paris Saint-Joseph / Marie-Lannelongue | Inlog partnership reference customer; Infection Tracker use not specified | Unknown | INDICATIVE | [Ascentry x Inlog](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |

**Negative check:** do **not** attribute the CHU Limoges IPC-software story to Ascentry, because the vendor is not named ([Hospitalia](https://www.hospitalia.fr/L-hygiene-hospitaliere-prend-de-plain-pied-le-virage-numerique_a3993.html)).

---

## 5. Oncology CDSS and prescription tools

**None found.** No oncology CDSS, chemotherapy prescribing, sepsis alerting, diagnostic-stewardship CDSS or other prescription tool exists in the portfolio. Lab Composer's autovalidation rules and patient moving averages are lab QC features, not clinical CDSS.

This is UNKNOWN / none found. The sources searched were the ascentry.com product pages, About, FAQ, the Newswise launch release, Keensight releases, trade press, PubMed/Europe PMC and HAL ([ascentry.com](https://www.ascentry.com); [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software)).

---

## 6. Integrations, deployment model and technology stack

| Topic | Finding | Confidence | Source |
|---|---|---|---|
| Positioning | Vendor-neutral, multi-LIS, multi-site, multi-instrument; "compatible avec tous les SIL et SIH" | CONFIRMED (company claim) | [Biologiste365 Yline](https://www.biologiste365.fr/a-decouvrir/yline-linnovation-au-service-de-la-digitalisation-des-laboratoires-de-biologie-medicale/); [Spectra SD031](https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf) |
| Standards | HL7 named only for legacy INFECTIO.GLOBAL. The current FAQ names no HL7, FHIR or HPRIM. HPRIM support is likely for French middleware but not evidenced | CONFIRMED (company claim) for HL7 legacy; rest UNKNOWN | [partner4lab](https://partner4lab.com/shop/infectio-global/); [FAQ](https://www.ascentry.com/faq/) |
| Named LIS partners | **Technidata** (TDMind OEM middleware inside the TD LIS; renewed Feb 2026); **Inlog** (Oct 2025, covers Infection Tracker) | CONFIRMED | [Technidata PR](https://www.technidata-web.com/images/PDF/Press/English/202602_PR_Partnership_TECHNIDATA_x_ASCENTRY.pdf); [Inlog PR](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |
| Other LIS in the field | CHU Nancy's microbiology moved to GLIMS (MIPS) in 2015 while Info Partner tools stayed as data sources, so co-existence with Clinisys/GLIMS is historical fact at one site | CONFIRMED (independent, 2015) | [HAL 01734170](https://hal.univ-lorraine.fr/hal-01734170v1) |
| Named EHR/DPI partners (Dedalus, Maincare, Softway, Cerner, Epic, Agfa, Cegedim) | None | UNKNOWN | product pages, FAQ, web |
| IVD partners | QuidelOrtho (2023, extends a France agreement); homepage logos: Stago, Thermo Fisher, Binding Site | CONFIRMED | [QuidelOrtho](https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings); [ascentry.com](https://www.ascentry.com) |
| Deployment of Infection Tracker | Cloud **not stated explicitly** for Infection Tracker. Legacy Ynfectio/nYna likely on-premise | UNKNOWN / INDICATIVE | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) |
| Deployment of other products | Validation Manager and POC Controller are "cloud-based" | CONFIRMED (company claim) | [Validation Manager](https://www.ascentry.com/products/validation-manager/); [POC Controller](https://www.ascentry.com/products/poc-controller/) |
| Hosting / data residency | Corporate website on OVHcloud Roubaix. SaaS hosting provider and EU residency not stated | CONFIRMED (website); UNKNOWN (SaaS) | [Legal notice](https://www.ascentry.com/legal-notice/); [Trust](https://www.ascentry.com/trust/) |
| Tech stack | ASP.NET Core, Angular 14+, Entity Framework, TFS (job-ad summary, no traceable URL); WordPress website | INDICATIVE / CONFIRMED (observed) | [LinkedIn – S. Jamin](https://www.linkedin.com/in/st%C3%A9phane-jamin-39801757/) (not opened); [ascentry.com](https://www.ascentry.com) |
| Languages | 11 languages claimed | CONFIRMED (company claim) | [Keensight 2024](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/) |

---

## 7. Certifications and regulatory status

| Item | Status | Confidence | Source |
|---|---|---|---|
| ISO 13485:2016 | Held by Ascentry France (BYG Informatique SAS) for "design, development and maintenance of medical device software", covering Lab Composer, POC Controller, **Infection Tracker**. Obtained 2014–2016 | CONFIRMED (company claim) | [Trust Center](https://www.ascentry.com/trust/); [About us](https://www.ascentry.com/about-us/) |
| ISO/IEC 27001:2022 | **Validation Manager only** (Ascentry Finland). None stated for Infection Tracker | CONFIRMED (company claim) | [Trust Center](https://www.ascentry.com/trust/) |
| ISO 9001 | Since 2012 | CONFIRMED (company claim) | [About us](https://www.ascentry.com/about-us/) |
| IEC 62304, GDPR, HIPAA | Mentioned in the FAQ | CONFIRMED (company claim) | [FAQ](https://www.ascentry.com/faq/) |
| CE marking; IVDR vs MDR class for Infection Tracker | Not disclosed. Alerting and antibiogram functions could qualify as MDR or IVDR software | UNKNOWN (EUDAMED not queried) / INDICATIVE | [CSDmed / Team-NB](https://www.csdmed.mc/en/news/news/position-paper-team-nb-150) (general context) |
| HDS (French health-data hosting certification) | Not found | UNKNOWN (Trust, FAQ, legal notice searched) | [Trust](https://www.ascentry.com/trust/) |
| FDA, UKCA | Not found | UNKNOWN | — |
| Penetration testing | Claimed "regular" | CONFIRMED (company claim) | [Trust Center](https://www.ascentry.com/trust/) |

---

## 8. Pricing model and commercial packaging

### The model: licence, then single-source 4-year maintenance

There is **no public price list**, and no licence or SaaS terms are published for any product ([ascentry.com](https://www.ascentry.com)). The French public procurement record shows how customers pay. They acquire the software once (licence, installation, connections). They then buy **corrective and evolutive maintenance under multi-year contracts, mostly 48 months**, usually **negotiated without competition or awarded "sans publicité ni mise en concurrence"**, because only the publisher can maintain its own software ([Pappers contract listing](https://www.pappers.fr/entreprise/byg-informatique-326649407); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)).

The price drivers appear to be **per product, per establishment (GHT site) and per analyser connection**. Contracts itemise "maintenance du matériel, du logiciel et de la connexion d'automates", and CHU Caen's scope is "trois établissements du GHT" (INDICATIVE). **No per-bed or per-test pricing was found**, and a SaaS subscription is confirmed only for the Finbiosoft line (Validation Manager, quote-based) ([Finbiosoft](https://finbiosoft.com/validation-manager-features/)).

There are two IPC price points:

| Case | Scope | Value | Per year | Share attributable to IPC |
|---|---|---|---|---|
| **CH Nevers** | Infectio Labo / Ynfectio Labo updates and maintenance, 48 months | €10,314.92 | about €2.6k | All of it (standalone) |
| **CHU Caen** | nYna + Ynfectio + Qualynk + EVM-IH, three GHT sites, 44 months (see C7) | €415,155 | about €113k over 44 months, or about €104k/yr if 4 years | Not broken down |

Assuming maintenance at the usual 15–20% of licence value (a market convention, **not** sourced for Ascentry), the Nevers figure implies a small-hospital Infectio licence in the **low tens of thousands of euros** (INDICATIVE heuristic only).

A third route matters to bioMérieux. **Ascentry costs are sometimes carried inside IVD tenders.** At CHU Caen in 2019, "prise en charge de la solution EVM® de la société BYG Informatique" was a mandatory supplementary item in a Grifols analyser award (€250,000 total) ([TED 583476-2019](https://ted.europa.eu/en/notice/-/detail/583476-2019)). At Avranches-Granville, BYG was bundled in an Ortho Clinical Diagnostics lot ([DECP](https://data.economie.gouv.fr/explore/dataset/decp-v3-marches-valides/)). Belgian MALDI and antibiogram tenders require connection to the buyer's existing BYG4lab middleware (see chapter 11).

### Standalone or bundled? Correcting the "LIS upsell" frame

Ascentry **sells no LIS**. Its only LIS-like tie is TDMind, its middleware shipped inside Technidata's LIS ([Inovallée 2021](https://www.inovallee.com/technidata-tisse-un-partenariat-strategique-avec-byg4lab-pour-repondre-aux-enjeux-futurs-des-laboratoires-medicaux/)). Every Infection Tracker site therefore runs someone else's LIS. The real question is whether Infection Tracker is sold (a) standalone to labs without Ascentry middleware, (b) as a cross-sell into Ascentry middleware accounts, or (c) through LIS partners. The evidence supports all three.

| Evidence | Points to | Confidence | Source |
|---|---|---|---|
| CH Nevers holds a **separate** Infectio Labo maintenance contract naming no middleware | Standalone product line | CONFIRMED (contract) | [DECP 2026S00059](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| partner4lab sold INFECTIO independently of BYG before 2020 (HL7 LIS feed); CH Abbeville and CHRU Nancy used it alongside other LIS | Legacy standalone base | CONFIRMED (company claim + theses) | [partner4lab](https://partner4lab.com/shop/infectio-global/); [DUMAS 02884834](https://dumas.ccsd.cnrs.fr/dumas-02884834v1) |
| CHU Caen buys Ynfectio **in one contract with nYna middleware**, Qualynk and EVM-IH | Bundle / cross-sell into the middleware account | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024) |
| Inlog partnership explicitly covers Infection Tracker with Inlog's LIS | LIS-partner channel | CONFIRMED (company claim) | [Inlog PR](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |
| Technidata TDMind covers middleware; inclusion of Infection Tracker not stated | LIS-partner channel for middleware only | CONFIRMED (middleware); IT inclusion UNKNOWN | [Technidata PR](https://www.technidata-web.com/images/PDF/Press/English/202602_PR_Partnership_TECHNIDATA_x_ASCENTRY.pdf) |
| No tender found with Ynfectio/Infection Tracker as a **first-time competitive lot** | Gap (no competitive standalone win evidenced) | UNKNOWN (TED, DECP; BOAMP/PLACE not queried) | — |
| No UniHA/RESAH/CAIH catalogue listing found. UGAP presence only as a member of an Ortho-led analyser group (2021) | No central-purchasing route for IPC | CONFIRMED (UGAP) / UNKNOWN (others) | [TED 495457-2021](https://ted.europa.eu/en/notice/-/detail/495457-2021) |

**Verdict (INDICATIVE, medium-low confidence).** Infection Tracker is a **technically standalone, LIS-agnostic product that can be bought and maintained on its own**, as Nevers and the legacy partner4lab base show. **Commercially, its growth appears to come from cross-selling into Ascentry middleware accounts** (the Caen GHT bundle) and, since October 2025, from the **Inlog LIS channel**. It is **not** an "LIS upsell", and there is no evidence that it is sold *only* as an add-on.

The following would settle the question:
1. The CCTPs for CHU Caen (ref. 2023132 on PLACE) and Nevers, showing whether Nevers runs Ascentry middleware and giving a per-product price split.
2. A reference-site list for Infection Tracker cross-checked against each site's LIS and middleware vendor.
3. Any BOAMP/PLACE notice for a competitive first acquisition of Ynfectio or Infection Tracker.

---

## 9. Home-market footprint: France

**Occitanie is the home region, but no Occitanie customer was found** (CHU Toulouse, Montpellier, Nîmes and GHT Haute-Garonne were searched in DECP, TED and on the web: UNKNOWN, not proven absent). The IPC line's centre of gravity is **Grand Est (Nancy)**, where Info Partner was based. Independent theses place Info Partner tools at **CHRU Nancy** (since 1995 for Bactério; InfectioGlobal in 2020) and **CHU Reims** (InfectioGlobal V4 in 2025) ([HAL 01734170](https://hal.univ-lorraine.fr/hal-01734170v1); [HAL 03298181](https://hal.univ-lorraine.fr/hal-03298181v1); [DUMAS 05322365](https://dumas.ccsd.cnrs.fr/dumas-05322365v1)). A Biologiste365 feature reportedly says **CHRU Nancy works with LUMED (bioMérieux)** for its project. This is INDICATIVE only: the summary came from a fetch tool, not the full paywalled text ([Biologiste365](https://www.biologiste365.fr/antibiotherapie/)).

| Region | Sites evidenced | Product | Confidence |
|---|---|---|---|
| Occitanie (home) | HQ only; no customer found | — | UNKNOWN |
| Grand Est | CHRU Nancy, CHU Reims; Villers-lès-Nancy site | InfectioGlobal (IPC) | CONFIRMED (independent theses) |
| Normandie | CHU Caen GHT (Ynfectio + middleware); CHU Rouen (bacteriology); CH Avranches-Granville (via Ortho) | IPC + middleware | CONFIRMED |
| Bourgogne-Franche-Comté | CH Nevers (Infectio Labo); CHU Dijon (Info Partner maintenance) | IPC + microbiology | CONFIRMED |
| Hauts-de-France | CH Beauvais (EVM/NINA), CH Lens, CH Abbeville (INFECTIO.GLOBAL, 2019) | Middleware + IPC (legacy) | CONFIRMED |
| Auvergne-Rhône-Alpes | CHU Grenoble (PILOT MALDI), CHU Saint-Étienne (MALDI connections) | Microbiology | CONFIRMED |
| Centre-Val de Loire | CHR Orléans (middleware) | Middleware | CONFIRMED |
| Île-de-France | CH Gonesse (EVM); Hôpitaux Paris Saint-Joseph / Marie-Lannelongue (Inlog reference); Lab Composer User Day, Paris, 27 Nov 2025 | Middleware | CONFIRMED / CONFIRMED (company claim) |
| Bretagne | CHU Rennes (AI pilot); CPias Bretagne 2026 attendance | IPC | CONFIRMED (company claim) |
| National private | Unilabs France chose EVM as its single middleware (2016; current status unknown). Biogroup, Cerballiance, Eurofins, Synlab France, Inovie: UNKNOWN | Middleware | CONFIRMED (company claim, 2016) |

Company scale claims for France: "over 400 technical platforms … in France use EVM" (older profile) ([French Healthcare](https://frenchhealthcare.fr/membres/byg4lab/)); "4,500+ labs worldwide" ([About us](https://www.ascentry.com/about-us/)). The middleware reach is large. The IPC reach (90+ sites Europe-wide) is an order of magnitude smaller (INDICATIVE).

---

## 10. Europe footprint

Verification of the user's statement: **France is CONFIRMED. Belgium is CONFIRMED** (official tenders plus a legacy IPC site). **Switzerland is NOT verified** beyond a pre-2020 partner4lab claim.

| Country | Status | Evidence | IPC product present? | Confidence | Source |
|---|---|---|---|---|---|
| **France** | Active contracts; HQ | 12 direct public contracts (chapter 12); partners Technidata and Inlog | **Yes** (Caen, Nevers, Reims, Nancy, Abbeville) | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| **Belgium** | Installed base, no direct contract found | Tenders naming BYG4lab middleware: CHR Sambre & Meuse (Pilot.Maldi, 2022), Clinique Saint-Pierre Ottignies (2023), HUmani Charleroi (AST, 2024–2025), AHSM (AST, 2025). Arlon INFECTIO.GLOBAL site (legacy). IPC events: BICS/ABIHH/WIN, Sciensano 2026. Product manager listed in Brussels. EuroMedLab 2025 exhibitor | **Yes, legacy** (Arlon); current use unverified | CONFIRMED (tenders, events); CONFIRMED (company claim, Arlon) | [TED 346413-2022](https://ted.europa.eu/en/notice/-/detail/346413-2022); [TED 451036-2023](https://ted.europa.eu/en/notice/-/detail/451036-2023); [TED 180670-2024](https://ted.europa.eu/en/notice/-/detail/180670-2024); [partner4lab Arlon](https://partner4lab.com/feed-back-journee-pilot4lab/); [BICS event](https://www.ascentry.com/event/bics-abihh-win-joint-symposium-2026/) |
| **Switzerland** | Legacy claim only | partner4lab: "equipped … labs in France, Belgium, Luxembourg, Switzerland, Great-Britain". HUG "VigiGerme" is **not** linked; do not count it | Unknown | CONFIRMED (company claim, legacy); rest UNKNOWN (simap.ch, Zefix not queried) | [partner4lab Company](https://partner4lab.com/en/company/) |
| **Italy** | Historical plus event | VIGI@ct (bioMérieux-branded) at Tor Vergata, Rome (2007–2008); VIGIguard at Gemelli (2014) and Senigallia (2020, de-duplication). AMCLI 2026 Rimini attendance. No current contract found | Legacy (bioMérieux-branded) | CONFIRMED (papers, historical); ANAC not queried | [PubMed 17544166](https://pubmed.ncbi.nlm.nih.gov/17544166); [BMC ID 2008](https://doi.org/10.1186/1471-2334-8-79); [BMC ID 2014](https://doi.org/10.1186/s12879-014-0634-9) |
| **Spain** | Selling / events only | JNI/SEIMC 2026, Bilbao (event page titled "Infection Surveillance Software") | Marketing only | CONFIRMED (company claim, event); contracts UNKNOWN (PLACSP not queried) | [JNI 2026](https://www.ascentry.com/event/jni-2026-infection-surveillance-ascentry/) |
| **UK** | Active customers (Validation Manager) | Airedale, Bedfordshire, NHS Lothian, UHB, Dumfries & Galloway, Salford, PEH Guernsey. partner4lab legacy GB claim | No IPC evidence | CONFIRMED (company claim); FTS/CF not queried | [Customer stories](https://www.ascentry.com/customer-stories/) |
| Luxembourg | Legacy claim | partner4lab | Unknown | CONFIRMED (company claim, legacy) | [partner4lab Company](https://partner4lab.com/en/company/) |
| Portugal | Historical | Hospital da Luz Lisbon planned VIGIguard (bioMérieux), 2010 abstract | Legacy | CONFIRMED (abstract) | [Crit Care 2010](https://doi.org/10.1186/cc9154) |
| Germany | Customers (Validation Manager) | Labor Dr. Heidrich, Uniklinik Ulm, Labor Mönchengladbach; UKE Hamburg papers | No | CONFIRMED (company claim) | [Customer stories](https://www.ascentry.com/customer-stories/) |
| Ireland | Customer | Cork University Hospital (Validation Manager) | No | CONFIRMED (company claim) | same |
| Finland / Nordics / Estonia | Legal entity (Finland) plus customers | HUSLAB, Sørlandet, Linköping, Tartu, Finnish Red Cross; NCCB 2026 Aarhus | No | CONFIRMED | same; [News & events](https://www.ascentry.com/news-and-events/) |
| Netherlands | None found | — | — | UNKNOWN | — |

Belgium is the country where the IPC overlap matters most outside France. It has an inherited Walloon installed base (INDICATIVE, given Info Partner's location near the border), a legacy Sciensano reporting claim, a Brussels-based product manager, and 2026 attendance at both the Belgian IPC societies' symposium and Sciensano.

---

## 11. Rest-of-world footprint

| Country / region | Active contracts | Selling without known contract | Research presence | Legal presence | Confidence | Source |
|---|---|---|---|---|---|---|
| USA | None named | Yes (VP Sales US, ADLM 2025, ASCP, Executive War College 2026) | — | BYG4lab, Inc. | CONFIRMED | [ADLM exhibitor](https://adlm25.myexpoonline.com/co/byg4lab-inc); [News & events](https://www.ascentry.com/news-and-events/) |
| Global via QuidelOrtho | OEM/software development partnership (2023) | Yes | — | — | CONFIRMED | [QuidelOrtho](https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings) |
| UAE / Middle East | None | WHX Labs Dubai 2026 | — | — | CONFIRMED (company claim, event) | [News & events](https://www.ascentry.com/news-and-events/) |
| Morocco | None found | — | EVM middleware used in two Moroccan papers (2023, 2024) | — | CONFIRMED (papers) | [J Med Biochem](https://doi.org/10.5937/jomb0-48306); [Adv Virol](https://doi.org/10.1155/2023/9313666) |
| Maghreb (other), francophone Africa, APAC, LatAm, DOM-TOM | None | None | None | None | UNKNOWN (web search only) | — |

---

## 12. Commercial contracts

Direct contracts use awardee SIRET 326 649 407 00052 (BYG INFORMATIQUE) unless noted. Values are as published.

| # | Customer | Country | Product | Notified / duration | Value | Procurement route | Notice ID | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | CHU Caen Normandie (3 GHT sites) | FR | nYna, **Ynfectio**, Qualynk, EVM-IH maintenance | 17/04/2024 (conclusion); modified 17/12/2025; 44 months (DECP) / "4 yrs" (Pappers) | €415,155 | Negotiated without prior call; framework without reopening | TED 348571-2024; DECP 20240033001000 | CONFIRMED |
| 2 | CH intercommunal Agglomération de Nevers (SIRET 20001120300011, verified in registry) | FR | **Infectio Labo / Ynfectio Labo** update and maintenance | 02/02/2026; 48 months | €10,314.92 | Without publicity or competition; 1 offer | DECP 2026S00059 | CONFIRMED |
| 3 | CH Beauvais | FR | EVM + NINA hardware, software, analyser connections | 28/01/2025; 48 months | €43,104 | Without publicity or competition | DECP 2025y7rcyXHbgj00 | CONFIRMED |
| 4 | CH Beauvais | FR | EVM maintenance | 30/12/2019; 48 months | €7,937 | Without publicity or competition | DECP 2019cty4HwOQH500 | CONFIRMED |
| 5 | CH Lens (Dr Schaffner) | FR | "Maintenance BYG4LAB" | 21/11/2024; 12 months | €2,639.99 | Without publicity or competition | DECP 2402 | CONFIRMED |
| 6 | CHU Grenoble Alpes | FR | PILOT MALDI flat-rate maintenance | 26/04/2023; 48 months | €0 (as published; probable data error) | MAPA | DECP 20232023S0768100 | CONFIRMED |
| 7 | CHR/CHU Orléans | FR | BYG middleware maintenance (contract 238-457) | 13/04/2023; 2 years | €21,000 | Not stated | Pappers listing | CONFIRMED |
| 8 | CHR Orléans | FR | BYG-INFORMATIQUE middleware maintenance | 22/02/2019; 48 months | €40,965.80 | Negotiated with prior competition | DECP 20192019S0601500 | CONFIRMED |
| 9 | CHU Rouen | FR | Bacteriology "identification" module + analyser connections | 06/04/2023; 48 months | €40,028.60 | Not stated | DECP 20232023S1951900 | CONFIRMED |
| 10 | CHU Saint-Étienne | FR | BYG4LAB hardware/software/connections for Bruker MALDI | 06/02/2023; 48 months | €9,120 | Not stated | DECP 20232023S0565500 | CONFIRMED |
| 11 | CH Gonesse (via CH Saint-Denis) | FR | EVM software, hardware, connections | 02/01/2023; 48 months | €12,334 | Not stated | DECP 20232022S2329000 | CONFIRMED |
| 12 | CHU Dijon Bourgogne (awardee **Info Partner**) | FR | BYG4LAB software and connections | 04/05/2022; 48 months | €19,386 | Not stated | DECP 20222022S1506200 | CONFIRMED |
| 13 | CH Avranches-Granville (awardee **Ortho Clinical Diagnostics**) | FR | Ortho Vision + "BYG" | 16/12/2019; 48 months | €36,824 (lot) | Open tender, lot 5 | DECP 2019k9B9ar2dta00 | CONFIRMED (OEM route) |
| 14 | CHU Caen / GHT Normandie Centre (awardee **Grifols**) | FR | EVM support as mandatory supplementary item in an analyser tender | 2019 | €250,000 (whole award) | Open | TED 583476-2019 | CONFIRMED (XML reading) |
| 15 | UGAP framework 17U032 (group led by Ortho-Clinical Diagnostics; BYG INFORMATIQUE a member) | FR | Lab analysers, lot "biochimie immunologie chimie sèche" | 2021; up to 12 years | Framework €282.09M total; lot about €7.5M (INDICATIVE parse) | Open, national central purchasing | TED 495457-2021 / 577496-2021 | CONFIRMED (XML) |
| 16 | CHR Sambre & Meuse (buyer requirement) | BE | MALDI-TOF with connection to Pilot.Maldi (BYG4lab) | 2022 | n/a to Ascentry | Open | TED 346413-2022 | CONFIRMED |
| 17 | Clinique Saint-Pierre Ottignies (buyer requirement) | BE | MALDI-TOF with "connexion au middleware BYG4lab" | 2023 | n/a to Ascentry | Open | TED 451036-2023 | CONFIRMED |
| 18 | HUmani Charleroi (buyer requirement) | BE | Antibiogram systems 2024–2032, "raccordement à la connexion Byg4lab existante"; **awarded to bioMérieux Benelux** | 2024 / award 2025 | €895,143.27 (bioMérieux award, not Ascentry revenue) | Open | TED 180670-2024; TED 423892-2025 | CONFIRMED |
| 19 | AHSM (buyer requirement) | BE | AST systems (TED "BYG4lab" full-text hit) | 2025 | n/a | Not extracted | Not recorded in notes | CONFIRMED (hit); details UNKNOWN |

**Totals (recomputed from the rows).**

- **Direct contracts, rows 1–6 and 8–12** (as used in the home-market note): 415,155 + 43,104 + 7,937 + 40,966 + 40,029 + 19,386 + 12,334 + 10,315 + 9,120 + 2,640 + 0 = **€600,986**.
- **Adding row 7** (Orléans 2023, €21,000, from the Pappers listing only): **€621,986**.
- **IPC-specific identified spend:** €10,315 (CH Nevers) plus an undisclosed share of Caen's €415,155.
- **Excluded:** rows 13–19. These are IVD-vendor or buyer-requirement contracts, not Ascentry revenue.

The totals are a **floor**: DECP is incomplete (many below-threshold maintenance awards are unpublished), and BOAMP/PLACE were not queried. TED full-text hits were "Ascentry" 0, "BYG4lab" 7, "BYG Informatique" 5 and "Ynfectio" 1, all French or Belgian ([TED API](https://api.ted.europa.eu/v3/notices/search)).

---

## 13. France: legacy Infectio sites, contract renewals and LUMED ZINC opportunities

**NEW (research date 29/09/2026).** This chapter answers one question: which French hospitals still run the legacy INFECTIO product line, when do their Ascentry contracts end, and how could they buy a replacement. It uses a fresh search of the French and EU public procurement data plus internal intelligence supplied by the user. Section 13.7 (added the same day) widens the view to Ascentry's whole French middleware base as the likely cross-sell pool for Infection Tracker.

### 13.1 What we know about the June 2027 end of maintenance

| Item | Status | Confidence | Source |
|---|---|---|---|
| Legacy INFECTIO (INFECTIO.LABO / INFECTIO.GLOBAL, from Info Partner / partner4lab) stops being maintained from **June 2027** | Supplied by the user | CONFIRMED (user-provided internal intelligence) | Internal |
| Public confirmation of that date by Ascentry | Not found. Searched ascentry.com (old byg4lab.com URLs now redirect there), Spectra Diagnostic issues 8, 12, 25, 37 and 40, and the web. partner4lab.com and web.archive.org could not be read | UNKNOWN | [Spectra Diagnostic no. 37](https://spectradiagnostic.com/wp-content/uploads/2025/03/SD037_WEB.pdf); [Spectra Diagnostic no. 40](https://spectradiagnostic.com/wp-content/uploads/2025/10/SD040_WEB.pdf) |
| Replacement product Ascentry offers | Ynfectio, now Ascentry Infection Tracker, a rewrite of INFECTIO on the Yline platform "that inherits the experience gained with many laboratories and hospitals" | CONFIRMED (company claim) | [Spectra Diagnostic no. 12, BYG4lab advertorial](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD012_Publi-Byg4lab.pdf) |
| Product names customers may still use | INFECTIO.LABO (connected to the lab analysers) and INFECTIO.GLOBAL (fed from the LIS over HL7); the Reims thesis cites "InfectioGlobal V4" | CONFIRMED (company claim; independent for Reims) | [partner4lab INFECTIO.LABO page, search snippet only](https://partner4lab.com/fr/shop/infectio-labo/); [Reims thesis 2025](https://dumas.ccsd.cnrs.fr/dumas-05322365v1) |

**Why this matters (ANALYST OPINION).** An end of maintenance forces every legacy site to choose before mid-2027. It can migrate to Infection Tracker, usually as a negotiated, single-source change with Ascentry. It can go out to tender for an IPC surveillance tool. Or it can use a national purchasing framework. Chapter 8 showed that Ascentry renews almost always without competition. The legacy sites are therefore the one point where the buying decision is genuinely open.

### 13.2 Why public data under-reports the Infectio base

- **Most Infectio contracts are too small to be published.** French hospitals must publish essential contract data (DECP) only above a threshold, so small maintenance contracts like Infectio's usually never appear. The CH Nevers Infectio contract (€10,315 over 4 years) is visible only because it was published voluntarily. CONFIRMED (inference from the rule plus the observed data).
- **Only two French public contracts name the epidemiology product.** CHU Caen names Ynfectio and CH Nevers names Infectio Labo / Ynfectio Labo. Searching DECP, BOAMP and TED for "Infectio", "InfectioGlobal", "Info Partner", "partner4lab", "Ascentry" and "Infection Tracker" found nothing else in France. CONFIRMED ([DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/); [BOAMP open data](https://boamp-datadila.opendatasoft.com/explore/dataset/boamp/); [TED](https://ted.europa.eu/)).
- **The installed base is better evidenced by theses and internal intelligence than by tenders.** Three independent theses name Infectio sites: Reims (2025), Nancy (2020) and Abbeville (2019).

### 13.3 Legacy Infectio / Info Partner sites in France and their renewal windows

End dates are computed as notification date plus stated duration. They are **INDICATIVE**, because the real start date can differ from the notification date.

| # | Site (GHT) | Evidence of legacy INFECTIO or Info Partner software | Current Ascentry contract found | Indicative contract end | Other context | Confidence | Source |
|---|---|---|---|---|---|---|---|
| 1 | **GHT Coeur Grand Est** (support hospital CH Verdun Saint-Mihiel; labs pooled in GCS Biologie Médicale Triangle et Der) | Current Infectio customer | None visible in DECP, BOAMP or TED; probably below the publication threshold | Driven by the June 2027 end of maintenance | GHT-wide hygiene team; the GHT buys lab supplies jointly for GHT + GCS; bacteriology lab at Verdun refurbished in 2019–2020 | CONFIRMED (user-provided internal intelligence) for Infectio; CONFIRMED for context | Internal; [GHT lab GCS](https://ght-coeurgrandest.fr/gcs-laboratoire/); [GHT hygiene team](https://ght-coeurgrandest.fr/specialites/hygiene-hospitaliere/); [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 2 | **CHU Grenoble Alpes** | Current Infectio customer; also runs the legacy PILOT MALDI microbiology middleware | PILOT MALDI flat-rate maintenance, BYG INFORMATIQUE, MAPA, DECP 20232023S0768100 | **25/04/2027** | CHU Grenoble speaker at Ascentry's sponsored SF2H 2025 session "AI for detecting cross-contamination with Ynfectio"; Ascentry's AI partner GeodAIsics is a Grenoble start-up | CONFIRMED (user-provided internal intelligence) for Infectio; CONFIRMED for contract and SF2H | Internal; [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/); [SF2H 2025 abstract book](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf) |
| 3 | **CHU Reims** (GHU Champagne) | Infection-control team receives MRSA alert forms "via the epidemiology software InfectioGlobal V4 (BYG4Lab)" | None visible | Driven by the June 2027 end of maintenance | LIS is INLOG "Labo Serveur" (GHU Champagne maintenance contract, 01/10/2019, 39 months, €233,859). Inlog signed an Ascentry partnership covering Infection Tracker in October 2025 | CONFIRMED (independent thesis, 2025) | [Reims thesis 2025](https://dumas.ccsd.cnrs.fr/dumas-05322365v1); [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/); [Ascentry x Inlog](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |
| 4 | **CHRU Nancy** (GHT Sud Lorraine) | InfectioGlobal fed a daily lab-result import into an in-house database for highly-resistant-bacteria carriers and contacts (2020) | None visible | Not applicable | **Existing LUMED customer: LUMED APSS and ZINC in use since 2021.** GHT Sud Lorraine also signed a follow-on contract under RESAH lot 1 with bioMérieux on 18/12/2024 (see 13.4). Whether InfectioGlobal still runs alongside LUMED is unknown | CONFIRMED (independent, 2020) for InfectioGlobal; CONFIRMED (user-provided internal intelligence) for LUMED | [Nancy thesis 2020](https://hal.univ-lorraine.fr/hal-03298181v1); [DECP 2024F13529](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 5 | **CH Abbeville** | Infectio.Global (partner4lab) linked to the LIS and patient movements | None visible | Unknown | — | CONFIRMED (independent, 2019 state); current state UNKNOWN | [Abbeville thesis 2019](https://dumas.ccsd.cnrs.fr/dumas-02884834v1) |
| 6 | **CH Nevers** (CHI Agglomération de Nevers) | "INFECTIO LABO / YNFECTIOLABO" update and maintenance | DECP 2026S00059, €10,314.92, 48 months, no publicity or competition | **01/02/2030** | The joint name suggests the Ynfectio migration is already in this contract (INDICATIVE). Near-term opening is unlikely | CONFIRMED (contract) | [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 7 | **CHU Dijon** | Awardee is Info Partner itself (the INFECTIO publisher); object "software and connections by BYG4LAB"; products not named | DECP 20222022S1506200, €19,386, 48 months | **03/05/2026 (already passed)** | No renewal found in DECP by 29/09/2026. It may be unpublished, below threshold or still in progress | CONFIRMED (contract); Infectio use UNKNOWN | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 8 | **CHU Caen** (GHT Normandie Centre, 3 sites) | Already migrated to Ynfectio | TED 348571-2024, €415,155 bundle, 44 months | **17/12/2027** | Inside the same GHT, CH Aunay-Bayeux bought an automated antibiogram reader with bacteriology middleware and epidemiology software from **i2a** (DECP 2555665, 11/09/2024, 48 months, €78,673) | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/); [registry: I2A](https://recherche-entreprises.api.gouv.fr/search?q=347717118) |
| 9 | CHU Rouen / CHU Saint-Étienne | Legacy partner4lab microbiology middleware (bacteriology identification module; MALDI connections). No evidence of Infectio | Rouen €40,028.60; Saint-Étienne €9,120; both 48 months | Rouen **05/04/2027**; Saint-Étienne **05/02/2027** | Adjacent: Ascentry will use these renewals to cross-sell Infection Tracker (INDICATIVE) | CONFIRMED (contracts); Infectio UNKNOWN | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |

Outside France, Belgium has one named legacy INFECTIO.GLOBAL site, a lab platform in Arlon (chapter 10).

### 13.4 Purchasing routes a legacy site could use

| Route | What it covers | Holder | Term | Implication | Confidence | Source |
|---|---|---|---|---|---|---|
| **RESAH "innovative solutions against antimicrobial resistance" framework**: lot 8 (BMR/BHRe surveillance and alert software), lot 9 (antibiotherapy monitoring from patient-record and lab data), lot 10 (antibiotic consumption and resistance surveillance software) | IPC and AMS software, bought without a local tender | **NOSOTECH EUROPE (Nosokos)** on all three lots; 4, 3 and 3 offers received | Notified 29/05/2024; 48 months (to about 28/05/2028) | The direct competitor route for any Infectio site that wants a quick switch. **Ascentry is not a framework holder** | CONFIRMED | [TED 489752-2024](https://ted.europa.eu/en/notice/-/detail/489752-2024); [DECP 2024F04547 / 2024F04548](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/); [registry: Nosotech](https://recherche-entreprises.api.gouv.fr/search?q=828570606) |
| **RESAH lot 1 (relaunched)**: global microbiology solution "and software (surveillance and alert of infections, antibiotic consumption and antibiotherapy monitoring)" | Instruments plus IPC/AMS software, bought through follow-on contracts | **bioMérieux SA** | Framework notified 18/10/2024, 48 months (to about 17/10/2028) | Follow-on contracts since: GHT Sud Lorraine (Nancy), Val-d'Oise, CH Rodez, CH Nîmes / Alès / Louis Pasteur, GH Sud Île-de-France, CHU Poitiers, Var. Values are not reproduced here because they are bioMérieux's own awards | CONFIRMED | [TED 450483-2024](https://ted.europa.eu/en/notice/-/detail/450483-2024); [TED 81198-2025](https://ted.europa.eu/en/notice/-/detail/81198-2025); [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/); [registry: RESAH](https://recherche-entreprises.api.gouv.fr/search?q=130005010) |
| **Negotiated migration with Ascentry** (Infectio to Infection Tracker) | Upgrade under a maintenance or evolution contract | Ascentry | Typically 4 years, no competition (chapter 8) | The default path unless the site's IPC team or pharmacy asks for more than lab-side alerting | CONFIRMED (pattern); INDICATIVE (applied to 2027) | Chapter 8 |
| **Through the LIS vendor** | Infection Tracker bundled via the Inlog partnership | Inlog + Ascentry | Since October 2025 | Relevant where the LIS is Inlog, as at CHU Reims | CONFIRMED (partnership); INDICATIVE (applied to Reims) | [Ascentry x Inlog](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |

**Other IPC incumbents visible in the data.** CHU Limoges runs Nosokos: acquired 20/10/2020 for €209,305 over 48 months, then a support subscription from 01/12/2025 for €93,044 over 36 months. CONFIRMED ([DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)).

### 13.5 Prioritised ZINC opportunity list (ANALYST OPINION)

| Priority | Site | Why | Timing | Main risk | Confidence |
|---|---|---|---|---|---|
| 1 | GHT Coeur Grand Est | Confirmed current Infectio user; GHT-wide IPC team and pooled lab make a GHT-level deal possible | Decision needed before June 2027 | Low-cost negotiated migration to Infection Tracker; Nosokos via RESAH lots 8–10 | CONFIRMED (user-provided internal intelligence) + INDICATIVE |
| 1 | CHU Grenoble Alpes | Confirmed current Infectio user; Ascentry's microbiology middleware contract also ends 25/04/2027 | Two Ascentry renewals fall together in April–June 2027 | **High:** Ascentry is already showcasing Ynfectio + AI with CHU Grenoble staff and a Grenoble AI partner (GeodAIsics); it can offer a combined middleware + Infection Tracker renewal | CONFIRMED + INDICATIVE |
| 2 | CHU Reims | Independent 2025 evidence of InfectioGlobal V4 in daily IPC use | Before June 2027 | Inlog (Reims' LIS vendor) now resells Infection Tracker | CONFIRMED + INDICATIVE |
| 2 | CHU Dijon | Info Partner maintenance contract ended 03/05/2026 with no published renewal | Now | Infectio use is not proven; contact needed | INDICATIVE |
| 3 | CH Abbeville | Legacy Infectio.Global (2019) | Before June 2027 if still in use | Evidence is 7 years old | INDICATIVE |
| Reference | CHRU Nancy / GHT Sud Lorraine | **Existing LUMED APSS + ZINC site since 2021**, and the historic home of INFECTIO. It is the natural reference for every legacy-Infectio prospect and for extending ZINC across GHT Sud Lorraine | Now | Any residual InfectioGlobal use at Nancy or other GHT sites could be targeted by Ascentry's migration offer | CONFIRMED (user-provided internal intelligence) |
| 4 | CHU Caen GHT; CH Nevers | Already on Ynfectio or with a migration contract | Caen December 2027; Nevers February 2030 | Locked in; Caen also has i2a epidemiology software at Aunay-Bayeux | CONFIRMED |

### 13.6 bioMérieux to confirm internally

- Whether ZINC, LUMED or both are the software delivered under RESAH lot 1, and whether a legacy Infectio site can join through a follow-on contract.
- Whether a legacy INFECTIO site can move to ZINC before June 2027 without a new tender (RESAH follow-on contract, below-threshold procedure, or innovation route).
- Which data feeds ZINC needs that INFECTIO sites already have (LIS HL7 feed, patient movements). This matters for the migration argument.
- Whether InfectioGlobal has been switched off at CHRU Nancy since LUMED APSS and ZINC went live in 2021. This matters for the reference story, and for any other GHT Sud Lorraine site still on Infectio.
- Account status at GHT Coeur Grand Est and CHU Grenoble: who owns the Infectio budget (lab or IPC team) and when the Ascentry migration quote is expected.
- Whether any VIGI@ct or VIGIguard sites sold under the bioMérieux name (chapter 15) overlap with this list.

### 13.7 Ascentry middleware installed base in France: Infection Tracker cross-sell targets and renewal dates

**NEW (research date 29/09/2026).** Ascentry sells no LIS. Its French base is lab middleware:

- EVM, now nYna / Lab Composer, for core-lab data management
- EVM-IH for immuno-haematology
- PILOT / PILOT MALDI for microbiology, inherited from partner4lab
- Ypoc / POC Controller for point-of-care testing

Each middleware site is a natural target for an Infection Tracker upsell. CHU Caen shows the pattern: Ynfectio sits in the same maintenance contract as the middleware (chapter 8). Ascentry claims **"more than 400 private or hospital technical platforms in France"** on EVM, and says nYna and pocY are "in routine use within major French biology structures, public and private". CONFIRMED (company claim) ([Spectra Diagnostic no. 12, BYG4lab advertorial](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD012_Publi-Byg4lab.pdf)). Public sources name only about 20 of those sites, and they are listed below.

**How this list was built.** Sources were:

- DECP, BOAMP and TED searched for the supplier IDs and for every product name: EVM, EVM-IH, nYna/NINA, B-Link, PILOT/pYlot, Qualynk, Lab Composer, Validation Manager, Ypoc/pocY, Infectio/Ynfectio.
- Analyser tenders that name BYG middleware as a connection requirement.
- Hospital lab quality manuals, which list the lab's middleware.
- Legacy BYG4lab and partner4lab communications.

#### A. Public-sector sites with an Ascentry / BYG / Info Partner contract or tender requirement

End dates are notification date plus stated duration: **INDICATIVE**. Rows are sorted by indicative end date.

| # | Site | Ascentry product(s) | Contract evidence | Indicative end / renewal window | IPC product known at site | Confidence | Source |
|---|---|---|---|---|---|---|---|
| 1 | CHR Orléans | BYG middleware | 22/02/2019, 48 months, €40,965.80 (negotiated with competition); then 13/04/2023, 2 years, €21,000 (Pappers listing) | About 12/04/2025, **passed**; no newer notice found | None known | CONFIRMED (2019); company-registry listing for 2023 | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/); [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) |
| 2 | CH Lens | "Maintenance BYG4LAB" for the hospital labs | 21/11/2024, 12 months, €2,639.99, no competition | About 20/11/2025, **passed**; annual renewals are probably below the publication threshold | None known | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 3 | CHU Dijon | Info Partner software and connections | 04/05/2022, 48 months, €19,386 | About 03/05/2026, **passed**; no renewal found | Possibly Infectio (13.3) | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 4 | CH Gonesse (via CH Saint-Denis) | EVM, hardware and analyser connections | 02/01/2023, 48 months, €12,334 | **01/01/2027** | None known | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 5 | CHU Saint-Étienne | BYG4LAB connections for Bruker MALDI | 06/02/2023, 48 months, €9,120 | **05/02/2027** | None known | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 6 | CHU Rouen | Bacteriology identification module + analyser connections (partner4lab line) | 06/04/2023, 48 months, €40,028.60 | **05/04/2027** | None known | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 7 | CHU Grenoble Alpes | PILOT MALDI | 26/04/2023, 48 months, MAPA | **25/04/2027** | **Infectio** (internal intelligence) | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/) |
| 8 | CHU Caen (GHT Normandie Centre, 3 sites) | nYna, Ynfectio, Qualynk, EVM-IH | 18/04/2024, 44 months, €415,155 | **17/12/2027** | **Ynfectio** | CONFIRMED | [TED 348571-2024](https://ted.europa.eu/en/notice/-/detail/348571-2024) |
| 9 | CH Beauvais | EVM + "NINA" (probably nYna), hardware and connections | 28/01/2025, 48 months, €43,104, no competition | **27/01/2029** | None known | CONFIRMED (contract); "NINA = nYna" INDICATIVE | [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 10 | CH Nevers | Infectio Labo / Ynfectio Labo | 02/02/2026, 48 months, €10,314.92 | **01/02/2030** | **Infectio → Ynfectio** | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/) |
| 11 | CH Avranches-Granville | BYG with Ortho Vision (immuno-haematology), inside Ortho's maintenance lot | 16/12/2019, 48 months, lot 5 €36,824 (awardee Ortho-Clinical Diagnostics); lot relaunched in October 2023 as "Orthovision et BYG … I2A" | First contract ended about 15/12/2023; 2023 relaunch winner not found | None known | CONFIRMED | [DECP](https://data.economie.gouv.fr/explore/dataset/decp_augmente/); [BOAMP 23-142021](https://www.boamp.fr/pages/avis/?q=idweb:23-142021) |
| 12 | CHU Caen / GHT Normandie Centre | EVM support, as a mandatory supplementary item in the Grifols Erytra (immuno-haematology) tender | 2019 | Historical | (see row 8) | CONFIRMED | [BOAMP 19-146017](https://www.boamp.fr/pages/avis/?q=idweb:19-146017); [TED 583476-2019](https://ted.europa.eu/en/notice/-/detail/583476-2019) |
| 13 | CH Sud Essonne Dourdan-Étampes | EVM (BYG), required to connect the immuno-haematology analyser to the Glims LIS | 2016 tender | Historical; current status UNKNOWN | None known | CONFIRMED (2016 state) | [BOAMP 16-28267](https://www.boamp.fr/pages/avis/?q=idweb:16-28267) |
| 14 | CH Centre Bretagne (Pontivy) | BYG middleware support and a BYG client workstation at the immuno-haematology bench | 2015 tender | Historical; current status UNKNOWN | None known | CONFIRMED (2015 state) | [BOAMP 15-168566](https://www.boamp.fr/pages/avis/?q=idweb:15-168566) |
| 15 | UGAP national lab-analyser framework | BYG INFORMATIQUE a member of the Ortho-Clinical-led winning group | 2021, up to 12 years | Open to any UGAP customer buying through that lot | n/a | CONFIRMED | [BOAMP 21-100129](https://www.boamp.fr/pages/avis/?q=idweb:21-100129); [TED 495457-2021](https://ted.europa.eu/en/notice/-/detail/495457-2021) |

#### B. Sites identified from lab documents and company communications (no public contract found)

| # | Site / group | Evidence | Date of evidence | Why it matters for ZINC | Confidence | Source |
|---|---|---|---|---|---|---|
| 1 | **CH Cannes Simone Veil** | Lab systems: LIS **Inlog** (Haemonetics); "concentrator systems: MPL (Roche) and **Nyna (bYg)**"; patient record DxCare | Quality manual v8, approved 02/09/2025 | Inlog LIS plus Ascentry middleware is the profile the October 2025 Inlog–Ascentry partnership targets for Infection Tracker | CONFIRMED (hospital document) | [CH Cannes quality manual](https://ch-cannes.manuelprelevement.fr/DocumentNew.aspx?idDoc=30291) |
| 2 | CH Mâcon | PILOT.MALDI installed with Bruker MALDI Biotyper sirius (July–August 2021; routine from October 2021) | 2021–2022 | Microbiology middleware site; Infection Tracker cross-sell candidate | CONFIRMED (company claim) | [BYG4lab user case, Mâcon](https://byg4lab.com/en/case-studies/user-case-macon-hospital-center/) |
| 3 | CH Brive | Analyser interfaces "MPL, Biolink, **Byg**, SIR"; Inlog server | Quality manual dated 29/01/2013 | Old evidence; current use UNKNOWN | CONFIRMED (2013 state) | [CH Brive quality manual 2013](https://ch-brive.manuelprelevement.fr/Docs/lbm-chdebrive/DefaultDocs/DocN4.pdf) |
| 4 | **Unilabs France** (about 100 sites, 1,300 staff in 2016) | EVM chosen as the single middleware for the network | June 2016 | Private-lab network; current status UNKNOWN | CONFIRMED (company claim, 2016) | [BYG4lab: Unilabs partnership](https://byg4lab.com/case-studies/partenariat-unilabs-france/) |
| 5 | Biosèvres (private lab) | Samples packed with "the BYG packaging software" | Procedure v10, applicable 18/07/2025 | Private lab using an Ascentry module | CONFIRMED (lab document) | [Biosèvres procedure](https://biosevres.manuelprelevement.fr/DocumentNew.aspx?idDoc=282) |
| 6 | GCS Charente-Maritime Nord, CHU La Réunion, GHT Nord-Ouest Vexin Val d'Oise, CH Lannion | Named as "recent customers" of EVM in a search-engine summary of the old byg-info.com news page. The page itself returns HTTP 503 and could not be read | Undated (pre-2020 site) | Possible hospital middleware sites | INDICATIVE (search-engine summary only) | [byg-info.com news (unreadable)](http://byg-info.com/index.php/fr/actualites-2) |
| 7 | CHU Reims, CHRU Nancy, CH Abbeville | Info Partner INFECTIO sites (see 13.3) | 2019–2025 | IPC base, not middleware | CONFIRMED (theses) | 13.3 |
| 8 | Biogroup, Cerba, Eurofins, Synlab France, Inovie, LBI | No public evidence of Ascentry middleware | — | — | UNKNOWN (searched company site, press, DECP) | Chapter 9 |

#### C. What the renewal calendar means (ANALYST OPINION)

- **2027 is the pressure point.** Gonesse (January), Saint-Étienne (February), Rouen (April), Grenoble (April), the Infectio end of maintenance (June) and Caen (December) all fall within 12 months. Expect Ascentry to use each renewal to propose Lab Composer plus Infection Tracker as a single, negotiated, no-competition package, as at Caen.
- **Inlog sites carry double risk.** CH Cannes (Inlog + nYna) and CHU Reims (Inlog + InfectioGlobal) can be offered Infection Tracker by both Ascentry and Inlog.
- **Contracts already passed with no visible renewal** (Orléans April 2025, Lens November 2025, Dijon May 2026) may be running on tacit or below-threshold renewals. Those are the cheapest accounts to open a conversation with now.
- **Scale caveat.** The table names about 20 sites against more than 400 claimed platforms. It is a sample, not a census.

#### D. How to complete the list

- **bioMérieux's own connectivity records** are the fastest way to widen the list: installation and service records for VITEK, VITEK MS and BacT/ALERT connections name the middleware each lab uses. bioMérieux to confirm internally.
- A systematic read of the lab quality manuals published on manuelprelevement.fr, where many French hospital labs host them. Search each for "bYg", "EVM", "Nyna" and "Pilot".
- Each target hospital's annual list of concluded contracts, held by its purchasing office. It includes below-threshold maintenance contracts.

---

## 14. Partnerships and collaborations

| Partner | Type | Date | IPC relevance | NEW? | Confidence | Source |
|---|---|---|---|---|---|---|
| **Inlog** (FR LIS / transfusion) | Strategic partnership covering Lab Composer, POC Controller, Validation Manager and **Infection Tracker**; France first, then international | 2 Oct 2025 | **Direct**: LIS channel for IPC | **NEW** | CONFIRMED (company claim) | [Ascentry x Inlog](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/) |
| **Technidata** (FR LIS, TDNexLabs) | OEM: Ascentry middleware sold as **TDMind** in the Technidata LIS. First deal Oct 2021; renewed Feb 2026; new TDMind Jan 2026 | 2021 / 2026 | Indirect (middleware) | **NEW** (renewal) | CONFIRMED | [Inovallée](https://www.inovallee.com/technidata-tisse-un-partenariat-strategique-avec-byg4lab-pour-repondre-aux-enjeux-futurs-des-laboratoires-medicaux/); [Technidata PR](https://www.technidata-web.com/images/PDF/Press/English/202602_PR_Partnership_TECHNIDATA_x_ASCENTRY.pdf) |
| **GeodAIsics** | AI cross-transmission and cluster detection on Ynfectio / Infection Tracker | 26 Jan 2024 | **Direct** | No | CONFIRMED (company claim) | [Ascentry PR](https://www.ascentry.com/event/ascentry-signs-a-partnership-agreement-with-geodaisics/) |
| **CHU Rennes** (Dr G. Ménard) | Clinical AI evaluation site | 2025–2026 | Direct | **NEW** (2026 results session) | CONFIRMED (company claim) | [SF2H 2026](https://www.ascentry.com/event/sf2h-2026/) |
| **QuidelOrtho** | Software development / OEM partnership extending a French agreement | 24 Jul 2023 | None | No | CONFIRMED | [QuidelOrtho](https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings) |
| Grifols, Ortho, Bruker (via tenders) | BYG software carried inside IVD offers | 2019–2023 | None | No | CONFIRMED | [TED 583476-2019](https://ted.europa.eu/en/notice/-/detail/583476-2019) |
| Stago, Thermo Fisher, Binding Site, SYNLAB, Unilabs, NHS, Finnish Red Cross | Homepage logos | — | None | — | CONFIRMED (company claim) | [ascentry.com](https://www.ascentry.com) |
| bioMérieux (historical) | VIGI@ct / VIGIguard published by Info Partner and sold under the bioMérieux name (company claim) | c. 1996–2020 | **Legacy IPC** | No | CONFIRMED (company claim + papers) | [JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf) |
| EHR/DPI vendors (Dedalus, Maincare, Softway, Epic, Cerner); Beckman, Sysmex, Roche, Werfen, BD; CPias, SpF, Sciensano formal ties | None found | — | — | — | UNKNOWN | web search, ascentry.com |

Note: one search summary wrongly equated QuidelOrtho with Beckman. **No Beckman link is verified.**

---

## 15. Publications and evidence base

### IPC / epidemiology / AMS

| # | Year | Country / site | Type | Product | Key point | Independent? (Y/N) | COI | Confidence | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2025 | FR, CHU Reims | PharmD thesis | InfectioGlobal V4 | MRSA alert form sent to the EOH via the software; no performance data | Y | None stated | CONFIRMED | [DUMAS 05322365](https://dumas.ccsd.cnrs.fr/dumas-05322365v1) |
| 2 | 2020 | FR, CHRU Nancy | Pharmacy thesis | InfectioGlobal (data source) | BHRe tracking in an in-house Access DB; 671 carriers (2004–2019); manual steps criticised | Y | None stated | CONFIRMED | [HAL 03298181](https://hal.univ-lorraine.fr/hal-03298181v1) |
| 3 | 2019 | FR, CH Abbeville | Biology thesis | INFECTIO.GLOBAL | Blood-culture epidemiology extraction; LIS + patient-movement link | Y | None stated | CONFIRMED | [DUMAS 02884834](https://dumas.ccsd.cnrs.fr/dumas-02884834v1) |
| 4 | 2015 | FR, CHU Nancy | Thesis | Bacterio (Info Partner) | Had HAI/MDRO detection functions; being replaced by GLIMS | Y | None stated | CONFIRMED | [HAL 01734170](https://hal.univ-lorraine.fr/hal-01734170v1) |
| 5 | 2015 | FR, CHU Nancy | Thesis | ENTREPOT, BACTERIO | Antibiogram data extraction | Y | None stated | CONFIRMED | [HAL 01733856](https://hal.univ-lorraine.fr/hal-01733856v1) |
| 6 | 2007 | IT, Tor Vergata | J Hosp Infect (peer-reviewed) | VIGI@ct (bioMérieux) | 306 suspected HAIs flagged, 92% confirmed; 4 of 7 outbreaks clonal | Likely Y | Not listed (paywalled) | CONFIRMED (abstract) | [doi 10.1016/j.jhin.2007.04.004](https://doi.org/10.1016/j.jhin.2007.04.004) |
| 7 | 2008 | IT, Tor Vergata | BMC Infect Dis | VIGI@ct + DiversiLab | Earlier detection of an MDR A. baumannii ICU cluster | Y | None declared | CONFIRMED | [doi 10.1186/1471-2334-8-79](https://doi.org/10.1186/1471-2334-8-79) |
| 8 | 2010 | PT, Hospital da Luz | Crit Care abstract | VIGIguard (bioMérieux) | Planned real-time surveillance | Probably Y | Not stated | CONFIRMED | [doi 10.1186/cc9154](https://doi.org/10.1186/cc9154) |
| 9 | 2014 | IT, Gemelli | BMC Infect Dis | VIGIguard (data export) | ESKAPE forecasting | Y | None declared | CONFIRMED | [doi 10.1186/s12879-014-0634-9](https://doi.org/10.1186/s12879-014-0634-9) |
| 10 | 2015 | FR, CHU Dijon / Besançon | PLoS One | VIGIguard (data source) | SaTScan vs WHONET cluster detection | Y | None declared | CONFIRMED | [doi 10.1371/journal.pone.0139920](https://doi.org/10.1371/journal.pone.0139920) |
| 11 | 2020 | IT, Senigallia | BMC Bioinformatics | VIGIguard (de-duplication) | ML prediction of MDR UTI | Y | None declared | CONFIRMED | [doi 10.1186/s12859-020-03566-7](https://doi.org/10.1186/s12859-020-03566-7) |
| 12 | 2025 | FR, Grenoble + Rennes | SF2H sponsored innovation session | Ynfectio + AI | No abstract text | N | Company-sponsored | CONFIRMED (event) | [SF2H 2025](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf) |
| 13 | 2026 | FR, CHU Rennes | SF2H innovation session | Infection Tracker + AI "first results" | Results not published | N | Company speaker | CONFIRMED (company claim) | [SF2H 2026](https://www.ascentry.com/event/sf2h-2026/) |
| 14 | 2024 | FR | Spectra Diagnostic advertorials; BYG4lab white paper | Ynfectio | Marketing claims | N | Advertorial | CONFIRMED (company claim) | [SD031](https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf); [SD035](https://spectradiagnostic.com/wp-content/uploads/2024/11/SD035_WEB.pdf) |

No PubMed or Europe PMC hit exists for Ynfectio, InfectioGlobal, Infection Tracker, BYG4lab or Ascentry (checked 2026-09-26). **No peer-reviewed evaluation of the current product and no AMS outcome study exist.** The most substantial peer-reviewed body for this lineage is **bioMérieux-branded (VIGI@ct/VIGIguard)**.

### Middleware / validation (brief)

| Product | Evidence | Independent? (Y/N) | COI | Confidence | Source |
|---|---|---|---|---|---|
| EVM (BYG Informatique) | Methods-section tool in 2 Moroccan papers (2023, 2024) | Y | None declared | CONFIRMED | [J Med Biochem](https://doi.org/10.5937/jomb0-48306); [Adv Virol](https://doi.org/10.1155/2023/9313666) |
| Validation Manager (Finbiosoft) | About 10 papers, mostly UKE Hamburg, as an analysis tool | Y | No Finbiosoft authors in sampled texts | CONFIRMED | e.g. [Emerg Infect Dis 2022](https://doi.org/10.3201/eid2809.220917) |
| PILOT.4lab (Info Partner) | Background mention, Lille newborn screening (2019) | Y (re Ascentry) | Biomaneo authors (another company) | CONFIRMED | [IJNS 2019](https://doi.org/10.3390/ijns5030031) |

---

## 16. Events and trade shows

| Date | Event | Location | Presence | IPC-relevant? | NEW? | Confidence | Source |
|---|---|---|---|---|---|---|---|
| 2019, 2022, 2024 | RICAI | Paris | Sponsor (partner4lab 2019; BYG4lab 2022, 2024, stand 39) | Yes | No | CONFIRMED | [RICAI 2024](https://www.ricai.fr/sponsor-byg4lab-2024); [RICAI 2022](https://www.ricai.fr/sponsor-byg4lab-2022) |
| 2021–2025 | SF2H | FR | Exhibitor every year; 2025 stand 37 (bioMérieux at stand 38); sponsored AI session 2025 | Yes | No | CONFIRMED | [SF2H 2025](https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf) |
| 2021 | JIB | Paris | Talk; Innovation Trophy for Ynfectio | Yes | No | CONFIRMED | [JIB Trophées](https://jib-innovation.com/trophees) |
| 18–22 May 2025 | EuroMedLab | Brussels | Exhibitor (as BYG4LAB) | No | No | CONFIRMED | [EuroMedLab 2025](https://www.euromedlab2025brussels.org/sponsors-and-exhibitors/) |
| 27–30 Jul 2025 | ADLM | Chicago | Booth #1651; rebrand launch | Partial | No | CONFIRMED | [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software) |
| 27 Nov 2025 | Lab Composer User Day | Paris | Organiser | No | **NEW** | CONFIRMED (company claim) | [Lab Composer](https://www.ascentry.com/products/lab-composer/) |
| 27 Jan 2026 | BICS/ABIHH/WIN Joint Symposium | Brussels | Attendee/exhibitor | **Yes** | **NEW** | CONFIRMED (company claim) | [event page](https://www.ascentry.com/event/bics-abihh-win-joint-symposium-2026/) |
| Feb–Mar 2026 | WHX Labs Dubai; ASCP KnowledgeLab | Dubai; St. Louis | Listed | No | **NEW** | CONFIRMED (company claim) | [News & events](https://www.ascentry.com/news-and-events/) |
| 27–30 Mar 2026 | AMCLI | Rimini | Listed | Yes (microbiology) | **NEW** | CONFIRMED (company claim) | same |
| 19–21 Apr 2026 | ESCMID Global | Munich | **Visitor only**; Infection Tracker featured | Yes | **NEW** | CONFIRMED (company claim) | [ESCMID page](https://www.ascentry.com/event/escmid-2026/) |
| 18–21 May 2026 | SFTA | Aix-en-Provence | Listed (transfusion) | No | **NEW** | CONFIRMED (company claim) | [News & events](https://www.ascentry.com/news-and-events/) |
| 20 May 2026 | CPias Bretagne | Saint-Quay-Portrieux | Listed | **Yes** | **NEW** | CONFIRMED (company claim) | same |
| 21 May 2026 | Sciensano | Brussels | Listed | **Yes** | **NEW** | CONFIRMED (company claim) | same |
| 28–30 May 2026 | JNI / SEIMC | Bilbao | Listed ("Infection Surveillance Software") | **Yes** | **NEW** | CONFIRMED (company claim) | [JNI page](https://www.ascentry.com/event/jni-2026-infection-surveillance-ascentry/) |
| 3–5 Jun 2026 | SF2H | Lille | Innovation session "AI & Infection Tracker: first results at Rennes" | **Yes** | **NEW** | CONFIRMED (company claim) | [SF2H 2026](https://www.ascentry.com/event/sf2h-2026/) |
| 15–18 Sep 2026 | NCCB | Aarhus | Listed | No | **NEW** | CONFIRMED (company claim) | [News & events](https://www.ascentry.com/news-and-events/) |
| 2025–2026 | JIB, RICAI 2025, Medica, HIMSS Europe, Santexpo, Swiss congresses | — | Not found | — | — | UNKNOWN (exhibitor lists not reached) | — |

The 2026 calendar shows a **deliberate move onto IPC and infectious-disease audiences** in France, Belgium and Spain, which is LUMED's ground (INDICATIVE).

---

## 17. Head-to-head with LUMED

**No internal tender encounters or win/loss records were provided.** One account where both are present is known: **CHRU Nancy** has used LUMED APSS and ZINC since 2021 (CONFIRMED (user-provided internal intelligence)), and it is also the historic InfectioGlobal site (2020 thesis). The two known current Infectio customers, GHT Coeur Grand Est and CHU Grenoble, are open ZINC opportunities (chapter 13). Otherwise the comparison is built from public Ascentry evidence. The LUMED column is left for bioMérieux to complete.

### Tender-readiness scorecard

| Criterion | Ascentry status | Confidence | Source | LUMED |
|---|---|---|---|---|
| Hosting / data residency | Infection Tracker hosting not stated; website on OVHcloud Roubaix; legacy likely on-premise | UNKNOWN / INDICATIVE | [Trust](https://www.ascentry.com/trust/); [Legal notice](https://www.ascentry.com/legal-notice/) | bioMérieux to confirm |
| MDR/IVDR/CE | Not disclosed | UNKNOWN (EUDAMED not queried) | [FAQ](https://www.ascentry.com/faq/) | bioMérieux to confirm |
| ISO 13485 / ISO 27001 | 13485 covers Infection Tracker; 27001 covers Validation Manager only | CONFIRMED (company claim) | [Trust Center](https://www.ascentry.com/trust/) | bioMérieux to confirm |
| HDS | Not found | UNKNOWN | [Trust](https://www.ascentry.com/trust/) | bioMérieux to confirm |
| Named interoperability | LIS-fed (HL7 legacy); partners Inlog and Technidata; no named EHR/DPI; no FHIR | CONFIRMED (company claim) / UNKNOWN | [Inlog PR](https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/); [partner4lab](https://partner4lab.com/shop/infectio-global/) | bioMérieux to confirm |
| Live references (IPC) | CHU Caen GHT, CH Nevers, CHU Reims, CHU Rennes (pilot); "90+ sites" claimed | CONFIRMED (partly company claim) | chapter 4 | bioMérieux to confirm |
| Independent evidence | Theses only (descriptive); peer-reviewed body is historical, bioMérieux-branded VIGI@ct/VIGIguard | CONFIRMED | chapter 15 | bioMérieux to confirm |
| Local language support | French native; 11 languages claimed | CONFIRMED (company claim) | [Keensight 2024](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/) | bioMérieux to confirm |
| Company scale and implementation capacity | About 120 staff group-wide; €13.7M revenue (FR entity, 2024); IPC team size unknown | CONFIRMED / UNKNOWN | [Pappers](https://www.pappers.fr/entreprise/byg-informatique-326649407) | bioMérieux to confirm |
| Purchasing frameworks | UGAP 2021 only as a member of an Ortho-led analyser group; no UniHA/RESAH/CAIH listing found | CONFIRMED / UNKNOWN | [TED 495457-2021](https://ted.europa.eu/en/notice/-/detail/495457-2021) | bioMérieux to confirm |
| National-surveillance exports | Contested: legacy ConsoRes/Sciensano claim; SPARES/PRIMO/WHONET/EARS-Net in one page reading only | INDICATIVE | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) | bioMérieux to confirm |
| AMS scope | Lab-side only (antibiograms, resistance trends); no prescription-level AMS | CONFIRMED (company claim) / UNKNOWN | [Infection Tracker](https://www.ascentry.com/products/infection-tracker/) | bioMérieux to confirm |

### bioMérieux to confirm internally

- **VIGI@ct / VIGIguard.** Ascentry claims Info Partner designed these products, and papers show them sold under the bioMérieux name. Confirm the history of the OEM/distribution agreement, whether it has ended, whether any contractual obligations survive, and which sites form a **legacy installed base** that may have migrated to Infectio, Ynfectio or Infection Tracker (France, Italy, Portugal, Belgium). Do not use the lineage externally until confirmed.
- **HUmani Charleroi.** bioMérieux Benelux won the antibiogram tender (TED 423892-2025), which required "raccordement à la connexion Byg4lab existante". Confirm the connection arrangement, the cost bearer and the working relationship with Ascentry in Belgium. Check the same for other Belgian and French sites where bioMérieux instruments connect to BYG4lab middleware.
- **CHRU Nancy.** Has used LUMED APSS and ZINC since 2021 (CONFIRMED (user-provided internal intelligence)). Nancy is also the historic Info Partner / InfectioGlobal site. Confirm whether InfectioGlobal still runs alongside LUMED, and whether Nancy will act as a reference for legacy-Infectio prospects.
- **UGAP 2021 framework 17U032.** BYG INFORMATIQUE is listed in the Ortho-led group. Confirm internally whether and how bioMérieux relates to this framework before citing it. **No bioMérieux status is asserted here.**
- **SF2H 2025.** Ascentry's stand (37) was adjacent to bioMérieux's (38). Check for field intelligence from the event.
- **Any bioMérieux–Ascentry connectivity or partnership agreement** (none is public). Also establish whether Ascentry's VP Industrial Partnerships has approached bioMérieux.
- The **LUMED column** of the scorecard above.

---

## 18. Competitive implications for bioMérieux LUMED (ANALYST OPINION)

This chapter is ANALYST OPINION built on the evidence above.

Ascentry is **not a like-for-like CDSS competitor**. It is a lab-data company whose IPC product sits downstream of microbiology results, while LUMED's differentiation lies in prescription-level stewardship. The threat is narrower but real. Where the buying centre is the **laboratory**, and the lab already runs Ascentry middleware, an IPC surveillance need can be met by a low-cost add-on bought through a single-source maintenance vehicle. That skips a competitive tender entirely, as the CHU Caen GHT framework (to about Dec 2027) and the Nevers renewal (to about Feb 2030) show.

The 2025–2026 moves sharpen this: the Inlog channel, the SF2H/CPias/Sciensano/JNI presence and the Rennes AI results. Ascentry now **addresses IPC teams directly**, not only biologists.

The opportunities for LUMED lie in the gaps: AMS depth, independent evidence, certification transparency (MDR/IVDR class, HDS, 27001 for the IPC product) and the documented manual work around InfectioGlobal at Nancy. The windows to target are **GHT convergence and middleware re-procurement**, when single-source maintenance ends.

Belgium deserves specific attention. bioMérieux instruments already connect to BYG4lab middleware there (HUmani), and Ascentry is courting BICS/ABIHH and Sciensano.

### Battlecard (one page)

**Ascentry strengths**
- Installed middleware base (claimed 4,500+ labs; 400+ French platforms historically) that provides the data feed and the procurement vehicle.
- 25+ years of IPC lineage (Nancy); ISO 13485; vendor-neutral and LIS-agnostic.
- New LIS channel (Inlog) and IVD OEM channel (Technidata, QuidelOrtho).
- AI story with an academic CHU (Rennes).
- Cheap entry price (about €2.6k/yr maintenance at a small hospital).

**Ascentry weaknesses**
- No prescription-level AMS.
- No peer-reviewed evaluation of the current product.
- 27001 not stated for Infection Tracker; HDS and CE/IVDR/MDR class undisclosed.
- No named EHR/DPI integration.
- Small company (about 120 staff; €13.7M French revenue, flat in 2024); IPC team size unknown.
- CEO transition in July 2026 and a PE owner at a probable exit stage.
- No named Infection Tracker customer stories.

**Likely Ascentry claims and evidence-based counters**

| Likely Ascentry claim | Evidence-based counter | Confidence of counter |
|---|---|---|
| "Unified platform for IPC **and antimicrobial stewardship**" | AMS functions published are antibiograms, resistance trends and reports to pharmacists. No consumption, prescription linkage or AMS alerts were found ([Infection Tracker](https://www.ascentry.com/products/infection-tracker/)). Ask for a demonstration of prescription-level AMS workflows | CONFIRMED (absence = UNKNOWN after search) |
| "90+ sites across Europe, 25+ years" | No named Infection Tracker customer story exists; all 11 stories are Validation Manager ([Customer stories](https://www.ascentry.com/customer-stories/)). Ask for named IPC references and go-live dates | CONFIRMED |
| "AI outbreak detection" | Results so far are company-sponsored congress sessions (SF2H 2025/2026) with no published data ([SF2H 2026](https://www.ascentry.com/event/sf2h-2026/)). Ask for validation data, sensitivity/specificity and regulatory status of the AI function | CONFIRMED |
| "Automatic national reporting (SPARES/ConsoRes/PRIMO/Sciensano)" | Only a legacy snippet and advertorials support it; the live page reading is contested; no formal agreement with SpF, CPias or Sciensano was found. Ask for proof of accepted submissions | INDICATIVE |
| "ISO 13485 certified, secure" | ISO 27001 is stated only for Validation Manager (Finland); HDS and CE class are not disclosed ([Trust Center](https://www.ascentry.com/trust/)). Require certificates in the tender | CONFIRMED (company claim) |
| "Integrates with any LIS/HIS" | No EHR/DPI partner is named; the independent Nancy thesis shows the IPC team ran BHRe follow-up in an Access database alongside InfectioGlobal ([HAL 03298181](https://hal.univ-lorraine.fr/hal-03298181v1)). Ask for named HIS/ADT interfaces in production | CONFIRMED (historical) |
| "Evidence base" | Independent evidence is limited to descriptive theses. The peer-reviewed lineage is VIGI@ct/VIGIguard, branded bioMérieux (use only after internal confirmation) | CONFIRMED |
| "Already in your lab, so just add the module" | Bundled maintenance is single-source and non-competitive; IPC/AMS is a clinical decision that merits its own evaluation and competition. Time bids to GHT convergence and middleware renewal dates | INDICATIVE |

---

## 19. Information gaps and recommended next checks

| Gap | Why it matters | Where to check | Status |
|---|---|---|---|
| Per-product price split and CCTP for CHU Caen (ref. 2023132) | Isolates the IPC licence/maintenance price in a bundle | PLACE (marches-publics.gouv.fr) | Open, not queried |
| Whether CH Nevers (buyer identity now confirmed) runs Ascentry middleware | Settles standalone vs bundled | Nevers CCTP; DECP history for SIREN 200011203 | Open (buyer resolved 26/09/2026; middleware question open) |
| Competitive first acquisition of Ynfectio / Infection Tracker | Shows whether it wins open IPC tenders | BOAMP, PLACE, regional platforms | Open, not queried |
| Infection Tracker reference list with each site's LIS/middleware | Measures true standalone share of the 90+ sites | Ascentry sales material; Spectra n°41; field intelligence | Open |
| CE/IVDR/MDR class, UDI | Tender eligibility | EUDAMED | Open, not queried |
| HDS, hosting provider, ISO 27001 scope for Infection Tracker | French hosting compliance | Ascentry help centre; tender Q&A | Open |
| Live national-surveillance exports | Key IPC differentiator | Re-read the live product page; SpF/CPias/Sciensano contacts; archived byg4lab.com | Contested |
| Operating-company rename date; 10/09/2026 filing | Correct entity name for tenders | Bodacc, RNE, Infogreffe | Open |
| 2025 accounts (Ascentry France, Group) | Current scale/growth | Pappers, Infogreffe (filed Jul–Aug 2026) | Filed, figures not retrieved |
| Belgian customers beyond Arlon; KBO entity; Sciensano link | Verify the Belgian IPC base | publicprocurement.be, KBO, Vivalia | Open |
| Swiss presence | User-stated market, not verified | simap.ch, Zefix, Romandy hospitals | Open |
| Italy, Spain, UK IPC contracts | Priority markets | ANAC/BDNCP, PLACSP, Find a Tender, Contracts Finder | Open, not queried |
| Rennes AI results; SF2H 2026 abstract | Validates or undercuts the AI claim | SF2H 2026 abstract book; Dr Ménard publications | Open |
| VIGI@ct/VIGIguard legacy base | Possible former bioMérieux-distributed sites | bioMérieux internal records | bioMérieux to confirm |
| Keensight exit / ownership change | Strategic stability of the competitor | CFNEWS, Fusacq, press | Watch |
| CEO background (d'Apréa) | Strategic direction | LinkedIn, press | Open |
| Full list of Ascentry middleware sites in France (EVM, nYna, EVM-IH, PILOT, Ypoc) | Cross-sell pool for Infection Tracker | bioMérieux connectivity/service records for VITEK, VITEK MS and BacT/ALERT; lab quality manuals on manuelprelevement.fr; purchasing offices | Open |
| Full list of legacy INFECTIO sites in France | Sizes the June 2027 ZINC opportunity | bioMérieux field teams; CPias regional networks; hospital purchasing offices (annual contract lists); Ascentry user club | Open |
| Ascentry's public end-of-maintenance notice for INFECTIO | Confirms the June 2027 date and the migration offer | Customer letters (via friendly sites), Ascentry sales material | Open (internal intelligence only) |
| CHU Dijon: whether Info Partner products include Infectio; renewal status after May 2026 | Possible immediate opportunity | CHU Dijon purchasing office; PLACE | Open |
| GHT Coeur Grand Est and CHU Grenoble: Infectio contract vehicle, value and end date | Timing of the ZINC offer | Account teams; hospital purchasing offices | Open |

---

## Sources

### Company and partner sources
- https://www.ascentry.com
- https://www.ascentry.com/products/infection-tracker/
- https://www.ascentry.com/products/lab-composer/
- https://www.ascentry.com/products/poc-controller/
- https://www.ascentry.com/products/validation-manager/
- https://www.ascentry.com/solution/lis-providers/
- https://www.ascentry.com/about-us/
- https://www.ascentry.com/leadership-team/
- https://www.ascentry.com/trust/
- https://www.ascentry.com/faq/
- https://www.ascentry.com/legal-notice/
- https://www.ascentry.com/customer-stories/
- https://www.ascentry.com/news-and-events/
- https://www.ascentry.com/case-studies/
- https://www.ascentry.com/case-studies/1ere-annee-dune-fusion-reussie-entre-byg-informatique-et-info-partner-partner4lab/
- https://www.ascentry.com/articles/finbiosoft-joins-forces-with-byg4lab/
- https://www.ascentry.com/articles/sample-carryover-study/
- https://www.ascentry.com/event/ascentry_appoints_ludovic_d_aprea_as_new_chief_executive_officer/
- https://www.ascentry.com/event/ascentry-launches-advisory-board-to-drive-strategic-growth/
- https://www.ascentry.com/event/ascentry-x-inlog-a-strategic-partnership/
- https://www.ascentry.com/event/ascentry-signs-a-partnership-agreement-with-geodaisics/
- https://www.ascentry.com/event/sf2h-2026/
- https://www.ascentry.com/event/escmid-2026/
- https://www.ascentry.com/event/jni-2026-infection-surveillance-ascentry/
- https://www.ascentry.com/event/bics-abihh-win-joint-symposium-2026/
- https://www.ascentry.com/wp-content/uploads/2026/02/Press-Release-Ascentry-x-TechniData-February-2026-1.pdf
- https://www.technidata-web.com/images/PDF/Press/English/202602_PR_Partnership_TECHNIDATA_x_ASCENTRY.pdf
- https://byg4lab.com/en/product-ynfectio/
- https://byg4lab.com/en/product-pocy/
- https://byg4lab.com/case-studies/lancement-nyna-votre-nouvelle-generation-de-middleware/
- https://byg4lab.com/case-studies/acquisition-de-lensemble-des-activites-de-la-societe-infopartner-partner4lab/
- https://byg4lab.com/case-studies/%F0%9F%94%B5-livre-blanc-les-benefices-dun-systeme-depidemiologie-et-dhygiene-centralise/
- https://byg4lab.com/case-studies/%F0%9F%8E%99%EF%B8%8F-pleniere-sfm-les-benefices-dun-systeme-depidemiologie-et-dhygiene-centralise/
- https://byg4lab.com/case-studies/byg4lab-remporte-le-trophee-de-linnovation-en-biologie-medicale-%F0%9F%8F%86/
- https://byg4lab.com/case-studies/partenariat-unilabs-france/
- https://byg4lab.com/en/case-studies/press-release-byg4lab-x-geodaisics/
- http://byg-info.com/index.php/fr/partenariat-unilabs-france
- https://partner4lab.com/en/company/
- https://partner4lab.com/shop/infectio-global/
- https://partner4lab.com/fr/shop/infectio-labo/
- https://partner4lab.com/feed-back-journee-pilot4lab/
- https://finbiosoft.com/validation-manager-features/
- https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings
- https://www.businesswire.com/news/home/20230724368435/en/QuidelOrtho-Partners-With-BYG4lab-to-Strengthen-Informatics-Offerings
- https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/
- https://keensight.com/wp-content/uploads/2022/07/PR-BYG4lab-v17.07.2022-FR-KEENSIGHT-ONLY-Final.pdf
- https://brandpie.com/work/ascentry/
- https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf

### Registry and financial sources
- https://www.pappers.fr/entreprise/byg-informatique-326649407
- https://www.pappers.fr/entreprise/ascentry-group-915233837
- https://www.pappers.fr/entreprise/byg4lab-group-915233837
- https://www.societe.com/societe/byg-informatique-326649407.html
- https://www.societe.com/societe/byg4lab-group-915233837.html
- https://www.societe.com/societe/info-partner-349314948.html
- https://recherche-entreprises.api.gouv.fr/search?q=326649407
- https://annuaire-entreprises.data.gouv.fr/entreprise/326649407
- https://recherche-entreprises.api.gouv.fr/search?q=200011203 (buyer identity of CH intercommunal Agglomération de Nevers, checked 26/09/2026)
- https://pitchbook.com/profiles/company/58554-73
- https://www.privsource.com/acquisitions/deal/keensight-capital-acquires-majority-stake-in-byg4lab-x7Sx5w
- https://www.castren.fi/cases/byg4lab-and-keensight-capital-acquisition-of-finbiosoft/

### Procurement sources
- https://www.boamp.fr/pages/avis/?q=idweb:23-142021
- https://www.boamp.fr/pages/avis/?q=idweb:19-146017
- https://www.boamp.fr/pages/avis/?q=idweb:16-28267
- https://www.boamp.fr/pages/avis/?q=idweb:15-168566
- https://www.boamp.fr/pages/avis/?q=idweb:21-100129
- https://ch-cannes.manuelprelevement.fr/DocumentNew.aspx?idDoc=30291
- https://ch-brive.manuelprelevement.fr/Docs/lbm-chdebrive/DefaultDocs/DocN4.pdf
- https://biosevres.manuelprelevement.fr/DocumentNew.aspx?idDoc=282
- https://byg4lab.com/en/case-studies/user-case-macon-hospital-center/
- https://byg4lab.com/case-studies/partenariat-unilabs-france/
- http://byg-info.com/index.php/fr/actualites-2
- https://ted.europa.eu/en/notice/-/detail/489752-2024
- https://ted.europa.eu/en/notice/-/detail/450483-2024
- https://ted.europa.eu/en/notice/-/detail/81198-2025
- https://boamp-datadila.opendatasoft.com/explore/dataset/boamp/
- https://recherche-entreprises.api.gouv.fr/search?q=130005010 (RESAH)
- https://recherche-entreprises.api.gouv.fr/search?q=828570606 (NOSOTECH EUROPE)
- https://recherche-entreprises.api.gouv.fr/search?q=347717118 (I2A)
- https://ght-coeurgrandest.fr/gcs-laboratoire/
- https://ght-coeurgrandest.fr/specialites/hygiene-hospitaliere/
- https://spectradiagnostic.com/wp-content/uploads/2021/05/SD012_Publi-Byg4lab.pdf
- https://spectradiagnostic.com/wp-content/uploads/2025/03/SD037_WEB.pdf
- https://spectradiagnostic.com/wp-content/uploads/2025/10/SD040_WEB.pdf
- https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/
- https://data.economie.gouv.fr/explore/dataset/decp-v3-marches-valides/
- https://data.economie.gouv.fr/explore/dataset/decp_augmente/
- https://api.ted.europa.eu/v3/notices/search
- https://ted.europa.eu/en/notice/-/detail/348571-2024
- https://ted.europa.eu/en/notice/348571-2024/xml
- https://ted.europa.eu/en/notice/-/detail/583476-2019
- https://ted.europa.eu/en/notice/-/detail/495457-2021
- https://ted.europa.eu/fr/notice/-/detail/577496-2021
- https://ted.europa.eu/en/notice/-/detail/346413-2022
- https://ted.europa.eu/en/notice/-/detail/451036-2023
- https://ted.europa.eu/en/notice/-/detail/180670-2024
- https://ted.europa.eu/en/notice/-/detail/423892-2025
- https://centraledesmarches.com/marches-publics/Caen-CHU-CAEN-NORMANDIE-Maintenance-evolutive-et-corrective-du-middleware-NYNA-du-logiciel-depidemiologie-et-dhygiene-Ynfectio-du-logiciel-de-validation-des-methodes-Qualynk-du-logiciel-de-gestion-de-la-paillasse-dimmunohematologie-EVM-IH-de-la-societe-BYG4LAB-pour-trois-etablissements-du-GHT-et-prestations-associees/250499

### Trade press, news and associations
- https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software
- https://www.biologiste365.fr/biologiste365-fr/actualites-biologiste365-fr/byg4lab-devient-ascentry/
- https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/
- https://www.biologiste365.fr/strategie/numerique/quand-les-donnees-de-biologie-ne-sont-quun-depart/
- https://www.biologiste365.fr/a-decouvrir/yline-linnovation-au-service-de-la-digitalisation-des-laboratoires-de-biologie-medicale/
- https://www.biologiste365.fr/antibiotherapie/
- https://www.inovallee.com/technidata-tisse-un-partenariat-strategique-avec-byg4lab-pour-repondre-aux-enjeux-futurs-des-laboratoires-medicaux/
- https://www.privateequitywire.co.uk/keensight-capital-acquires-majority-stake-byg4lab/
- https://www.privateequitywire.co.uk/2022/07/22/316278/keensight-capital-acquires-majority-stake-byg4lab/
- https://www.lemondedudroit.fr/deals/82918-hoche-avocats-conseille-keensight-capital-dans-le-cadre-de-l-acquisition-d-une-participation-majoritaire-dans-byg4lab.html
- https://www.forbes.fr/brandvoice/byg4lab-lexpert-des-logiciels-pour-les-laboratoires-de-biologie-medicale/
- https://spectradiagnostic.com/wp-content/uploads/2021/05/SD008_Publi-Byg.pdf
- https://spectradiagnostic.com/wp-content/uploads/2021/05/SD012_Publi-Byg4lab.pdf
- https://spectradiagnostic.com/wp-content/uploads/2024/04/SD031_WEB.pdf
- https://spectradiagnostic.com/wp-content/uploads/2024/11/SD035_WEB.pdf
- https://spectradiagnostic.com/wp-content/uploads/2025/12/SD041_WEB_2.pdf
- https://frenchhealthcare.fr/membres/byg4lab/
- https://frenchhealthcare.fr/en/adherents/byg4lab/
- https://www.preventioninfection.fr/actualites/spares-nouvelle-version-de-consores-disponible/
- https://www.hospitalia.fr/L-hygiene-hospitaliere-prend-de-plain-pied-le-virage-numerique_a3993.html
- https://www.csdmed.mc/en/news/news/position-paper-team-nb-150
- https://vigigerme.hug.ch/
- http://www.professeurs-medecine-nancy.fr/Informatique_medicale.htm
- https://www.linkedin.com/in/st%C3%A9phane-jamin-39801757/

### Academic and grey literature
- https://dumas.ccsd.cnrs.fr/dumas-05322365v1
- https://hal.univ-lorraine.fr/hal-03298181v1
- https://dumas.ccsd.cnrs.fr/dumas-02884834v1
- https://hal.univ-lorraine.fr/hal-01734170v1
- https://hal.univ-lorraine.fr/hal-01733856v1
- https://hal.inrae.fr/hal-02742661v1
- https://pubmed.ncbi.nlm.nih.gov/17544166
- https://doi.org/10.1016/j.jhin.2007.04.004
- https://doi.org/10.1186/1471-2334-8-79
- https://link.springer.com/article/10.1186/1471-2334-8-79
- https://doi.org/10.1186/cc9154
- https://doi.org/10.1186/s12879-014-0634-9
- https://doi.org/10.1371/journal.pone.0139920
- https://doi.org/10.1186/s12859-020-03566-7
- https://doi.org/10.5937/jomb0-48306
- https://doi.org/10.1155/2023/9313666
- https://doi.org/10.3390/ijns5030031
- https://doi.org/10.1186/s40064-015-1457-x
- https://doi.org/10.3201/eid2809.220917
- https://doi.org/10.1038/s41598-024-54037-5
- https://doi.org/10.1128/spectrum.02756-23
- https://doi.org/10.1016/j.jmsacl.2023.07.001
- https://doi.org/10.1007/s00430-025-00837-z
- https://doi.org/10.1002/jmv.70824
- https://doi.org/10.1038/s41598-026-45563-5

### Events
- https://www.sf2h.net/k-stock/data/uploads/2021/09/SF2H_2021_livre_des_resumes_FINAL.pdf
- https://www.sf2h.net/k-stock/data/uploads/2022/06/SF2H_2022_livre_des_resumes_FINAL.pdf
- https://www.sf2h.net/k-stock/data/uploads/2023/05/SF2H_2023ProgrammeCompletCongresLille2023.pdf
- https://www.sf2h.net/k-stock/data/nancy2024/SF2H_2024_livre_des_resumes_V5.pdf
- https://www.sf2h.net/k-stock/data/marseille_2025/sf2h_2025_livre_resume.pdf
- https://www.ricai.fr/sponsor-partner4lab-2019
- https://www.ricai.fr/sponsor-partner4lab
- https://www.ricai.fr/sponsor-byg4lab-2022
- https://www.ricai.fr/sponsor-byg4lab-2024
- https://jib-innovation.com/trophees
- https://www.euromedlab2025brussels.org/sponsors-and-exhibitors/
- https://adlm25.myexpoonline.com/co/byg4lab-inc
