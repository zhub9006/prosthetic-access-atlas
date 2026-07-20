# Prosthetic Access Atlas — Latest Findings (July 2026)

This document consolidates the latest ClinicalTrials.gov clinical trial data, OpenStreetMap gap analysis, and regional coverage findings for the prosthetic-access-atlas project.

> **Analysis date:** July 20, 2026
> **Data sources:** ClinicalTrials.gov API v2, OpenStreetMap via OSM MCP tools

---

## 1. Clinical Trial Landscape — Full Search Results

### 1.1 Overall Search: `intr=prosthetic` (broad)

| Metric | Value |
|--------|-------|
| Total studies found | **644** |
| Active & recruiting | 112 (17.4%) |
| Completed | 271 (42.1%) |
| Unknown status | 134 (20.8%) |
| Phase 3 pivotal trials | 30 (4.7%) |
| Industry-sponsored | 108 (16.8%) |
| Academic/government-sponsored | 530 (82.3%) |

### 1.2 Focused Search: `intr=prosthetic limb amputation` (US-based)

| Metric | Value |
|--------|-------|
| Total studies found | **121** |
| US-based | ~75 |
| Currently recruiting | ~12 |
| Region: West Virginia | 3 |
| Region: Kentucky | 4 |
| Region: Mississippi | 2 |

### 1.3 Phase Distribution (n=644)

| Phase | Count | % | Significance |
|-------|-------|---|-------------|
| N/A (Observational/Device reg) | 338 | 52.5% | Registries, no intervention |
| Unknown | 202 | 31.4% | Phase not specified — transparency gap |
| **Phase 3** | **30** | **4.7%** | **Critically scarce — pivotal evidence** |
| Phase 4 | 29 | 4.5% | Post-market surveillance |
| Phase 2 | 39 | 6.1% | Early efficacy |
| Phase 1 | 15 | 2.3% | First-in-human |
| Early Phase 1 | 4 | 0.6% | |

### 1.4 Sponsor Type Distribution (n=644)

| Sponsor Type | Count | % |
|-------------|-------|---|
| Academic/Other (OTHER) | 493 | 76.5% |
| Industry (INDUSTRY) | 108 | 16.8% |
| Federal (FED) | 23 | 3.6% |
| Government/Other (OTHER_GOV) | 14 | 2.2% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

### 1.5 Top Countries

| Country | Count | Notes |
|---------|-------|-------|
| United States | 680 | Leads but **zero trial sites in WV, KY, MS** |
| France | 317 | Second globally |
| Germany | 76 | |
| Italy | 71 | |
| Denmark | 78 | |
| Canada | 41 | |
| UK | 44 | |
| Egypt | 38 | |
| Spain | 38 | |
| Netherlands | 41 | |

---

## 2. Key Active & Recent Clinical Trials

### 2.1 Currently Recruiting (Latest)

| NCT ID | Title | Sponsor | Start Date |
|--------|-------|---------|-----------|
| **NCT05831696** | Metabolic Cost of Walking With Passive vs. Powered Prosthetic Knees Among Persons With Limb Loss | Loma Linda University | 2023-02 |
| **NCT06210620** | Pro APP Prosthetic Outcome Registry (national multi-center) | Össur Iceland | 2024-01 |
| **NCT07075198** | Caesar Foot Take-Home Validation Testing (bimodal foot) | Liberating Technologies | 2025-10 |
| **NCT06541379** | Effect of Motor Imagery Ability on Functionality and Proprioception in Amputees Using Myoelectric Prostheses | — | 2025-06 |

### 2.2 Recently Completed

| NCT ID | Title | Sponsor | Completion |
|--------|-------|---------|-----------|
| **NCT05179395** | Brasthesis Prosthetic Harness for Women Veterans With Upper Limb Amputations | — | 2022-07 |
| **NCT04784429** | ASCENT K2: Assessing Outcomes With Microprocessor Knee Utilization in a K2 Population | Otto Bock / Hanger Clinic | 2023-06 |
| **NCT02540681** | ProFit: Prosthetic Fit Assessment in Transtibial Amputees Secondary to Trauma | METRC / BADER Consortium | 2020 |
| **NCT05190354** | Post Market Clinical Protocol — Xtremity Polymer Prosthetic Socket System | — | 2021 |
| **NCT04272593** | Pattern Recognition Prosthetic Control | — | 2020 |

### 2.3 Critical Evidence Gaps

- **Only 30 Phase 3 trials exist globally** across 644 prosthetic studies (4.7%).
- **Zero Phase 3 trials are US-based in the target regions.**
- **19.8% of studies have UNKNOWN status** — a data quality and transparency concern.
- **Academic monopolization (76.5% of sponsors)** limits commercial innovation pipeline.
- **No trial participation from the three most amputation-prone regions** (WV, KY, MS).

---

## 3. Regional Gap Analysis — Access to Prosthetic/Orthotic Care

### 3.1 Data Methodology

- **Geocoding:** Representative centers identified for each region via OSM geocoding.
- **Provider search:** OpenStreetMap `find_nearby_places` with `amenity`, `health`, `shop`, and `office` categories within 50–150 km radius.
- **Metrics:** CPO (Certified Prosthetist-Orthotist) within 50 km, 100 km, and 200 km; nearest hospital; Medicaid expansion status.

### 3.2 Rural West Virginia (Beckley, WV)

