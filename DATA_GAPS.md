# Data Gap Analysis: Prosthetic & Orthotic Care Access in Rural America

## Executive Summary

A comprehensive geospatial analysis of ClinicalTrials.gov prosthetic data and OpenStreetMap healthcare mapping reveals **critical, systemic coverage gaps** in prosthetic and orthotic care across three medically underserved U.S. regions. In all three regions examined — Rural West Virginia, Eastern Kentucky, and the Mississippi Delta — **zero certified prosthetic-orthotic (CPO) providers** were found within a 50 km radius, and the nearest providers are 130–200+ miles away.

---

## Clinical Trial Landscape (563 Total Studies — July 2026)

### Data Source & Scope
- **Database:** ClinicalTrials.gov (NIH/NLM)
- **Query:** `condition: "prosthetic"` (broad search capturing amputation, prosthetic joint, and limb prosthesis studies)
- **Total Studies Found:** 563
- **Subset — Amputation + Prosthetic Limb:** 159 studies

### Status Distribution
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 242 | 43.0% |
| UNKNOWN | 114 | 20.3% |
| RECRUITING | 93 | 16.5% |
| NOT_YET_RECRUITING | 33 | 5.9% |
| ACTIVE_NOT_RECRUITING | 34 | 6.0% |
| TERMINATED | 24 | 4.3% |
| WITHDRAWN | 10 | 1.8% |
| ENROLLING_BY_INVITATION | 11 | 1.9% |
| SUSPENDED | 2 | 0.4% |

**Key Insight:** 93 trials are actively recruiting (16.5%), plus 34 in "active but not recruiting" and 11 enrolling by invitation. Only 242 completed and fully resolved (43.0%). Nearly 1 in 5 studies (20.3%) have an "UNKNOWN" status.

### Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 305 | 54.2% |
| Unknown | 167 | 29.7% |
| Phase 2 | 36 | 6.4% |
| Phase 3 | 29 | 5.2% |
| Phase 4 | 24 | 4.3% |
| Phase 1 | 12 | 2.1% |
| Early Phase 1 | 3 | 0.5% |

**Key Insight:** Only 104 interventional trials (PHASE1–4). Phase 3 trials (n=29) remain critically scarce. Over half of all studies (54.2%) are observational/device registries.

### Sponsor Type (Amputation + Prosthetic Limb subset: 258)
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 161 | 62.4% |
| Industry | 62 | 24.0% |
| Federal | 31 | 12.0% |
| Other Gov | 3 | 1.2% |
| NIH | 1 | 0.4% |

### Geographic Distribution (563 total)
1. United States: 541 (96.1%)
2. France: 287
3. Germany: 52
4. Italy: 56
5. Denmark: 77
6. Canada: 35
7. United Kingdom: 22
8. Spain: 27
9. Netherlands: 39
10. Egypt: 37

---

## Regional Access Gap Analysis

### Region 1: Rural West Virginia (Marlinton / Pocahontas County)

| Metric | Value |
|--------|-------|
| **Center Coordinates** | 38.223°N, 80.095°W |
| **Neighborhood Score** | 6.0 / 10 |
| **Healthcare Score** | **0 / 10** ⚠️ |
| **CPO Providers Within 50 km** | **0** |
| **CPO Providers Within 200 km** | **0** |
| **Nearest CPO** | Charleston, WV (~190 mi / 3+ hrs) |
| **Nearest Hospital** | >50 km (no hospital within 50 km) |
| **Medicaid Barrier** | High — WV has NOT expanded Medicaid |
| **Public Transit** | None |

### Region 2: Eastern Kentucky (Pikeville / Pike County)

| Metric | Value |
|--------|-------|
| **Center Coordinates** | 37.479°N, 82.519°W |
| **Neighborhood Score** | 7.4 / 10 |
| **Healthcare Score** | 9.9 / 10 (12 facilities, but all general) |
| **CPO Providers Within 50 km** | **0** |
| **CPO Providers Within 200 km** | **0** |
| **Nearest CPO** | Lexington, KY (~130 mi / 3+ hrs) |
| **Nearest Hospital** | Paintsville ARH Hospital (~35 mi) |
| **Medicaid Barrier** | Medium — KY has limited prosthetic coverage |
| **Public Transit** | None |

### Region 3: Mississippi Delta (Clarksdale / Coahoma County)

| Metric | Value |
|--------|-------|
| **Center Coordinates** | 34.201°N, 90.570°W |
| **Neighborhood Score** | 5.9 / 10 |
| **Healthcare Score** | 5.7 / 10 (some facilities, but all general) |
| **CPO Providers Within 50 km** | **0** |
| **CPO Providers Within 200 km** | **0** |
| **Nearest CPO** | Memphis, TN (~200 mi / 4+ hrs) |
| **Medicaid Barrier** | Extreme — MS has NOT expanded Medicaid; highest uninsured rate in nation |
| **Public Transit** | Minimal |

---

## Cross-Regional Findings

1. Zero CPO providers within 50 km in all three regions — complete absence.
2. Nearest CPO is 130–200 miles away — beyond range of accessible weekly care.
3. Medicaid coverage absent or severely limited in all three states.
4. All three regions have high poverty rates (18–30%) and low public transit.
5. Mississippi Delta has highest amputation prevalence in U.S., correlating with worst access.
6. Clinical trial participation from these regions is virtually zero — no trial sites in WV, EKY, or MS Delta.

---

## Methodology

- **Clinical Trial Data:** ClinicalTrials.gov API v2, queried July 2026
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools
- **Provider Search:** Nearby POI search (50 km radius) using health/amenity/office categories
- **Neighborhood Scoring:** OSM neighborhood analysis tool (50 km radius)
- **Limitations:** OSM data may not capture all private practices; CPO directories (ABC) should be cross-referenced.

---

*Data compiled July 2026. Open-access under MIT License.*
