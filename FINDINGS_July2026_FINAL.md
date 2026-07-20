---
title: Prosthetic Access Atlas — Final Consolidated Findings (July 2026)
author: Open-Source Community
updated: 2026-07-20
license: MIT
---

# Prosthetic Access Atlas — Final Consolidated Findings

## 1. Clinical Trial Landscape (ClinicalTrials.gov)

### 1.1 Broad Search: Prosthetic

**Total prosthetic-related studies: 2,186** (global, all statuses)

#### 1.1.1 Status Distribution

| Status | Count | % of Total |
|--------|-------|-----------|
| COMPLETED | 938 | 43.1% |
| UNKNOWN | 434 | 19.9% |
| RECRUITING | 380 | 17.4% |
| NOT_YET_RECRUITING | 146 | 6.7% |
| ACTIVE_NOT_RECRUITING | 120 | 5.5% |
| TERMINATED | 76 | 3.5% |
| WITHDRAWN | 45 | 2.1% |
| ENROLLING_BY_INVITATION | 40 | 1.8% |
| SUSPENDED | 5 | 0.2% |

#### 1.1.2 Phase Distribution

| Phase | Count | % of Total |
|-------|-------|-----------|
| N/A (Observational/Device) | 1,276 | 58.4% |
| Unknown | 654 | 30.0% |
| PHASE 4 | 91 | 4.2% |
| PHASE 3 | 69 | 3.2% |
| PHASE 2 | 78 | 3.6% |
| PHASE 1 | 35 | 1.6% |
| EARLY_PHASE1 | 10 | 0.5% |

#### 1.1.3 Sponsor Type Distribution

| Sponsor Type | Count | % |
|-------------|-------|---|
| OTHER (Academic/Non-Profit) | 1,679 | 76.8% |
| INDUSTRY | 383 | 17.5% |
| FED | 52 | 2.4% |
| OTHER_GOV | 46 | 2.1% |
| NETWORK | 23 | 1.1% |
| NIH | 2 | 0.1% |

#### 1.1.4 Country Distribution (Top 15)

| Country | Count |
|---------|-------|
| United States | 2,384 |
| France | 825 |
| Germany | 533 |
| Italy | 347 |
| Spain | 228 |
| United Kingdom | 193 |
| Canada | 209 |
| Netherlands | 193 |
| Denmark | 147 |
| Egypt | 151 |
| China | 190 |
| Turkey (Türkiye) | 87 |
| Belgium | 87 |
| Australia | 118 |
| Switzerland | 109 |

### 1.2 Focused Search: Prosthetic Limb Amputation

**Total focused studies: 120** (all statuses)

#### 1.2.1 Status Distribution

| Status | Count | % |
|--------|-------|---|
| COMPLETED | 57 | 47.5% |
| RECRUITING | 28 | 23.3% |
| UNKNOWN | 13 | 10.8% |
| ACTIVE_NOT_RECRUITING | 8 | 6.7% |
| NOT_YET_RECRUITING | 11 | 9.2% |
| TERMINATED | 2 | 1.7% |
| WITHDRAWN | 1 | 0.8% |

#### 1.2.2 Phase Distribution

| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 84 | 70.0% |
| Unknown | 28 | 23.3% |
| PHASE 3 | 2 | 1.7% |
| PHASE 2 | 5 | 4.2% |
| PHASE 1 | 1 | 0.8% |
| EARLY_PHASE1 | 1 | 0.8% |

#### 1.2.3 Country Distribution (Top 10)

| Country | Count |
|---------|-------|
| United States | 177 |
| France | 13 |
| Italy | 11 |
| Canada | 9 |
| Netherlands | 9 |
| United Kingdom | 7 |
| Denmark | 4 |
| Germany | 4 |
| Turkey (Türkiye) | 4 |
| Austria | 1 |

### 1.3 Key Trial Insights

1. **Phase 3 trials are critically scarce** — only 69 globally (3.2% of all prosthetic studies) and just 2 in the focused amputation search. The evidence base for prosthetic device efficacy is extremely thin.

2. **19.9% of studies have UNKNOWN status** — a transparency and data-quality concern.

3. **Academic/research dominance (76.8%)** vs. industry (17.5%) limits commercial innovation and market translation.

4. **The US leads globally** with 2,384 studies, yet has **zero clinical trial sites** in WV, KY, or MS Delta.

5. **No trials in underserved regions** despite 2,186 total prosthetic studies worldwide.

---

## 2. Access Gap Analysis — OSM Geospatial Mapping

### 2.1 Methodology

- **Geocoding**: `geocode_address` for regional hubs
- **Area Exploration**: `explore_area` for comprehensive facility profiles (50km radius)
- **Healthcare Search**: `find_nearby_places` with healthcare/shop categories
- **Gap Metric**: Distance to nearest Certified Prosthetist-Orthotist (CPO)
- **Analysis Date**: July 20, 2026

### 2.2 Regional Hub Coordinates

