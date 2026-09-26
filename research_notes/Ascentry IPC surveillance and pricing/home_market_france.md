# Ascentry (ex-BYG4lab) – Home-market footprint and contracts (France)

Research cut-off: 2026-09-26. Evidence labels: CONFIRMED (official) = official/independent source; CONFIRMED (company) = company claim; INDICATIVE = my inference, reasoning given; UNKNOWN = searched, not found (places searched named).
DECP = French public procurement open data ("données essentielles de la commande publique"), queried live on 2026-09-26 through the data.economie.gouv.fr Opendatasoft API. Datasets queried: `decp-v3-marches-valides` (pre-2024 format), `decp-2022-marches-valides` (2024+ format), `decp_augmente`. Dataset page: https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/ . TED = EU tenders journal, queried through the TED v3 search API (https://api.ted.europa.eu/v3/notices/search). No internal LUMED intelligence exists for this company.

## Q0. Identity: home country, HQ city, home region, legal entities

### Takeaway
Ascentry is French. Its HQ is in L'Union (31240), a suburb of Toulouse in Haute-Garonne, Occitanie region. It has a second French site in Nancy (Grand Est), which came from the 2020 acquisition of partner4lab / Info Partner. The operating company that holds the public contracts is SIREN 326 649 407 (SIRET 326 649 407 00052). It was formerly called "BYG INFORMATIQUE" and is now registered as "ASCENTRY FRANCE". The holding company is BYG4LAB GROUP (SIREN 915 233 837).

### Cited Findings
- CONFIRMED (official): SIREN 326649407 is registered as "ASCENTRY FRANCE". Head office SIRET 32664940700052, ZA de Montredon, 13 rue d'Ariane, 31240 L'Union, département 31, region code 76 (Occitanie). NAF 58.29C (software publishing). Created 2003-10-01. — [recherche-entreprises API (annuaire-entreprises)](https://recherche-entreprises.api.gouv.fr/search?q=326649407); see also [annuaire-entreprises](https://annuaire-entreprises.data.gouv.fr/entreprise/326649407)
- CONFIRMED (official): Every French public contract found below was awarded to SIRET 32664940700052, listed under the name "BYG INFORMATIQUE". — [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)
- CONFIRMED (official/aggregator): BYG4LAB GROUP (SIREN 915233837) is an SAS at the same L'Union address with share capital of about €49.0M. Its 2024 revenue was about €1.9M, so it is a holding company. — [societe.com](https://www.societe.com/societe/byg4lab-group-915233837.html); [pappers](https://www.pappers.fr/entreprise/byg4lab-group-915233837)
- CONFIRMED (company): The company was founded in France in 1982. Ascentry is the new name of BYG4lab, launched at ADLM 2025, and it combines BYG4lab and Finbiosoft (Finland). — [Newswise press release](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software)
- CONFIRMED (independent): Keensight Capital took a majority stake. BYG4lab then agreed to acquire Finbiosoft (announced March 2024). — [Keensight](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/); [Castrén & Snellman](https://www.castren.fi/cases/byg4lab-and-keensight-capital-acquisition-of-finbiosoft/)
- CONFIRMED (company): BYG acquired partner4lab, a microbiology software publisher in Nancy, with effect from 28 Feb 2020. partner4lab brought the INFECTIO epidemiology/hygiene range and the PILOT.4lab bacteriology middleware. BYG gave its reason as "La seule brique logiciel manquante chez BYG était la microbiologie" ("the only software building block BYG was missing was microbiology"). Staff numbered 66 in 2020, with a revenue target of about €9M for end 2020. About one third of 2019 revenue came directly or indirectly from outside France. — [Spectra Diagnostic n°8, Apr–Jun 2020 (paid feature)](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD008_Publi-Byg.pdf)
- CONFIRMED (company): In Dec 2020 there were about 80 staff, 30+ of them in R&D. BYG also moved into new premises in Nancy, in addition to L'Union. — [Spectra Diagnostic n°12, Dec 2020–Jan 2021 (paid feature)](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD012_Publi-Byg4lab.pdf)
- CONFIRMED (company): 2021 revenue was about €10M. The company claims 4,000 data-management solutions worldwide. The deck states "Février 2020 : Acquisition d'INFO PARTNER", which confirms that partner4lab's legal entity was Info Partner. — [JIB 2021 presentation, Mulot/Mercier/Lelièvre](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf)
- CONFIRMED (official): The Info Partner SIRET is 34931494800036. It appears as the awardee on a 2022 CHU Dijon contract whose object names BYG4LAB (see Q2). — [DECP augmenté](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)

### Inferences
- INDICATIVE: Occitanie is the home region. The Nancy site means Grand Est is a second centre of gravity specifically for microbiology and epidemiology, because the INFECTIO/Ynfectio team came from Nancy. For IPC competitive work, the Grand Est installed base may matter more than Occitanie.
- INDICATIVE: Anyone searching procurement portals should query BYG INFORMATIQUE (SIREN 326649407), ASCENTRY FRANCE, INFO PARTNER (SIREN 349314948) and the product names (EVM, NYNA/nYna, Ynfectio, Infectio, Pilot, Qualynk). No DECP record uses the name "ASCENTRY" yet.

### Gaps
- The annuaire-entreprises web page was not rendered. The API worked, but calls were intermittently reset by the proxy. The date the company changed its name to ASCENTRY FRANCE was not retrieved; check the BODACC or RNE record.

## Q1. Named customers in France (public hospitals, private lab groups, others), split by home region vs rest of France, with products

### Takeaway
Customers were identified almost entirely through DECP/TED records (maintenance contracts), plus one company-published private-group partnership (Unilabs France, 2016). No customer could be confirmed in Occitanie, the home region. Every public buyer found is outside it: Normandy, Centre-Val de Loire, Hauts-de-France, Île-de-France, Auvergne-Rhône-Alpes, Bourgogne-Franche-Comté. Only two buyers are CONFIRMED to use the epidemiology/IPC product: CHU Caen Normandie (Ynfectio, GHT-wide) and a Nièvre-based buyer (INFECTIO LABO / Ynfectio Labo).

### Summary table – confirmed or indicated French users

| # | Customer | Region (home?) | Products | Epidemiology/IPC? | Status | Evidence |
|---|---|---|---|---|---|---|
| 1 | CHU Caen Normandie (buyer for 3 GHT establishments) | Normandie (no) | nYna middleware, **Ynfectio (épidémiologie et hygiène)**, Qualynk, EVM-IH | **YES – Ynfectio** | Active framework, awarded Apr 2024, 44 months (to about end 2027) | CONFIRMED (official) – DECP 20240033001000; TED 348571-2024 |
| 2 | Buyer SIRET 20001120300011, place of performance Nièvre (58) | Bourgogne-Franche-Comté (no) | **INFECTIO LABO / YNFECTIOLABO** | **YES** | Active, notified 2026-02-02, 48 months | CONFIRMED (official) – DECP 2026S00059; buyer name not resolved |
| 3 | CHU Rouen | Normandie (no) | Bacteriology "identification" module + bacteriology analyser connections | Microbiology (not confirmed IPC) | Maintenance notified 2023-04-06, 48 months (to about 2027) | CONFIRMED (official) – DECP 20232023S1951900 |
| 4 | CHU Grenoble Alpes (CHR Grenoble) | Auvergne-Rhône-Alpes (no) | PILOT MALDI software (partner4lab microbiology middleware) | Microbiology | Maintenance notified 2023-04-26, 48 months, MAPA | CONFIRMED (official) – DECP 20232023S0768100 |
| 5 | CHU Saint-Étienne | Auvergne-Rhône-Alpes (no) | BYG4LAB hardware, software and connections for Bruker MALDI mass spectrometers | Microbiology | Maintenance notified 2023-02-06, 48 months | CONFIRMED (official) – DECP 20232023S0565500 |
| 6 | CHU Dijon Bourgogne | Bourgogne-Franche-Comté (no) | "logiciels et connexions … BYG4LAB" (awardee Info Partner, i.e. ex-partner4lab) | Probably microbiology (INDICATIVE) | Maintenance notified 2022-05-04, 48 months (to about 2026) | CONFIRMED (official) – DECP 20222022S1506200 |
| 7 | CHR Orléans | Centre-Val de Loire (no) | BYG-INFORMATIQUE middleware | No evidence | Maintenance notified 2019-02-22, 48 months (expired about 2023; renewal unknown) | CONFIRMED (official) – DECP 20192019S0601500 |
| 8 | CH Beauvais | Hauts-de-France (no) | EVM + "NINA" (nYna) middleware and analyser connections | No evidence | Renewed 2025-01-28, 48 months | CONFIRMED (official) – DECP 2025y7rcyXHbgj00; earlier 2019cty4HwOQH500 |
| 9 | CH Lens (Dr Schaffner) | Hauts-de-France (no) | "Maintenance BYG4LAB pour les laboratoires" | No evidence | 2024-11-21, 12 months | CONFIRMED (official) – DECP 2402 |
| 10 | CH Gonesse (contract notified via CH Saint-Denis SIRET) | Île-de-France (no) | EVM software, hardware and analyser connections | No evidence | 2023-01-02, 48 months | CONFIRMED (official) – DECP 20232022S2329000 |
| 11 | CH Avranches-Granville | Normandie (no) | "BYG" for Ortho Vision blood-grouping analyser, via Ortho Clinical Diagnostics (not a direct contract) | No | 2019-12-16, 48 months, lot 5, open tender | CONFIRMED (official) – DECP 2019k9B9ar2dta00; BYG is an OEM component |
| 12 | UNILABS France (private group) | National | EVM chosen as the single middleware across the network | No evidence | Partnership announced June 2016; current status unknown | CONFIRMED (company) |
| — | Occitanie customers (e.g. CHU Toulouse, CHU Montpellier, CHU Nîmes) | Home region | — | — | None found | UNKNOWN |

### Cited Findings – public contracts (DECP / TED)
- CONFIRMED (official): **CHU Caen Normandie** (buyer SIRET 26140093100018). The DECP object reads "Maintenance évolutive et corrective du middleware « NYNA », du logiciel d'épidémiologie et d'hygiène « Ynfectio », du logiciel de validation des méthodes « Qualynk », du logiciel de gestion de la paillasse d'immunohématologie « EVM-IH »". Other DECP fields:
  - Amount €415,155; duration 44 months; flat-rate price, revisable; framework agreement ("Accord-cadre").
  - Procedure "Procédure avec négociation"; 1 offer received; subcontracting declared "oui"; flagged "marché innovant: oui".
  - Notification date 2024-04-18. One modification was published 2025-12-17, with no amount shown.
  - Oddity: the place-of-performance code is "28", which conflicts with Caen being in Calvados (14). Probably a data-entry error.
  — [DECP id 20240033001000](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)
- CONFIRMED (official): The same award was published on TED as contract award notice **348571-2024** (2024-06-13). Buyer: CHU CAEN NORMANDIE. Winner: BYG INFORMATIQUE. Other TED fields:
  - Procedure type "neg-wo-call" (negotiated without prior call for competition).
  - Framework "fa-wo-rc" (framework agreement without reopening of competition).
  - Winner decision date 2024-04-15; contract conclusion date 2024-04-17.
  - Scope: "pour trois établissements du GHT" (for three establishments of the GHT), i.e. the regional hospital group.
  — [TED 348571-2024](https://ted.europa.eu/fr/notice/-/detail/348571-2024) (fields retrieved via the TED API; the HTML page did not render); [centraledesmarches mirror (now 404)](https://centraledesmarches.com/marches-publics/Caen-CHU-CAEN-NORMANDIE-Maintenance-evolutive-et-corrective-du-middleware-NYNA-du-logiciel-depidemiologie-et-dhygiene-Ynfectio-du-logiciel-de-validation-des-methodes-Qualynk-du-logiciel-de-gestion-de-la-paillasse-dimmunohematologie-EVM-IH-de-la-societe-BYG4LAB-pour-trois-etablissements-du-GHT-et-prestations-associees/250499)
- CONFIRMED (official): **Buyer SIRET 20001120300011**, place of performance Nièvre (58). DECP fields:
  - Object "INX Mise à jour et maintenance de la solution INFECTIO LABO / YNFECTIOLABO – BYG 4 LAB".
  - €10,314.92; 48 months; purchase orders under a framework agreement.
  - "Marché passé sans publicité ni mise en concurrence préalable" (no prior publication or competition); 1 offer.
  - Notified 2026-02-02; published 2026-02-18; source ATEXO.
  — [DECP id 2026S00059](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)
- CONFIRMED (official): **CHU Rouen** (SIRET 26760168000015). Object "Maintenance du module 'identification' et des logiciels de connexion aux automates de bactériologie". €40,028.60; 48 months; notified 2023-04-06. — [DECP augmenté id 20232023S1951900](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)
- CONFIRMED (official): **CHU Grenoble** (SIRET 26380030200014). Object "Maintenance forfaitaire et prestations associées – logiciel PILOT MALDI". Procédure adaptée (MAPA, the French simplified procedure below EU thresholds); 48 months; amount recorded as 0. Notified 2023-04-26. — [DECP augmenté id 20232023S0768100](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)
- CONFIRMED (official): **CHU Saint-Étienne** (SIRET 26420030400014). Object "DTE-EM 2022-28 Maintenance du matériel, des logiciels et des connexions BIG4LAB fournis pour les spectromètres de masse MALDI (BRUKER)". €9,120; 48 months; notified 2023-02-06. — [DECP augmenté id 20232023S0565500](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)
- CONFIRMED (official): **CHU Dijon** (SIRET 26210007600013). Object "Maintenance de logiciels et de connexions informatiques par la société BYG4LAB pour le CHU Dijon Bourgogne". Awardee INFO PARTNER (SIRET 34931494800036). €19,386; 48 months; notified 2022-05-04. — [DECP augmenté id 20222022S1506200](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)
- CONFIRMED (official): **CHR Orléans** (SIRET 26450009100014). Object "Maintenance du Middleware BYG-INFORMATIQUE et prestations associées MNSPPSMC 2018-92". €40,965.80; 48 months. "Procédure négociée avec mise en concurrence préalable" (negotiated with prior competition). Notified 2019-02-22. Four duplicate ids exist: …S0601500 to …S0601503. — [DECP id 20192019S0601500](https://data.economie.gouv.fr/explore/dataset/decp-v3-marches-valides/)
- CONFIRMED (official): **CH Beauvais** (SIRET 26600697200183), two contracts, both "sans publicité ni mise en concurrence préalable":
  - 2019-12-30: "Maintenance produit EVM…"; €7,937; 48 months.
  - Renewed 2025-01-28: "Maintenance du matériel, du logiciel et de la connexion d'automates pour le produit EVM et NINA"; €43,104; 48 months; 1 offer.
  — [DECP ids 2019cty4HwOQH500 / 2025y7rcyXHbgj00](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)
- CONFIRMED (official): **CH Lens** (SIRET 26620932900017). Object "2024-161 – Maintenance BYG4LAB pour les laboratoires du Centre Hospitalier de Lens". €2,639.99; 12 months; no prior publication or competition; notified 2024-11-21. — [DECP id 2402](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/)
- CONFIRMED (official): **CH Gonesse laboratory**. Buyer recorded as CH Saint-Denis SIRET 26930101600011. Object "Maintenance du logiciel EVM, matériels et connexions d'automates pour le laboratoire du Centre Hospitalier de Gonesse". €12,334; 48 months; notified 2023-01-02. — [DECP augmenté id 20232022S2329000](https://data.economie.gouv.fr/explore/dataset/decp_augmente/)
- CONFIRMED (official): **CH Avranches-Granville**. Lot 5 "Maintenance de l'automate de groupage sanguins Orthovision et BYG Ortho Clinical Diagnostic". Awardee Ortho-Clinical Diagnostics France; €36,824; open tender (appel d'offres ouvert); 2019-12-16. BYG software sits inside an IVD vendor's offer (OEM route), not in a direct contract. — [DECP id 2019k9B9ar2dta00](https://data.economie.gouv.fr/explore/dataset/decp-v3-marches-valides/)
- CONFIRMED (official), role unverified: A TED full-text search for "BYG Informatique" also returns two notices whose role for BYG could not be checked:
  - UGAP, the national public purchasing agency (Marne-la-Vallée). "Appareils d'analyses" (analysers); contract notice 495457-2021 and award notice 577496-2021; total value €282,090,000; open procedure.
  - CHU Caen. "Réactifs de laboratoire" (laboratory reagents); 456827-2019 and award 583476-2019; €250,000; open.
  The notice rendering/PDF was blocked, so BYG's role in them is UNVERIFIED. — [TED 577496-2021](https://ted.europa.eu/fr/notice/-/detail/577496-2021); [TED 583476-2019](https://ted.europa.eu/fr/notice/-/detail/583476-2019)

### Cited Findings – private groups and company claims
- CONFIRMED (company): **UNILABS France** chose BYG INFORMATIQUE's EVM suite as its single ("unique") middleware to harmonise production systems across its network. The company news item is dated June 2016. — [BYG4lab case study "Partenariat UNILABS France"](https://byg4lab.com/case-studies/partenariat-unilabs-france/) (now redirects to ascentry.com without the content); [old byg-info.com page, "Juin 2016"](http://byg-info.com/index.php/fr/partenariat-unilabs-france) (503 when fetched; content taken from the search snippet)
- CONFIRMED (company): "Over 400 technical platforms, both private and hospital, in France use their EVM solutions" (1 to 80 instruments each). About 50 staff in Toulouse. This is an older, pre-2020 company profile. — [French Healthcare member page](https://frenchhealthcare.fr/membres/byg4lab/)
- CONFIRMED (company): nYna and pocY "are now in routine use within major French biology structures, both public and private". Growth was 15%/yr for ten years and 25% in 2023. In 2024 the company created a US subsidiary and acquired Finbiosoft. — [Forbes France BrandVoice (paid)](https://www.forbes.fr/brandvoice/byg4lab-lexpert-des-logiciels-pour-les-laboratoires-de-biologie-medicale/) (search snippet; the page failed DNS when fetched)
- CONFIRMED (company): Ascentry held a "Lab Composer User Day" in Paris on 27 Nov 2025. Lab Composer is the renamed nYna. — [Ascentry Lab Composer page](https://www.ascentry.com/products/lab-composer/) (via search snippet)
- CONFIRMED (company): In 2020 partner4lab described INFECTIO as a complete epidemiology and hygiene solution with "nos nombreux clients hospitaliers" (our many hospital customers), and said private labs were also users. No customer names were given. — [Spectra Diagnostic n°8](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD008_Publi-Byg.pdf)
- CONFIRMED (company): The Infection Tracker product page (the new name for Ynfectio) claims "90+ sites across Europe", with no France split. The only named references on the site are Labor Mönchengladbach and SYNLAB Group, and both relate to Validation Manager (Finbiosoft), not Infection Tracker. — [Ascentry Infection Tracker](https://www.ascentry.com/products/infection-tracker/)

### Inferences
- INDICATIVE: The public-hospital installed base is spread across France and weighted to the North/West and East (Normandy, Hauts-de-France, Burgundy, Rhône-Alpes). This is inferred from the DECP hits. Home-region (Occitanie) public wins are UNKNOWN, not proven absent, because many hospitals do not publish maintenance renewals to DECP, especially below €40k.
- INDICATIVE: The microbiology contracts at CHU Grenoble (PILOT MALDI), CHU Saint-Étienne (MALDI connections), CHU Rouen (identification module) and CHU Dijon (Info Partner) come from the partner4lab/Info Partner legacy. Those hospitals are the most likely legacy INFECTIO users, but none is confirmed as using the epidemiology module.
- INDICATIVE: The "90+ sites across Europe" figure for Infection Tracker probably consists mostly of French INFECTIO/Ynfectio sites, given that the product originated in Nancy. This is not verified.
- INDICATIVE: Renewals are typically single-supplier ("sans publicité", 1 offer received). That points to strong lock-in once installed and a low contestability window except at re-procurement or GHT convergence.

### Gaps
- UNKNOWN: whether Biogroup, Cerba/Cerballiance, Eurofins, Synlab France, Inovie or Biomnis use BYG4lab/Ascentry in France. No public statement was found. Searched: web search in English and French, ascentry.com, byg4lab.com (redirects).
- UNKNOWN: any Occitanie customer, e.g. CHU Toulouse, Montpellier, Nîmes or GHT Haute-Garonne. Searched: DECP by SIREN and names, TED, web.
- The Unilabs France relationship: it is not known whether the relationship is still active (2016 announcement only).
- The buyer behind SIRET 20001120300011 (Nièvre) is unresolved because the entreprise API was reset by the proxy. It is possibly a GHT/GCS or CH Nevers entity; to be checked on annuaire-entreprises.
- The BYG4lab/partner4lab case-study archive (byg4lab.com/case-studies, partner4lab.com, byg-info.com) could not be read: redirects, 502/503 errors, and archive.org connection reset.

## Q2. Public contracts: procurement routes, values, notice IDs, frameworks (UGAP/RESAH/UniHA/CAIH)

### Takeaway
DECP holds 11 distinct French contracts naming BYG/BYG4lab as awardee or subject: 10 direct awards to BYG INFORMATIQUE/Info Partner, plus 1 via Ortho Clinical Diagnostics. Values range from €2.6k to €415k. The routes are mostly no-publicity or negotiated sole-source maintenance awards. The largest is CHU Caen's €415k GHT-wide framework covering nYna + Ynfectio + Qualynk + EVM-IH. No UniHA, RESAH or CAIH catalogue listing was found. A UGAP analyser framework (2021) references "BYG Informatique" on TED, but its role is unverified.

### Cited Findings
- CONFIRMED (official): The procurement routes observed are:
  - Negotiated without prior call: CHU Caen 2024 (TED neg-wo-call).
  - "Sans publicité ni mise en concurrence préalable": CH Beauvais 2019 and 2025, CH Lens 2024, Nièvre buyer 2026.
  - Negotiated with prior competition: CHR Orléans 2019.
  - MAPA (procédure adaptée): CHU Grenoble 2023.
  - Open tender via an IVD vendor: Avranches-Granville 2019.
  — [DECP](https://data.economie.gouv.fr/explore/dataset/decp-2022-marches-valides/); [TED 348571-2024](https://ted.europa.eu/fr/notice/-/detail/348571-2024)
- INDICATIVE (arithmetic on CONFIRMED DECP amounts): The direct BYG/Info Partner contracts identified add up to about **€601k** over 2019–2026. The sum is 415,155 + 43,104 + 7,937 + 40,966 + 40,029 + 19,386 + 12,334 + 10,315 + 9,120 + 2,640 + 0 (Grenoble). The Ortho lot (€36,824) is excluded. This is a floor, because DECP is incomplete. — computed from the DECP records above
- CONFIRMED (official): A TED search for "Ascentry" returned 0 notices, and "Ynfectio" returned 1 (Caen). A search for "BYG4lab" returned 7. Of those, 1 is French (Caen). The other 6 are Belgian: CHR Sambre & Meuse (MALDI), Clinique Saint-Pierre Ottignies, HUmani (AST systems, won by bioMérieux Benelux, 2025) and AHSM (AST systems, 2025). Those Belgian notices are out of scope here but show BYG4lab named in AST/MALDI tenders. — [TED API query FT~"BYG4lab"](https://api.ted.europa.eu/v3/notices/search)
- UNKNOWN: No BYG4lab/Ascentry listing was found in UniHA, RESAH or CAIH catalogues. Searched: web search; the UniHA marketplace was not queried because it requires a login. The UGAP 2021 "Appareils d'analyses" framework (TED 577496-2021, €282.09M) mentions BYG Informatique, most likely as the software partner or subcontractor of an analyser lot holder (INDICATIVE, unverified).

### Inferences
- INDICATIVE: The CHU Caen award of Ynfectio together with nYna shows the commercial pattern: Ascentry bundles the epidemiology/hygiene module into a GHT-wide lab-middleware maintenance framework. A LUMED IPC offer would face an incumbent bundled with the lab middleware, running until about Dec 2027 (44 months from April 2024).
- INDICATIVE: The Nièvre INFECTIO LABO / Ynfectio Labo renewal (Feb 2026, 48 months) runs to about Feb 2030.

### Gaps
- BOAMP and PLACE (marches-publics.gouv.fr) were not queried directly. BOAMP full-text and PLACE need interactive search, so results there are unverified, not absent. DECP is known to be incomplete (many hospital MAPA and maintenance awards are unpublished).
- TED notice HTML and PDF rendering was blocked (HTTP 202 / empty). Fields for 348571-2024 came from the TED API only, and it did not return the value field.

## Q3. Epidemiology / surveillance / IPC module users and links with French IPC bodies (CPias, SPARES, PRIMO, SpF, e-SIN)

### Takeaway
Ynfectio (now "Infection Tracker") is Ascentry's epidemiology and hygiene product. Its lineage is INFECTIO from partner4lab/Info Partner in Nancy, first released more than 25 years ago. It has two confirmed French public users: CHU Caen GHT and the Nièvre buyer. No evidence was found of any formal integration with, or automated export to, SPARES, PRIMO, CPias, Santé publique France or e-SIN. Company material mentions only generic "automatic extraction", "Gestion des MDO" (notifiable-disease management) and export in multiple formats.

### Cited Findings
- CONFIRMED (company): Ynfectio was launched in France in 2023 as epidemiology and infectious-event monitoring software for private and hospital labs, connected to the hospital and laboratory information systems (SIH/SIL). Features listed:
  - Real-time alerts for BHRe (emerging highly resistant bacteria), resistance phenotypes and MDO (notifiable diseases).
  - Management of healthcare-associated infections (IAS).
  - Automatic reporting to clinicians.
  - Epidemiological statistics.
  - A hygiene module for the EOH (hospital infection-control team).
  — [Biologiste365 – Surveillance épidémiologique](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/)
- CONFIRMED (company): "BYG Informatique acquired Info Partner four years ago, which owned the Infectio software first released over 25 years ago… we redeveloped and modernized it on our YLine technical platform to create Ynfectio." This is attributed to Wendy van der Linden, Marketing Manager Microbiology, in an article dated 23 May 2024. — [Biologiste365 / Biologiste Infos](https://www.biologiste365.fr/strategie/numerique/quand-les-donnees-de-biologie-ne-sont-quun-depart/)
- CONFIRMED (company): The 2021 deck lists these Ynfectio features: epidemiology bulletins, rounds sheets, unit alerts, "Extraction automatique", "Gestion des MDO", resistance studies, outbreak detection ("bouffées épidémiques") with de-duplication, a hygiene patient file and an expert system. — [JIB 2021 deck](https://presentations.jib-innovation.com/2021/dist/pdf/ROOM_142_PDF/Matthieu-MULOT-Laurence-MERCIER-Christelle-LELIEVRE-BYG4lab_Le_Data_Management_complet_et_innovant_pour_votre_laboratoire.pdf)
- CONFIRMED (independent award, company-reported): Ynfectio won the JIB 2021 "Trophée de l'Innovation en biologie médicale", category "traitement des données de santé" (health-data processing). — [BYG4lab news](https://byg4lab.com/case-studies/byg4lab-remporte-le-trophee-de-linnovation-en-biologie-medicale-%F0%9F%8F%86/); [JIB Trophées](https://jib-innovation.com/trophees)
- CONFIRMED (company): The legacy INFECTIO.GLOBAL recovers bacteriology, serology, parasitology and virology data, and can connect to patient-movement software to track the patient's stay in hospital. INFECTIO.LABO targets private labs and their clinic clients. — [partner4lab INFECTIO.GLOBAL](https://partner4lab.com/shop/infectio-global/); [partner4lab INFECTIO.LABO](https://partner4lab.com/fr/shop/infectio-labo/) (content via search snippet; site returned 502 when fetched)
- CONFIRMED (company): Infection Tracker: "surveillance data and forms … are available for export in different formats". The product page names no national surveillance network. — [Ascentry Infection Tracker](https://www.ascentry.com/products/infection-tracker/)
- CONFIRMED (official): Confirmed users of the epidemiology module are CHU Caen Normandie (3 GHT establishments; DECP 20240033001000 / TED 348571-2024) and the Nièvre buyer (DECP 2026S00059). See Q1.
- CONFIRMED (company): partner4lab/BYG4lab sponsored RICAI, the French antimicrobial-resistance congress, in 2019 and 2022. — [RICAI sponsor partner4lab-2019](https://www.ricai.fr/sponsor-partner4lab-2019); [RICAI sponsor BYG4lab-2022](https://www.ricai.fr/sponsor-byg4lab-2022)
- Negative check: The CHU Limoges "virage numérique" IPC software story (Hospitalia, Dec 2023, deployed 2021, SPIADI integration) does **not** name its vendor. It must NOT be attributed to Ascentry. — [Hospitalia](https://www.hospitalia.fr/L-hygiene-hospitaliere-prend-de-plain-pied-le-virage-numerique_a3993.html)

### Inferences
- INDICATIVE: "Gestion des MDO" and "extraction automatique" suggest support for notifiable-disease workflows and generic exports usable for SPARES/PRIMO surveillance. There is no evidence of a certified or automated feed to SpF, CPias or e-SIN, so this is not a confirmed differentiator.
- INDICATIVE: Ynfectio is lab-centric: it starts from microbiology results and adds an EOH hygiene module. It is not a prescription-linked AMS CDSS. Its overlap with LUMED is strongest on IPC alerting and epidemiology, and weaker on stewardship decision support.

### Gaps
- UNKNOWN: any partnership or project with CPias, SPARES, PRIMO, Santé publique France or e-SIN. Searched: web search in English and French, product pages, Biologiste365.
- UNKNOWN: the number of French INFECTIO/Ynfectio sites and the list of hospital users beyond Caen GHT and the Nièvre buyer.

## Q4. Public funding, grants, awards

### Takeaway
No public grant was found: no Bpifrance, France 2030, i-Nov or Occitanie regional aid linked to BYG4lab or Ascentry. Growth was financed by founder/management ownership and then by private equity (Keensight Capital majority stake, then the Finbiosoft acquisition in 2024).

### Cited Findings
- CONFIRMED (independent): Keensight Capital holds a majority stake and supported the Finbiosoft acquisition (2024). — [Keensight](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/)
- CONFIRMED (company): In 2020 BYG described its shareholding as "personnel et non financier" (personal, not financial), i.e. before Keensight. — [Spectra Diagnostic n°8](https://spectradiagnostic.com/wp-content/uploads/2021/05/SD008_Publi-Byg.pdf)
- CONFIRMED (company-reported): JIB 2021 Innovation Trophy for Ynfectio (see Q3).

### Inferences
- INDICATIVE: The share capital of BYG4LAB GROUP (about €49M) is consistent with a PE-backed acquisition holding created in 2022. The date is inferred from the SIREN 915… series. Keensight entry date: UNKNOWN.

### Gaps
- UNKNOWN: Bpifrance, France 2030, i-Nov or Région Occitanie grants. Searched: web search. Not searched: aides-entreprises.fr, Bpifrance press archive, the Occitanie region's aid register (manual check).
- The Keensight majority-stake date was not retrieved (the PrivSource page was not fetched).

## Blocked / unverified sources for manual checks
- BOAMP (boamp.fr) full-text search for "BYG", "BYG4LAB", "Ynfectio", "Infectio", "nYna", "EVM", "Ascentry": not queried (interactive).
- PLACE (marches-publics.gouv.fr) and regional platforms (Maximilien, e-marchespublics, AWS-achat, Atexo instances): not queried.
- TED notice rendering and PDFs for 577496-2021 / 495457-2021 (UGAP) and 583476-2019 (CHU Caen reagents): blocked (HTTP 202 / empty). BYG's role is unverified.
- UniHA, RESAH, CAIH and UGAP catalogues: login or interactive access needed.
- byg4lab.com/case-studies (redirects to ascentry.com with no archive), byg-info.com (503), partner4lab.com (502), web.archive.org (connection reset): the historical customer news archive was not reviewed.
- Forbes France BrandVoice article (DNS failure) and the Biologiste Infos full article (paywall).
- recherche-entreprises API: intermittent resets. The buyer SIRET 20001120300011 (Nièvre) is unresolved.
- Occitanie hospital annual reports and CHU Toulouse/Montpellier/Nîmes procurement pages: not checked.
