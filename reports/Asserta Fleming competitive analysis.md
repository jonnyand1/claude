# Asserta's Fleming rides Silicon without a CE mark

Competitive analysis of Asserta Global Healthcare Solutions SL and Fleming Antimicrobial Stewardship, prepared for bioMérieux LUMED (AMS/IPC clinical decision support). Research cut-off: 2 October 2026.

## Bottom line

**CE/MDR: UNVERIFIED. There is no public evidence that Fleming is CE-marked.** Queried on 2 Oct 2026, EUDAMED shows no actor registration (SRN) for Asserta and no Asserta device. The only certificate Asserta publishes is ENS (Spanish information security). One trap: EUDAMED does list a Class IIa device called "FLEMING", but it belongs to the unrelated Guangdong Transtek. Registration for legacy devices stays open until about 27 Nov 2026, so this verdict needs re-checking after that date.

**Fleming footprint:** the only figure is a company claim of 14 hospitals and 600+ primary care centres in Spain and Latin America. No public contract or named site was found anywhere.

**Silicon footprint:** the core is Catalonia (ICS, IAS, GSS, ICO and others) and Galicia (an unlimited SERGAS corporate NextGen licence), plus Huelva (Infanta Elena). It is Spain-only in practice.

**Bundling:** Asserta's own site confirms bundling at portfolio level. Fleming is formally a module of Silicon Advanced Analytics and integrates with Silicon NextGen workflows (company claim). No public tender names Fleming. The closest signal is the Reus pharmacy-analytics contract (€110,000), which requires a PROA module (INDICATIVE).

## Confidence labels and research limitations

### Confidence-label legend

| Label | Meaning |
|---|---|
| CONFIRMED (independent/official) | Verified in an official registry, a procurement record, a peer-reviewed paper or an independent third party |
| CONFIRMED (company claim) | Stated by Asserta or its partners or distributors (asserta.net, exhibitor profiles, brochures, CEO interviews); not independently verified |
| CONFIRMED (user-provided internal intelligence) | Taken from the two user-provided documents (00_user_doc_*) and not contradicted by newer research; corrected where newer evidence differs |
| INDICATIVE | An inference from indirect or partial evidence; the reasoning is stated |
| UNKNOWN | Searched for but not found; where we searched is stated |

### Consolidated research-limitations box

| Limitation / blocked source | What it means | Manual check implied |
|---|---|---|
| The user asked to use their Chrome browser, but **Chrome was not connected to this cloud session**. Web search, fetch and public APIs were used instead | Login-walled and JS-only sites could not be browsed interactively | Repeat the key checks in Chrome (LinkedIn, PLACSP, EUDAMED UI) |
| EUDAMED: actor and device modules were queried via the public API on 2 Oct 2026; the **certificate module was not queried**; no UI screenshots | Absence of an actor/device is confirmed for that date; a notified-body certificate under another name cannot be fully excluded | EUDAMED UI: Economic operators "Asserta"; Devices "Fleming"/"Silicon"; Certificates by manufacturer. Repeat after ~27 Nov 2026 |
| AEMPS RECOPS / legacy CCPS-RPS: not queried (interactive application) | No Spanish national registry check | Manual RECOPS search for Asserta, Fleming and Silicon |
| Grifols EUDAMED device lists (SRN ES-MF-000000767 / ES-MF-000000784) not enumerated for Silicon | Silicon's CE status under Grifols is unknown | Filter EUDAMED devices by the Grifols SRNs |
| PLACSP (contrataciondelestado.es): no scriptable full-text search | No national full-text search for "Fleming" | Full-text search for "Fleming", "Fleming PROA" and "Asserta"; verify the Reus SSJRBC 0358/25 and Dénia 002/2024 dates |
| el-vinculo keyword search needs a login; only supplier and contract pages were readable | A Fleming tender may exist under a generic title | Logged-in keyword search |
| PPTs for GSS-2026-186, ICO NSP-2026-03 and IAS CONTR/2026/45 not downloaded | Hidden PROA/Fleming scope in Silicon contracts cannot be excluded | Download the PPTs from contractaciopublica.cat |
| Regional portals for Madrid, Osakidetza, GVA (Valencia) and contratosdegalicia.gal: not searched | Under-counts non-Catalan contracts | Search "Asserta" and "Fleming" on each |
| Italy (ANAC BDNCP, MEPA/Consip, ARIA Sintel, Intercent-ER, START Toscana, SORESA), Switzerland (simap.ch), UK (Find a Tender; Contracts Finder returned no data), France (BOAMP), Germany, Portugal (base.gov.pt returned 404): not queried | European footprint beyond the TED check is unverified | Manual portal searches for Asserta, Fleming and Medilogy |
| LatAm portals (CompraNet, SECOP, SEACE, Mercado Público) and the Bahrain Tender Board: not queried | LatAm customer logos are not verified by contracts | Manual searches |
| TED full "Asserta" result list not fully reviewed (output truncated; first hit was a false positive) | Possible missed EU notices | Review all TED hits |
| LinkedIn, InfoJobs and GitHub blocked or no results | Headcount trend, tech stack and job ads unverified | Manual LinkedIn review |
| Company registries (librebor 403, datoscif 403; einforma, axesor and infonif paywalled) | Exact revenue and profit are unknown | Buy the FY2023–FY2025 accounts |
| SEFH, SEIMC, ESCMID and EAHP abstract books and exhibitor lists not full-text searched | A Fleming poster or exhibition may be missed | Manual search of the e-poster engines and the SEFH 70/71 exhibitor lists |
| CORDIS JS page unreadable; API returned no hits | The "3 EU Horizon consortia" claim is unverified | CORDIS participant search by name/PIC |
| Medilogy brochure: text extracted only; images were partially reviewed in the user doc | A CE logo inside an image cannot be fully excluded | Visual review of all 10 pages |

## Executive summary of key findings

NEW = item dated within the last 12 months (since October 2025).

| # | Finding | Confidence | Source | NEW |
|---|---|---|---|---|
| 1 | Asserta has **no EUDAMED actor registration (no SRN)**. Searches for "asserta" and "Asserta Global" returned 0 actors, while the control search "grifols" returned 9 | CONFIRMED (independent/official), absence as of 2 Oct 2026 | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en | NEW |
| 2 | EUDAMED trade-name "fleming" returns 91 devices, **none from Asserta**. They include a **Class IIa "FLEMING" by Guangdong Transtek** (SRN CN-MF-000010684) | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=fleming&iso2Code=en&languageIso2Code=en | NEW |
| 3 | The only published certification is **ENS category MEDIUM**: cert. 34/5704/26/06711, issued by OCA, valid 30 Jun 2026 to 30 Jun 2028. It is not a medical-device certificate | CONFIRMED (company-hosted certificate) | https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf | NEW |
| 4 | Fleming was **relabelled in Aug 2026** as a "governance-driven intelligence platform" but keeps the "clinical decision support dashboards" wording | CONFIRMED (company claim) | https://asserta.net/fleming-antimicrobial-stewardship/ ; https://asserta.net/page-sitemap.xml | NEW |
| 5 | Fleming is formally **one of three modules of Silicon Advanced Analytics** (with Pharmacy Analytics Manager and OncoAnalytics) and "integrates with Silicon NextGen medication workflows" | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-advanced-analytics/ | NEW (suite pages dated Aug 2026) |
| 6 | Fleming installed-base claim: **14 hospitals + 600+ primary care centres, Spain and LatAm, 7M population, 80+ labs** (Mar 2024). No site is named | CONFIRMED (company claim) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html | |
| 7 | **No public contract, tender or peer-reviewed paper names Fleming**: Spain aggregators, TED "Fleming PROA" = 0, Europe PMC = 0 | UNKNOWN / none found (searches listed in the chapters below) | https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309 ; https://ted.europa.eu | |
| 8 | Asserta acquired Grifols' **Silicon business unit effective 1 Apr 2025**, with 7 staff subrogated | CONFIRMED (independent/official) | https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/ | |
| 9 | Since April 2025, Asserta-direct Silicon contracts have been won at GSS Lleida, ICO, IAS Girona and SAS Huelva (Hospital Infanta Elena) | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578 ; https://el-vinculo.com/licitacion/0001320-2025-servicio-de-mantenimiento-y-reparacion-de-sistemas-paraprocesos-de-5631681 | NEW (Apr–Jul 2026 awards) |
| 10 | SERGAS awarded Asserta a hospital-pharmacy drug catalogue contract that includes **rule-based automatic prescription validation** (€374,472 excl. VAT / €453,111 incl. VAT, Feb 2026) | CONFIRMED (independent/official) | https://ted.europa.eu/en/notice/-/detail/112929-2026 ; https://el-vinculo.com/licitacion/ab-ser1-25-046-contratacion-de-los-servicios-de-consultoria-generacion-y-manteni-5345107 | NEW |
| 11 | Reus SSJRBC 0358/25 (pharmacy data analysis with a **PROA module**) was **awarded to Asserta for €110,000**. This corrects the user doc | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/ssjrbc-0358-25-contratacion-de-un-servicio-de-analisis-de-datos-orientado-al-pro-5818144 ; https://ted.europa.eu/en/notice/-/detail/502545-2024 | |
| 12 | The ICS (8 historic Silicon hospitals) launched its own in-house **PADEICS-PROA** tool | CONFIRMED (independent/official) | https://ics.gencat.cat/ca/detall/noticia/padeics-proa-eina | NEW (18 Nov 2025) |
| 13 | Italy: Medilogy S.r.l. hosts an Italian Fleming brochure (dated 04_25). No Italian customer was found | CONFIRMED (distributor document); customers UNKNOWN | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf | |
| 14 | Company scale: 17 employees (2025), sales band €1.5–3M, sales +148% in 2025 | CONFIRMED (independent aggregator) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions ; https://empresite.eleconomista.es/ASSERTA-GLOBAL-HEALTHCARE-SOLUTIONS.html | NEW (FY2025 accounts filed 31 Aug 2026) |
| 15 | No IPC/infection-control product was found | UNKNOWN / none found (full sitemap, CETEC, EAHP, web) | https://asserta.net/ | |
| 16 | Asserta is listed as an exhibitor at MWC27 (4YFN, Hall 8.0) with Silicon, PAM, Fleming and OncoAnalytics | CONFIRMED (company claim); edition INDICATIVE | https://www.mwcbarcelona.com/exhibitors/34420-asserta-global-healthcare-solutions-sl | NEW |

## 1. Company profile and headcount: a founder-run boutique doubled by a Grifols carve-out

