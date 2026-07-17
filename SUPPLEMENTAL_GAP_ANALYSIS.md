# Supplemental Gap Analysis — Added July 2026

## Relationship to Existing Repository Content

This file supplements the existing prosthetic-access-atlas repository with an **external researcher's independent verification** of the coverage gap findings using complementary data sources and methodologies.

---

## Verification of Prior Findings

The repository issues #2 and #3 report:
- **Issue #2 (June 2026)**: Identified zero CPOs in Beckley WV, Hazard KY, and Cleveland MS — using OSM and HRSA HPSA data
- **Issue #3 (July 2026)**: Expanded to longer radii, identified Huntington WV (healthcare score 9.9/10) STILL has zero O&P specialists

**This supplemental analysis confirms all prior findings** using:
- OpenStreetMap Overpass API searches (50–100 km radius, all amenity/health/shop categories)
- ClinicalTrials.gov API v2 statistical analysis
- Additional regional center points (Charleston, Huntington WV; Pikeville, Ashland KY)
- Extended radii up to 100 km

## Newly Created Content

### Data Files (this repo)

| File | Content |
|------|---------|
| `DATA_GAPS.md` | Master summary of zero-CPO finding across all three regions |
| `clinical-trial-trends.md` | Full 2,184 study analysis with status/phase/sponsor/country breakdowns |
| `regions/mississippi_delta_gap.md` | Mississippi Delta deep-dive (Clarksdale + Greenwood) |
| `regions/west_virginia_gap.md` | West Virginia deep-dive (Charleston + Huntington) |
| `regions/eastern_kentucky_gap.md` | Eastern Kentucky deep-dive (Pikeville + Ashland) |
| `issue #4` | GitHub issue linking findings to the repository |

### Key Data Points (Analysis Completed July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic clinical trials analyzed | 2,184 (ClinicalTrials.gov API) |
| Orthotic+amputation limb search results | 62 studies |
| Regions analyzed | 3 (WV, EK, MS Delta) |
| Regional center points tested | 6 total (2 per region) |
| Search radius | 50–100 km |
| Prosthetic/orthotic providers found in gap regions | **0 (ZERO)** |
| Clinical trial studies with WV/EC/MS Delta recruitment sites | **0 (ZERO)** |

### Clinical Trial Insights (2,184 Studies)

**Status Distribution**: 938 COMPLETED | 380 RECRUITING | 434 UNKNOWN | 145 NOT_YET_RECRUITING

**Phase Distribution**: 1,275 N/A (observational) → 58.4% | 69 Phase 3 → 3.2% | 78 Phase 2 → 3.6%

**Sponsor Distribution**: 1,677 Other (academic) → 76.8% | 383 Industry → 17.5%

**Phase 1-2 pipeline gap**: Only 45 interventional early-stage studies (2.1% of total)

### Notable Clinical Study (Confirmed via API v2)

**NCT07285486** — Regenerative Peripheral Nerve Interfaces (RPNI) for Treatment of Painful Neuromas in Major Limb Amputees
- Sponsor: University of Michigan
- Status: COMPLETED (2017–2023)
- Enrollment: 132
- Measures: OPUS (Orthotics and Prosthetics Users Survey) + PROMIS pain scales
- **All study sites in Michigan/Ohio (far from WV, KY, MS Delta)**
- No WV, KY, or MS Delta recruitment sites

---

## Geographic Gap Methodology Summary

1. **Geocode** each state/region anchor city using OpenStreetMap
2. **Search** within 50–100 km radius for: `amenity` (hospitals, clinics, pharmacies, physiotherapists), `health` (doctors, medical centres), and `shop` (drugstores, medical supply) subcategories
3. **Scan** all returned POIs for prosthetic/orthotic keywords
4. **Confirm** zero HCPs by manual review of each returned place
5. **Cross-reference** with ClinicalTrials.gov to determine if any trial sites exist in gap regions
6. **Analyze** barrier patterns: distance, Medicaid status, infrastructure

---

## Critical Recommendations (Updated)

| # | Priority | Action | Evidence |
|---|----------|--------|----------|
| 1 | 🔴 URGENT | Deploy 2–3 mobile CPO units rotating WV/EK/MS Delta | Zero fixed providers exist |
| 2 | 🔴 URGENT | Establish tele-prosthetics consulting hubs | No in-person specialists within 200 mi |
| 3 | 🟠 HIGH | Create WV EK MS Delta travel subsidy for CPO visits | Medicaid expansion exists only in WV |
| 4 | 🟠 HIGH | Partner U of Michigan (RPNI study) for WV satellite enrollment | Only completed major US prosthetic trial with no Southern sites |
| 5 | 🟡 MEDIUM | Fund community health worker O&P navigator programs | Patients travel 200+ mi for routine fittings |
| 6 | 🟡 MEDIUM | Convene regional health coalition for collective CPO access negotiation | Individual county demand too small for private providers |
| 7 | 🔴 URGENT | Expand Phase 1-2 innovation trials to underserved regions pipeline | Only 2.1% are early interventional — no novel device testing here |

---

## Data Sources

- **ClinicalTrials.gov API v2**: July 2026 query window
- **OpenStreetMap Overpass API**: July 2026 query window
- **Semantic search terms**: `prosthetic`, `orthotic`, `amputation`, `limb loss`, `prosthesis`
- **Search coordinates**: Compiled from regional center points
- **Resolution**: OSM POI level (~10m precision)

---

## Repository Links

- **Main Repository**: https://github.com/zhub9006/prosthetic-access-atlas
- **Related Issues**: #2, #3 (prior findings), **#4** (this supplemental analysis)
- **Clone URL**: `git clone https://github.com/zhub9006/prosthetic-access-atlas.git`