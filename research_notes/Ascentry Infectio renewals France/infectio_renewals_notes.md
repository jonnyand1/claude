# Notes: Infectio legacy base, French public contracts and renewal windows

Research date: 2026-09-29. Scope: France. Scripts used for the queries are saved next to this file.

## User-provided internal intelligence (CONFIRMED (user-provided internal intelligence))

- Legacy INFECTIO (Info Partner / partner4lab line) will no longer be maintained from June 2027.
- GHT Coeur Grand Est and CHU Grenoble Alpes are current Infectio customers and are current opportunities for LUMED ZINC.
- Public check of the June 2027 date: searched ascentry.com, byg4lab.com redirects, Spectra Diagnostic issues 8, 12, 25, 37 and 40, and web search ("Ynfectio fin de maintenance Infectio 2027"). No public statement found. partner4lab.com (502 via proxy) and web.archive.org (blocked by egress policy) could not be read.

## Sources queried and how

| Source | Method | Result |
|---|---|---|
| DECP (data.economie.gouv.fr: decp-2022-marches-valides, decp-v3-marches-valides, decp_augmente, decp_aws, exclus/invalides) | API; supplier SIREN 326649407 (BYG/Ascentry France), 349314948 (Info Partner), 915233837 (holding); full-text on infectio, ynfectio, byg4lab, partner4lab, info partner, ascentry, infection tracker, nyna | 12 direct BYG/Info Partner contracts (already in chapter 12) plus the Nevers Infectio Labo contract. Only 2 contracts name the epidemiology product: CHU Caen (Ynfectio) and CH Nevers (Infectio Labo / Ynfectio Labo). v3 SIREN filters returned HTTP 400; decp_augmente covered them. |
| DECP, IPC/AMS keyword sweep | API full-text: infectiovigilance, logiciel d'hygiène, logiciel d'épidémiologie, surveillance des infections, Nosokos, ICNet, Consores, BMR/BHRe logiciel, antibiothérapie logiciel, LUMED, ZINC, Clarisys | Found RESAH AMR framework lots (Nosotech; bioMérieux relaunched lot 1), CHU Limoges Nosokos contracts, CH Aunay-Bayeux i2a contract. No contract naming LUMED or ZINC. |
| DECP, buyer sweep | Buyer names Verdun, Saint-Mihiel, Triangle, Bar-le-Duc, Saint-Dizier, Grenoble, Reims, Nancy, Abbeville, Dijon, Nevers + software/lab keywords | No Infectio/BYG contract for GHT Coeur Grand Est, CHU Reims, CHRU Nancy or CH Abbeville. CHU Reims LIS maintenance with INLOG (Labo Serveur, GHU Champagne, 01/10/2019, 39 months, €233,859). |
| BOAMP (boamp-datadila.opendatasoft.com) | API full-text: infectio, ynfectio, byg4lab, "byg informatique", "info partner", partner4lab, ascentry, infectioglobal, "infection tracker", nyna; plus IPC-software keywords since 2023 | Only CHU Caen award (24-68271) names Ynfectio. Grifols CHU Caen 2019 and CH Sud Essonne 2016 mention BYG. No Infectio notice. |
| TED | API FT search: infectio, ynfectio, BYG4LAB, "BYG INFORMATIQUE", "INFO PARTNER", partner4lab, Ascentry, "Infection Tracker", "résistance anti-microbienne", "Solution globale de microbiologie" | TED 348571-2024 (Caen) only French notice naming Ynfectio; TED 489752-2024 RESAH AMR framework award; TED 450483-2024 / 467070-2024 / 81198-2025 lot 1 relaunch. Belgian MALDI tenders mention partner4lab/Info Partner (Chimay 2019, HeCaPP 2025). |
| HAL / DUMAS full text | API: InfectioGlobal, Infectio.Global, "Infectio Labo", "logiciel Infectio", Ynfectio, Vigi@ct | Only 3 theses: CHU Reims 2025 (InfectioGlobal V4), CHRU Nancy 2020 (InfectioGlobal), CH Abbeville 2019 (Infectio.Global). |
| Registry (recherche-entreprises.api.gouv.fr) | SIREN lookups | 130005010 = RESAH; 828570606 = NOSOTECH EUROPE; 347717118 = I2A (Montpellier); 673620399 = bioMérieux SA; 200011203 = CHI Agglomération de Nevers. |

