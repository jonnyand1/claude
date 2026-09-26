# Ascentry (ex-BYG4lab): products, IPC/AMS features, integrations, deployment, tech stack, certifications

Research date: 2026-09-26. Labels: CONFIRMED (independent/official source), CONFIRMED (company claim), INDICATIVE (inference, reasoning given), UNKNOWN (searched and not found).
Blocked or unreadable sources, to check by hand: web.archive.org (WebFetch refused; curl tunnel closed, so no archived byg4lab.com pages were read); LinkedIn (not fetched); BusinessWire QuidelOrtho press release (HTTP 403); Biologiste365 "Quand les données de biologie ne sont qu'un départ" (paywalled after the intro); EUDAMED (not queried, because the public UI is JS-only); Spectra Diagnostic PDFs n°35 (Nov 2024) and n°41 (Nov 2025) (downloaded, but text extraction failed because of font encoding). Every old byg4lab.com URL now returns a 301 redirect to ascentry.com, so legacy product pages cannot be read directly.

## 1. Company basics and the rebrand

### Takeaway
BYG4lab rebranded as Ascentry at ADLM 2025 in Chicago (announced 27–28 July 2025). The website publisher is BYG4lab Group SAS, L'Union (Toulouse metro area), France. The medical-device software is made by BYG Informatique SAS ("Ascentry France") under ISO 13485. Finbiosoft Oy ("Ascentry Finland") was acquired in March 2024.

