# Asserta (Fleming / Fleming-PROA, Silicon, Pharmacy Analytics Manager): publications, evidence and events

Research date: 2 October 2026 (cut-off). Labels: CONFIRMED = read in a primary source; CONFIRMED (company claim) = stated by Asserta or its partners and not independently verified; INDICATIVE = indirect or partial evidence; UNKNOWN = searched but not found (search locations given).

## Q1. Peer-reviewed papers, abstracts, theses and whitepapers that mention Fleming, Asserta, or Asserta tools

### Takeaway
I found **no peer-reviewed paper, congress abstract, thesis or whitepaper that evaluates Fleming / Fleming-PROA**. Europe PMC full-text searches for "Fleming-PROA" and "Fleming PROA" return 0 hits, and no Fleming outcome data (DDD, DOT, de-escalation or cost) is published anywhere I could reach. Only **3 peer-reviewed papers have Asserta-affiliated authors**: 2 Vall d'Hebron oncology cost studies (2023, 2024) and 1 Hospital de Dénia anticholinergic-burden study (2025). All 3 are company co-authored and all 3 declare "no conflicts of interest", even though 2 of them name Asserta's own Pharmacy Analytics Manager as the analysis tool. Independent papers mention **Silicon only as the data source** (the e-prescribing system), not as the thing being evaluated.

### Master table: company-authored (Asserta staff or founder among the authors)

| # | Year | Country / institution | Venue | Peer-reviewed | Design | Summary | Key results | DOI / URL | COI / Asserta authors | Label |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | 2023 | Spain, Vall d'Hebron University Hospital (Pharmacy and Medical Oncology/VHIO) | *Current Oncology* 30(9) (MDPI); PMID 37754495; PMC10528466 | Y | Single-centre retrospective cohort, 2010–2019 | Describes drug use and the cost of antineoplastic treatment for adult solid tumours over 10 years. Data came from several systems, including **Silicon® v8.5–11.2**, QuimioProcess, Sisinf and Kiro. These were integrated and analysed with **Pharmacy Analytics Management (PAM) V.2022.1.0, "a health analytics tool developed by Asserta Global Healthcare Solutions"**. | 13,209 patients; total antineoplastic spend EUR 120,396,097 over 10 years | https://doi.org/10.3390/curroncol30090580 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10528466/ | **E. Tomás-Guillén and J. Monterde (Asserta founder/CEO) are affiliated with Asserta Global Healthcare Solutions** (emails @asserta.net). COI statement lists only pharma ties of other authors; "the remaining authors declare no conflict of interest", so Asserta's commercial interest in PAM is **not disclosed**. No external funding. | CONFIRMED |
| A2 | 2024 | Spain, Vall d'Hebron University Hospital | *Cancers* 16(8):1529 (MDPI); PMID 38672610; PMC11048575 | Y | Single-centre retrospective, 2010–2019 | Measures drug cost avoidance from sponsor-supplied drugs in solid-tumour clinical trials. Analyses were run on "Pharmacy Analytics Manager (V.2022.1.0) (https://www.asserta.net)". | 2,930 trials and 10,488 participants; trials grew from 140 (2010) to 459 (2019), a 228% increase; 421 different antineoplastics were used | https://doi.org/10.3390/cancers16081529 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11048575/ | **Tomás-Guillén E and Monterde J are affiliated with Asserta.** "Remaining authors declare no conflicts of interest", so the Asserta tool interest is not disclosed. No external funding. | CONFIRMED |
| A3 | 2025 | Spain, Hospital de Dénia (Alicante), Pharmacy Service | ***Revista de la OFIL·ILAPHAR*** 35(4), Jul–Aug 2025 (SciELO ISSN 1699-714X). **Not *Farmacia Hospitalaria***: the SciELO pid prefix S1699-714X is the OFIL journal. | Y (OFIL is a peer-reviewed journal; review process not checked) | Retrospective observational, data extracted 31 Mar 2022 | Measures anticholinergic burden (ACB scale) in 3,044 patients aged ≥65 in one health department. The article does not explicitly name the software used. | 61.83% women, mean age 77.5; 88.73% scored ACB 3; quetiapine 28.69%, amitriptyline 15.20%, paroxetine 13.49%; CNS drugs 67.56% of anticholinergics | https://scielo.isciii.es/scielo.php?pid=S1699-714X2025000400006&script=sci_arttext ; https://www.ilaphar.org/analisis-de-la-carga-anticolinergica-en-personas-de-edad-avanzada/ ; DOI as displayed on SciELO: https://dx.doi.org/10.4321/s1699-714x2025000400005 (**note the suffix mismatch**: pid ends …006, DOI ends …005; verify manually) | **M. Enríquez Torres and J. Monterde Junyent are affiliated with Asserta Global Healthcare Solutions, Sant Quirze del Vallès.** Authors declare "no tener conflictos de intereses". No funding statement. Not antimicrobial and not Fleming. | CONFIRMED |

