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

| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid | Healthcare Score |
|--------|----------------|-------------|------------|----------|-----------------|
| Rural West Virginia (Beckley) | 0 | Charleston (~190 mi) | 3+ hrs | Not expanded | N/A |
| Eastern Kentucky (Pikeville) | 0 | Lexington (~130 mi) | 3+ hrs | Yes (2014) | 0/10 |
| Mississippi Delta (Greenville) | 0 | Memphis (~200 mi) | 4+ hrs | Not expanded | 2/10 |

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

## Sponsor Type

| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.7% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

---

## Key Findings

1. **Zero CPO providers within 30 km in all three underserved regions** — a complete absence, not a marginal gap
2. **Nearest CPO is 130–200 miles away** — beyond reasonable care access for prosthetic adjustments
3. **Mississippi Delta has the highest amputation rate in the U.S.** yet the worst care access — a double crisis
4. **All three regions lack public transit** — personal vehicle essential for any medical travel
5. **Healthcare scores are among the lowest nationally**: 0/10 (Eastern KY), 2/10 (MS Delta)
6. **Only 30 Phase 3 trials** exist across 644 studies — the evidence gap for prosthetic device efficacy is wide
7. **76.5% academic-sponsored, only 16.8% industry** — limited commercial innovation pipeline
8. **17.4% of trials actively recruiting** — modest active research engagement

---

## Repository Structure

| File | Description |
|------|-------------|
| README.md | Overview with latest data (this file) |
| FINDINGS_JULY_2026.md | Comprehensive findings report with trial trends and gap analysis |
| CLINICAL_TRIAL_REPORT.md | Detailed clinical trial analysis with sponsor/phase breakdown |
| access_gap_summary_updated.csv | Precise gap metrics CSV |
| data/access_gaps/region_profiles.md | Per-region CPO gap profiles with OSM provider listings |
| data/clinical-trial-trends-july2026.md | Trend data from ClinicalTrials.gov (644-study breakdown) |
| data/clinical-trial-trends.md | Previous trend analysis |
| data/access_gaps/region_profiles.md | Per-region CPO gap profiles |
| data/regional-healthcare-scores.md | Neighborhood livability scores |
| data/country_distribution.md | Full international distribution data |

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