### Cited Findings
- The rebrand was announced at ADLM 2025 in Chicago (27–30 July 2025). The press release is dated 28 July 2025, CEO Cyril Verhille is quoted, and it names four products: Validation Manager, Lab Composer, POC Controller, Infection Tracker. CONFIRMED (company claim, via newswire) — [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software)
- The branding agency says the rebrand followed BYG4lab's acquisition of Finbiosoft. The name blends "ascendancy" and "laboratory". CONFIRMED (agency claim) — [Brandpie](https://brandpie.com/work/ascentry/)
- The website publisher is **BYG4lab Group SAS**, SIREN 915 233 837, 13 rue d'Ariane, 31240 L'Union, France. The site is hosted by OVHcloud in Roubaix. Subsidiaries exist in France, Finland and the US. CONFIRMED (company legal notice) — [Ascentry legal notice](https://www.ascentry.com/legal-notice/)
- Company timeline: BYG founded 1982. Cyril Verhille acquired it in 2012 (ISO 9001, about 20 staff). ISO 13485:2016 obtained in 2014–2016. Info Partner acquired 2020 (microbiology and infection control). Keensight Capital investment and 100+ employees in 2022–2023. US subsidiary, Finbiosoft acquisition, advisory board and rebrand in 2024–2025. Stated figures: 120 employees, 4,500+ labs, 23% of revenue spent on R&D. CONFIRMED (company claim) — [Ascentry About us](https://www.ascentry.com/about-us/)
- On 14 March 2024 BYG4lab announced it would acquire Finbiosoft (Finland, founded 2011, customers in 16 countries), backed by Keensight Capital. BYG4lab is described as serving over 4,500 labs, in 11 languages. CONFIRMED (investor press release) — [Keensight](https://keensight.com/byg4lab-to-acquire-finbiosoft-a-leading-software-provider-for-medical-laboratories-with-the-support-of-keensight-capital/)
- Aggregators give BYG Informatique's HQ as L'Union, France, and the Finbiosoft deal date as 14 or 18 March 2024. The two dates differ slightly (exclusivity signing vs closing?). CONFIRMED (aggregator) — [PitchBook](https://pitchbook.com/profiles/company/58554-73)

### Inferences
- There are two French legal entities. BYG4lab Group SAS (SIREN 915…, registered around 2022) looks like a holding company, probably created with the Keensight deal. BYG Informatique SAS is the manufacturer and ISO 13485 holder. INDICATIVE: based on the SIREN range and the trust-page wording.

### Gaps
- Revenue: UNKNOWN (not in the Keensight, About or Newswise pages).
- The exact closing date of the Finbiosoft deal is unclear (14 vs 18 March 2024 across sources).

## 2. Full product list (legacy BYG4lab names and current Ascentry names)

### Takeaway
The current portfolio has four products: Lab Composer (middleware/data management), POC Controller (POCT management), Infection Tracker (IPC/AMS epidemiology) and Validation Manager (cloud method validation, from Finbiosoft). Legacy BYG4lab names were B-Link (connector), EVM (central-lab middleware), Pilot NextGen (microbiology middleware), and the Yline web platform with nYna (central lab), pocY/Ypoc (POCT) and Ynfectio (epidemiology). The names "Bylis", "Bymanager" and "BYG4Epi" that the brief mentions were **not found**. Ascentry does not appear to sell a LIS of its own. It positions itself as vendor-neutral middleware that sits beside third-party LIS products.

### Cited Findings
- The legacy portfolio included the universal connector B-Link™, EVM™ (central lab) and Pilot NextGen® (microbiology). The new Yline® web-based baseline includes nYna® (central lab), pocY® (POCT) and Ynfectio® (epidemiology). CONFIRMED (company claim, QuidelOrtho/BYG4lab press release of 24 July 2023, read via search snippet because the page returned 403) — [BusinessWire](https://www.businesswire.com/news/home/20230724368435/en/QuidelOrtho-Partners-With-BYG4lab-to-Strengthen-Informatics-Offerings); [QuidelOrtho](https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings)
- Yline is described as a "full-web", fully interoperable base: multi-site and multi-LIS, works in any browser, and connects to any instrument. nYna and pocY were in routine use in major French public and private labs. CONFIRMED (trade press / company claim) — [Biologiste365 – Yline](https://www.biologiste365.fr/a-decouvrir/yline-linnovation-au-service-de-la-digitalisation-des-laboratoires-de-biologie-medicale/)
- Launch pages: "Lancement nYna®" and "pocY® middleware for EBMD (POCT)". The pocY product page URL is titled "Ypoc®". CONFIRMED (company) — [byg4lab nYna launch](https://byg4lab.com/case-studies/lancement-nyna-votre-nouvelle-generation-de-middleware/); [byg4lab Ypoc](https://byg4lab.com/en/product-pocy/)
- **Lab Composer** is a vendor-neutral, modular data-management platform. Features: custom dashboards, smart multi-discipline validation, an **expert rule engine**, dual-layer QC (internal QC plus patient moving averages), TAT monitoring and LIS backup continuity. Add-on modules: Master Data Management and custom ETL for BI. Claims up to 95% more autovalidation. Native multi-site and multi-LIS support. CONFIRMED (company claim) — [Lab Composer](https://www.ascentry.com/products/lab-composer/)
- **POC Controller** is a vendor-neutral, cloud-based POCT management platform. Features: operator certification/competency matrix, instrument map and connection status, bidirectional connectivity, centralised QC, LIS integration. CONFIRMED (company claim) — [POC Controller](https://www.ascentry.com/products/poc-controller/)
- **Validation Manager** is cloud software for instrument and method verification/validation. It imports data from instruments, middleware, LIS or Excel. Reference customers: SYNLAB, several NHS bodies (Dumfries & Galloway, Bedfordshire, Salford), Cork University Hospital and German labs. Stated scale: 18 countries and 10,000+ verifications. CONFIRMED (company claim) — [Validation Manager](https://www.ascentry.com/products/validation-manager/)
- There is also an offering for LIS vendors ("expand the value of your LIS"). CONFIRMED (company) — [Ascentry LIS providers](https://www.ascentry.com/solution/lis-providers/)
- Named homepage clients/partners: Binding Site, Stago, Thermo Fisher Scientific, SYNLAB, Unilabs, NHS, Finnish Red Cross Blood Service. CONFIRMED (company claim) — [ascentry.com](https://www.ascentry.com)

### Inferences
- Name mapping: nYna/EVM → Lab Composer; pocY/Ypoc → POC Controller; Ynfectio → Infection Tracker; Finbiosoft Validation Manager keeps its name. INDICATIVE. The Ynfectio → Infection Tracker mapping is strong because byg4lab.com/en/product-ynfectio/ 301-redirects to ascentry.com/en/product-ynfectio/, which serves the Infection Tracker page. The other two mappings rest only on matching functional scope. Where Pilot NextGen (microbiology middleware) went is unclear; it may have been folded into Lab Composer.

### Gaps
- Bylis, Bymanager, BYG4Epi: UNKNOWN. Searched ascentry.com and general web; not found and probably not real product names.
- AI features: UNKNOWN. No AI or ML claims appear on the Newswise launch release or on any product page read. The only related wording is "Automated intelligence" as a heading on the Infection Tracker page.
- 2024–2026 version numbers and release notes: UNKNOWN.

## 3. IPC focus: Infection Tracker (formerly Ynfectio, before that Infectio)

### Takeaway
Ascentry has a dedicated IPC and AMR epidemiology product, **Infection Tracker**. It descends from Info Partner's "Infectio" (more than 25 years old), was rebuilt on Yline as Ynfectio (French launch February 2023) and was renamed after the 2025 rebrand. Features: real-time alerts (BHRe/CPE, resistance phenotypes, notifiable diseases), alerts on readmission of MDRO carriers and their contacts, a hygiene (EOH) module, filters by ward/building/facility, configurable surveillance questionnaires, automated antibiograms and statistics, and scheduled reports. It is fed from the LIS and linked with the HIS. The company claims 90+ sites in Europe.

### Cited Findings
- Infection Tracker is "a unified platform for infection control and antimicrobial stewardship" that links microbiology labs and IPC teams. Stated capabilities: real-time alerts on critical pathogens with **patient contact tracing**, outbreak detection, automated antibiogram generation, on-demand epidemiological statistics, configurable questionnaires and surveillance forms, compliance with national and international guidelines, and support for multi-site networks with interoperable databases. Covers bacteriology, virology, parasitology and mycology (culture/ID, AST, blood cultures, molecular, urine cytology). Claims "25+ years microbiology expertise" and "90+ sites in Europe". The page was published 9 Dec 2025 and modified 9 Feb 2026 (schema.org metadata). CONFIRMED (company claim) — [Infection Tracker](https://www.ascentry.com/products/infection-tracker/)
- Product FAQ (verbatim substance):
  - (a) It is connected to the LIS, and "all data in the LIS system can be sent to Infection Tracker" for alerts and reports.
  - (b) It can alert when a **known MDRO carrier is readmitted**, and also when **patients who were in contact with MDRO carriers** are readmitted.
  - (c) Infection preventionists can filter patients by **department, facility, building**.
  - (d) A statistics module exports every data field and the completed surveillance forms in several formats.
  - (e) Users can set up their own reports for **ID specialists and pharmacists**, on any schedule (daily, weekly, monthly).
  CONFIRMED (company claim) — [Infection Tracker FAQ](https://www.ascentry.com/products/infection-tracker/)
- Ynfectio (BYG4lab) launched in France in **February 2023**. It connects to the SIH (HIS) and SIL (LIS). Features: real-time alert monitoring of BHRe, resistance phenotypes and MDO (notifiable diseases); management of healthcare-associated infections (IAS); automatic reporting to clinicians and prescribers; epidemiological statistics; a hygiene module for EOH teams. Built on Yline. Aimed at private and public labs. CONFIRMED (trade press relaying company) — [Biologiste365 – Surveillance épidémiologique](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/)
- Infectio (Info Partner) was "one of the pioneers of digital management of antibiotic resistance data, epidemiology and hygiene". Its first version dates back more than 25 years. BYG acquired Info Partner around 2020 and redeveloped Infectio on Yline as Ynfectio (Wendy van der Linden, quoted May 2024). CONFIRMED (trade press, partly paywalled) — [Biologiste365 – Quand les données de biologie…](https://www.biologiste365.fr/strategie/numerique/quand-les-donnees-de-biologie-ne-sont-quun-depart/)
- There is a BYG4lab news page on the acquisition of "l'ensemble des activités de la société INFOPARTNER (Partner4lab)". It now redirects to Ascentry news. The About page gives 2020 for the Info Partner acquisition. CONFIRMED (company) — [byg4lab acquisition page](https://byg4lab.com/case-studies/acquisition-de-lensemble-des-activites-de-la-societe-infopartner-partner4lab/); [About us](https://www.ascentry.com/about-us/)
- Marketing collateral: a white paper and an SFM plenary talk titled "Les bénéfices d'un système d'épidémiologie et d'hygiène centralisé". CONFIRMED (company) — [White paper](https://byg4lab.com/case-studies/%F0%9F%94%B5-livre-blanc-les-benefices-dun-systeme-depidemiologie-et-dhygiene-centralise/); [SFM plenary](https://byg4lab.com/case-studies/%F0%9F%8E%99%EF%B8%8F-pleniere-sfm-les-benefices-dun-systeme-depidemiologie-et-dhygiene-centralise/)
- Search-engine snippet of the legacy Ynfectio page: "epidemiology and hygiene solution featuring real-time alerts, resistance evolution tracking, and automatic reporting for **CONSORES/SCIENSANO**". CONFIRMED (company claim, snippet only; the live page now redirects and the archive was blocked) — [byg4lab Ynfectio (legacy URL)](https://byg4lab.com/en/product-ynfectio/)

### Inferences
- **Data sources:** mainly lab data from the LIS. Readmission and contact alerts, plus ward/building filters, need patient location and admission (ADT) data. This is presumably HIS/ADT data through the "HIS integration", though no ADT message type is named. INDICATIVE.
- **Pharmacy data:** no evidence that it ingests pharmacy or dispensing data. Pharmacists appear only as report recipients. INDICATIVE.
- **Standalone vs LIS module:** it is a standalone, vendor-neutral application fed by any LIS (the "LIS and EMR compatibility" and "vendor-neutral" claims). It is not part of an Ascentry LIS, since Ascentry sells no LIS. So it can in principle sit on top of Glims/Clinisys, Dedalus, Inlog, Technidata and similar. INDICATIVE: no specific third-party LIS is named as a live Infection Tracker interface.
- **Market footprint:** the Belgian/Dutch roots (Info Partner, a Dutch-named spokesperson, the Sciensano reporting claim) and "90+ sites in Europe" point to an installed base mainly in Belgium and France. INDICATIVE.
- **Cluster detection:** "outbreak detection" is claimed, but there is no statement of statistical or algorithmic cluster detection (for example SaTScan or genomic linkage). It appears to be rule- or alert-based. INDICATIVE.

### Gaps
- Customer names for Ynfectio or Infection Tracker: UNKNOWN (not on the product page, Biologiste365 or the About page).
- Whether reporting to SPARES/ConsoRes (France), Sciensano/NSIH/HD4DP (Belgium), ANRESIS/Swissnoso (Switzerland), EARS-Net or PRIMO is live today: only the legacy snippet mentions CONSORES/SCIENSANO. UNKNOWN for PRIMO, ANRESIS, Swissnoso and EARS-Net. The current Ascentry page says only "comply with national and international guidelines".
- Genomics/WGS or typing integration: UNKNOWN.

## 4. AMS focus

### Takeaway
The AMS features are **lab-epidemiology AMS**: automated antibiograms, resistance-trend statistics, resistance-phenotype alerts and reports for ID physicians and pharmacists. There is **no evidence** of antibiotic-consumption tracking (DDD/DOT), prescription linkage, restricted-antibiotic workflows, prescribing alerts or an AMS CDSS, and no AMS partnership was found.

### Cited Findings
- Infection Tracker "automates antibiogram generation" and does "resistance pattern detection". "Timely insights into resistance trends facilitates clinical decisions for antibiotic prescriptions and strengthening AMS efforts." CONFIRMED (company claim) — [Infection Tracker](https://www.ascentry.com/products/infection-tracker/)
- Ynfectio offered "automatic reporting to clinicians and prescribers". CONFIRMED (trade press) — [Biologiste365](https://www.biologiste365.fr/informations-produits/surveillance-epidemiologique/)
- For context, ConsoRes (the French SPARES tool) collects both resistance and antibiotic-consumption data. Version 1 stopped working in November 2023 and a new version has been available since March 2025. CONFIRMED (independent) — [Répia](https://www.preventioninfection.fr/actualites/spares-nouvelle-version-de-consores-disponible/)
- Lab Composer has an "expert rule engine" for autovalidation. It is not described as AST expert rules (EUCAST/CA-SFM interpretation). CONFIRMED (company claim) — [Lab Composer](https://www.ascentry.com/products/lab-composer/)

### Inferences
- The legacy claim of CONSORES reporting probably covers only the **resistance** part. Consumption data come from pharmacy systems, which Infection Tracker does not appear to ingest. INDICATIVE.
- Relevance for LUMED: Infection Tracker overlaps with the lab-side IPC surveillance and antibiogram parts of LUMED. It does not appear to compete on prescription-level AMS decision support. INDICATIVE.

### Gaps
- Antibiotic consumption, DDD/DOT, restricted-antibiotic reporting, prescription linkage, AMS alerts, AMS partnerships and AMS roadmap: all UNKNOWN. Searched ascentry.com (Infection Tracker page and FAQ, FAQ, Trust, About), Biologiste365 and the Newswise release.
- Whether the antibiogram reports follow CLSI M39 or CA-SFM/EUCAST cumulative rules (first isolate per patient, etc.): UNKNOWN.

## 5. Oncology CDSS and other CDSS (sepsis, diagnostic stewardship, AI)

### Takeaway
No oncology, sepsis or AI-based CDSS was found.

### Cited Findings
- The product line-up is limited to Lab Composer, POC Controller, Infection Tracker and Validation Manager. CONFIRMED (company) — [ascentry.com](https://www.ascentry.com); [Newswise](https://www.newswise.com/articles/ascentry-launches-at-adlm-2025-ushering-in-a-new-era-of-laboratory-software)

### Gaps
- Oncology CDSS/prescribing: UNKNOWN / none found (searched ascentry.com product pages, About, Newswise, Keensight).
- Sepsis alerts, diagnostic-stewardship CDSS, AI/ML: UNKNOWN / none found (same sources). Lab Composer's autovalidation rules and patient moving averages are lab QC/validation features, not clinical CDSS.

## 6. Integrations and standards

### Takeaway
All products are marketed as vendor-neutral, multi-LIS and multi-instrument. Named partners are IVD companies (QuidelOrtho, Stago, Thermo Fisher, Binding Site). No EHR/DPI partner (Dedalus, Maincare, Softway, Epic, Cerner, Agfa, Cegedim) is named in the sources read, and no standard (HL7 v2, FHIR, HPRIM) is explicitly listed.

### Cited Findings
- QuidelOrtho partnered with BYG4lab (24 July 2023) to strengthen its informatics offering. CONFIRMED (press release, read via snippet) — [QuidelOrtho](https://www.quidelortho.com/global/en/resources/press-releases/quidelortho-partners-with-bytg4lab-to-strengthen-informatics-offerings)
- Yline is multi-site/multi-SIL and connects to any instrument. CONFIRMED (trade press) — [Biologiste365 – Yline](https://www.biologiste365.fr/a-decouvrir/yline-linnovation-au-service-de-la-digitalisation-des-laboratoires-de-biologie-medicale/)
- Infection Tracker: "Seamless LIS and EMR compatibility", LIS/HIS/middleware integration. CONFIRMED (company claim) — [Infection Tracker](https://www.ascentry.com/products/infection-tracker/)
- The Ascentry FAQ gives no protocol details (HL7, FHIR, HPRIM not mentioned). It mentions IEC 62304, ISO 13485, HIPAA and GDPR. CONFIRMED (company) — [Ascentry FAQ](https://www.ascentry.com/faq/)

### Gaps
- Named EHR/DPI integrations and HL7/FHIR/HPRIM/Interop'Santé support: UNKNOWN (product pages and FAQ read). HPRIM is very likely supported by legacy French middleware, but that is not evidenced.
- Connections to national systems: only the legacy CONSORES/SCIENSANO snippet (see section 3).

## 7. Deployment and hosting

### Takeaway
Validation Manager and POC Controller are described as cloud-based. Infection Tracker is described as cloud-based by the fetch summariser, but the page text read directly confirms only "vendor-neutral" and "multi-site"; cloud is not stated explicitly for it. Lab Composer's deployment model is not stated. No HDS certification was found.

### Cited Findings
- Validation Manager is "cloud-based software" and POC Controller a "cloud-based" platform. CONFIRMED (company claim) — [Validation Manager](https://www.ascentry.com/products/validation-manager/); [POC Controller](https://www.ascentry.com/products/poc-controller/)
- The corporate website is hosted by OVHcloud, Roubaix. CONFIRMED (company) — [Legal notice](https://www.ascentry.com/legal-notice/)
- The Trust Center does not state hosting providers or data residency; it refers readers to the help center. CONFIRMED (company) — [Trust](https://www.ascentry.com/trust/)

### Inferences
- The legacy Yline/nYna middleware and Ynfectio were most likely installed on-premise at hospitals and labs, as is typical in France. INDICATIVE, not evidenced.

### Gaps
- HDS certification, hosting provider for the SaaS products, EU data residency: UNKNOWN (Trust, FAQ and legal notice searched).

## 8. Tech stack

### Cited Findings
- A job ad (Fullstack developer, permanent contract, L'Union) lists ASP.NET Core, Angular 14+, Entity Framework, TFS and Visual Studio. Applications go to an @byg4lab.com address. INDICATIVE: seen only in a search-engine summary with no traceable job-board URL, found near a LinkedIn profile of an Ascentry employee — [LinkedIn – Stéphane Jamin](https://www.linkedin.com/in/st%C3%A9phane-jamin-39801757/) (not opened)
- The corporate website runs on WordPress (visible in page source). CONFIRMED (observed) — [ascentry.com](https://www.ascentry.com)

### Gaps
- GitHub organisation: not searched in depth, nothing found. The original job-ad URL on Welcome to the Jungle, Indeed or APEC should be checked by hand.

## 9. Certifications and regulatory status

### Takeaway
Ascentry France (BYG Informatique SAS) holds ISO 13485:2016 for Lab Composer, POC Controller and Infection Tracker. Ascentry Finland (Finbiosoft Oy) holds ISO/IEC 27001:2022 for Validation Manager. CE/IVDR or MDR class, EUDAMED registration, FDA, UKCA and HDS status are **not disclosed**.

### Cited Findings
- ISO 13485:2016 covers "design, development, and maintenance of medical device software" at Ascentry France (BYG Informatique SAS), for Lab Composer, POC Controller, Infection Tracker and related solutions. ISO/IEC 27001:2022 covers Validation Manager at Ascentry Finland (Finbiosoft Oy). Regular penetration testing is also claimed. CONFIRMED (company claim) — [Trust Center](https://www.ascentry.com/trust/)
- The About page says ISO 13485:2016 was obtained in 2014–2016 and ISO 9001 in 2012. CONFIRMED (company claim) — [About us](https://www.ascentry.com/about-us/)
- The FAQ mentions IEC 62304, ISO 13485, HIPAA and GDPR, but no CE class. CONFIRMED (company) — [FAQ](https://www.ascentry.com/faq/)
- Validation Manager "supports compliance with" IVDR, CLIA, CAP and others. This refers to helping labs comply, not to the product's own certification. CONFIRMED (company claim) — [Validation Manager](https://www.ascentry.com/products/validation-manager/)
- Regulatory context: middleware that supports an IVD without its own medical purpose may count as an IVDR accessory. CONFIRMED (independent, general) — [CSDmed / Team-NB position](https://www.csdmed.mc/en/news/news/position-paper-team-nb-150)

### Inferences
- The ISO 13485 wording ("medical device software") suggests at least some products are CE-marked as IVD or medical-device software, possibly IVDR class A (self-declared) for the middleware. INDICATIVE, unverified. Infection Tracker's alerting and antibiogram functions could qualify as MDR software; its status is unknown.
- There is a small inconsistency: 27001 covers only Validation Manager, while the French products (including Infection Tracker) have no stated ISO 27001 or HDS.

### Gaps
- CE/IVDR/MDR class per product, EUDAMED actor/UDI entries for BYG Informatique or Finbiosoft, FDA listings, UKCA: UNKNOWN. EUDAMED was not queryable; check by hand at ec.europa.eu/tools/eudamed and in the FDA establishment registration database.
- HDS: UNKNOWN (Trust, legal notice and FAQ searched).
