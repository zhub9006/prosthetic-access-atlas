# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies analyzed | **644** (broad search: `cond=prosthetic`) |
| Trials actively recruiting | **112** (17.4%) |
| Trials completed | **271** (42.1%) |
| Phase 3 efficacy trials | **30** (4.7%) — critically scarce |
| Industry-sponsored trials | **108** (16.8%) |
| Academic-sponsored trials | **493** (76.5%) |
| Regions with zero CPO providers (30km) | **3 of 3** |
| Average distance to nearest CPO | **130–200+ miles** |

---

## Access Gap Summary

| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid Expanded | Healthcare Score |
|--------|----------------|-------------|------------|-------------------|-----------------|
| Rural West Virginia (Beckley) | 0 | Charleston (~190 mi) | 3+ hrs | No | N/A |
| Eastern Kentucky (Hazard) | 0 | Lexington (~130 mi) | 3+ hrs | No | ~2.8/10 |
| Mississippi Delta (Greenville) | 0 | Memphis (~200 mi) | 4+ hrs | No | ~3.5/10 |

> **Note:** None of the three target states (WV, KY, MS) have expanded Medicaid. The previous README erroneously listed KY as "Yes (2014)" — **Kentucky did NOT expand Medicaid** under the ACA. This has been corrected.

---

## Clinical Trial Status Distribution (n=644)

| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| RECRUITING | 112 | 17.4% |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| TERMINATED | 24 | 3.7% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

---

## Phase Distribution (n=644)

| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 4 | 29 | 4.5% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

---

## Key Findings

1. **Zero CPO providers within 30 km in all three underserved regions** — a complete absence, not a marginal gap
2. **Nearest CPO is 130–200 miles away** — beyond reasonable care access
3. **All three states (WV, KY, MS) have not expanded Medicaid** — compounding geographic barriers
4. **MS Delta has highest amputation rates yet worst care access** — a double crisis
5. **Only 30 Phase 3 trials across all 644 studies** — the evidence gap for prosthetic device efficacy is wide
6. **76.5% academic-sponsored, only 16.8% industry** — limited commercial innovation pipeline
7. **Personalisation of Prosthetic Care (NCT06243549, University of Bath)** is the most recent notable trial, studying biomechanical/psychological pathways of lower back pain in below-knee amputees

---

## Repository Structure

### New / Recently Updated Files (July 2026)

| File | Description |
|------|-------------|
| **clinical-trial-trends-latest.md** | Full status, phase, sponsor, and geographic trend analysis with structured tables |
| **coverage-gap-analysis.md** | Comprehensive per-region provider search results, gap metrics, and next-step recommendations |
| data/clinical-trial-trends-full.md | Raw trial data with full status, phase, sponsor, and geographic breakdowns |
| data/access_gap_metrics.csv | Precise gap metrics in CSV format for programmatic use |
| data/regional-healthcare-scores.md | Updated livability and healthcare access scores with DHS-verified provider data |

### Existing Files

| File | Description |
|------|-------------|
| README.md | Overview with latest data (this file) |
| CLINICAL_TRIAL_REPORT.md | Detailed clinical trial analysis |
| clinical-trial-trends.md | Full trial trends with selected study profiles |
| access_gap_summary_updated.csv | Gap metrics CSV |
| data/clinical_trials_data.md | Original trial data extract |
| data/clinical-trials-data.md | Latest trial data with full study details |
| data/key_studies.md | Detailed study profiles for notable prosthetic trials |
| data/country_distribution.md | Full international distribution data |

---

## Methodology

- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
  - List Studies: `GET /api/v2/studies?query.cond=prosthetic&query.term=prosthetic+care`
  - Analyze Trends: `countByStatus`, `countByPhase`, `countBySponsorType`, `countByCountry`
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (30–50 km radius from representative towns)
- **Provider Search:** Nearby POI search using healthcare and amenity categories
- **Neighborhood Scoring:** OSM neighborhood analysis tool (0–10 scale across 10 categories)
- **Gap Metrics:** Distance to nearest Certified Prosthetist-Orthotist (CPO) from representative town in each region

## Contributing
1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License
MIT (Open Access) — free to use for research, policy, and advocacy.

---

*Built to improve prosthetic care access for all. Open and free.*