### Independent papers that cite Silicon (Grifols, now Asserta) as the e-prescribing or data source
None of these evaluates Silicon or any Asserta CDSS; Silicon is only the place the data came from. They are useful as evidence of where Silicon is installed and how it is used for AMS data capture.

| # | Year | Institution | Venue | Peer-rev | Design | Silicon role / key results | DOI | COI (Asserta?) | Label |
|---|---|---|---|---|---|---|---|---|---|
| I1 | 2021 | Vall d'Hebron Children's Hospital, Barcelona | *BMC Infect Dis* | Y | Prospective modified point-prevalence (PROAFUNGI, Jul–Oct 2018) | Patients on antifungals were identified through "Silicon® v11, Grifols" plus Centricity Critical Care | https://doi.org/10.1186/s12879-021-05774-9 | Gilead ISR grant; no Asserta authors | CONFIRMED |
| I2 | 2024 | Vall d'Hebron (PROA-NEN paediatric AMS) | *Antibiotics* 13(6):511 | Y | 5-year evaluation of an AMS programme | Antimicrobial use, treatment and cost data were extracted from "Silicon® v11 (Grifols)" and SAP Business Objects | https://doi.org/10.3390/antibiotics13060511 | Pharma grants (Pfizer, Gilead, MSD…); no Asserta authors | CONFIRMED |
| I3 | 2020 | Hospital Univ. Arnau de Vilanova, Lleida (Jover-Sáenz et al.) | *Infection Prevention in Practice* | Y | 5-year descriptive AMS impact study | Consumption data (DDD) came from "SILICON" e-prescribing integrated in SAP | https://doi.org/10.1016/j.infpip.2020.100048 | No Asserta authors | CONFIRMED |
| I4 | 2023 | Lleida (Jover-Sáenz et al.) | *Antibiotics* 12(5):834 | Y | Pre/post intervention at surgical discharge | Data from "Silicon®, integrated into SAP-ARGOS"; the authors report about a 60% reduction in antibiotic exposure attributed to the **AMS strategy, not the software** | https://doi.org/10.3390/antibiotics12050834 | Declared none; no Asserta authors | CONFIRMED |
| I5 | 2026 | Spain (Vazquez-Piqueras, Padullés, Sabé et al.; carbapenem multimodal intervention) | *BMJ Open* (protocol) | Y (protocol) | Quasi-experimental ITS protocol | Acceptance of AMS recommendations "will be extracted from Silicon, the hospital's electronic prescribing system" | https://doi.org/10.1136/bmjopen-2026-118013 | No Asserta authors seen in the author string | CONFIRMED |
| I6 | 2024 | Galicia (González Freire et al.) | *EPMA J* | Y | Outpatient pharmacy description | Europe PMC lists it as a "Silicon®" hit; I did not read the context | https://doi.org/10.1007/s13167-023-00346-0 | Not checked | INDICATIVE |

### Historical background (pre-Asserta, founder's earlier work; context only)
- J. Monterde co-authored "Monitoring of antimicrobial therapy by an integrated computer program" in 1999 (*Pharm World Sci*), which is evidence of the founder's long interest in IT-supported antimicrobial monitoring — https://doi.org/10.1023/a:1008610912290 (CONFIRMED that the paper exists via Europe PMC; content not read).
- Also "Impact of local guidelines and an integrated dispensing system on antibiotic prophylaxis quality in a surgical centre" (*J Hosp Infect* 2005, Alerany, Campany, Monterde, Semeraro) — https://doi.org/10.1016/j.jhin.2004.07.022 (CONFIRMED that it exists; not read).

### Theses
- The *Cancers* 2024 paper cites "Carreras M.J. Ph.D. Thesis. Universitat Autònoma de Barcelona; 2020", on pharmaceutical expenditure for solid tumours at Vall d'Hebron. It appears to use the same dataset (likely the PAM analysis) — cited in https://pmc.ncbi.nlm.nih.gov/articles/PMC11048575/. Whether Monterde or Asserta was a supervisor: UNKNOWN (TDX search for "Asserta" returned no hits; TESEO not checked).

