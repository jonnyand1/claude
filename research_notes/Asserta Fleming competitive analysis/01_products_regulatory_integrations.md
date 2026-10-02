# Asserta Global Healthcare Solutions SL: product portfolio, Fleming regulatory status, integrations, deployment and technology

Research date: 2 October 2026. Labels: **CONFIRMED (official/independent)**, **CONFIRMED (company claim)**, **INDICATIVE** (with the reasoning), **UNKNOWN** (with where I searched).
Scratch method note: Asserta pages were fetched raw with curl and parsed; EUDAMED was queried through its public JSON API (`ec.europa.eu/tools/eudamed/api/...`) on 2 Oct 2026; TED was queried through `api.ted.europa.eu/v3/notices/search`.

---

## Q1. Is Fleming CE-marked under MDR (EU 2017/745)? Which class and which notified body?

### Takeaway
Public evidence now goes further than the prior user document. As of 2 Oct 2026, **Asserta Global Healthcare Solutions is not registered as an economic operator (no SRN) in EUDAMED**. No EUDAMED device with the trade name "Fleming" belongs to Asserta. No Asserta page, brochure, CETEC entry or press item claims CE marking, an MDR class, a notified body, ISO 13485 or a UDI. The only certification Asserta publishes is **ENS (Esquema Nacional de Seguridad) category MEDIUM**. That is an information-security certificate, not a medical-device certificate. Verdict: there is no public evidence that Fleming is CE-marked under MDR. The INDICATIVE reading is that Fleming is currently sold as non-device analytics/governance software. Its own clinical-decision-support wording creates regulatory exposure (MDR Rule 11).

### Cited Findings

**EUDAMED (retried 2 Oct 2026; it worked through the public API)**
- An economic-operator search for "asserta" and "Asserta Global" in EUDAMED returned **0 actors**. The same endpoint is known to work: "grifols" returned 9 actors, including Laboratorios Grifols ES-MF-000000767, and "Tecnocl" returned Tecnoclínic SA. **CONFIRMED (official registry; absence as of query date)**: [EUDAMED actor API, name=asserta](https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=25&name=asserta&languageIso2Code=en); validation query [name=grifols](https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=20&name=grifols&languageIso2Code=en)
- A EUDAMED UDI-DI search for trade name "fleming" returned **91 device records**, all from unrelated manufacturers: Fleming Comercial S.A. (ES-MF-000004259, 69 records), For.me.sa. srl ("Superfleming" pessaries, Class IIb, 11 records), Tecnoclínic SA ("FLEMING", Class I, 9 records), Guangdong Transtek ("FLEMING", Class IIa, 1 record) and Radiant Innovation (1 record). **None are Asserta.** **CONFIRMED (official registry)**: [EUDAMED UDI-DI API, tradeName=fleming](https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=fleming&iso2Code=en&languageIso2Code=en)
  - Caution for the report: a EUDAMED search for "Fleming" shows a **Class IIa device called "FLEMING"**. It is made by Guangdong Transtek Medical Electronics (SRN CN-MF-000010684, authorised representative MDSS GmbH) and is unrelated to Asserta. This could be the source of a mistaken "Fleming = CE Class IIa" claim. **INDICATIVE** (a hypothesis about where the claim came from; not proven): same source.
- Trade-name searches for "silicon nextgen", "silicon advanced", "oncoanalytics", "pharmacy analytics" and "antimicrobial stewardship" each returned **0** devices. "PROA" returned 189 unrelated orthopaedic, dental and other devices, none from Asserta. **CONFIRMED (official registry)**: [EUDAMED UDI-DI API](https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&tradeName=silicon%20nextgen&iso2Code=en&languageIso2Code=en)
- Italian distributor Medilogy SRL is registered in EUDAMED as a **manufacturer** (SRN IT-MF-000041270). Its only device is "MediDss CLIN", Class I. That device is Medilogy's own product, not Fleming. **CONFIRMED (official registry)**: [EUDAMED actor API name=Medilogy](https://ec.europa.eu/tools/eudamed/api/eos?page=0&pageSize=5&name=Medilogy&languageIso2Code=en); [EUDAMED devices srn=IT-MF-000041270](https://ec.europa.eu/tools/eudamed/api/devices/udiDiData?page=0&pageSize=20&srn=IT-MF-000041270&iso2Code=en&languageIso2Code=en)
- Context from the prior document: EUDAMED's Actor and UDI/Devices modules became mandatory on 28 May 2026, with a transition window of about 12 months (to roughly 27 Nov 2026) for legacy devices. A **manufacturer** of a CE-marked device on the EU market would still normally need an SRN. Under MDR the actor registration precedes device registration, so a missing actor is a stronger signal than a missing device. **INDICATIVE**: [EC EUDAMED mandatory notice](https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en)

