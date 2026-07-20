# Prosthetic Access Atlas

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions.

## Clinical Trial Landscape (644 Total Studies — July 2026)

### Data Source
- **Database:** ClinicalTrials.gov (NIH/NLM) — API v2
- **Query:** `condition: "prosthetic"` (broad search capturing amputation, prosthetic joint, and limb prosthesis studies)
- **Total Studies:** 644
- **Subset — U.S. Location:** 202 studies (with U.S. facility)
- **Subset — France:** 317 studies (largest non-U.S. contributor)

### Status Distribution (All 644 Studies)
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

**Key Insight:** 112 trials actively recruiting (17.4%) + 38 active-not-recruiting + 12 enrolling-by-invitation = 162 trials with some active engagement. Only 271 completed (42.1%). Over 1 in 5 (20.8%) have UNKNOWN status — a data quality concern.

### Phase Distribution (All 644 Studies)
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 1 | 15 | 2.3% |
| Phase 4 | 29 | 4.5% |
| Early Phase 1 | 4 | 0.6% |

**Key Insight:** Only 88 interventional Phase 1–4 trials. Phase 3 trials (n=30) are critically scarce — the evidence gap for prosthetic device efficacy remains wide. Over half (52.5%) are observational/device registries.

### U.S.-Based Trial Breakdown (202 Studies with U.S. Locations)
| Metric | Value |
|--------|-------|
| Total U.S. trials | 202 |
| Phase 3 | 7 (3.5%) |
| Phase 2 | 19 (9.4%) |
| Phase 1 | 7 (3.5%) |
| Phase 4 | 11 (5.4%) |
| Active/Recruiting | 112 (55.4%) |
| Interventional | 44 (21.8%) |
| Observational | 158 (78.2%) |

**Key Insight:** 7 Phase 3 trials across 202 U.S. studies — the evidence pipeline is extremely thin.

### Sponsor Type
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal | 23 | 3.6% |
| Other Gov | 14 | 2.2% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

### U.S. Sponsor Breakdown (202 U.S. Location Studies)
| Sponsor Type | Count | % |
|-------------|-------|---|
| Academic/Other | 120 | 59.4% |
| Industry | 55 | 27.2% |
| Federal | 23 | 11.4% |
| Network | 3 | 1.5% |
| NIH | 1 | 0.5% |

### Geographic Distribution (Top 10 Countries)
1. United States: 680 locations
2. France: 317
3. Germany: 76
4. Italy: 71
5. Denmark: 78
6. Canada: 41
7. United Kingdom: 44
8. Spain: 38
9. Netherlands: 41
10. Egypt: 38

## Access Gap Analysis

### Four Underserved Regions Examined

| Region | Center | Coordinates | CPO in 50km | Nearest CPO | Travel | Medicaid | Neighborhood Score |
|--------|--------|-------------|-------------|-------------|--------|----------|-------------------|
| **Rural West Virginia** | Beckley, WV | 37.778, -81.188 | **0** | Charleston (~190 mi) | 3+ hrs | Not expanded | 7.1 |
| **Eastern Kentucky** | Pikeville, KY | 37.479, -82.519 | **0** | Lexington (~130 mi) | 3+ hrs | Not expanded | 4.4 |
| **Mississippi Delta** | Greenville, MS | 33.411, -91.064 | **0** | Memphis (~200 mi) | 4+ hrs | Not expanded | 4.1 |
| **MS Delta Heartland** | Clarksdale, MS | 34.201, -90.570 | **0** | Memphis (~200 mi) | 4+ hrs | Not expanded | **1.5** |

### Key Findings
- **Zero prosthetic-orthotic providers within 50 km in all four regions** — a complete absence, not a marginal gap
- **Nearest CPO is 130–200 miles away** — beyond accessible daily/weekly care
- **All three states have not expanded Medicaid** (WV, KY, MS) — compounding geographic barriers
- **MS Delta has the highest amputation rates in the U.S.** yet the worst access to prosthetic care
- **Clinical trial participation from these regions is virtually zero** — no trial sites in WV, EKY, or MS Delta
- **Clarksdale, MS (Delta heartland) scores 1.5/10** — zero healthcare, zero groceries, zero restaurants within 20 km
- **Rural WV has highest disability rate in the U.S. (~19.4%) yet lowest prosthetic access**

### Detailed Neighborhood Scores (20 km radius)

#### Rural West Virginia (Beckley)
- **Overall:** 7.1/10 | Healthcare: 9.5 (pharmacies/clinics only, NO prosthetists)
- Groceries: 9.9, Restaurants: 9.9, Education: 9.9, Parks: 9.0, Shopping: 9.3
- **Services: 0/10** — no social services, vocational rehab, or disability services

#### Eastern Kentucky (Pikeville)
- **Overall:** 4.4/10 | Healthcare: 9.8 (6 facilities, all general — zero prosthetics)
- Education: 10.0 (University of Pikeville), Groceries: 6.1
- **Restaurants: 0/10, Public Transport: 0/10, Services: 0/10**

#### Mississippi Delta (Greenville)
- **Overall:** 4.1/10 | **Healthcare: 0/10** — zero clinics, hospitals, or pharmacies within 20km
- Restaurants: 9.9, Education: 9.8, Parks: 9.5
- **Groceries: 6.3, Public Transport: 0/10**

#### Clarksdale, MS (Delta Heartland)
- **Overall: 1.5/10** — one of the most underserved communities in the U.S.
- **Healthcare: 0/10, Groceries: 0/10, Restaurants: 0/10**
- **Shopping: 0/10, Services: 0/10, Entertainment: 0/10**

## Methodology
- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (20–50 km radius)
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