### Whitepapers / case studies
- None found. Asserta's "Experiencias" page shows only client logos (40+ European hospital logos, including Vall d'Hebron, Bellvitge, HM Hospitales and Quirónsalud), with no case studies, metrics or dates — https://asserta.net/es/experiencias/ (CONFIRMED (company claim) for the logos).

### Inferences
- The scientific footprint of Asserta's own staff is in **oncology and geriatric drug-utilisation analytics** (PAM / analytics), not antimicrobial stewardship. Fleming has **zero published evidence**.
- In the 2 Vall d'Hebron papers the Asserta-affiliated authors used Asserta's own commercial tool while declaring no COI. A competitor or reviewer could reasonably flag this as an **undisclosed commercial interest**.
- Silicon's academic visibility is passive: hospitals (Vall d'Hebron, Lleida/Arnau de Vilanova, and the BMJ Open 2026 protocol site) name it as their data source. That confirms the installed base, but none of these papers attributes any effect to Silicon.

### Gaps
- SEFH congress e-poster books 2018–2025 (68–70 Congreso), EJHP EAHP supplements, ESCMID Global and SEIMC abstract books: I found no hit for "Fleming" + Asserta through web search or Europe PMC (Europe PMC indexes the EJHP abstract supplements; the EJHP query for "Fleming" + antimicrobial returned only 2 irrelevant hits). A manual check of the SEFH e-poster search engines is still needed (see the blocked sources section).
- Google Scholar, Dialnet and TESEO were not queried directly (no API access in this session).

## Q2. Evidence on Fleming outcomes (DDD/DOT reduction, de-escalation, cost savings)

### Takeaway
**UNKNOWN / none published.** All Fleming information is company or partner marketing. It describes capabilities (indicators, microbiology, outcomes monitoring) but gives no quantified results.

### Cited findings
- Asserta's Fleming product page lists features (real-time antibiotic consumption, resistance trends, protocol adherence, dashboards) but **no hospitals, no metrics and no publications** — https://asserta.net/es/fleming-antimicrobial-stewardship/ (CONFIRMED that no data is shown).
- Fleming is described as an on-premise, multi-device web app. Vademecum says it covers "all indicators required to achieve EXCELLENT level" under the AEMPS/PRAN PROA team certification standard — https://www.vademecum.es/noticia-240108-... (8 Jan 2024) (CONFIRMED (company/partner claim)). This is a claim about indicator coverage, not an AEMPS certification of the software. The Vademecum product page wording ("certified by AEMPS") overstates it — https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69.
- Fleming's decision-support algorithms use ViDAL Vademecum drug content — same Vademecum URL (CONFIRMED (partner claim)).
- The Fleming page shows a badge linking to a certificate "RD311-2022". RD 311/2022 is Spain's Esquema Nacional de Seguridad (ENS), so this looks like an information-security certificate, not a clinical one — https://asserta.net/fleming/ (INDICATIVE; certificate PDF not opened).
- Deployment claim: Fleming integrates data from more than 80 laboratories, covers a population of 7 million, and is used in "más de 600 centros de atención primaria y 14 hospitales en España y Latinoamérica"; Asserta had a 12-person team (Mar 2024) — https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html (CONFIRMED (company claim)).
- Homepage claims: 2+ billion records processed, 76 hospitals, 20+ countries — https://asserta.net/es/ (CONFIRMED (company claim)).

### Inferences
- Without published DDD, DOT or de-escalation data, Fleming's value claims rest only on its feature list. The "14 hospitals + 600 primary care centres" figure suggests deployments in regional health services, but none is named publicly.

### Gaps
- No named Fleming reference sites; no SEFH, SEIMC or ESCMID abstract reporting Fleming-derived indicators was found.

## Q3. Silicon ownership transfer (context for "Silicon CDSS/analytics" evidence)

### Takeaway
Asserta bought Grifols' Silicon business unit effective 1 April 2025, taking over 7 employees.

### Cited findings
- CCOO (24 Mar 2025): Asserta bought the Silicon product business unit; the 7 staff were subrogated on 1 Apr 2025 and each received EUR 7,800 compensation — https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/ (CONFIRMED).
- Silicon was released by Grifols in 2006 as an e-prescribing and hospital pharmacy management system — https://www.grifols.com/en/-/automating-hospital-pharmacy-services (CONFIRMED). It is listed in the SEFH CETEC catalogue — https://cetec.sefh.es/producto/silicon/?lang=en.
- The MWC exhibitor profile lists Asserta's portfolio as Silicon, Pharmacy Analytics Manager, Fleming Antimicrobial Stewardship and OncoAnalytics — https://www.mwcbarcelona.com/exhibitors/34420-asserta-global-healthcare-solutions-sl (CONFIRMED (company claim)).