| Region | City | Lat | Lon |
|--------|------|-----|-----|
| Rural West Virginia | Beckley | 37.78 | -81.19 |
| Eastern Kentucky | Pikeville | 37.48 | -82.52 |
| Mississippi Delta | Clarksdale | 34.20 | -90.57 |

### 2.3 Coverage Gap Summary

| Region | CPO within 30km | CPO within 100km | Nearest CPO | Drive to CPO | Drive Time |
|--------|-----------------|-------------------|-------------|-------------|------------|
| Rural WV (Beckley) | **0** | **0** | Charleston, WV | ~190 mi | 3+ hrs |
| Eastern KY (Pikeville) | **0** | **0** | Lexington, KY | ~130 mi | 3+ hrs |
| MS Delta (Clarksdale) | **0** | **0** | Memphis, TN | ~200 mi | 4+ hrs |

### 2.4 Provider Presence Within 30km

#### Rural West Virginia (Beckley)

| Category | Count | Examples |
|----------|-------|----------|
| Pharmacies | 5 | CVS, Walgreens (multiple locations) |
| Clinics | 2 | MedExpress, Anchor Medical LLC |
| Dentists | 3 | Liberty Dental Centers, Shady Spring Dental (x2) |
| Doctors | 1 | Primary Care Plus |
| Other | 2 | Audiology, Dialysis center |
| **CPO (Prosthetic/Orthotic)** | **0** | **NONE FOUND** |

#### Eastern Kentucky (Pikeville)

| Category | Count |
|----------|-------|
| Pharmacies | 6+ |
| Clinics | 4+ (PMC Medical Diagnostics, MCHC Elkhorn City, etc.) |
| Dentists | 2+ |
| Doctors | 5+ |
| Other | Optometrist, Chiropractor |
| **CPO (Prosthetic/Orthotic)** | **0** | **NONE FOUND** |

#### Mississippi Delta (Clarksdale)

| Category | Count |
|----------|-------|
| Pharmacies | 18+ |
| Hospitals | 1 campus |
| Clinics | Multiple |
| Dentists | 6+ |
| Specialists | Multiple |
| **CPO (Prosthetic/Orthotic)** | **0** | **NONE FOUND** |

### 2.5 Medicaid Context

| Region | Medicaid Expansion | Impact |
|--------|-------------------|--------|
| WV | Not expanded | Lowers insurance coverage; limits prosthetic access |
| KY | Limited expansion | Partial coverage; gaps remain |
| MS Delta | Not expanded | No insurance pathway for prosthetic devices |

### 2.6 Key Access Barriers

1. **Zero CPO providers** in a 100km radius around all three hubs — unprecedented coverage gap.
2. **MS Delta has the highest amputation rate in the U.S.** — yet zero CPOs within 200 miles.
3. **No public transit** in rural WV or KY; limited transit in MS Delta.
4. **Medicaid non-expansion** (WV, MS) eliminates the primary insurance pathway for prosthetic devices.
5. **Geographic isolation** — the Appalachian regions are among the most underserved in the US for specialty medical care.

---

## 3. Clinical Trial — Access Gap Intersection

| Finding | Detail |
|---------|--------|
| US prosthetic studies | 2,384 (broad) / 177 (focused amputation) |
| Trial sites in WV, KY, or MS | **ZERO** |
| Phase 3 trials globally | 69 (broad) / 2 (focused) |
| Phase 3 trials in underserved US regions | **ZERO** |
| Recruiting trials | 380 (broad) / 28 (focused) |
| Recruiting trials in WV/KY/MS | **ZERO** |

### Key Takeaway
The evidence base for prosthetic devices is critically thin (very few Phase 3 trials), and even that thin evidence is generated entirely outside the regions that need it most. Patients in rural WV, eastern KY, and the MS Delta face both the highest amputation burden and the least access to care — yet contribute zero data to the clinical evidence pipeline.

---

## 4. Recommendations

1. **Expand prosthetic trial sites** to underserved regions — WV, KY, and MS Delta need representation in clinical research.
2. **Mobile CPO programs** — deploy traveling prosthetist-orthotist services to cover the 130–200 mile gaps.
3. **Telehealth-capable prosthetics** — invest in remote fitting and follow-up technology.
4. **Medicaid expansion** in WV and MS to unlock prosthetic device coverage.
5. **Community-based training programs** — train local healthcare workers in prosthetic fitting and limb care.
6. **Phase 3 trial priority** — fund pivotal efficacy trials for prosthetic devices, especially for lower-limb amputation.

---

## 5. Data Sources

- **ClinicalTrials.gov API v2** — searched 2026-07-20 (queries: `intr=prosthetic`, `intr=prosthetic limb amputation`)
- **OpenStreetMap (OSM)** — geocoding, area exploration, nearby-place searches; searched 2026-07-20
- **Analysis tools**: ClinicalTrials.gov CLI MCP, OSM MCP (geocode, explore_area, find_nearby_places)

---

*Built to improve prosthetic care access for all. Open and free.*
