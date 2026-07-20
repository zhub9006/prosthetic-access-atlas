# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies analyzed | **563** (broad search) |
| Trials actively recruiting | **93** (16.5%) |
| Trials completed | **242** (43.0%) |
| Phase 3 efficacy trials | **29** (5.2%) — critically scarce |
| Industry-sponsored trials | **108** (16.8%) |
| Academic-sponsored trials | **493** (76.5%) |
| Regions with zero CPO providers (30km) | **3 of 3** |
| Average distance to nearest CPO | **130–200+ miles** |

---

## Access Gap Summary

| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid |
|--------|----------------|-------------|------------|----------|
| Rural West Virginia | 0 | Charleston (~190 mi) | 3+ hrs | Not expanded |
| Eastern Kentucky | 0 | Lexington (~130 mi) | 3+ hrs | Limited |
| Mississippi Delta | 0 | Memphis (~200 mi) | 4+ hrs | Not expanded |

---

## Clinical Trial Trends (n=563, July 2026)

### Status Distribution
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 242 | 43.0% |
| UNKNOWN | 114 | 20.3% |
| RECRUITING | 93 | 16.5% |
| ACTIVE_NOT_RECRUITING | 34 | 6.0% |
| NOT_YET_RECRUITING | 33 | 5.9% |
| TERMINATED | 24 | 4.3% |
| WITHDRAWN | 10 | 1.8% |
| ENROLLING_BY_INVITATION | 11 | 1.9% |
| SUSPENDED | 2 | 0.4% |

### Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 305 | 54.2% |
| Unknown | 167 | 29.7% |
| Phase 4 | 24 | 4.3% |
| Phase 2 | 36 | 6.4% |
| Phase 3 | 29 | 5.2% |
| Phase 1 | 12 | 2.1% |
| Early Phase 1 | 3 | 0.5% |

### Sponsor Type
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.8% |
| Network + NIH | 6 | 0.9% |

---

## Key Findings

1. **Zero CPO providers within 30 km in all three underserved regions** — a complete absence, not a marginal gap
2. **Nearest CPO is 130–200 miles away** — beyond reasonable care access
3. **All three states (WV, KY, MS) have not expanded Medicaid** — compounding geographic barriers
4. **MS Delta has highest amputation rates yet worst care access** — a double crisis
5. **Only 29 Phase 3 trials across all 563 studies** — the evidence gap for prosthetic device efficacy is wide
6. **76.5% academic-sponsored, only 16.8% industry** — limited commercial innovation pipeline

---

## Repository Structure

| File | Description |
|------|-------------|
| README.md | Overview with latest data (this file) |
| CLINICAL_TRIAL_REPORT.md | Detailed clinical trial analysis with sponsor/phase breakdown |
| clinical-trial-trends.md | Full trial trends with selected study profiles |
| access_gap_summary_updated.csv | Precise gap metrics CSV |
| data/access_gaps/region_profiles.md | Per-region CPO gap profiles with OSM provider listings |
| data/regional-healthcare-scores.md | Neighborhood livability scores (30km radius) |
| data/clinical-trial-trends.md | Trend data from ClinicalTrials.gov Analysis |
| data/clinical_trials_data.md | Original trial data extract |
| data/clinical-trials-data.md | Latest trial data with full study details |
| data/key_studies.md | Detailed study profiles for notable prosthetic trials |
| data/country_distribution.md | Full international distribution data |
| data/sources.md | Methodology, API endpoints, and data lineage |

---

## Methodology

- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (30 km radius)
- **Provider Search:** Nearby POI search using health/amenity/office categories
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