### Gaps
- I found no paper evaluating Silicon's CDSS functions (dose-range alerts, interaction alerts) using "Silicon" and "decision support" in Europe PMC. Earlier SEFH posters mention Silicon validation workflows (e.g. https://www.sefh.es/53congreso/documentos/posters/747.pdf, not read).

## Q4. Events and trade shows 2024–2026 where Asserta exhibited or presented

### Takeaway
The only confirmed event is **MWC Barcelona**: Asserta exhibited in 2024, when Fleming was showcased. The current MWC exhibitor page lists Asserta for the next edition. I found no evidence of Asserta exhibiting at SEFH, SEIMC, ESCMID, EAHP, HIMSS Europe, Expo eHealth, DigitalES or SIFO.

| Event | Date | Evidence | Label |
|---|---|---|---|
| MWC Barcelona 2024 | 26–29 Feb 2024 | Stand CS210/CS220, Congress Square; Fleming presented with the campaign "Be an activist to overcome bacterial resistances" — https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/ ; https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html | CONFIRMED |
| MWC Barcelona (exhibitor profile now displayed for the 2027 edition, 1–4 Mar 2027) | — | Hall 8.0, 4YFN & Partner District, stand 8.0C22.1 — https://www.mwcbarcelona.com/exhibitors/34420-asserta-global-healthcare-solutions-sl. This may be carried over from 2025 or 2026; which edition it applies to is unverified. | INDICATIVE |
| Italy (Medilogy, Milan) | — | A search snippet associates Medilogy with "Fleming platform" for reducing antibiotic resistance, which suggests Medilogy is an Italian distributor or partner. No SIFO congress presence was confirmed — search result only, no primary page (e.g. https://www.linkedin.com/in/claudio-moroni-4aa48612/) | INDICATIVE |
| 70 Congreso SEFH, Málaga, 15–17 Oct 2025; 71 Congreso SEFH, Gran Canaria, 21–23 Oct 2026 | — | No Asserta exhibitor listing found (dates from https://www.immedicohospitalario.es/noticia/53256/el-70-congreso-sefh-arranca-en-malaga-marcando-un-punto-de-infle.html ; https://71congreso.sefh.es/) | UNKNOWN |
| HIMSS Europe 2025 (Paris, 10–12 Jun) / 2026 (Copenhagen, 19–21 May) | — | No Asserta mention found — https://www.himss.org/news-center/himss-european-health-conference-exhibition-heads-copenhagen-2026/ | UNKNOWN |
| SEIMC, ESCMID Global, EAHP, Expo eHealth, DigitalES, SIFO 2025–26 | — | Not found in web searches | UNKNOWN |
| Acadèmia de Ciències Mèdiques de Catalunya activity | — | Search hit listing Monterde; content not read — https://www.academia.cat/detallactivitat/id/26623 | INDICATIVE |

### Inferences
- Asserta seems to market through tech and digital-health venues (MWC/4YFN) and LinkedIn more than through clinical-society exhibitions. After acquiring Silicon, attending SEFH 2025/2026 would be expected, but I could not confirm it.

## Blocked sources / manual checks
- **SEFH e-poster search engines** (e.g. https://eventos.sefh.es/68congreso/e-posters-pantallas/ , 69/70 congress libro de comunicaciones in *Farm Hosp* supplements): JS search engines were not queried. Manually search for "Fleming", "Asserta", "Silicon" and "Pharmacy Analytics".
- **SEFH 70/71 exhibitor lists** (70congreso.sefh.es, 71congreso.sefh.es): not retrieved.
- **ESCMID Global 2025/2026 and SEIMC 2025/2026 abstract books; EJHP EAHP 2025/2026 supplements**: Europe PMC returned no Fleming/Asserta hits, but supplement indexing is incomplete.
- **Google Scholar, Dialnet, TESEO**: not directly searchable here; TDX (tdx.cat) search for "Asserta" returned no results.
- **LinkedIn** (company posts about congresses and Medilogy/SIFO): login-walled.
- **SciELO DOI mismatch** for the Dénia/OFIL paper (pid …006 vs DOI …005): resolve the DOI manually.
- The **RD311/2022 certificate PDF** on asserta.net/fleming was not opened.