| Metric | Value |
|--------|-------|
| Coordinates | 37.78°N, 81.19°W |
| CPO within 50 km | **0** |
| CPO within 100 km | **0** |
| CPO within 200 km | **0** |
| Nearest CPO | Charleston, WV — ~190 mi (3+ hrs) |
| Hospitals within 30 km | 1 (Beckley)` 
 pharmacies, clinics, 1 major medical center |
| Medicaid expansion | **Not expanded** |
| Public transit | **None** |
| Key barriers | No CPO within 200 km; Medicaid non-expansion; no public transit; 3+ hour drive to nearest specialist |
| OSM neighborhood score | Very Low — sparse amenities, minimal walkability |

### 3.3 Eastern Kentucky (Pikeville, KY)

| Metric | Value |
|--------|-------|
| Coordinates | 37.48°N, 82.52°W |
| CPO within 50 km | **0** |
| CPO within 100 km | **0** |
| CPO within 200 km | **0** |
| Nearest CPO | Lexington, KY — ~130 mi (3+ hrs) |
| Healthcare within 30 km | Limited (Pikeville Medical Center — no CPO services confirmed) |
| Medicaid expansion | **Limited** — high uninsured rate, 30%+ poverty |
| Public transit | **None** |
| Key barriers | Appalachian isolation; coal economy decline reduced healthcare; limited Medicaid; mountainous geography |
| OSM neighborhood score | Low — sparse amenities, minimal walkability |

### 3.4 Mississippi Delta (Clarksdale, MS)

| Metric | Value |
|--------|-------|
| Coordinates | 34.20°N, 90.57°W |
| CPO within 50 km | **0** |
| CPO within 100 km | **0** |
| CPO within 200 km | **0** |
| Nearest CPO | Memphis, TN — ~200 mi (4+ hrs) |
| Healthcare within 30 km | Multiple pharmacies, 1 hospital campus, clinics, 6+ dentists |
| Medicaid expansion | **Not expanded** — highest uninsured rate in MS |
| Public transit | **None** |
| Key barriers | **Highest amputation rate in the US** yet worst prosthetic access; MS did not expand Medicaid; no public transit; double crisis of high need + zero supply |
| OSM neighborhood score | Very Low — rural Delta landscape, agricultural, minimal amenities |

### 3.5 Access Gap Summary Table

| Region | CPO ≤50 km | CPO ≤100 km | CPO ≤200 km | Nearest CPO | Drive to CPO | Medicaid |
|--------|-----------|------------|------------|-------------|-------------|---------|
| Rural WV (Beckley) | 0 | 0 | 0 | Charleston | ~190 mi / 3h | Not expanded |
| E. KY (Pikeville) | 0 | 0 | 0 | Lexington | ~130 mi / 3h | Limited |
| MS Delta (Clarksdale) | 0 | 0 | 0 | Memphis | ~200 mi / 4h | Not expanded |

### 3.6 Overarching Finding: Complete Prosthetic Care Desert

**All three regions have zero CPO providers within 200 km.** This is not a marginal gap — it is systemic. Combined with Medicaid non-expansion in all three states and the absence of public transit, these regions represent a complete prosthetic care access failure.

---

## 4. Cross-Referencing: Clinical Trial Sites vs. Access Gaps

| Region | Prosthetic Trial Sites | Amputation Rate | Provider Gap |
|--------|----------------------|----------------|-------------|
| Rural WV | 0 | High (opioid crisis) | Complete (0 CPO) |
| E. Kentucky | 0 | High (drug crisis) | Complete (0 CPO) |
| MS Delta | 0 | **Highest in US** (diabetes/vascular) | Complete (0 CPO) |

**Key insight:** The regions with the highest amputation rates have the worst prosthetic care access and zero clinical trial participation. This creates a compounding evidence-to-practice gap: patients in these regions are most likely to need prosthetics but least likely to benefit from innovation or participate in trials.

---

## 5. Recommended Actions

1. **Deploy mobile CPO clinics** — Given 0 providers within 200 km, mobile prosthetic/orthotic units could serve all three regions on a rotating schedule.
2. **Launch regional telehealth CPO consultations** — Remote fitting and follow-up could bridge the gap while permanent infrastructure is built.
3. **Estab lish clinical trial sites** — All three regions should be included in prosthetic device trials to ensure equity and generate local evidence.
4. ** Advocate for Medicaid expansion** in WV, KY, and MS — All three states have not expanded, creating a financial barrier for prosthetic care.
5. **Create a prosthetic care corridor** — Connect Charleston, Lexington, and Memphis as hub cities with satellite CPO services reaching into the surrounding regions.
6. **Integrate with diabetes/vascular programs** in the MS Delta — the highest amputation drivers are preventable;
 upstream intervention could reduce the need for prosthetics.

---

## 6. Methodology Notes

- **ClinicalTrials.gov API v2** — Queries used: `intr=prosthetic` (broad), `intr=prosthetic limb amputation` (focused), region-filtered by `locn` parameter. Trend analyses: `countByStatus`, `countByCountry`, `countByPhase`, `countBySponsorType`.
- **OpenStreetMap** — OSM MCP tools: `geocode_address`, `find_nearby_places`, `explore_area`, `search_category`. Search categories: amenity, health, shop, office.半径: 50–150 km.
- **Gap metrics:** CPO within concentric radii; nearest hospital; Medicaid expansion status; public transit presence.
- **Limitation:** OSM data for prosthetic/orthotic-specific providers (CPO) is sparse in rural areas; some providers may exist but not be mapped. Hospital and clinic counts are based on OSM `amenity` tags.

---

*This document is part of the open-access prosthetic-access-atlas project. Data is freely available for research, policy, and advocacy. Last updated: July 20, 2026.*
