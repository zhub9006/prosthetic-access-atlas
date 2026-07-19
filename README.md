# Prosthetic Access Atlas

An open-access resource mapping prosthetic clinical trial landscapes and uncovering care access gaps in underserved U.S. regions.

## Clinical Trial Trends (563 Total Studies — Updated July 2026)

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

**Key Insight:** 93 trials actively recruiting + 34 active-not-recruiting + 11 enrolling-by-invitation = 138 trials with some form of active patient engagement. Only 242 completed (43.0%). 20.3% have UNKNOWN status — a data quality concern.

### Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 305 | 54.2% |
| Unknown | 167 | 29.7% |
| Phase 2 | 36 | 6.4% |
| Phase 3 | 29 | 5.2% |
| Phase 1 | 12 | 2.1% |
| Phase 4 | 24 | 4.3% |
| Early Phase 1 | 3 | 0.5% |

**Key Insight:** Only 104 interventional trials. Phase 3 trials (n=29) are critically scarce — the evidence gap for prosthetic device efficacy remains wide. Over half (54.2%) are observational/device registries.

### Sponsor Type
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.8% |
| Network + NIH | 6 | 0.9% |

### Geographic Distribution (Top 10)
1. United States: 541
2. France: 287
3. Germany: 52
4. Italy: 56
5. Denmark: 77
6. Canada: 35
7. United Kingdom: 22
8. Spain: 27
9. Netherlands: 39
10. Egypt: 37

## Access Gap Summary
| Region | CPO Within 50km | Nearest CPO | Travel | Medicaid Barrier | Transit |
|--------|----------------|-------------|--------|-----------------|---------|
| Rural WV | **0** | Charleston (~190 mi) | 3+ hrs | High (WV unexpanded) | None |
| Eastern KY | **0** | Lexington (~130 mi) | 3+ hrs | Medium (KY limited) | None |
| MS Delta | **0** | Memphis (~200 mi) | 4+ hrs | Extreme (MS unexpanded) | Minimal |

## Key Findings
- **Zero prosthetic-orthotic providers within 50 km in all three underserved regions** — a complete absence, not a marginal gap
- **Nearest CPO is 130–200 miles away** — beyond accessible daily/weekly care
- **All three states have not expanded Medicaid** (WV, KY, MS) — compounding geographic barriers
- **MS Delta has the highest amputation rates in the U.S.** yet the worst access to prosthetic care
- **Clinical trial participation from these regions is virtually zero** — no trial sites in WV, EKY, or MS Delta

## Repository Structure
| File | Description |
|------|-------------|
| README.md | This file — overview with latest data |
| DATA_GAPS.md | Comprehensive gap analysis with OSM neighborhood scores |
| osm_neighborhood_analysis.md | Per-region neighborhood category scores (50 km radius) |
| osm_provider_search_results.md | Detailed POI search results per region |
| data/clinical_trials_updated.csv | Latest trial data extract (563 studies) |
| access_gap_summary_updated.csv | Precise gap metrics CSV |
| data/clinical_trials.csv | Original trial data extract |
| data/key_studies.md | Detailed study profiles |
| data/status_breakdown.json | Status distribution JSON |
| data/access_gap_summary.csv | Original gap summary |

## Methodology
- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (50 km radius)
- **Provider Search:** Nearby POI search using health/amenity/office categories
- **Neighborhood Scoring:** OSM neighborhood analysis tool

## Contributing
1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License
MIT (Open Access) — free to use for research, policy, and advocacy.

---

*Built to improve prosthetic care access for all. Open and free.*
