# Prosthetic Access Atlas

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions.

## Clinical Trial Landscape (644 Total Studies — July 2026)

### Data Source
- **Database:** ClinicalTrials.gov (NIH/NLM) — API v2
- **Query:** `condition: "prosthetic"` (broad search capturing amputation, prosthetic joint, and limb prosthesis studies)
- **Total Studies:** 644
- **Subset — Prosthetic + Care Terms:** 155 studies (detailed trend analysis in `findings_2026_update.md`)
- **Subset — U.S. Location:** 202 studies (with U.S. facility)

### Status Distribution (155 Prosthetic Care Studies)
| Status | Count | % |
|--------|-------|---|
| RECRUITING | 32 | 20.6% |
| COMPLETED | 53 | 34.2% |
| UNKNOWN | 25 | 16.1% |
| NOT_YET_RECRUITING | 15 | 9.7% |
| ACTIVE_NOT_RECRUITING | 17 | 11.0% |
| TERMINATED | 4 | 2.6% |
| WITHDRAWN | 3 | 1.9% |
| ENROLLING_BY_INVITATION | 2 | 1.3% |
| SUSPENDED | 3 | 1.9% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.6% |

**Key Insight:** 47 trials with future patient engagement (32 recruiting + 15 not-yet). 53 completed studies may contain actionable results. The 16.1% UNKNOWN rate is a transparency concern.

### Phase Distribution (155 Prosthetic Care Studies)
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 80 | 51.6% |
| Unknown | 52 | 33.5% |
| Phase 2 | 11 | 7.1% |
| Phase 4 | 8 | 5.2% |
| Phase 3 | 4 | 2.6% |
| Phase 1 | 2 | 1.3% |

**Critical Gap:** Only 4 Phase 3 pivotal trials among 155 studies — the evidence gap for prosthetic device efficacy remains wide.

### Sponsor Type (155 Prosthetic Care Studies)
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 109 | 70.3% |
| Industry | 30 | 19.4% |
| Federal | 11 | 7.1% |
| Other Gov | 4 | 2.6% |
| Network | 1 | 0.6% |

### Geographic Distribution (Top 10 Countries)
1. United States: 336 locations
2. United Kingdom: 25
3. France: 17
4. Germany: 20
5. Spain: 17
6. Netherlands: 20
7. Australia: 35
8. Sweden: 8
9. Switzerland: 8
10. Canada: 13

**Key Insight:** Zero trial sites exist in West Virginia, Eastern Kentucky, or the Mississippi Delta — the regions with the highest amputation rates and worst access.

---

## Access Gap Analysis

### Four Underserved Regions Examined

| Region | Center | Coordinates | CPO in 50km | Nearest CPO | Travel | Medicaid | Neighborhood Score |
|--------|--------|-------------|-------------|-------------|--------|----------|-------------------|
| **Rural West Virginia** | Marlinton, WV | 38.223, -80.095 | **0** | Charleston (~190 mi) | 3+ hrs | Not expanded | 7.1 |
| **Eastern Kentucky** | Pikeville, KY | 37.479, -82.519 | **0** | Lexington (~130 mi) | 3+ hrs | Not expanded | 7.4 |
| **Mississippi Delta** | Greenville, MS | 33.411, -91.064 | **0** | Memphis (~200 mi) | 4+ hrs | Not expanded | 5.0 |
| **MS Delta Heartland** | Clarksdale, MS | 34.201, -90.570 | **0** | Memphis (~200 mi) | 4+ hrs | Not expanded | **1.5** |

### Key Findings
- **Zero prosthetic-orthotic providers within 50 km in all four regions** — a complete absence, not a marginal gap
- **Nearest CPO is 130–200 miles away** — beyond accessible daily/weekly care
- **All three states have not expanded Medicaid** (WV, KY, MS) — compounding geographic barriers
- **MS Delta has the highest amputation rates in the U.S.** yet the worst access to prosthetic care
- **Clinical trial participation from these regions is virtually zero** — no trial sites in WV, EKY, or MS Delta
- **Clarksdale, MS (Delta heartland) scores 1.5/10** — zero healthcare, zero groceries, zero restaurants within 20 km
- **Rural WV has highest disability rate in the U.S. (~19.4%) yet lowest prosthetic access**

---

## Methodology
- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (50 km radius)
- **Provider Search:** POI search using health/amenity/office categories + keyword searches for prosthetist/orthotist/CPO
- **Neighborhood Scoring:** OSM neighborhood analysis tool (walkability, amenities, services)
- **Gap Analysis:** Cross-referencing CPO provider locations with population centers in high-need regions

## Contributing
1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License
MIT (Open Access) — free to use for research, policy, and advocacy.

---

*Built to improve prosthetic care access for all. Open and free.*