## Key records

- **CHU Reims**: "L'EOH reçoit quant à elle une fiche d'alerte via le logiciel d'épidémiologie InfectioGlobal V4® (BYG4Lab)" (thesis 2025, dumas-05322365, p. ~33). CONFIRMED (independent).
- **CHRU Nancy**: InfectioGlobal daily lab-result import into an in-house Access database (hal-03298181, 2020). CONFIRMED (independent, 2020 state).
- **CH Abbeville**: Infectio.Global (partner4lab) linked to LIS and patient movements (dumas-02884834, 2019). CONFIRMED (independent, 2019 state).
- **CH Nevers**: DECP 2026S00059, 02/02/2026, 48 months, €10,314.92, "INX Mise à jour et maintenance de la solution INFECTIO LABO / YNFECTIOLABO", no publicity or competition. End = 01/02/2030 (computed).
- **CHU Caen / GHT Normandie Centre**: TED 348571-2024; DECP 20240033001000; 18/04/2024; 44 months; Ynfectio already deployed. End ≈ 17/12/2027 (computed).
- **CHU Grenoble Alpes**: DECP 20232023S0768100; 26/04/2023; 48 months; PILOT MALDI maintenance (legacy partner4lab microbiology middleware). End ≈ 25/04/2027 (computed). CHU Grenoble speaker at the sponsored SF2H 2025 Ynfectio AI session; GeodAIsics (Ascentry's AI partner) is a Grenoble start-up.
- **CHU Dijon**: DECP 20222022S1506200; awardee Info Partner; 04/05/2022; 48 months; €19,386; "Maintenance de logiciels et de connexions informatiques par la société BYG4LAB". End ≈ 03/05/2026 (computed). No renewal found in DECP by 29/09/2026. Products not named.
- **CHU Rouen**: 06/04/2023, 48 months, €40,028.60, bacteriology identification module + connections. End ≈ 05/04/2027.
- **CHU Saint-Étienne**: 06/02/2023, 48 months, €9,120, MALDI (Bruker) connections. End ≈ 05/02/2027.
- **RESAH AMR framework (TED 489752-2024; DECP 2024F04547/2024F04548)**: notified 29/05/2024, 48 months (≈ 28/05/2028). Lot 8 BMR/BHRe surveillance and alert software, lot 9 antibiotherapy monitoring software, lot 10 antibiotic consumption and resistance surveillance software: all awarded to NOSOTECH EUROPE. Offers received per lot (BT-759): lot 8 = 4, lot 9 = 3, lot 10 = 3. Lot 1 closed without award in that notice. Ascentry/BYG not among winners.
- **RESAH lot 1 relaunch (framework A0Z2024F13492119; DECP 2024F13492)**: "Solution globale de microbiologie ... et logiciels (surveillance et alerte des infections, consommation des antibiotiques et monitorage de l'antibiothérapie)", awarded to bioMérieux SA, notified 18/10/2024, 48 months. Subsequent contracts (DECP): GHT Sud Lorraine (2024F13529, 18/12/2024), Val-d'Oise dept 95 (2025F11402, 17/10/2025), CH Rodez (2026F01283, 06/02/2026), CH Nîmes / CH Alès-Cévennes / CH Louis Pasteur (2026F03443, 25/03/2026), GH Sud Île-de-France (2026F05049, 04/05/2026), CHU Poitiers (2026F05816, 26/05/2026), dept 83 (2026F05912, 08/06/2026). Values deliberately not reproduced in the report (bioMérieux's own awards).
- **CHU Limoges / Nosotech (Nosokos)**: 20/10/2020 acquisition €209,305 / 48 months; 26/07/2024 maintenance €21,000 / 43 months; 01/12/2025 support subscription €93,044 / 36 months.
- **CH Aunay-Bayeux (GHT Normandie Centre, buyer CHU Caen)**: DECP 2555665, 11/09/2024, 48 months, €78,673, awardee I2A: automated AST reader + bacteriology middleware + epidemiology software. Shows a second epidemiology vendor inside the Caen GHT.
- **GHT Coeur Grand Est**: support hospital CH Verdun Saint-Mihiel; labs pooled in GCS Biologie Médicale Triangle et Der; GHT buys lab reagents for the GHT + GCS as one group. No Infectio or BYG contract visible in DECP/BOAMP/TED.