**Company statements on certification**
- The Fleming pages (EN and ES) display only an **ENS badge**: image file `distintivo_ens_certificacion_MEDIA_RD311-2022.png`. They contain no "CE", "MDR", "medical device"/"producto sanitario", "Class IIa" or "ISO 13485". **CONFIRMED (company page, raw HTML inspected)**: [Fleming EN](https://asserta.net/fleming-antimicrobial-stewardship/); [Fleming-PROA ES](https://asserta.net/es/fleming/)
- ENS certificate details (new; not in the prior document):
  - Issuer: **OCA Instituto de Certificación, S.L.U.**, which displays ISO 17065 accreditation No. 11/C-PR375.
  - Certificate No. **34/5704/26/06711**, category **MEDIUM** (C/I/T/A/D all MEDIUM), 65 measures.
  - Audit report dated 03/06/2026. Initial certification and grant date **30 June 2026**; expiry **30 June 2028**.
  - Scope: "information systems that support technical assistance, consulting, and the development and maintenance of clinical management applications".
  - **CONFIRMED (certificate PDF hosted by Asserta)**: [ENS certificate PDF](https://asserta.net/wp-content/themes/asserta/docs/34_5704_26_06711_ASSERTA%20GLOBAL%20HEALTHCARE%20SOLUTIONS_CAST-ENG.pdf)
  - **INDICATIVE**: the initial ENS certification date of 30 June 2026 conflicts with older pages that already showed an ENS badge. Either the badge predates the certificate, or the certificate PDF is a reissue. The CETEC page also cites ENS.
- Asserta's Security Policy references RD 311/2022 (ENS), GDPR/LOPDGDD, eIDAS and other laws. It cites **no MDR, no ISO 13485 and no ISO 27001**. Its mission line mentions "Health Analytics systems and artificial intelligence to support value-based decision-making". **CONFIRMED (company page)**: [Security policy](https://asserta.net/politica-de-seguridad/)
- The legal notice gives: ASSERTA GLOBAL HEALTHCARE SOLUTIONS, S.L.; Ronda Maiols 1, office 303, Sant Quirze del Vallès; Barcelona Commercial Registry Vol. 43406, Sheet 428611; NIF **B-65880593**. It contains no regulatory or medical-device statement. **CONFIRMED (company page)**: [Legal notice](https://asserta.net/legal-notice/). The Spanish URL `/es/aviso-legal/` returned 404.
- The SEFH CETEC Fleming-PROA entry has category "Software". Its only certification is "Asserta dispone de certificación del Esquema Nacional de Seguridad (RD 311/2022)". It shows no CE marking or class. **CONFIRMED (independent catalogue, text supplied by vendor)**: [CETEC Fleming-PROA](https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/)
- Medilogy Italian brochure (`Fleming-Brochure_ITA_04_25.pdf`; 10 pages; PowerPoint export with PDF creation date 17 Jul 2025): the extracted text has no "CE", "marcatura", "dispositivo medico", "MDR" or "ISO". **CONFIRMED (distributor document; text extraction only, logos/images not inspected)**: [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)
- A staff bio lists ISO 13485, IEC 62304/14971/62366 and AAMI TIR-45 among **personal** expertise. Jose Pineda Sánchez, "Head of Development & Support – Silicon Division", ex-Grifols per the CCOO/Grifols context below. This is not a company certification claim. **CONFIRMED (company page) as personal expertise; INDICATIVE** that medical-device quality-system know-how came across with the Grifols Silicon team: [Jose Pineda profile](https://asserta.net/team/jose-pineda-sanchez/)

**Claims that create MDSW / Rule 11 exposure (for the report's regulatory analysis)**
- "Clinical decision support dashboards" (Fleming EN) and "Real-time clinical decision support" (Silicon Advanced Analytics suite page). **CONFIRMED (company claim)**: [Fleming EN](https://asserta.net/fleming-antimicrobial-stewardship/); [Silicon Advanced Analytics](https://asserta.net/solutions/silicon-advanced-analytics/)
- CETEC says the product "Facilita la identificación de oportunidades de desescalada, ajuste de duración, terapia secuencial y adecuación al antibiograma" (helps identify opportunities for de-escalation, duration adjustment, sequential therapy and adequacy to the antibiogram). **CONFIRMED (vendor text in catalogue)**: [CETEC](https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/)
- Vidal Vademecum states that Fleming PROA "alimenta sus algoritmos de ayuda a la toma de decisiones con información farmacológica... actualizada por Vidal Vademecum" (feeds its decision-support algorithms with pharmacological information updated by Vidal Vademecum). **CONFIRMED (partner page)**: [Vademecum – Fleming PROA alimenta sus algoritmos](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69)
- Asserta won a SERGAS contract (Feb 2026, €374,472) that includes "desarrollo de un sistema para la validación automática de prescripciones y tratamientos en base a reglas preestablecidas" (development of a system for rule-based automatic validation of prescriptions and treatments), compatible with the corporate pharmacy system (Silicon is SERGAS's pharmacy system; see Q3). This is rule-based prescribing CDS of the kind usually scoped under MDR Rule 11. **CONFIRMED (TED official)**: [TED 112929-2026](https://ted.europa.eu/en/notice/-/detail/112929-2026)

**Grifols-era Silicon CE status**
- Grifols describes Silicon (2006) as e-prescription and pharmacy software. It "performs an initial validation to check there are no dosage, frequency or duration errors in the prescription". The page makes no CE or medical-device claim. **CONFIRMED (Grifols page)**: [Grifols – Automating hospital pharmacy services](https://www.grifols.com/en/-/automating-hospital-pharmacy-services)
- No public source found stating that Silicon was CE-marked as a medical device under Grifols. **UNKNOWN**. Searched: web searches "Silicon Grifols marcado CE", "Silicon producto sanitario"; the Grifols page above; CETEC Silicon entry (now relabelled "Silicon NextGen", provider Asserta, no CE); EUDAMED trade-name search "silicon" (19,194 hits, mostly silicone products; only the first page was inspected, so not exhaustive). EUDAMED Grifols actors include Laboratorios Grifols ES-MF-000000767 and Diagnostic Grifols ES-MF-000000784. Their device lists were **not** enumerated for Silicon.

### Inferences
- **INDICATIVE**: Fleming (and the wider Asserta portfolio) is very likely marketed **without MDR CE marking**. Grounds: no SRN for Asserta; no device record; the only certification published is ENS; the 2026 rewording centres on "governance-driven intelligence platform", which is a non-medical positioning, while "clinical decision support" claims remain. A Class IIa claim for Fleming is unsupported and should be treated as **false unless Asserta produces a DoC and a notified-body certificate**.
- **INDICATIVE**: Asserta's MDR exposure is growing. It now owns Silicon e-prescribing (dose, frequency and duration checks) and is building rule-based automatic prescription validation for SERGAS. Both features are classic Rule 11 MDSW territory. For bioMérieux this is a sales argument (regulatory-grade CDS against governance analytics) and a watch item: Asserta may register later.

### Gaps
- EUDAMED certificate module and NB-certificate search not queried (the API path for certificates was not identified). RECOPS/AEMPS was not queried: the public interface needs interactive use. See "Blocked sources / manual checks".
- Grifols EUDAMED device lists not enumerated for a "Silicon" software device.

---

## Q2. What is in Asserta's whole portfolio, and is Fleming bundled into the Silicon suite?

### Takeaway
Asserta (founded 2012, Sant Quirze del Vallès) presents four "solutions": Silicon NextGen, Silicon Advanced Analytics, Real World Research and Strategy.
- **Silicon NextGen** is the pharmacy/e-prescribing/eMAR operational platform. Its business unit was bought from Grifols, with staff subrogated from 1 April 2025.
- **Silicon Advanced Analytics** is the analytics suite. **Fleming Antimicrobial Stewardship is formally one of its three modules**, alongside Pharmacy Analytics Manager and OncoAnalytics.
- Fleming is therefore **bundled at the portfolio level and integrated by design** with Silicon NextGen. It is also sold standalone and is "platform-agnostic".
- No IPC/infection-control product was found.

### Cited Findings
- Main navigation (2026): Silicon NextGen ("Integrated Pharmacotherapy Governance"), Silicon Advanced Analytics ("Structured Institutional Intelligence"), Real World Research and Strategy. Fleming is **not** a top-level menu item. **CONFIRMED (company site)**: [Asserta home](https://asserta.net/)
- "The Silicon Advanced Analytics Suite: Pharmacy Analytics Manager; Fleming Antimicrobial Stewardship ('Structured AMR Governance Intelligence'); OncoAnalytics." The page also claims "Explainable AI methodologies; audit-ready algorithm transparency", and integration with "HIS, EHR, PhIS, departmental systems, IoMT infrastructures, automated dispensing systems and robotic platforms". **CONFIRMED (company claim)**: [Silicon Advanced Analytics](https://asserta.net/solutions/silicon-advanced-analytics/)
- Silicon NextGen's "modular design allows institutions to deploy specific domains — such as **oncology, antimicrobial stewardship** or sterile compounding". It covers procurement, inventory, sterile compounding, dispensing (manual and automated), e-prescribing support, barcode administration, eMAR, and "inpatient, critical care, oncology day hospital, pediatrics and outpatient settings". It integrates with HIS, EHR, robotic dispensing, national prescription platforms and data warehouses. **CONFIRMED (company claim)**: [Silicon NextGen](https://asserta.net/solutions/silicon-nextgen/); same text in [CETEC Silicon NextGen](https://cetec.sefh.es/producto/silicon/) (CETEC version adds "con procesos de monitorización y alertas", i.e. with monitoring and alert processes).
- The Fleming page says it "integrates with: **Silicon NextGen medication workflows**; clinical, operational and enterprise healthcare platforms; executive governance dashboards; national AMR modernization initiatives". **CONFIRMED (company claim)**: [Fleming EN](https://asserta.net/fleming-antimicrobial-stewardship/)
- Pharmacy Analytics Manager (page dated 27 Feb 2026): expenditure monitoring, prescribing variability, KPI architecture, benchmarking; "operates within Silicon NextGen operational environments". **CONFIRMED (company claim)**: [Pharmacy Analytics Manager](https://asserta.net/pharmacy-analytics-manager/)
- OncoAnalytics (pages dated 2024 and Feb 2026): oncology treatment cost, protocol adherence, outcome and safety indicators, day hospital/outpatient, **clinical trial treatment monitoring**, executive dashboards. **CONFIRMED (company claim)**: [OncoAnalytics](https://asserta.net/oncoanalytics/); [Onco Analytics (2024)](https://asserta.net/onco-analytics/)
- Legacy/secondary pages (still live, 2024):
  - "Silicon Analytics": analytics on top of "Silicon (*) ... an e-prescription and hospital pharmacy management application developed and commercialized by Grifols".
  - "Clinical Trial Analytics": the cost impact of clinical-trial drug supply.
  - **CONFIRMED (company pages)**: [Silicon Analytics](https://asserta.net/silicon-analytics/); [Clinical Trial Analytics](https://asserta.net/clinical-trial-analytics/); page dates from [page sitemap](https://asserta.net/page-sitemap.xml)
- **Silicon acquisition from Grifols:** CCOO (union) reported on 24 Mar 2025 that Grifols sold "la unitat de negoci del producte Silicon" (the Silicon product business unit) to Asserta Global Healthcare Solutions. Asserta subrogated the 7 staff from **1 April 2025**, each receiving €7,800. **CONFIRMED (independent)**: [CCOO Indústria](https://www.ccoo.cat/industria/noticies/ccoo-aconsegueix-una-compensacio-per-a-la-plantilla-de-grifols-afectada-per-la-subrogacio-a-asserta-que-ha-comprat-la-unitat-de-negoci-del-producte-silicon/)
- Asserta now has a "Silicon Division": a General Manager who previously led Hospital Business Development Iberia at Grifols, a Head of Development & Support, and two Regional Managers TS. One of them was Silicon project manager at SERGAS for 15 years. **CONFIRMED (company pages)**: [Team](https://asserta.net/team/); [Juan José Ibáñez del Saz](https://asserta.net/team/juan-jose-ibanez-del-saz/); [Miguel Ángel González Prieto](https://asserta.net/team/miguel-angel-gonzalez-prieto/)
- The EAHP exhibitor profile says Asserta was "Founded in 2012... more than 20 countries in Europe, the Middle East, and Latin America. Its core activities include Silicon, its integrated pharmacotherapy management software (pharmacy management, medical prescribing, prescription monitoring, and nursing administration records)... Pharmacy Analytics Manager, Fleming Antimicrobial Stewardship, and OncoAnalytics". **CONFIRMED (company claim on congress site)**: [EAHP exhibitor – Asserta](https://eahp.eu/exhibitor/asserta/)
- Real World Research division: Phase IV, drug-utilisation, registries and HEOR. Priority domains include "Antimicrobial Resistance & Stewardship" and oncology. Asserta is a member of 3 EU Horizon consortia (Closer, Share4Rare, MyHealth). **CONFIRMED (company claim)**: [Real World Research](https://asserta.net/solutions/real-world-research/); [Projects](https://asserta.net/projects/)
- Strategy/consulting ("360° Clinical Digital Assessment"); partnership model: "Joint bids and UTE models... We do not compete with global vendors". **CONFIRMED (company claim)**: [Strategic Alliances](https://asserta.net/strategic-alliances/)
- Company scale claims (home page, 2026): 76 hospitals, 600+ primary care centres, 194 institutions, 53,000+ concurrent users, 17M+ e-prescriptions, 400M+ administered doses, 20+ countries. **CONFIRMED (company claim)**: [Asserta home](https://asserta.net/). These figures likely now include the Grifols Silicon installed base: the 2025 brochure gave 78 hospitals but only 1,000M records. **INDICATIVE**.
- A 2024 press interview put Asserta at 12 people in 2024 and described its work in Bahrain with Indra on national health-system digitalisation. **CONFIRMED (press)**: [ON ECONOMIA, 4 Mar 2024](https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html)

**IPC / infection control**
- No infection-control or HAI surveillance product found. **UNKNOWN / none found**. Searched: full Asserta sitemap (page, solution, project and team sitemaps), CETEC search, EAHP profile, web searches. Fleming covers MDR-pathogen incidence and prevalence and outcomes such as bacteraemia and mortality (brochure). That is AMS-oriented surveillance, not an IPC workflow product. **CONFIRMED (distributor/company text)**: [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf); [Vademecum news](https://www.vademecum.es/noticia-240108-descubre+la+nueva+aplicaci+oacute+n+web+multidispositivo+desarrollada+para+optimizar+el+uso+de+los+antimicrobianos+y+combatir+el+desarrollo+y+diseminaci+oacute+n+de+las+resistencias+bacterianas_19331)

### Inferences
- **INDICATIVE**: Asserta's 2026 strategy is "Silicon as operational core + analytics layer". Fleming is positioned as an add-on module of the analytics suite that runs natively on Silicon NextGen data. In Silicon accounts (SERGAS, ICO, GSS, IAS and other former Grifols sites), Fleming is the natural upsell.
- **INDICATIVE**: Asserta also partners with large integrators (Indra in Bahrain; UTE/subcontracting model). Fleming could therefore reach the market inside larger HIS bids.

### Gaps
- No public price list or published bundle SKU combining Fleming and Silicon. CETEC says pricing is case-by-case.
- No tender found that names "Fleming" explicitly (TED search on "Asserta" and Gobierto/Sophia lists).

---

## Q3. Fleming: purpose, modules, origin, launch, AI claims and 2024–2026 changes

### Takeaway
Fleming (Fleming-PROA) is an Asserta-developed, multi-device web AMS analytics application. It was publicly launched at **Mobile World Congress in March 2024**, although it was claimed to have been in use "for some years" before that. It organises indicators into three groups: antimicrobial use, microbiology/resistance, and health outcomes. It covers hospital (DDD/DOT) and primary care (DHD, prescribing quality) and supports Spanish PRAN/AEMPS PROA certification. In 2026 it was rebranded as a "governance-driven intelligence platform" inside Silicon Advanced Analytics. No hospital spin-off origin was found. Its DNA is the Vall d'Hebron hospital-pharmacy leadership that founded Asserta.

### Cited Findings
- Three indicator groups:
  1. Antimicrobial use, with standardised parameters for benchmarking.
  2. Microbiology: continuous susceptibility analysis and incidence/prevalence of MDR pathogens.
  3. Health outcomes such as bacteraemia and mortality.
  - The brochure adds "ampia varietà di filtri" (a wide range of filters), report and chart export to other systems, alignment with WHO, Joint Commission and CDC recommendations, and the claim of "used in real practice for more than 3 years in Spain and Latin America". **CONFIRMED (distributor brochure)**: [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf)
- Hospital metrics: DDD and DOT per stays/admissions, by service/unit. Primary care: DHD and prescribing-quality indicators. Analysis by health area or regional health service. Automated periodic indicators, traceable history and certification-ready reports for the **PRAN PROA certification** (basic/advanced/excellent levels), covering both hospital and community teams. **CONFIRMED (vendor text in CETEC)**: [CETEC Fleming-PROA](https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/)
- Other capabilities: protocol/guideline adherence indicators; "contrastar el patrón prescriptor real con el mapa de resistencias del propio centro y de cada unidad" (compare actual prescribing against the centre's and each unit's resistance map); de-escalation, duration, sequential (IV-to-oral) therapy and antibiogram adequacy opportunities; consumption and cost traceability. **CONFIRMED (vendor text)**: same source.
- Scale claims (Mar 2024): "más de 600 centros de atención primaria y 14 hospitales en España y Latinoamérica", ">80 laboratorios", "7 millones de personas" covered (600+ primary care centres and 14 hospitals in Spain and Latin America; more than 80 laboratories; 7 million people). The launch was at MWC 2024 alongside the "Be an activist to overcome bacterial resistances" campaign. **CONFIRMED (company claim via press)**: [ON ECONOMIA](https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html). The same 14 hospitals / 600+ centres / 7M / 80+ labs figures appear in the [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf).
- A Peru use case (two hospitals and their primary care areas) on empirical UTI treatment and resistance found 70% resistance to the antibiotics in use, which led to new protocols. **CONFIRMED (company claim)**: [ON ECONOMIA](https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html); a related RWR project, "Analysis of empirical treatment of UTI in women in primary care in... Callao and Villa María del Triunfo in Peru", is listed at [Asserta Projects](https://asserta.net/projects/)
- Drug knowledge base: Vidal Vademecum supplies the pharmacological data behind Fleming's "algoritmos de ayuda a la toma de decisiones" (decision-support algorithms). **CONFIRMED (partner)**: [Vademecum](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69)
- Timeline of web pages: `/es/fleming/` was last modified 12 Aug 2024. The new `/fleming-antimicrobial-stewardship/` (EN/ES) was modified **3 Aug 2026**, with the "governance-driven intelligence platform" wording. The Silicon Advanced Analytics suite pages are dated Aug 2026. **CONFIRMED (sitemap)**: [page sitemap](https://asserta.net/page-sitemap.xml); [solution sitemap](https://asserta.net/solucion-sitemap.xml)
- AI claims:
  - Fleming page: none explicit.
  - Suite page: "Explainable AI methodologies; audit-ready algorithm transparency".
  - Brochure: Asserta specialises in "Health Analytics e Intelligenza Artificiale" (health analytics and artificial intelligence).
  - The CEO stresses that clinical technology "no se puede permitir tener un 10% de errores" (cannot afford a 10% error rate).
  - **CONFIRMED (company claims)**: [Silicon Advanced Analytics](https://asserta.net/solutions/silicon-advanced-analytics/); [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf); [ON ECONOMIA](https://www.elnacional.cat/oneconomia/es/economia/monterde-ceo-asserta-gran-reto-tecnologico-combatir-bacterias_1169740_102.html)
- Origin: Asserta was founded in 2012 by Josep Monterde, PhD, former Director of Central Clinical Services and Pharmacy at **Vall d'Hebron** for 14 years and director of pharmaceutical services at IMAS Barcelona. Core clinical staff are former Vall d'Hebron hospital pharmacists: Julio Martínez (former Head of Pharmacy) and Elena Tomás (former head of the pharmacoepidemiology unit). **CONFIRMED (company pages)**: [Josep Monterde](https://asserta.net/team/josep-monterde/); [Team](https://asserta.net/team/)
- Fleming originated as an in-house development and not as a spin-off. "Fleming PROA es una solución ... desarrollada por [Asserta]" (developed by Asserta). **CONFIRMED (partner text)**: [Vademecum](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69). A specific originating hospital PROA team was **UNKNOWN**. Searched: web searches (Dénia/Marina Salud, Peru, SERGAS, Vall d'Hebron combinations), Asserta pages and projects. Asserta lists several RWR projects with Hospital/Health Department of **Dénia**, which suggests the Dénia area as an early data partner. That link is **INDICATIVE only**: [Projects](https://asserta.net/projects/)
- Italy: Medilogy SRL distributes the Italian brochure (dated "04_25"). No Italian hospital customer was found. **CONFIRMED (brochure exists)**; customers **UNKNOWN** (Italian web search returned nothing).

### Inferences
- **INDICATIVE**: The 2026 shift from "aplicación web... facilita la toma de decisiones clínicas" (web application that facilitates clinical decision-making) to "governance-driven intelligence platform" fits a repositioning toward committee- and population-level analytics, which keeps the product further from MDSW qualification.
- **INDICATIVE**: Fleming is retrospective and real-time **population/unit-level** analytics with "opportunity identification". Public material does not show patient-level, push-alert CDS of the kind LUMED provides (for example, bedside alerts in the EHR).

### Gaps
- Version numbers and release notes: none public.
- Named Fleming customer hospitals: none confirmed. The CETEC "Búsqueda por hospital" sidebar lists dozens of Spanish hospitals, but it is a **site-wide** CETEC navigation list for all vendors, **not** Fleming customers. Do not cite it as a Fleming customer list.

---

## Q4. Integrations, deployment model and technology stack

### Takeaway
Fleming is described as platform-agnostic and integrates pharmacy, prescription, EHR, laboratory/microbiology, CMBD (the Spanish minimum basic dataset of hospital discharges) and consumption data through an ETL layer. It is **deployed on-premise at the customer site**: "data do not leave the institution". No named EHR or LIS vendor integrations are published for Fleming. Silicon has documented integrations with Pyxis, Kardex/Mercurio and ROWA, plus HL7/FHIR expertise. The visible technology hints are Java/J2EE, Tomcat, Linux and HL7/FHIR on the Silicon side.

### Cited Findings
- Deployment: "Fleming PROA è una soluzione On Premise che viene installata nel centro clienti, in modo che i dati non lascino l'istituto, a meno che non voglia condividerli... con l'Amministrazione Sanitaria" (an on-premise solution installed at the customer's centre, so data do not leave the institution unless it chooses to share them, e.g. with the health administration). The architecture slide shows sources (prescription, patients, microbiology, CMBD, consumption) feeding ETL/integration, then the algorithm. **CONFIRMED (distributor brochure)**: [Medilogy brochure](https://www.medilogy.it/public/Fleming-Brochure_ITA_04_25.pdf); the same on-premise wording appears in [Vademecum](https://www.vademecum.es/productos-vademecum-fleming+proa+alimenta+sus+algoritmos+con+vidal+vademecum-69)
- Integration claims: "pharmacy systems, EHR platforms, clinical workstations, IoMT infrastructures and automated technologies"; CETEC adds "sistemas de laboratorio y microbiología" (laboratory and microbiology systems). The scope is scalable from a single unit to multicentre, regional or national. **CONFIRMED (company claim)**: [Fleming EN](https://asserta.net/fleming-antimicrobial-stewardship/); [CETEC](https://cetec.sefh.es/producto/fleming-proa-antimicrobial-stewardship/)
- Named Fleming integrations (SAP, Cerner/Oracle, SAVAC, HCIS, Gacela, IANUS, Millennium, Dedalus; Modulab, GestLab, OpenLab, GLIMS; WHONET): **UNKNOWN / none named publicly**. Searched: both Fleming pages, CETEC, the Medilogy brochure, Vademecum items and web searches.
- Silicon integrations (historic, Grifols era): at HCUVA (Murcia), Silicon was integrated with **Pyxis MS3500, Kardex-Mercurio and ROWA** and was being replaced by SAVAC/MIRA. **CONFIRMED (official procurement document)**: [CARM technical specification](https://www.carm.es/web/PDescarga?IDCONTENIDO=1618&PARAM=idDocumento%3Dworkspace%3A%2F%2FSpacesStore%2Fbf7bb43e-9d98-40ec-b255-1034857d2524%2F1.0&fechaVersion=24092019091152&descargar=true)
- Silicon platform history: Grifols launched it in 2006, "runs on Unix and uses web technology". **CONFIRMED (Grifols)**: [Grifols](https://www.grifols.com/en/-/automating-hospital-pharmacy-services)
- Silicon has been deployed across **SERGAS** (Galicia) for about 15 years. **CONFIRMED (company bio)**: [González Prieto](https://asserta.net/team/miguel-angel-gonzalez-prieto/)
- Silicon Division technical expertise: "J2EE, CI/CD, HL7, FHIR, open EHR"; "Java EE, Tomcat, and Linux"; "HL7 integrations". **CONFIRMED (staff bios, not product specifications)**: [Pineda](https://asserta.net/team/jose-pineda-sanchez/); [Naranjo](https://asserta.net/team/victor-naranjo/)
- The analytics/BI team focuses on "integration and interoperability of systems for Business Intelligence and Big Data", ETL and continuous integration. **CONFIRMED (staff bios)**: [Daniel García](https://asserta.net/team/daniel-garcia/); [Toni Huertas](https://asserta.net/team/toni-huertas-2/)
- Public contracts (relevant to installed base and integration contexts):
  - SERGAS, Feb 2026, €374,472: hospital drug catalogue, interactions model, and **rule-based automatic prescription validation** compatible with the corporate pharmacy system. [TED 112929-2026](https://ted.europa.eu/en/notice/-/detail/112929-2026)
  - EDP Salut Sant Joan de Reus, Aug 2024, €110,000: "servicio de análisis de datos orientado al proceso farmacoterapéutico" (data-analysis service for the pharmacotherapeutic process). [TED 502545-2024](https://ted.europa.eu/en/notice/-/detail/502545-2024)
  - ICO, 2026, €81,191.70: "Servei de manteniment de l'aplicatiu silicon" (Silicon maintenance service).
  - Servicio Andaluz de Salud, 2026, €31,500: application maintenance.
  - CatSalut, 2026, €14,784: consultancy, corporate platform.
  - All **CONFIRMED (official/aggregator)**: [Gobierto – Asserta](https://contratos.gobierto.es/adjudicatarios/asserta-global-healthcare-solutions)
  - Also listed: GSS (Silicon maintenance, Apr 2026) and IAS (pharmacy software maintenance, Jun 2026). **CONFIRMED (aggregator)**: [Sophia – Asserta](https://www.sophia-anphis.es/empresa-licitadora/asserta-global-healthcare-solutions-sl__B65880593)
  - Note: Lithuanian TED awards to "UAB Asserte" are a **different company** (Lithuanian IT firm) and should not be confused with Asserta.

### Inferences
- **INDICATIVE**: On-premise deployment plus ETL from heterogeneous sources (including 80+ labs) points to a data-warehouse/BI architecture with batch or near-real-time loads, not an embedded, event-driven CDS engine.
- **INDICATIVE**: The likely technology stack is Java/J2EE web apps on Linux/Tomcat for Silicon, plus a separate BI/ETL stack for the analytics suite. The specific BI tools are not public.

### Gaps
- No Asserta job posts found (InfoJobs/LinkedIn search returned nothing relevant). GitHub organisation search was blocked in this environment.
- No SaaS/cloud hosting statement found for any product.

---

## Q5. Oncology products (for the separate chapter)

### Takeaway
Asserta has oncology in two places:
1. **Silicon NextGen**: operational/prescribing scope explicitly covering the "oncology day hospital" and a deployable "oncology" domain, plus sterile compounding. The ICO (Institut Català d'Oncologia) pays for Silicon maintenance.
2. **OncoAnalytics**: an analytics module for oncology cost, protocol adherence, outcomes/safety and clinical-trial drugs.

No standalone oncology-protocol CDSS with a CE mark was found.

### Cited Findings
- Silicon NextGen covers "oncology day hospital"; it can be implemented "by clinical domain (e.g., oncology)"; it includes sterile compounding. **CONFIRMED (company claim)**: [Silicon NextGen](https://asserta.net/solutions/silicon-nextgen/)
- The ICO contracted Asserta for "manteniment de l'aplicatiu silicon" (Silicon maintenance) in 2026 (NSP-2026-03, €81,191.70). **CONFIRMED (official/aggregator)**: [Gobierto](https://contratos.gobierto.es/adjudicatarios/asserta-global-healthcare-solutions)
- OncoAnalytics capabilities: treatment cost, protocol adherence, outcome/safety dashboards, day hospital/outpatient, clinical-trial treatment monitoring. **CONFIRMED (company claim)**: [OncoAnalytics](https://asserta.net/oncoanalytics/)
- Oncology RWE: Vall d'Hebron solid-tumour cost studies; vial-fractionation optimisation in antineoplastic preparation; Closer (paediatric leukaemia, EU Horizon). **CONFIRMED (company claim)**: [Projects](https://asserta.net/projects/)
- Phrases specific to the Silicon oncology module ("Silicon oncohematológico", "Silicon citostáticos"): **UNKNOWN**. No page using those terms was found. Searched: Asserta sitemap pages, CETEC Silicon NextGen entry, Grifols Silicon page, web searches.

### Inferences
- **INDICATIVE**: The Grifols Silicon product historically covered chemotherapy prescribing, preparation and day-hospital workflows; ICO as a customer supports this. The specific oncology protocol module name is not public.

### Gaps
- Oncology module feature list (protocol library, dose banding, BSA calculations) not published.

---

## Blocked sources / manual checks
- **EUDAMED**: actor and device queries **worked** through the public API (2 Oct 2026). Not done: **certificate search** (NB certificates) and UI screenshots. Manual check: EUDAMED UI → Economic operators → "Asserta"; Devices → "Fleming", "Silicon"; Certificates → manufacturer name.
- **AEMPS RECOPS / CCPS legacy registry**: not queried (interactive application). Manual check is recommended, though RECOPS draws product data from EUDAMED.
- **Grifols EUDAMED device list**: not enumerated for a Silicon software UDI. Manual check: Devices filtered by SRN ES-MF-000000767 / ES-MF-000000784, searching "Silicon".
- **Medilogy brochure images**: only extracted text was checked. A CE logo inside an image would not appear; the prior document's visual review found none on the cover or architecture slides.
- **GitHub org search**: blocked in this environment (session-scoped API).
- **LinkedIn (company posts, jobs) and InfoJobs**: not accessible or no results. Manual check needed for Asserta job ads (tech stack) and for LinkedIn posts about Fleming/Silicon bundles.
- **SEFH congress 2024–2026 posters/abstracts mentioning Fleming**: none found by web search. A manual SEFH abstract-book search is recommended.
- **Direct request to Asserta** (contact@asserta.net): ask for the EU DoC, intended purpose, MDR class, NB, Basic UDI-DI and SRN (see the prior document's checklist). The EUDAMED actor absence means an SRN should be requested first.
