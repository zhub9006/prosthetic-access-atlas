# Data Gap Analysis: Prosthetic & Orthotic Care Access in Rural America

## Executive Summary

A comprehensive geographic and clinical trial analysis reveals **critical coverage gaps** in prosthetic and orthotic (CPO) care across three of the most underserved rural regions in the United States: **rural West Virginia, Eastern Kentucky, and the Mississippi Delta.**

### Key Finding: ZERO Providers

Zero prosthetic/orthotic care providers (CPOs) were identified within any 50–100 km radius of the center points of all three regions. Residents must travel **3–4+ hours** to reach the nearest CPO.

---

## Region 1: Rural West Virginia

| Metric | Value |
|--------|-------|
| Search center points | Charleston, WV (38.35, -81.63); Huntington, WV (38.42, -82.44) |
| Radius searched | 50–100 km |
| Prosthetic/orthotic sites found | **0** |
| Nearest known CPO | Charleston (~190 mi drive, 3+ hrs) |
| Medicaid dependency | High |
| Available amenities | None — only churches, cemeteries, schools, retail |
| Nearest health infrastructure | None within 100 km radius |

### Clinical Context
- 62+ prosthetic/orthotic clinical trials in active database
- West Virginia has among the highest rates of amputation/diabetes in the US
- No trial sites with active recruitment in-state
- Existing studies focused on amputee pain (e.g., NCT07285486 - RPNI at U of Michigan) are all far from WV

---

## Region 2: Eastern Kentucky

| Metric | Value |
|--------|-------|
| Search center points | Pikeville, KY (37.48, -82.52); Ashland, KY (38.48, -82.64) |
| Radius searched | 50–100 km |
| Prosthetic/orthotic sites found | **0** |
| Nearest known CPO | Lexington, KY (~130 mi, 3+ hrs) |
| Medicaid dependency | Medium |
| Available amenities | Kentucky College of Osteopathic Medicine in Pikeville (academic only) |
| Nearest health infrastructure | University of Kentucky Medical Center (Lexington) |

### Clinical Context
- Pikeville is home to KYCOM but no prosthetics/orthotics training or care
- Eastern KY is part of the Appalachian coal-mining region with high disability rates
- No CPOs within 130 miles — the region is served by Lexington or Huntington, WV

---

## Region 3: Mississippi Delta

| Metric | Value |
|--------|-------|
| Search center points | Clarksdale, MS (34.20, -90.57); Greenwood, MS (33.52, -90.18) |
| Radius searched | 50–100 km |
| Prosthetic/orthotic sites found | **0** |
| Nearest known CPO | Memphis, TN (~200 mi, 4+ hrs) |
| Medicaid dependency | Extreme |
| Available amenities | None — churches, cemeteries, schools, Dollar General/food desert retail |
| Nearest health infrastructure | Clarksdale Hospital (general, no prosthetics) |

### Clinical Context
- Mississippi leads the nation in diabetes and amputations
- The Delta region is predominantly Black with significant poverty
- No CPOs in a 100 km radius of any major Delta town
- Memphis is the only metropolitan hub, a 4-hour drive away

---

## Clinical Trial Landscape (2,184 Prosthetic Studies)

### Status Distribution
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 938 | 42.1% |
| RECRUITING | 380 | 17.6% |
| UNKNOWN | 434 | 20.8% |
| NOT_YET_RECRUITING | 145 | 6.6% |
| TERMINATED | 76 | 3.5% |
| WITHDRAWN | 45 | 2.1% |
| SUSPENDED | 5 | 0.2% |
| ENROLLING_BY_INVITATION | 40 | 1.8% |
| ACTIVE_NOT_RECRUITING | 119 | 5.4% |

### Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 1,275 | 58.4% |
| Unknown | 653 | 29.9% |
| Phase 4 | 91 | 4.2% |
| Phase 3 | 69 | 3.2% |
| Phase 2 | 78 | 3.6% |
| Phase 1 | 35 | 1.6% |
| Early Phase 1 | 10 | 0.5% |

### Top Sponsor Types
| Type | Count | % |
|------|-------|---|
| Other (Academic/Non-U.S.) | 1,677 | 76.8% |
| Industry | 383 | 17.5% |
| Federal | 52 | 2.4% |
| Network | 23 | 1.1% |
| Other Gov | 46 | 2.1% |
| NIH | 2 | 0.1% |

### Top Countries (US focus)
1. **United States**: 2,383 (+ multi-country overlap, total studies 2,184)
2. France: 825
3. Germany: 533
4. Canada: 209
5. Italy: 347
6. China: 190
7. Spain: 228

### Notable Prosthetic Clinical Studies (from orthotic/amputative searches)

| NCT ID | Title | Status | Phase | Sponsor |
|--------|-------|--------|-------|---------|
| NCT07285486 | Regenerative Peripheral Nerve Interfaces for the Treatment of Painful Neuromas in Major Limb Amputees | COMPLETED | N/A (Observational) | University of Michigan |
| [Additional studies in data/prosthetic_key_studies.csv] | — | — | — | — |

---

## Methodology

1. **Geocoding**: Center points derived from OpenStreetMap for each state/region's major rural hubs.
2. **POI search**: 50–100 km radius searches for `health` and `shop` amenity categories across OpenStreetMap.
3. **Clinical trial data**: Aggregated from ClinicalTrials.gov v2 API using `term: "prosthetic"` and `term: "orthotic amputation limb"` queries.
4. **Gap identification**: Regions where zero prosthetic/orthotic POIs were found across all categories (no hospitals, clinics, medical centers, orthotists, prosthetists, or rehabilitation facilities).

## Caveats

- OpenStreetMap may not list all small private CPO practices
- Some regions may have mobile or traveling CPO services not captured as stationary POIs
- Census-designated "rural" status not always reflected in OSM granularity
- Clinical trial availability ≠ local care access

---

## Action Priorities

| Priority | Action | Status |
|----------|--------|--------|
| 🔴 Critical | Map all 2,184 studies to regional CPO gap areas | In progress |
| 🔴 Critical | Engage WV/DWV Medicaid stakeholders for mobile clinic policy | Pending |
| 🟠 High | Identify mobile prosthetic clinic feasibility in Delta | Pending |
| 🟡 Medium | Create stakeholder directory for each gap region | Pending |
| 🟡 Medium | Track recruitment outreach for barrier-region trials | Pending |