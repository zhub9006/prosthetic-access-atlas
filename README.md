# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies analyzed | 155 (core) / 563+ (broad) |
| Trials actively recruiting | 32 (20.6%) |
| Trials completed | 53 (34.2%) |
| Phase 3 trials | **4 (2.6%)** — critically scarce |
| Industry-sponsored trials | 30 (19.4%) |
| Academic-sponsored trials | 109 (70.3%) |
| Regions with zero CPO providers | **3 of 3** |
| Average distance to nearest CPO | 250+ km (155+ mi) |

## Access Gap Summary

| Region | CPO Within 100km | Nearest CPO | Drive Time | Medicaid |
|--------|------------------|-------------|------------|----------|
| Rural West Virginia | 0 | Charleston (~250+ km) | 3+ hrs | Not expanded |
| Eastern Kentucky | 0 | Lexington (~350+ km) | 4+ hrs | Limited |
| Mississippi Delta | 0 | Memphis (~250+ km) | 3+ hrs | Not expanded |

## Clinical Trial Trends (n=155, July 2026)

| Status | Count | % |
|--------|-------|---|
| RECRUITING | 32 | 20.6% |
| COMPLETED | 53 | 34.2% |
| UNKNOWN | 25 | 16.1% |
| NOT_YET_RECRUITING | 15 | 9.7% |
| ACTIVE_NOT_RECRUITING | 17 | 11.0% |

| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 80 | 51.6% |
| Unknown | 52 | 33.5% |
| Phase 2 | 11 | 7.1% |
| Phase 3 | 4 | 2.6% |

## Key Findings

- Zero CPO providers within 100 km in all three underserved regions
- Nearest CPO is 250-350+ km away — beyond reasonable care access
- All three states (WV, KY, MS) have not expanded Medicaid
- MS Delta has highest amputation rates yet worst care access
- Only 4 Phase 3 trials across all prosthetic studies
- 70% academic-sponsored — minimal industry investment
- 20.3% UNKNOWN status — data quality concern

## Repository Structure

| File | Description |
|------|-------------|
| ATLAS_FULL_REPORT.md | Comprehensive report with all findings |
| clinical-trial-trends-2026.md | Updated 2026 trends + 2025 comparison |
| data/access_gaps_2026.json | Updated 2026 gap data with neighborhood scores |
| data/access_gaps.json | Structured gap data (JSON) |
| data/clinical_trials.csv | Clinical trial data extract |

## Methodology

- Clinical Trial Data: ClinicalTrials.gov API v2 (July 2026)
- Geospatial Mapping: OpenStreetMap MCP tools (50-200 km radius)
- Provider Search: Nearby POI search using health/amenity/shop categories
- Gap Analysis: Provider density vs. population need

## License

MIT (Open Access) — free to use for research, policy, and advocacy.

*Built to improve prosthetic care access for all. Open and free.*