Asserta Global Healthcare Solutions SL (NIF **B65880593**) was incorporated in **October 2012**. It is headquartered at Ronda Maiols 1, Of. 303, 08192 **Sant Quirze del Vallès (Barcelona province)**, has share capital of €20,000, and is still registered under CNAE 7020 (management consulting), not software publishing ([einforma](https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions); [Legal notice](https://asserta.net/legal-notice/)). Founder and CEO **Josep Monterde Junyent** has been sole administrator since 2017. He is a former Director of Central Clinical Services and Pharmacy at Vall d'Hebron for 14 years ([infonif](https://infonif.economia3.com/ficha-empresa/asserta-global-healthcare-solutions-sl); [Monterde profile](https://asserta.net/team/josep-monterde/)). No investor, VC, PE or Grifols stake was found. Grifols' FY2025 20-F contains zero mentions of "Asserta" or "Silicon" ([SEC 20-F](https://www.sec.gov/Archives/edgar/data/1438569/000110465926044901/grfs-20251231x20f.htm)).

The defining event is the purchase of Grifols' **Silicon** pharmacy-software business unit, effective **1 April 2025**. Seven employees were subrogated and each received €7,800; no price was disclosed ([CCOO](https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/)). Sales in 2025 rose **148%** and total assets **133%**, within a sales band of **€1.5–3M** and with thin profitability (ROA 1.2%) ([einforma](https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions); [empresite](https://empresite.eleconomista.es/ASSERTA-GLOBAL-HEALTHCARE-SOLUTIONS.html)).

| Item | Value | Confidence | Source |
|---|---|---|---|
| Legal name / NIF | Asserta Global Healthcare Solutions SL / B65880593 | CONFIRMED (independent/official) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions |
| Incorporation | October 2012 (1 Oct per einforma/infonif; 31 Oct per empresite; a deed-date vs registration-date difference) | CONFIRMED (independent/official); exact day conflicts | https://empresite.eleconomista.es/ASSERTA-GLOBAL-HEALTHCARE-SOLUTIONS.html |
| Administrator | Josep Monterde Junyent (sole); proxy holder Maria Monterde Boix (COO) | CONFIRMED (independent/official) | https://infonif.economia3.com/ficha-empresa/asserta-global-healthcare-solutions-sl |
| Ownership | Privately held, founder/family controlled | INDICATIVE (sole family administrator, €20k capital, no funding records) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions |
| Headcount Mar 2024 | 12 | CONFIRMED (company claim, press) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html |
| Headcount 2025 | 17 (registry average) | CONFIRMED (independent aggregator) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions |
| Team page | 14 named people | CONFIRMED (company claim) | https://asserta.net/team/ |
| LinkedIn band | 11–50 | CONFIRMED (company claim, search snippet) | https://es.linkedin.com/company/asserta |
| Sales 2025 | €1.5–3M band; +148% vs 2024 | CONFIRMED (independent aggregator) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions |
| Estimated 2024 sales | ~€0.6–1.2M (band ÷ 2.48) | INDICATIVE (arithmetic estimate) | same |

Headcount sources conflict (12 → 17 → 14 named → 11–50). The most defensible reading is **about 17–20 staff**, of whom roughly 7 are Silicon engineers and support, about 4–5 are data scientists behind Fleming, PAM and OncoAnalytics, and **no regulatory/QA or dedicated sales function is visible** (INDICATIVE; based on team-page roles plus the CCOO count) ([Team](https://asserta.net/team/)). Company scale claims also drift: the homepage says **76 hospitals**, 194 institutions, 600+ primary care centres, 53,000+ concurrent users and 20+ countries ([Asserta home](https://asserta.net/)), while the April 2025 brochure says **78 hospitals** ([Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)). Both are company claims and likely now include the inherited Silicon base (INDICATIVE).

## 2. Product portfolio: one operational core, one analytics layer

Asserta's 2026 navigation presents four solutions: Silicon NextGen, Silicon Advanced Analytics, Real World Research and Strategy. Fleming is **not** a top-level item; it sits inside the analytics suite ([Asserta home](https://asserta.net/)).

| Product | What it is | Ownership/origin | Confidence | Source |
|---|---|---|---|---|
| Silicon NextGen | Pharmacy, e-prescribing and eMAR operational platform: procurement, inventory, sterile compounding, dispensing, barcode administration; inpatient, ICU, oncology day hospital, paediatrics, outpatient. "Modular design" lets institutions deploy domains "such as oncology, antimicrobial stewardship or sterile compounding" | Grifols (2006) → Asserta (Apr 2025) | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-nextgen/ |
| Silicon Advanced Analytics | Analytics suite: "Explainable AI methodologies; audit-ready algorithm transparency"; "Real-time clinical decision support" | Asserta | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-advanced-analytics/ |
| – Pharmacy Analytics Manager (PAM) | Expenditure, prescribing variability, KPIs, benchmarking; "operates within Silicon NextGen operational environments" | Asserta | CONFIRMED (company claim) | https://asserta.net/pharmacy-analytics-manager/ |
| – Fleming Antimicrobial Stewardship | AMS governance analytics ("Structured AMR Governance Intelligence") | Asserta in-house | CONFIRMED (company claim) | https://asserta.net/fleming-antimicrobial-stewardship/ |
| – OncoAnalytics | Oncology cost, protocol adherence, outcomes/safety, clinical-trial drug monitoring | Asserta | CONFIRMED (company claim) | https://asserta.net/oncoanalytics/ |
| Real World Research | Phase IV, drug utilisation, registries, HEOR; priority domains include AMR and oncology | Asserta | CONFIRMED (company claim) | https://asserta.net/solutions/real-world-research/ |
| Strategy / consulting | "360° Clinical Digital Assessment"; joint bids, UTE models and subcontracting | Asserta | CONFIRMED (company claim) | https://asserta.net/strategic-alliances/ |
| Legacy pages: Silicon Analytics, Clinical Trial Analytics | Earlier 2024 naming; Silicon described as "developed and commercialized by Grifols" | Asserta | CONFIRMED (company claim) | https://asserta.net/silicon-analytics/ ; https://asserta.net/clinical-trial-analytics/ |

## 3. AMS/CDSS products: Fleming is population-level governance analytics, not bedside CDS

### What Fleming does

Fleming (also Fleming-PROA) is an Asserta-developed, multi-device, multilingual web application. It was **publicly launched at MWC Barcelona in late February 2024**, although the CEO said it had then been in use "for some years" ([Diari Sant Quirze](https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/); [ON ECONOMIA](https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html)). It organises indicators into three families: antimicrobial use, microbiology/resistance (including MDR-pathogen incidence and prevalence) and health outcomes (bacteraemia, mortality). It claims alignment with WHO, Joint Commission and CDC recommendations ([Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)).

The vendor text in the SEFH CETEC catalogue adds DDD and DOT per stay or admission by service and unit; DHD and prescribing-quality indicators for primary care; certification-ready reports for **Spain's PRAN PROA team certification** (basic/advanced/excellent); comparison of actual prescribing against the centre's and each unit's resistance map; and identification of "opportunities" for de-escalation, duration adjustment, IV-to-oral switch and antibiogram adequacy ([CETEC Fleming-PROA](https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/)). Vidal Vademecum supplies the drug data feeding Fleming's "algoritmos de ayuda a la toma de decisiones" ([Vademecum](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69)).

| Fleming attribute | Detail | Confidence | Source |
|---|---|---|---|
| Launch | MWC 2024 (26–29 Feb 2024), campaign "Be an activist to overcome bacterial resistances" | CONFIRMED (independent press) | https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/ |
| Indicator families | Use; microbiology/resistance; outcomes | CONFIRMED (distributor brochure) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| Hospital and primary care metrics | DDD/DOT; DHD; PRAN PROA certification reports | CONFIRMED (vendor text in catalogue) | https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |
| "AEMPS certified" wording | Vademecum's product page says "certified by AEMPS". The news item only says it **covers the indicators needed for the EXCELENTE PROA level**. This is an overstatement: there is no AEMPS software certification | INDICATIVE (comparison of the two Vademecum texts) | https://www.vademecum.es/noticia-240108-descubre+la+nueva+aplicaci+oacute+n+web+multidispositivo+desarrollada+para+optimizar+el+uso+de+los+antimicrobianos+y+combatir+el+desarrollo+y+diseminaci+oacute+n+de+las+resistencias+bacterianas_19331 |
| Decision support | "Clinical decision support dashboards"; opportunity identification; Vidal-fed algorithms | CONFIRMED (company/partner claim) | https://asserta.net/fleming-antimicrobial-stewardship/ |
| Patient-level push alerts in the EHR | Not described in any public material | UNKNOWN (Fleming EN/ES pages, CETEC, brochure, Vademecum) | — |
| AI claims | None on the Fleming page; "Explainable AI" at suite level | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-advanced-analytics/ |
| Origin | Developed in-house by Asserta; no hospital spin-off found. Founders' DNA is Vall d'Hebron pharmacy | CONFIRMED (partner text); originating PROA team UNKNOWN | https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69 |
| 2026 repositioning | Pages modified 3 Aug 2026: "governance-driven intelligence platform", stewardship oversight, AMR reporting | CONFIRMED (company claim, sitemap) | https://asserta.net/page-sitemap.xml |
| Peru use case | UTI empiric-therapy analysis in two Peruvian PPP hospitals and their primary care areas; 70% resistance found, leading to new protocols | CONFIRMED (company claim) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html ; https://asserta.net/projects/ |

### Interpretation

Public material shows **retrospective and near-real-time analytics at unit and population level**. It does not show patient-level, event-driven alerts in the prescriber's workflow (INDICATIVE). The founder's interest in IT-supported antimicrobial monitoring goes back decades: he co-authored "Monitoring of antimicrobial therapy by an integrated computer program" in 1999 ([Pharm World Sci](https://doi.org/10.1023/a:1008610912290)). Asserta's other CDS-adjacent work is in prescribing, not AMS. It won a **Sant Pau contract (€195,500, OBE 23/375)** to develop a CDSS for person-centred prescription review ([el-vinculo](https://el-vinculo.com/licitacion/l-objecte-del-present-contracte-es-la-realitzacio-d-un-projecte-transformador-de-4292756)). It is also building **rule-based automatic prescription validation** for SERGAS ([TED 112929-2026](https://ted.europa.eu/en/notice/-/detail/112929-2026)).

## 4. IPC products: none found

No infection-control, HAI-surveillance or outbreak product was found on the full Asserta sitemap, in CETEC, in the EAHP profile or in web searches (UNKNOWN / none found) ([Asserta home](https://asserta.net/); [EAHP](https://eahp.eu/exhibitor/asserta/)). Fleming's MDR-pathogen incidence and prevalence dashboards are AMS-oriented surveillance, not IPC workflow ([Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)).

The one IPC-adjacent signal is **Cantabria's VIGÍA-MMR** preliminary market consultation for an intelligent multidrug-resistant-organism surveillance platform. Asserta was one of six entities interviewed, on 27 Aug 2025, alongside Baxter, CARTIF, La Refactoría, Pragmatech and TreeTechnology. This was a consultation, not a contract, and no subsequent tender was found (CONFIRMED (independent/official)) ([SCS CPM report](https://www.scsalud.es/documents/20117/604213/Informe%20conclusiones%20CPM%20VIGIA.pdf/f990b10d-9431-20c5-5f37-539e213e6404)).

| IPC capability | Asserta status | Confidence | Source |
|---|---|---|---|
| HAI surveillance / IPC workflow product | None found | UNKNOWN (sitemap, CETEC, EAHP, web) | https://asserta.net/ |
| MDR-pathogen incidence/prevalence dashboards (within Fleming) | Yes, AMS-oriented | CONFIRMED (distributor brochure) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| MDRO surveillance pre-procurement (Cantabria VIGÍA-MMR) | Interviewed 27 Aug 2025; no award | CONFIRMED (independent/official) | https://www.scsalud.es/documents/20117/604213/Informe%20conclusiones%20CPM%20VIGIA.pdf/f990b10d-9431-20c5-5f37-539e213e6404 |

## 5. Oncology CDSS and prescription tools: OncoAnalytics on top of Silicon's oncology workflow

Oncology appears in three places. **Silicon NextGen** explicitly covers the "oncology day hospital", can be deployed "by clinical domain (e.g., oncology)", and includes sterile compounding ([Silicon NextGen](https://asserta.net/solutions/silicon-nextgen/)). **OncoAnalytics** covers treatment cost, protocol adherence, outcome and safety indicators, and clinical-trial treatment monitoring ([OncoAnalytics](https://asserta.net/oncoanalytics/); [Onco Analytics 2024](https://asserta.net/onco-analytics/)). The **Institut Català d'Oncologia (ICO)** pays Asserta for Silicon maintenance (NSP-2026-03, €81,191.70, 1 Jul 2026 to 30 Jun 2027) ([el-vinculo](https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578)). The ICO also bought new Silicon functionality for €5,000 on 2 Jun 2025 ([menjometre](https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl)).

Asserta's published evidence is strongest in oncology. Two Vall d'Hebron papers used **Pharmacy Analytics Manager** on Silicon data: a 10-year solid-tumour cost study covering 13,209 patients and €120.4M of antineoplastic spend, and a clinical-trial cost-avoidance study covering 2,930 trials ([Current Oncology 2023](https://doi.org/10.3390/curroncol30090580); [Cancers 2024](https://doi.org/10.3390/cancers16081529)).

| Oncology item | Detail | Confidence | Source |
|---|---|---|---|
| Silicon NextGen oncology domain | Oncology day hospital, sterile compounding, deployable by domain | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-nextgen/ |
| OncoAnalytics | Cost, adherence, outcomes/safety, trial drugs | CONFIRMED (company claim) | https://asserta.net/oncoanalytics/ |
| ICO Silicon maintenance | NSP-2026-03, €81,191.70, 2026–27 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578 |
| ICO new Silicon functionality | €5,000, 02/06/2025 | CONFIRMED (independent/official) | https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl |
| Oncology protocol module names ("Silicon citostáticos", etc.), dose banding, BSA logic | Not published | UNKNOWN (sitemap, CETEC, Grifols page, web) | — |
| CE-marked oncology CDSS | None found | UNKNOWN (EUDAMED trade-name "oncoanalytics" = 0) | https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=silicon%20nextgen&iso2Code=en&languageIso2Code=en |
| Oncology RWE | Vall d'Hebron cost studies; vial fractionation; CLOSER paediatric leukaemia (EU) | CONFIRMED (company claim) | https://asserta.net/projects/ |

## 6. Integrations, deployment model and technology stack: on-premise ETL, no named EHR or LIS connectors

Fleming is sold as **on-premise**: "installed at the customer centre, so data do not leave the institution" unless the institution chooses to share them with the health administration. Its architecture feeds prescription, patient, microbiology, CMBD and consumption data through an ETL/integration layer into the algorithm ([Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf); [Vademecum](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69)). Asserta calls it "platform-agnostic and fully interoperable" with pharmacy systems, EHRs, clinical workstations and IoMT, scalable from a single unit to national level ([Fleming EN](https://asserta.net/fleming-antimicrobial-stewardship/)). **No named EHR or LIS integration is published for Fleming** (UNKNOWN; searched both Fleming pages, CETEC, the brochure, Vademecum and the web for SAP, Cerner/Oracle, SAVAC, HCIS, Gacela, IANUS, Millennium, Dedalus, Modulab, GestLab, OpenLab, GLIMS and WHONET).

| Integration / tech item | Detail | Confidence | Source |
|---|---|---|---|
| Fleming hosting | On-premise at the customer; no SaaS or cloud statement found | CONFIRMED (distributor/partner claim) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| Fleming data sources | Prescription, patients, microbiology, CMBD, consumption; 80+ labs | CONFIRMED (distributor/company claim) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| Fleming ↔ Silicon NextGen | "Integrates with Silicon NextGen medication workflows" | CONFIRMED (company claim) | https://asserta.net/fleming-antimicrobial-stewardship/ |
| Named EHR/LIS vendors for Fleming | None published | UNKNOWN (see above) | — |
| Silicon automation integrations | Pyxis MS3500, Kardex-Mercurio, ROWA (HCUVA Murcia, Grifols era) | CONFIRMED (independent/official) | https://www.carm.es/web/PDescarga?IDCONTENIDO=1618&PARAM=idDocumento%3Dworkspace%3A%2F%2FSpacesStore%2Fbf7bb43e-9d98-40ec-b255-1034857d2524%2F1.0&fechaVersion=24092019091152&descargar=true |
| Silicon legacy interfaces | LDAP, patient census, allergies, lab results, orders/consumption, day-hospital agendas, EDI | CONFIRMED (catalogue) | https://cetec.sefh.es/producto/silicon/?lang=en |
| Silicon platform | Launched 2006; "runs on Unix and uses web technology" | CONFIRMED (Grifols) | https://www.grifols.com/en/-/automating-hospital-pharmacy-services |
| Team skills | J2EE, Java EE, Tomcat, Linux, HL7, FHIR, openEHR, CI/CD; BI/ETL/Big Data | CONFIRMED (staff bios, not product specs) | https://asserta.net/team/jose-pineda-sanchez/ ; https://asserta.net/team/victor-naranjo/ ; https://asserta.net/team/daniel-garcia/ |
| Silicon in Grifols-era AMS research | Used as a data source for AMS studies at Vall d'Hebron and Lleida | CONFIRMED (independent, peer-reviewed) | https://doi.org/10.3390/antibiotics13060511 ; https://doi.org/10.1016/j.infpip.2020.100048 |
| Post-deal Kiro/robotics agreement | Not found | UNKNOWN (Grifols 20-F, web) | https://www.sec.gov/Archives/edgar/data/1438569/000110465926044901/grfs-20251231x20f.htm |

The on-premise ETL model plus batch loads from heterogeneous labs points to a **data-warehouse/BI architecture rather than an embedded event-driven CDS engine** (INDICATIVE).

## 7. Certifications and regulatory status: no MDR footprint at all

### EUDAMED results (queried 2 Oct 2026 via the public API)

| Query | Result | Confidence | Source |
|---|---|---|---|
| Actor name "asserta" / "Asserta Global" | **0 actors**; the control query "grifols" returned 9 (e.g. Laboratorios Grifols ES-MF-000000767) | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en ; https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=20&name=grifols&languageIso2Code=en |
| Device trade name "fleming" | 91 records, none Asserta: Fleming Comercial (69), For.me.sa "Superfleming" IIb (11), Tecnoclínic "FLEMING" Class I (9), **Guangdong Transtek "FLEMING" Class IIa (1; AR MDSS GmbH)**, Radiant Innovation (1) | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=fleming&iso2Code=en&languageIso2Code=en |
| "silicon nextgen", "silicon advanced", "oncoanalytics", "pharmacy analytics", "antimicrobial stewardship" | 0 devices each | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=silicon%20nextgen&iso2Code=en&languageIso2Code=en |
| "PROA" | 189 unrelated devices | CONFIRMED (independent/official) | same API |
| Medilogy (Italian distributor) | Registered manufacturer IT-MF-000041270; only device MediDss CLIN, Class I (its own product, not Fleming) | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&srn=IT-MF-000041270&iso2Code=en&languageIso2Code=en |
| Certificate module | Not queried | UNKNOWN | — |

The user-provided regulatory report could not reach EUDAMED ("Server temporarily unavailable"). The newer API results close that gap: **the absence of an Asserta actor is a stronger signal than the absence of a device**, because actor registration (SRN) precedes device registration (INDICATIVE) ([EC notice](https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en)).

Two timing caveats apply. EUDAMED's Actor and UDI/Devices modules became **mandatory on 28 May 2026**. Legacy devices first placed on the market before that date have until roughly **27 Nov 2026** to register (CONFIRMED (user-provided internal intelligence), citing EC Q&A) ([EUDAMED Q&A](https://health.ec.europa.eu/document/download/0e7327c7-0e06-4fbd-90d3-8ab7bb30fe9f_en?filename=eudamed-qa_en.pdf)). Spain's RECOPS draws its product data from EUDAMED and allows up to six months for national communication ([AEMPS RECOPS](https://www.aemps.gob.es/productos-sanitarios/registros-nacionales-de-productos-recops-rps/)).

**The Guangdong Transtek name collision is a plausible source of any mistaken "Fleming = CE Class IIa" claim** (INDICATIVE: a hypothesis about where such a claim could come from, not proven).

### What Asserta does publish

| Certification / statement | Detail | Confidence | Source |
|---|---|---|---|
| ENS (RD 311/2022) | OCA Instituto de Certificación (ISO 17065 accr. 11/C-PR375); cert. **34/5704/26/06711**; category MEDIUM (all dimensions); 65 measures; audit 03/06/2026; initial certification **30 Jun 2026**, expiry **30 Jun 2028**. Scope: information systems supporting technical assistance, consulting and the development/maintenance of clinical management applications | CONFIRMED (company-hosted certificate) | https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf |
| ENS date contradiction | An "initial certification" on 30 Jun 2026 conflicts with an ENS badge on older pages (the /es/fleming page was last modified Aug 2024) and a CETEC ENS mention. Either the badge predated the certificate or the PDF is a reissue | INDICATIVE | https://asserta.net/es/fleming/ ; https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |
| CE / MDR / "medical device" / Class IIa / notified body / UDI on Fleming pages | Absent (raw HTML inspected) | CONFIRMED (company page, absence) | https://asserta.net/fleming-antimicrobial-stewardship/ ; https://asserta.net/es/fleming/ |
| CE in CETEC entry | Category "Software"; only ENS cited | CONFIRMED (independent catalogue, vendor text) | https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |
| CE in Italian brochure | No CE/MDR/ISO text; cover and architecture images show no CE + NB number | CONFIRMED (distributor document; text plus partial visual) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| ISO 13485 / ISO 27001 | Not claimed. The Security Policy cites ENS, GDPR/LOPDGDD and eIDAS only | CONFIRMED (company page, absence) | https://asserta.net/politica-de-seguridad/ |
| ISO 13485 / IEC 62304 knowledge | Listed only as **personal** expertise of the Silicon Head of Development | CONFIRMED (company page) as personal skill | https://asserta.net/team/jose-pineda-sanchez/ |
| Silicon CE under Grifols | No public statement found | UNKNOWN (Grifols page, CETEC, EUDAMED first page of "silicon"; Grifols device lists not enumerated) | https://www.grifols.com/en/-/automating-hospital-pharmacy-services |

### MDR Rule 11 analysis

Under MDCG 2019-11, software qualifies as MDSW only if the manufacturer's **intended purpose** is medical. Once it qualifies, Rule 11 makes software that provides information for diagnostic or therapeutic decisions **Class IIa at minimum**. It rises to IIb if a wrong decision could cause serious deterioration, and to III if it could cause death or irreversible deterioration ([MDCG 2019-11](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf)). Asserta's public wording pulls in both directions.

| Fleming claim | Regulatory reading | Confidence | Source |
|---|---|---|---|
| "Governance-driven intelligence platform", AMR reporting, stewardship oversight | Supports a non-device (management/analytics) intended purpose | CONFIRMED (company claim); reading INDICATIVE | https://asserta.net/fleming-antimicrobial-stewardship/ |
| "Clinical decision support dashboards"; suite-level "Real-time clinical decision support" | Points toward MDSW; Rule 11 exposure | CONFIRMED (company claim); reading INDICATIVE | https://asserta.net/solutions/silicon-advanced-analytics/ |
| De-escalation, duration, IV-to-oral and antibiogram-adequacy opportunities | Potentially therapeutic information. If patient-specific, it would be consistent with Rule 11 Class IIa or higher | CONFIRMED (vendor text); reading INDICATIVE | https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |
| Vidal-fed "decision-support algorithms" | Same as above | CONFIRMED (partner claim) | https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69 |
| SERGAS rule-based automatic prescription validation (Feb 2026); Silicon dose, frequency and duration checks | Classic Rule 11 MDSW territory; Asserta's MDR exposure is growing | CONFIRMED (official/Grifols); reading INDICATIVE | https://ted.europa.eu/en/notice/-/detail/112929-2026 ; https://www.grifols.com/en/-/automating-hospital-pharmacy-services |

**Verdict: CE/MDR status is UNVERIFIED, and there is no public evidence of CE marking.** The most likely position is that Fleming is marketed as non-device governance analytics while using CDS language that creates Rule 11 exposure (INDICATIVE). A claim of "Fleming CE Class IIa" should be treated as unsupported until Asserta produces primary documents. The absence of public evidence does **not** prove that Fleming lacks a CE mark.

### Documents to request in any tender clarification

| Document | What to verify | Confidence | Source |
|---|---|---|---|
| SRN of the legal manufacturer | Asserta currently has none in EUDAMED, so ask first | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en |
| EU Declaration of Conformity | Manufacturer, product/version, Basic UDI-DI, MDR 2017/745, class, date, signature | CONFIRMED (user-provided internal intelligence; AEMPS guidance) | https://www.aemps.gob.es/productosSanitarios/docs/guia-comercializacion-ps.pdf |
| Notified-body certificate | NB name and 4-digit number (check NANDO), certificate number, scope, validity, modules/versions covered | CONFIRMED (user-provided internal intelligence) | https://health.ec.europa.eu/medical-devices-topics-interest/notified-bodies-medical-devices_en |
| Basic UDI-DI / UDI-DI, label/e-label, IFU | CE + NB number; exact intended purpose | CONFIRMED (user-provided internal intelligence) | https://www.aemps.gob.es/productosSanitarios/docs/guia-comercializacion-ps.pdf |
| Classification justification | Annex VIII Rule 11 rationale | CONFIRMED (user-provided internal intelligence) | https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf |
| ISO 13485 / ISO 27001 certificates | Neither is claimed publicly | CONFIRMED (company page, absence) | https://asserta.net/politica-de-seguridad/ |

## 8. Home-market footprint: Catalonia by count, Galicia by depth

Catalonia accounts for **10 of 13 Asserta-direct contracts**, worth about €733k (€733,269 in the ch. 11 table, including Fundació Sant Hospital, €126,532, which was awarded to Grifols and transferred to Asserta). Galicia carries the single deepest account: the **SERGAS unlimited corporate SILICON NextGen licence** (NB-SER1-24-005, €1,560,006 excl. VAT, awarded to Grifols Movaco on 19/03/2024) plus Asserta's own 2026 drug-catalogue and auto-validation contract ([adjudicacionestic](https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807); [el-vinculo](https://el-vinculo.com/licitacion/ab-ser1-25-046-contratacion-de-los-servicios-de-consultoria-generacion-y-manteni-5345107)).

Since April 2025 Asserta has kept the installed base largely through **negotiated procedures without publicity citing exclusivity** (GSS, ICO, IAS, SAS), which points to strong lock-in (INDICATIVE) ([el-vinculo supplier profile](https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309)). The ICS, the largest Catalan Silicon cluster, built its own **PADEICS-PROA** tool in November 2025. That is a structural barrier to selling Fleming into those 8 hospitals (INDICATIVE) ([ICS](https://ics.gencat.cat/ca/detall/noticia/padeics-proa-eina)).

### Silicon site table (Spain)

| Site / buyer | City / region | Silicon status | Latest evidence | Confidence | Source |
|---|---|---|---|---|---|
| Hospital Universitari Vall d'Hebron (ICS) | Barcelona / CAT | Silicon operational; version not specified | ICS 2021 award (8 hospitals); 2024 maintenance re-tender (est. €3.12M), winner not retrieved | CONFIRMED (user-provided internal intelligence) | https://contractaciopublica.cat/portal-api/descarrega-document-antic/74279276/c93bb9ee041222a1ec4c74befdd69a79 |
| Hospital Universitari de Bellvitge (ICS) | L'Hospitalet / CAT | Same | ICS 2021 | CONFIRMED (user-provided internal intelligence) | same |
| Hospital Germans Trias i Pujol (ICS) | Badalona / CAT | Same | ICS 2021 | CONFIRMED (user-provided internal intelligence) | same |
| Hospital de Viladecans (ICS) | Viladecans / CAT | Same | ICS 2021 | CONFIRMED (user-provided internal intelligence) | same |
| Hospital Arnau de Vilanova (ICS) | Lleida / CAT | Same; Silicon also cited in AMS papers | ICS 2021; Jover-Sáenz 2020/2023 | CONFIRMED (independent/official) | https://doi.org/10.3390/antibiotics12050834 |
| Hospital Joan XXIII (ICS) | Tarragona / CAT | Same | ICS 2021 | CONFIRMED (user-provided internal intelligence) | https://contractaciopublica.cat/portal-api/descarrega-document-antic/74279276/c93bb9ee041222a1ec4c74befdd69a79 |
| Hospital de Tortosa Verge de la Cinta (ICS) | Tortosa / CAT | Same | ICS 2021 | CONFIRMED (user-provided internal intelligence) | same |
| Hospital Dr. Josep Trueta (ICS) | Girona / CAT | Same | ICS 2021; IAS 2018 | CONFIRMED (user-provided internal intelligence) | https://www.ias.cat/ca/noticies/iasgirona/981 |
| IAS – Hospital Santa Caterina | Salt / CAT | Asserta pharmacy software maintenance | CONTR/2026/000000045, €68,934.74, awarded 01/06/2026 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/servei-de-manteniment-del-programari-de-gestio-de-farmacia-de-l-ias-5629903 |
| GSS – Hospital Jaume Nadal Meroles | Lleida / CAT | Silicon implementation by Asserta | GSS-2025-570, €62,030, Sep 2025 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/subministrament-i-implantacio-del-sistema-de-gestio-farmaceutica-silicon-per-a-l-4959768 |
| GSS (institutional) | Lleida / CAT | Silicon maintenance by Asserta | GSS-2026-186, €57,096.67, Apr 2026 | CONFIRMED (independent/official) | https://contratos.gobierto.es/licitaciones/5124441 |
| Institut Català d'Oncologia | L'Hospitalet / CAT | Silicon maintenance by Asserta | NSP-2026-03, €81,191.70, 2026–27 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578 |
| Fundació Sant Hospital | La Seu d'Urgell / CAT | Pharmacy software + integrations; Grifols → Asserta | FSH PN 4-2024, €126,532 | CONFIRMED contract; Silicon attribution INDICATIVE (the word "Silicon" is absent) | https://el-vinculo.com/licitacion/contractacio-del-subministrament-de-software-de-gestio-de-farmacia-i-integracion-4955719 |
| Hospital Comarcal de Móra d'Ebre | Móra d'Ebre / CAT | Silicon + traceability (Grifols, 2024) | EDP STE CT2024266 | CONFIRMED (user-provided internal intelligence) | https://el-vinculo.com/licitacion/contractacio-del-servei-d-evolucio-suport-i-manteniment-del-sistema-silicon-de-g-3865245 |
| SERGAS (corporate) | Galicia | **Silicon NextGen unlimited corporate licence**; individual hospital migration not published | NB-SER1-24-005, €1,560,006 (Grifols, 2024); ~15 years of SERGAS use | CONFIRMED (independent/official) | https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807 ; https://asserta.net/team/miguel-angel-gonzalez-prieto/ |
| SERGAS areas: A Coruña e Cee; CHUS Santiago; Lugo; CHUO Ourense | Galicia | Silicon in use (historic evidence 2016–2023) | Memorias, training guide, 2025 paper | CONFIRMED (user-provided internal intelligence) | https://xxicoruna.sergas.gal/DAnosaorganizacion/386/Area_Sanitaria_Coru%C3%B1a_Cee_Memoria2019_COMPLETA.pdf ; https://dialnet.unirioja.es/descarga/articulo/10317782.pdf |
| SAS – **Hospital Infanta Elena** | Huelva / Andalusia | Maintenance of "software de prescripción electrónica asistida (Silicon®)" | CONTR 2026 0000053787, €31,500, formalised 09/07/2026 | CONFIRMED (independent aggregator summary of the award PDF). **Corrects the user doc**, which inferred Juan Ramón Jiménez | https://el-vinculo.com/licitacion/0001320-2025-servicio-de-mantenimiento-y-reparacion-de-sistemas-paraprocesos-de-5631681 |
| HCU Virgen de la Arrixaca | Murcia | Historic; replaced by SAVAC/MIRA | 2016 install; later replacement documented | CONFIRMED (user-provided internal intelligence) | https://sms.carm.es/sms/licitacion/licitacion/documento?idDoc=R0155139&numExpediente=CSE%2F9900%2F1100991239%2F21%2FPASU |
| Hospital de Dénia | Dénia / Valencia | "Analytics de farmacia" (not Silicon); Advanced Analytics SKU not named | 002/2024, €12,501 | CONFIRMED contract; product INDICATIVE | https://licitaciones.incasursl.com/adjudicacion/722146-002-2024-analytics-farmacia-hospital-denia-atencion-primaria-alicante-alacant |
| Hospital Sant Joan de Reus | Reus / CAT | Pharmacy analytics with a PROA module (not Silicon) | SSJRBC 0358/25, €110,000 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/ssjrbc-0358-25-contratacion-de-un-servicio-de-analisis-de-datos-orientado-al-pro-5818144 |
| Private groups (Quirónsalud, HM, Vithas, Ribera) | Spain | Logos appear on Asserta's Experiences page; no contract or press linkage found | — | CONFIRMED (company claim, logos only); deployment UNKNOWN | https://asserta.net/en/experiences/ |

By region: Catalonia shows the highest density of named sites; Galicia the deepest system-wide penetration; Valencia and Andalusia one site each; Murcia is historic only. **No evidence was found** for Madrid, the Basque Country, Navarra, Aragón, Castilla y León, Asturias, Cantabria (beyond the VIGÍA consultation), Extremadura, Baleares, Canarias or La Rioja (CONFIRMED (user-provided internal intelligence)). Castilla-La Mancha shows only minor Asserta contracts with no product link.

### Fleming site table (Spain and claimed)

| Claimed / candidate site | Evidence | Confidence | Source |
|---|---|---|---|
| "14 hospitals + 600+ primary care centres, Spain and LatAm; 7M population; 80+ labs" | CEO interview (Mar 2024) and Medilogy brochure (Apr 2025); no site named | CONFIRMED (company claim) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html |
| Any named Spanish Fleming hospital | None found | UNKNOWN (el-vinculo all 10 awards, gobierto, menjometre, sociedad.info, Asserta site, SEFH/SEIMC web searches; PLACSP full-text not run) | https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309 |
| Hospital Sant Joan de Reus | Asserta analytics contract requiring "indicadors de suport, seguiment i compliment del programa d'optimització d'ús d'antibiòtics"; Fleming not named | INDICATIVE (PROA functionality from Asserta, most plausibly Fleming) | https://contractaciopublica.cat/portal-api/descarrega-document/300306623/549339D04465FC2CB8DF430C5FE1BF34 |
| Dénia health department | Several Asserta RWR projects plus "Analytics de farmacia" for hospital and primary care; scope detail unknown | INDICATIVE (early data partner; primary-care scope fits the Fleming PHC claim) | https://asserta.net/projects/ |
| Peru: Callao Salud and Villa María del Triunfo Salud | UTI empiric-therapy analysis, two hospitals plus primary care | CONFIRMED (company claim) | https://asserta.net/projects/ |
| ICS 8 hospitals | In-house PADEICS-PROA tool instead | CONFIRMED (independent/official); Fleming presence leans against (INDICATIVE) | https://ics.gencat.cat/ca/detall/noticia/padeics-proa-eina |
| CETEC "Búsqueda por hospital" list | A site-wide CETEC navigation list, **not** a Fleming customer list. Do not cite it as one | CONFIRMED (note on the catalogue) | https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |

## 9. Europe: a Spain-only business with an Italian brochure

| Market | Active contracts | Selling without known contract | Research presence | Legal presence | Confidence | Source |
|---|---|---|---|---|---|---|
| **Spain** | Yes: Silicon (CAT, Galicia, Huelva); analytics (Reus, Dénia, Sant Pau); no Fleming contract | — | Many | HQ Sant Quirze del Vallès | CONFIRMED (independent/official) | https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309 |
| **Italy** | None found | **Medilogy S.r.l. (Milan) hosts the Italian Fleming-PROA brochure (04_25)**. Medilogy is a CDSS vendor (MediDSS, adapted from Duodecim EBMeDS, selected by Regione Lombardia) | Regione Emilia-Romagna and an "istituto" logo; CLOSER Italian experts | None | Distributor document CONFIRMED; partnership agreement UNKNOWN; customers UNKNOWN (TED "Fleming PROA" = 0; ANAC/MEPA/regional portals not queried) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf ; https://www.aboutpharma.com/scienza-ricerca/un-software-supportare-medicini-italiani-nelle-decisioni/ |
| **Switzerland** | None found | None found | None found | None | UNKNOWN (not on Asserta's map; simap.ch not queried) | https://asserta.net/en/experiences/ |
| **UK** | None found | None found | Newcastle University, "greenw" and UK logos; CLOSER UK experts | None | Research: CONFIRMED (company claim); contracts UNKNOWN (Contracts Finder returned no data; Find a Tender not queried) | https://asserta.net/reasearch-projects/closer/ |
| **France** | None found | None found | A "France" research mention, but no French logo identified | None | UNKNOWN (BOAMP not queried; no French buyer in TED hits reviewed) | https://asserta.net/en/experiences/ |
| **Portugal** | None found | None found | None | None | UNKNOWN (base.gov.pt returned 404; Grifols Portugal exists, but no Silicon link) | https://www.racius.com/grifols-portugal-produtos-farmaceuticos-e-hospitalares-lda/ |
| Germany, Czech Republic, Austria, Ireland, Greece | None found | None | Charité, FNUSA, Univerzita Karlova, St Anna (CLOSER); IE/GR map pins | None | Research only, CONFIRMED (company claim) / INDICATIVE | https://asserta.net/en/experiences/ |

The Medilogy relationship is the one contradiction among the notes. One note could not verify it by web search. Another found the Fleming brochure hosted on medilogy.it, which is sufficient to confirm that Medilogy markets Fleming in Italy. The terms, start date and exclusivity of that arrangement remain UNKNOWN ([Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)). TED returned **0 notices** for "Fleming PROA" and for "Silicon Grifols" ([TED](https://ted.europa.eu)).

## 10. Rest of world: logos in LatAm, subcontracting in Bahrain

Asserta claims "20 countries"; its website map pins 17 countries besides Spain ([Global initiatives](https://asserta.net/en/global-initiatives/); [Experiences](https://asserta.net/en/experiences/)). Most European pins are research-consortium partners. Commercial evidence outside Spain consists of **client logos and press quotes**, with no contract found.

| Country | Active contracts | Selling without known contract | Research presence | Legal presence | Confidence | Source |
|---|---|---|---|---|---|---|
| Mexico | Logos: HRAE network (e.g. Oaxaca), ISSEMYM, SS Hidalgo, Bupa; product and dates unknown | — | — | None | CONFIRMED (company claim, logos) | https://asserta.net/en/experiences/ |
| Colombia | Logos: Clínica Reina Sofía, Clínica Pediátrica Colsanitas, Hospital Internacional de Colombia, Keralty, others | — | — | None | CONFIRMED (company claim, logos) | https://asserta.net/en/experiences/ |
| Peru | Logos: Callao Salud SAC, Villa María del Triunfo Salud SAC; UTI-resistance use case | — | RWR project | None | CONFIRMED (company claim) | https://asserta.net/projects/ |
| Chile | Logo: Hospital del Salvador | — | Hospital Roberto del Río (CLOSER) | Possible "Asserta ... Chile" (data-broker profile only) | Client: CONFIRMED (company claim); entity INDICATIVE | https://www.zoominfo.com/p/Marta-Naranjo/3264112084 |
| Argentina, Uruguay | None | — | Garrahan; Pérez Scremini (CLOSER) | None | CONFIRMED (company claim) | https://asserta.net/reasearch-projects/closer/ |
| Bahrain | Logos: King Hamad University Hospital, MoH/Salmaniya; delivered with **Indra** (iSeha national HIS), probably as a subcontractor | Via Indra | — | None | CONFIRMED (company claim); subcontractor role INDICATIVE | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html ; https://oxfordbusinessgroup.com/reports/bahrain/2015-report/economy/bahrain-seeks-to-stay-ahead-of-local-and-regional-health-trends |
| UAE | Map pin only (not Bahrain, which is inconsistent) | — | — | None | UNKNOWN | https://asserta.net/en/experiences/ |
| USA, Ecuador, Brazil, Dominican Republic | Map pins / brochure "USA" only | — | — | None | UNKNOWN | https://asserta.net/en/experiences/ |
| Saudi Arabia, APAC | None | — | — | None | UNKNOWN | — |

Beware look-alike companies that are unrelated: Asserta (Mexico, construction), Asserta Consultores (Chile, agri), Asserta Health (Utah), the Lithuanian "UAB Asserte", and the UK **Fleming Initiative** (Imperial College, which partners with Cepheid) ([asserta.mx](https://asserta.mx/); [Cepheid](https://www.cepheid.com/en-US/insights/insight-hub/antimicrobial-stewardship/2024/10/fleming-initiative-cepheid-announce-partnership-tackle-amr.html)).

## 11. Commercial contracts table

Values exclude VAT unless stated. The notes contain no Fleming-named contracts.

| Customer | Country | Product | Dates | Value | Procurement route | Notice ID | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| SERGAS | Spain | Silicon support/integration (Grifols) | Awarded 09/10/2015 | €473,361.84 | Open | NB-SER1-15-043 | CONFIRMED (user-provided internal intelligence) | https://www.xunta.gal/dog/Publicados/2015/20151211/AnuncioG0003-271115-0001_es.html |
| ICS (8 hospitals) | Spain | Silicon maintenance (Grifols) | 2021 | €982,104 | Open | CSE/CC00/1101226702/21/PNSP | CONFIRMED (user-provided internal intelligence) | https://contractaciopublica.cat/portal-api/descarrega-document-antic/75488703/447b6b959e4e7105140b72737c443ea4 |
| ICS | Spain | Silicon support/maintenance re-tender | 2023–24; winner not retrieved | est. €3,122,678 | Open | CSE/CC00/1101372359/24/PNSP | CONFIRMED (user-provided internal intelligence) | https://el-vinculo.com/licitacion/servei-de-suport-i-manteniment-del-sistema-silicon-de-gestio-de-farmacia-hospita-3531416 |
| Salut Sant Joan Reus–Baix Camp | Spain | Data-source assessment | 01/10/2023 | €12,200 | Minor | n/s | CONFIRMED (independent aggregator) | https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl |
| SERGAS | Spain | **Silicon NextGen** unlimited corporate licence (Grifols) | Awarded 19/03/2024 | €1,560,006 | Open (EU publication) | NB-SER1-24-005 | CONFIRMED (independent/official) | https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807 |
| Hospital de Dénia + primary care | Spain | Pharmacy analytics | Award 20/06/2024 **or** 05/05/2024 (sources conflict) | €12,501 | Minor/simplified | 002/2024 | CONFIRMED; date conflict | https://sociedad.info/spain/supplier/asserta-global-healthcare-solutions-sl-es |
| Salut Terres de l'Ebre (Móra d'Ebre) | Spain | Silicon + MTS traceability (Grifols) | Awarded 07/06/2024 | €72,149 + €7,364 | Open | EDP STE CT2024266 | CONFIRMED (user-provided internal intelligence) | https://el-vinculo.com/licitacion/contractacio-del-servei-d-evolucio-suport-i-manteniment-del-sistema-silicon-de-g-3865245 |
| Salut Sant Joan Reus–Baix Camp | Spain | Pharmacotherapy data analysis **with PROA module** | Published 29/04/2024; awarded 10/07/2024; DOUE award 21/08/2024 | €110,000 (est. €300,000; 2 yrs) | Open (EU) | SSJRBC 0358/25; TED 502545-2024 | CONFIRMED (independent/official). **Corrects the user doc** (winner = Asserta). The "/25" label versus 2024 dates is an oddity to check on PLACSP | https://el-vinculo.com/licitacion/ssjrbc-0358-25-contratacion-de-un-servicio-de-analisis-de-datos-orientado-al-pro-5818144 ; https://ted.europa.eu/en/notice/-/detail/502545-2024 |
| FGS Hospital de Sant Pau | Spain | CDSS for person-centred prescription review ("Codi Medicament") | Awarded 26/11/2024; formalised 19/12/2024 | €195,500 | Open | OBE 23/375 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/l-objecte-del-present-contracte-es-la-realitzacio-d-un-projecte-transformador-de-4292756 |
| Fundació Sant Hospital | Spain | Pharmacy software + integrations | Awarded to Grifols 07/02/2025; to Asserta from 01/04/2025 | €126,532 | Open | FSH PN 4-2024 | CONFIRMED | https://contractaciopublica.cat/portal-api/descarrega-document/301605968/E3663BF94849680139F55882902CDE4B |
| ICO | Spain | Silicon new functionality | 02/06/2025 | €5,000 | Minor | n/s | CONFIRMED (independent aggregator) | https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl |
| GSS | Spain | Silicon supply + implementation (Jaume Nadal Meroles) | Awarded 12/09/2025 | €62,030 | Negotiated without publicity | GSS-2025-570 | CONFIRMED (independent/official) | https://el-vinculo.com/licitacion/subministrament-i-implantacio-del-sistema-de-gestio-farmaceutica-silicon-per-a-l-4959768 |
| SERGAS | Spain | Hospital-pharmacy drug catalogue, interactions model, **rule-based automatic prescription validation** (MRR/NextGenerationEU) | Award notice 22/01/2026; formalised 13/02/2026 | **€374,472 excl. VAT = €453,111 incl. VAT** (est. €499,296) | Open | AB-SER1-25-046; TED 112929-2026 | CONFIRMED (independent/official). **NEW**. Note: one note lists €453,111 as excl. VAT, but €374,472 × 1.21 = €453,111, so it is VAT-inclusive (INDICATIVE) | https://ted.europa.eu/en/notice/-/detail/112929-2026 ; https://el-vinculo.com/licitacion/ab-ser1-25-046-contratacion-de-los-servicios-de-consultoria-generacion-y-manteni-5345107 |
| GSS | Spain | Silicon maintenance | Awarded 06/04/2026 | €57,096.67 | Negotiated | GSS-2026-186 | CONFIRMED (independent/official). **NEW** | https://contratos.gobierto.es/licitaciones/5124441 |
| CatSalut | Spain | "Corporate platform" consultancy; scope not retrieved | 05/05/2026 | €14,784 | Minor | n/s | CONFIRMED; scope UNKNOWN. **NEW** | https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl |
| ICO | Spain | Silicon maintenance, 01/07/2026–30/06/2027 | Awarded 13/05/2026 (notice 19/05) | €81,191.70 | Negotiated | NSP-2026-03 | CONFIRMED (independent/official). **NEW** | https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578 |
| IAS | Spain | Pharmacy software maintenance | Awarded 01/06/2026 | €68,934.74 | Negotiated | CONTR/2026/000000045 | CONFIRMED (independent/official). **NEW** | https://el-vinculo.com/licitacion/servei-de-manteniment-del-programari-de-gestio-de-farmacia-de-l-ias-5629903 |
| SAS – Hospital Infanta Elena | Spain | Silicon® e-prescribing maintenance | Awarded 17/06/2026; formalised 09/07/2026 | €31,500 (€38,115 incl. VAT) | Negotiated | CONTR 2026 0000053787 | CONFIRMED (independent aggregator). **NEW** | https://el-vinculo.com/licitacion/0001320-2025-servicio-de-mantenimiento-y-reparacion-de-sistemas-paraprocesos-de-5631681 |
| Cantabria SCS | Spain | VIGÍA-MMR MDRO surveillance (consultation only) | Interview 27/08/2025 | — | Preliminary market consultation | — | CONFIRMED (independent/official) | https://www.scsalud.es/documents/20117/604213/Informe%20conclusiones%20CPM%20VIGIA.pdf/f990b10d-9431-20c5-5f37-539e213e6404 |

Aggregator totals differ. El-vinculo shows **10 awards, €1,295,896, plus €57,215 in minor contracts**; gobierto shows 6 awards and €620,093 ([el-vinculo](https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309); [gobierto](https://contratos.gobierto.es/adjudicatarios/asserta-global-healthcare-solutions-s-l)).

## 12. Partnerships and collaborations

| Partner | Nature | Confidence | Source |
|---|---|---|---|
| Grifols | Seller of the Silicon business unit (Apr 2025); Kiro robotics stays with Grifols; no post-deal agreement found | CONFIRMED (independent/official); agreement UNKNOWN | https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/ |
| Vidal Vademecum | Drug-knowledge content feeding Fleming's algorithms (Jan 2024) | CONFIRMED (partner claim) | https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69 |
| Medilogy S.r.l. (Italy) | Hosts the Italian Fleming-PROA brochure; distribution terms unknown | CONFIRMED (distributor document) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf |
| Indra | Bahrain national HIS (iSeha) collaboration | CONFIRMED (company claim) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html |
| Generic alliance models | "Joint bids and UTE models... We do not compete with global vendors"; structured subcontracting; no partners named | CONFIRMED (company claim) | https://asserta.net/strategic-alliances/ |
| EU projects: MyHealth (grant 738091), Share4Rare (780262), CLOSER | Research consortia; "3 EU Horizon consortia" claim not verified in CORDIS | CONFIRMED (company claim); CORDIS UNKNOWN | https://asserta.net/reasearch-projects/myhealth/ ; https://asserta.net/reasearch-projects/share4rare/ ; https://asserta.net/reasearch-projects/closer/ |
| SEFH (CETEC catalogue) | Listing only, no partnership. The Silicon entry's supplier conflicts between notes: one shows "Silicon NextGen, provider Asserta", another still shows Grifols (the language versions may differ) | CONFIRMED listing; supplier field contradictory | https://cetec.sefh.es/producto/silicon/ ; https://cetec.sefh.es/producto/silicon/?lang=en |
| Named EHR/LIS/robotics partners (SAP, Oracle, DXC, BD, Omnicell, Swisslog) | None disclosed | UNKNOWN (site, alliances page, web) | — |

## 13. Publications and evidence base: zero Fleming evidence

**Europe PMC full-text searches for "Fleming-PROA" and "Fleming PROA" return 0 hits.** No Fleming outcome data (DDD, DOT, de-escalation, cost) is published anywhere reachable. All three Asserta-authored papers concern oncology or geriatric analytics. Two of them use Asserta's own PAM tool while declaring that the remaining authors have **no conflicts of interest**, leaving the commercial interest undisclosed ([Current Oncology 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10528466/); [Cancers 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11048575/)).

### Company-authored

| Year | Institution | Venue | Topic / result | Asserta tool | Independent? | COI | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| 2023 | Vall d'Hebron | Current Oncology 30(9) | 10-yr solid-tumour drug cost; 13,209 patients; €120.4M | PAM V.2022.1.0 on Silicon data | N (Tomás-Guillén, Monterde @asserta.net) | Asserta interest not disclosed | CONFIRMED (independent, peer-reviewed) | https://doi.org/10.3390/curroncol30090580 |
| 2024 | Vall d'Hebron | Cancers 16(8):1529 | Cost avoidance from trial-supplied drugs; 2,930 trials | PAM V.2022.1.0 | N | Not disclosed | CONFIRMED (independent, peer-reviewed) | https://doi.org/10.3390/cancers16081529 |
| 2025 | Hospital de Dénia | **Revista de la OFIL·ILAPHAR** 35(4), not Farmacia Hospitalaria | Anticholinergic burden, 3,044 patients ≥65; 88.73% ACB 3 | Software not named | N (Enríquez Torres, Monterde Junyent) | "No conflicts" declared | CONFIRMED; DOI suffix mismatch (pid …006 vs DOI …005) to verify | https://scielo.isciii.es/scielo.php?pid=S1699-714X2025000400006&script=sci_arttext ; https://www.ilaphar.org/analisis-de-la-carga-anticolinergica-en-personas-de-edad-avanzada/ |

### Independent papers citing Silicon only as a data source

| Year | Institution | Venue | Silicon role | Independent? | COI (Asserta) | Confidence | Source |
|---|---|---|---|---|---|---|---|
| 2020 | Arnau de Vilanova, Lleida | Infection Prevention in Practice | DDD consumption data from Silicon/SAP | Y | None | CONFIRMED | https://doi.org/10.1016/j.infpip.2020.100048 |
| 2021 | Vall d'Hebron Children's | BMC Infect Dis | Antifungal patients identified via Silicon v11 | Y | None (Gilead ISR grant) | CONFIRMED | https://doi.org/10.1186/s12879-021-05774-9 |
| 2023 | Lleida | Antibiotics 12(5):834 | Data from Silicon/SAP-ARGOS; ~60% exposure reduction attributed to the AMS strategy, not the software | Y | None | CONFIRMED | https://doi.org/10.3390/antibiotics12050834 |
| 2024 | Vall d'Hebron PROA-NEN | Antibiotics 13(6):511 | AMS use and cost data from Silicon v11 | Y | None (pharma grants) | CONFIRMED | https://doi.org/10.3390/antibiotics13060511 |
| 2024 | Galicia | EPMA J | Silicon hit; context not read | Y | Not checked | INDICATIVE | https://doi.org/10.1007/s13167-023-00346-0 |
| 2026 | Spain (carbapenem intervention protocol) | BMJ Open | AMS recommendation acceptance to be extracted from Silicon | Y | None seen | CONFIRMED. **NEW** | https://doi.org/10.1136/bmjopen-2026-118013 |

## 14. Events and trade shows: MWC rather than clinical congresses

| Event | Date | Evidence | Confidence | Source |
|---|---|---|---|---|
| MWC Barcelona 2024 | 26–29 Feb 2024 | Stand CS210/CS220; Fleming launch | CONFIRMED (independent press) | https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/ |
| MWC27 Barcelona | 1–4 Mar 2027 | Exhibitor listing, 4YFN Hall 8.0, stand 8.0C22.1; Silicon, PAM, Fleming, OncoAnalytics. **NEW** | CONFIRMED (company claim); the edition the listing applies to is INDICATIVE | https://www.mwcbarcelona.com/exhibitors/34420-asserta-global-healthcare-solutions-sl |
| EAHP | Year not stated | Exhibitor profile | CONFIRMED (company claim) | https://eahp.eu/exhibitor/asserta/ |
| SEFH 70 (Málaga, Oct 2025) / SEFH 71 (Gran Canaria, 21–23 Oct 2026) | — | No exhibitor listing found | UNKNOWN (exhibitor lists not retrieved) | https://71congreso.sefh.es/ |
| HIMSS Europe 2025/2026, SEIMC, ESCMID Global, Expo eHealth, DigitalES, SIFO | — | Not found | UNKNOWN (web search) | https://www.himss.org/news-center/himss-european-health-conference-exhibition-heads-copenhagen-2026/ |

SEFH 71 (21–23 Oct 2026) is the next opportunity to check Asserta's congress presence after the Silicon acquisition.

## 15. Head-to-head with LUMED: tender-readiness scorecard

**No internal LUMED encounters with Asserta were provided; bioMérieux to confirm.**

| Criterion | Asserta status | Confidence | Source | LUMED |
|---|---|---|---|---|
| Hosting / data residency | Fleming on-premise at the customer; "data do not leave the institution"; no SaaS statement. The Reus contract specified SaaS for analytics | CONFIRMED (distributor/partner claim; official PPT) | https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf ; https://contractaciopublica.cat/portal-api/descarrega-document/300306623/549339D04465FC2CB8DF430C5FE1BF34 | bioMérieux to confirm |
| MDR / CE | No public evidence; no SRN; no EUDAMED device | CONFIRMED (independent/official) for absence; status UNVERIFIED | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en | bioMérieux to confirm |
| ISO 13485 | Not claimed | CONFIRMED (company page, absence) | https://asserta.net/politica-de-seguridad/ | bioMérieux to confirm |
| ISO 27001 / ENS | No ISO 27001; **ENS MEDIUM** (valid to Jun 2028). ENS is a strong advantage in Spanish public tenders | CONFIRMED (company-hosted certificate) | https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf | bioMérieux to confirm |
| Named interoperability | Fleming: none named. Silicon: Pyxis, Kardex, ROWA (historic); HL7/FHIR skills | CONFIRMED (official/company) | https://www.carm.es/web/PDescarga?IDCONTENIDO=1618&PARAM=idDocumento%3Dworkspace%3A%2F%2FSpacesStore%2Fbf7bb43e-9d98-40ec-b255-1034857d2524%2F1.0&fechaVersion=24092019091152&descargar=true | bioMérieux to confirm |
| Live references (AMS) | No named Fleming site; claim of 14 hospitals + 600 PHC | CONFIRMED (company claim); named sites UNKNOWN | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html | bioMérieux to confirm |
| Live references (pharmacy) | Strong: SERGAS, ICS, ICO, GSS, IAS, Infanta Elena | CONFIRMED (independent/official) | https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807 | bioMérieux to confirm |
| Independent evidence | None for Fleming; 3 company-authored non-AMS papers | CONFIRMED (Europe PMC search) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10528466/ | bioMérieux to confirm |
| Local language | Spanish, Catalan, English web; Italian brochure; "multilingual" app | CONFIRMED (company claim) | https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/ | bioMérieux to confirm |
| Company scale / implementation capacity | ~17 staff; €1.5–3M sales; ~4–5 data scientists behind analytics; no visible QA/regulatory or sales team | CONFIRMED (aggregator) / INDICATIVE (split) | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions | bioMérieux to confirm |
| Purchasing frameworks | None found; exclusivity-based negotiated procedures for Silicon maintenance | CONFIRMED (no frameworks found) / INDICATIVE | https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309 | bioMérieux to confirm |
| PRAN PROA certification reporting (Spain) | Claims coverage of all indicators for the EXCELENTE level | CONFIRMED (partner claim) | https://www.vademecum.es/noticia-240108-descubre+la+nueva+aplicaci+oacute+n+web+multidispositivo+desarrollada+para+optimizar+el+uso+de+los+antimicrobianos+y+combatir+el+desarrollo+y+diseminaci+oacute+n+de+las+resistencias+bacterianas_19331 | bioMérieux to confirm |
| IPC module | None | UNKNOWN / none found | https://asserta.net/ | bioMérieux to confirm |

## 16. Competitive implications for bioMérieux LUMED (ANALYST OPINION)

ANALYST OPINION. Asserta is not a broad AMS/IPC competitor across Europe. It is a **Spanish incumbent-adjacent threat**. Its weapon is account control, not product depth. Owning Silicon gives it the pharmacy system, the prescribing data and an exclusivity-justified negotiated-procedure channel in roughly 20 named Spanish sites, including an unlimited NextGen licence across Galicia. Fleming is positioned as the analytics module that "runs on" that data. The danger is therefore not head-to-head AMS tenders, where Fleming has no named references, no evidence and no CE mark. It is **scope creep**: PROA indicators written into pharmacy-analytics or pharmacy-system contracts, as at Reus, or rule-based prescription validation folded into pharmacy-catalogue work, as at SERGAS, before an AMS/IPC tender is ever issued. Watch Galicia and the Catalan non-ICS providers (GSS, IAS, ICO, Fundació Sant Hospital, Terres de l'Ebre) most closely. In the ICS, the in-house PADEICS-PROA tool is a barrier for both vendors.

Regulatory status is LUMED's sharpest lever, but it must be used carefully and on evidence. Tender documents should require an EU DoC, an NB certificate, an SRN and a Basic UDI-DI for any software that produces patient-level antimicrobial therapy recommendations. That turns Asserta's own "clinical decision support" wording into a compliance question. Asserta's likely counter is that Fleming is governance analytics and not an MDSW, which is consistent with its August 2026 rewording. That answer concedes that Fleming does not deliver patient-level CDS. Outside Spain, Asserta's only visible channel is Medilogy in Italy, with no customers found. LUMED should treat Italy as a watch item, not a battleground.

### Battlecard

| Area | Content | Confidence | Source |
|---|---|---|---|
| **Asserta strength** | Owns Silicon pharmacy/e-prescribing; SERGAS unlimited NextGen licence; recurring Catalan maintenance contracts | CONFIRMED (independent/official) | https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807 |
| **Asserta strength** | ENS MEDIUM certified; Spanish and Catalan clinical-pharmacy credibility (Vall d'Hebron founders) | CONFIRMED | https://asserta.net/team/josep-monterde/ |
| **Asserta strength** | PRAN PROA certification-ready reporting; hospital + primary care scope; on-premise data residency | CONFIRMED (company/partner claim) | https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/ |
| **Asserta strength** | Portfolio bundle (Silicon + PAM + Fleming + OncoAnalytics) under one vendor | CONFIRMED (company claim) | https://asserta.net/solutions/silicon-advanced-analytics/ |
| **Asserta weakness** | No public MDR evidence: no SRN, no EUDAMED device, no ISO 13485 | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en |
| **Asserta weakness** | No named Fleming customer; no Fleming publication; no outcome data | CONFIRMED (searches) / UNKNOWN | https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309 |
| **Asserta weakness** | ~17 staff, no visible QA/regulatory team; thin margins | CONFIRMED (aggregator) / INDICATIVE | https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions |
| **Asserta weakness** | No IPC product; no named EHR/LIS integrations; population-level dashboards rather than bedside alerts | UNKNOWN / INDICATIVE | https://asserta.net/fleming-antimicrobial-stewardship/ |
| **Likely claim: "Used in 14 hospitals and 600+ primary care centres"** | Counter: ask for named, contactable references and the year of deployment. No public source names one site | CONFIRMED (company claim; no named site) | https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html |
| **Likely claim: "Clinical decision support"** | Counter: ask for intended purpose, MDR class, NB certificate and SRN. EUDAMED showed no Asserta actor on 2 Oct 2026 | CONFIRMED (independent/official) | https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en |
| **Likely claim: "Certified / AEMPS-certified"** | Counter: the certificate is ENS (information security), and "AEMPS" refers to PROA-team indicator coverage, not software certification | CONFIRMED (certificate) / INDICATIVE (wording) | https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf |
| **Likely claim: "Native integration with your Silicon system"** | Counter: Fleming itself is marketed as platform-agnostic, so integration is not exclusive to Asserta. Ask for HL7/FHIR interface specs. LUMED integration position: bioMérieux to confirm | CONFIRMED (company claim) | https://asserta.net/fleming-antimicrobial-stewardship/ |
| **Likely claim: "Explainable AI"** | Counter: ask for validation data. There is no published Fleming evaluation | CONFIRMED (company claim; no evidence found) | https://asserta.net/solutions/silicon-advanced-analytics/ |
| **Likely claim: "Present in 20+ countries"** | Counter: most non-Spanish pins are research partners; no contract outside Spain was found | CONFIRMED (company claim) / INDICATIVE | https://asserta.net/en/experiences/ |
| **Caution** | Do not state that "Fleming has no CE mark". State that "no public evidence was found". The legacy registration window runs to ~27 Nov 2026 | INDICATIVE | https://health.ec.europa.eu/document/download/0e7327c7-0e06-4fbd-90d3-8ab7bb30fe9f_en?filename=eudamed-qa_en.pdf |

## 17. Information gaps and recommended next checks

| Gap | Why it matters | Where to check | Status |
|---|---|---|---|
| Fleming MDR status (DoC, NB, SRN, UDI) | Central regulatory differentiator | Direct request to contact@asserta.net; EUDAMED certificate module; NANDO; RECOPS | Open; re-check EUDAMED after ~27 Nov 2026 |
| Named Fleming customers (Spain/LatAm) | Validates the 14 hospitals / 600 PHC claim | PLACSP full-text; regional portals; SEFH/SEIMC abstracts; LinkedIn | Open |
| Hidden PROA scope in Silicon contracts | Bundling evidence | PPTs of GSS-2026-186, NSP-2026-03, IAS CONTR/2026/45 on contractaciopublica.cat | Open |
| Reus SSJRBC 0358/25 label vs 2024 dates; Dénia award date conflict | Contract-record accuracy | PLACSP original XML | Open |
| SERGAS AB-SER1-25-046 VAT basis (€374,472 vs €453,111) | Correct value in battlecards | TED 112929-2026 and Galician contract record | Partly resolved (arithmetic indicates €453,111 incl. VAT) |
| SERGAS NextGen hospital roll-out list | Size of the Galician cross-sell base | Execution documents of NB-SER1-24-005; contratosdegalicia.gal | Open |
| ICS Silicon maintenance post-2024 award | Whether the 8 ICS hospitals remain Asserta customers | ICS contract file CSE/CC00/1101372359/24/PNSP | Open |
| CatSalut €14,784 "corporate platform" consultancy scope | Possible link to PROA Cat or a catalogue | contractaciopublica.cat | Open |
| Cantabria VIGÍA-MMR outcome | Possible AMR/IPC tender where Asserta is positioned | SCS / IDIVAL procurement portal | Open |
| Medilogy agreement terms; Italian customers | Italian market threat | ANAC, MEPA, ARIA Sintel, Intercent-ER; Medilogy | Open |
| Switzerland, UK, France, Portugal tenders | Confirms the absence of a European footprint | simap.ch, Find a Tender, BOAMP, base.gov.pt | Open |
| LatAm contract evidence | Validates logo claims | CompraNet, SECOP, SEACE, Mercado Público | Open |
| Silicon CE status under Grifols | Whether Silicon NextGen inherits a device file | EUDAMED by Grifols SRNs; Grifols | Open |
| Exact financials and shareholders | Implementation capacity and staying power | einforma/axesor accounts; BORME | Open (paywalled) |
| ENS certificate date contradiction | Credibility of the certification history | OCA register; Asserta | Open |
| CETEC Silicon supplier field (Asserta vs Grifols) | Catalogue accuracy | CETEC (ES vs EN pages) | Open |
| SEFH 71 (Oct 2026) exhibitor presence | Marketing push after the acquisition | 71congreso.sefh.es | Open; event 21–23 Oct 2026 |
| Private-group deployments (Quirónsalud, HM, Vithas, Ribera) | Logos without evidence | Direct field intelligence | Open |

## Sources

### Asserta company pages and documents
- https://asserta.net/
- https://asserta.net/fleming-antimicrobial-stewardship/
- https://asserta.net/es/fleming/
- https://asserta.net/fleming/
- https://asserta.net/es/fleming-antimicrobial-stewardship/
- https://asserta.net/solutions/silicon-nextgen/
- https://asserta.net/solutions/silicon-advanced-analytics/
- https://asserta.net/es/soluciones/silicon-advanced-analytics/
- https://asserta.net/pharmacy-analytics-manager/
- https://asserta.net/oncoanalytics/
- https://asserta.net/onco-analytics/
- https://asserta.net/silicon-analytics/
- https://asserta.net/clinical-trial-analytics/
- https://asserta.net/solutions/real-world-research/
- https://asserta.net/projects/
- https://asserta.net/strategic-alliances/
- https://asserta.net/en/experiences/
- https://asserta.net/es/experiencias/
- https://asserta.net/en/global-initiatives/
- https://asserta.net/who-we-are/
- https://asserta.net/team/
- https://asserta.net/team/josep-monterde/
- https://asserta.net/team/jose-pineda-sanchez/
- https://asserta.net/team/victor-naranjo/
- https://asserta.net/team/daniel-garcia/
- https://asserta.net/team/toni-huertas-2/
- https://asserta.net/team/juan-jose-ibanez-del-saz/
- https://asserta.net/team/miguel-angel-gonzalez-prieto/
- https://asserta.net/politica-de-seguridad/
- https://asserta.net/legal-notice/
- https://asserta.net/contact/
- https://asserta.net/page-sitemap.xml
- https://asserta.net/solucion-sitemap.xml
- https://asserta.net/reasearch-projects/closer/
- https://asserta.net/reasearch-projects/myhealth/
- https://asserta.net/reasearch-projects/share4rare/
- https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf

### Regulatory and official registries
- https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=20&name=grifols&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=fleming&iso2Code=en&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=silicon%20nextgen&iso2Code=en&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=5&name=Medilogy&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&srn=IT-MF-000041270&iso2Code=en&languageIso2Code=en
- https://ec.europa.eu/tools/eudamed/
- https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en
- https://health.ec.europa.eu/document/download/0e7327c7-0e06-4fbd-90d3-8ab7bb30fe9f_en?filename=eudamed-qa_en.pdf
- https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf
- https://health.ec.europa.eu/medical-devices-topics-interest/notified-bodies-medical-devices_en
- https://health.ec.europa.eu/medical-devices-eudamed/actor-registration-module_en
- https://www.aemps.gob.es/productosSanitarios/docs/guia-comercializacion-ps.pdf
- https://www.aemps.gob.es/productos-sanitarios/registros-nacionales-de-productos-recops-rps/
- https://www.aemps.gob.es/informa/puesta-en-marcha-de-recops-la-nueva-aplicacion-para-el-registro-de-comercializacion-de-productos-sanitarios/

### Public procurement (official and aggregators)
- https://ted.europa.eu/en/notice/-/detail/112929-2026
- https://ted.europa.eu/en/notice/-/detail/502545-2024
- https://ted.europa.eu/en/notice/-/detail/153488-2017
- https://el-vinculo.com/empresa/asserta-global-healthcare-solutions-sl-172309
- https://el-vinculo.com/licitacion/ssjrbc-0358-25-contratacion-de-un-servicio-de-analisis-de-datos-orientado-al-pro-5818144
- https://el-vinculo.com/licitacion/l-objecte-del-present-contracte-es-la-realitzacio-d-un-projecte-transformador-de-4292756
- https://el-vinculo.com/licitacion/contractacio-del-subministrament-de-software-de-gestio-de-farmacia-i-integracion-4955719
- https://el-vinculo.com/licitacion/subministrament-i-implantacio-del-sistema-de-gestio-farmaceutica-silicon-per-a-l-4959768
- https://el-vinculo.com/licitacion/ab-ser1-25-046-contratacion-de-los-servicios-de-consultoria-generacion-y-manteni-5345107
- https://el-vinculo.com/licitacion/servei-de-manteniment-i-suport-del-sistema-silicon-per-a-l-empresa-publica-gesti-5493090
- https://el-vinculo.com/licitacion/servei-de-manteniment-de-l-aplicatiu-siliconper-l-institut-catala-d-oncologia-5657578
- https://el-vinculo.com/licitacion/servei-de-manteniment-del-programari-de-gestio-de-farmacia-de-l-ias-5629903
- https://el-vinculo.com/licitacion/0001320-2025-servicio-de-mantenimiento-y-reparacion-de-sistemas-paraprocesos-de-5631681
- https://el-vinculo.com/licitacion/contractacio-del-servei-d-evolucio-suport-i-manteniment-del-sistema-silicon-de-g-3865245
- https://el-vinculo.com/licitacion/servei-de-suport-i-manteniment-del-sistema-silicon-de-gestio-de-farmacia-hospita-3531416
- https://contratos.gobierto.es/adjudicatarios/asserta-global-healthcare-solutions-s-l
- https://contratos.gobierto.es/adjudicatarios/asserta-global-healthcare-solutions
- https://contratos.gobierto.es/licitaciones/5124441
- https://www.menjometre.cat/entitat/asserta-global-healthcare-solutions-sl
- https://sociedad.info/spain/supplier/asserta-global-healthcare-solutions-sl-es
- https://www.sophia-anphis.es/empresa-licitadora/asserta-global-healthcare-solutions-sl__B65880593
- https://www.adjudicacionestic.com/front/adjudicaciones-contenido.php?id=132807
- https://www.concursospublicos.com/licitaciones/detalle/22424049/licencia-silicon-nextgeneration-la-contratacion-de-la-licencia-corporativa-ilimitada-de-silicon-nextgen-mantenimiento-y-soporte-3n-y-servicios-de-soporte-tecnico-y-apoyo-a-la-instalacion-nb-ser1-24-005-lot-0001-licencia-corporativa-ilimitada-de-silicon-nextgen-mantenimiento-y-soporte-3n-y-servicios-de-soporte-tecnico-y-apoyo-a-la-instalacion
- https://licitaciones.incasursl.com/adjudicacion/722146-002-2024-analytics-farmacia-hospital-denia-atencion-primaria-alicante-alacant
- https://contractaciopublica.cat/portal-api/descarrega-document/300306623/549339D04465FC2CB8DF430C5FE1BF34
- https://contractaciopublica.cat/portal-api/descarrega-document/301605968/E3663BF94849680139F55882902CDE4B
- https://contractaciopublica.cat/portal-api/descarrega-document/302453845/94EB2D97B1C413A63968B75F17BDB755
- https://contractaciopublica.cat/portal-api/descarrega-document/301965131/7FF94E8000B6B465E6EC0CD0AAF2117E
- https://contractaciopublica.cat/portal-api/descarrega-document-antic/74279276/c93bb9ee041222a1ec4c74befdd69a79
- https://contractaciopublica.cat/portal-api/descarrega-document-antic/75488703/447b6b959e4e7105140b72737c443ea4
- https://contractaciopublica.cat/portal-api/descarrega-document-antic/93497676/6389bf47058e60d2f761ac9bf69c42bd
- https://www.xunta.gal/dog/Publicados/2015/20151211/AnuncioG0003-271115-0001_es.html
- https://www.carm.es/web/PDescarga?IDCONTENIDO=1618&PARAM=idDocumento%3Dworkspace%3A%2F%2FSpacesStore%2Fbf7bb43e-9d98-40ec-b255-1034857d2524%2F1.0&fechaVersion=24092019091152&descargar=true
- https://sms.carm.es/sms/licitacion/licitacion/documento?idDoc=R0155139&numExpediente=CSE%2F9900%2F1100991239%2F21%2FPASU
- https://datosabiertos.regiondemurcia.es/carm/catalogo/hacienda/contratos-carm-2016-excluidos-contratos-menores
- https://www.scsalud.es/documents/20117/604213/Informe%20conclusiones%20CPM%20VIGIA.pdf/f990b10d-9431-20c5-5f37-539e213e6404

### Company registries and financial aggregators
- https://www.einforma.com/informacion-empresa/asserta-global-healthcare-solutions
- https://infonif.economia3.com/ficha-empresa/asserta-global-healthcare-solutions-sl
- https://empresite.eleconomista.es/ASSERTA-GLOBAL-HEALTHCARE-SOLUTIONS.html
- https://es.linkedin.com/company/asserta
- https://www.sec.gov/Archives/edgar/data/1438569/000110465926044901/grfs-20251231x20f.htm
- https://www.sec.gov/Archives/edgar/data/1438569/000110465925017501/tm257688d1_6k.htm
- https://www.zoominfo.com/p/Marta-Naranjo/3264112084
- https://www.racius.com/grifols-portugal-produtos-farmaceuticos-e-hospitalares-lda/

### Press, partners, catalogues and health-system news
- https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html
- https://www.elnacional.cat/oneconomia/ca/economia/monterde-ceo-asserta-gran-repte-tecnologic-combatre-bacteries_1169740_102.html
- https://www.diarisantquirze.cat/la-santquirzenca-asserta-global-healthcare-solutions-presenta-una-innovadora-app-al-mobile-2024/
- https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/
- https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69
- https://www.vademecum.es/noticia-240108-descubre+la+nueva+aplicaci+oacute+n+web+multidispositivo+desarrollada+para+optimizar+el+uso+de+los+antimicrobianos+y+combatir+el+desarrollo+y+diseminaci+oacute+n+de+las+resistencias+bacterianas_19331
- https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/
- https://cetec.sefh.es/producto/silicon/
- https://cetec.sefh.es/producto/silicon/?lang=en
- https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf
- https://www.medilogy.it
- https://www.aboutpharma.com/scienza-ricerca/un-software-supportare-medicini-italiani-nelle-decisioni/
- https://www.grifols.com/en/-/automating-hospital-pharmacy-services
- https://grifols.com/-/logister
- https://www.grifols.com/documents/3627767/3632465/05_np_19062006_signs_agreement_kardex_latin_america_en.pdf
- https://www.managementmedication.com/en/spain/pharmacy-information-systems-epoee/silicon
- https://ics.gencat.cat/ca/detall/noticia/padeics-proa-eina
- https://www.ias.cat/ca/noticies/iasgirona/981
- https://www.quironsalud.com/hospital-barcelona/ca/sala-de-premsa/noticies/dia-europeu-us-prudent-antibiotics
- https://oxfordbusinessgroup.com/reports/bahrain/2015-report/economy/bahrain-seeks-to-stay-ahead-of-local-and-regional-health-trends
- https://www.cepheid.com/en-US/insights/insight-hub/antimicrobial-stewardship/2024/10/fleming-initiative-cepheid-announce-partnership-tackle-amr.html
- https://asserta.mx/
- https://xxicoruna.sergas.gal/DAnosaorganizacion/386/Area_Sanitaria_Coru%C3%B1a_Cee_Memoria2019_COMPLETA.pdf
- https://lugomarinamonforte.sergas.gal/DDocenciaformacioneinvestigacion/23/FARMACIA%20HOSPITALARIA%20FIR%20CHUL.pdf
- https://www.eldiario.es/galicia/pacientes-oncologicos-retrasos-revisiones-santiago_1_4014961.html

### Events
- https://www.mwcbarcelona.com/exhibitors/34420-asserta-global-healthcare-solutions-sl
- https://eahp.eu/exhibitor/asserta/
- https://71congreso.sefh.es/
- https://www.himss.org/news-center/himss-european-health-conference-exhibition-heads-copenhagen-2026/

### Publications
- https://doi.org/10.3390/curroncol30090580
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10528466/
- https://doi.org/10.3390/cancers16081529
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11048575/
- https://scielo.isciii.es/scielo.php?pid=S1699-714X2025000400006&script=sci_arttext
- https://www.ilaphar.org/analisis-de-la-carga-anticolinergica-en-personas-de-edad-avanzada/
- https://doi.org/10.1186/s12879-021-05774-9
- https://doi.org/10.3390/antibiotics13060511
- https://doi.org/10.1016/j.infpip.2020.100048
- https://doi.org/10.3390/antibiotics12050834
- https://doi.org/10.1136/bmjopen-2026-118013
- https://doi.org/10.1007/s13167-023-00346-0
- https://doi.org/10.1023/a:1008610912290
- https://dialnet.unirioja.es/descarga/articulo/10317782.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6544138/
