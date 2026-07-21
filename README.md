# Prosthetic Access Atlas — Open-Access Resource

> An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies (ClinicalTrials.gov) | **644** |
| Amputation + prosthetic studies (focused) | **393** |
| Actively recruiting (all prosthetic) | **112 (17.4%)** |
| Completed (all prosthetic) | **271 (42.1%)** |
| Phase 3 trials (amputation+prosthetic) | **3 (0.8%)** — critically scarce |
| Academic-sponsored trials | **65–77%** of all studies |
| CPO providers within 30km of target regions | **0 of 3** |
| Average distance to nearest CPO | **130–200+ miles** |

## Access Gap Summary

| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid? |
|--------|----------------|-------------|------------|-----------|
| Rural West Virginia (Beckley) | 0 | Charleston, WV | 3+ hrs | Not expanded |
| Eastern Kentucky (Pikeville) | 0 | Lexington, KY | 3+ hrs | Limited |
| Mississippi Delta (Greenville) | 0 | Memphis, TN | 3+ hrs | Not expanded |

### Key Finding
**Zero prosthetic/orthotic (CPO) providers** exist within 30 km of any of the three target regions. The nearest CPO is 130–200+ miles away. WV and MS have not expanded Medicaid. The Mississippi Delta has the highest amputation rate in the U.S.

## Clinical Trial Landscape

### All Prosthetics (n=644)
- COMPLETED: 271 (42.1%) | RECRUITING: 112 (17.4%) | UNKNOWN: 134 (20.8%)
- PHASE3: 30 (4.7%) | NA (observational): 338 (52.5%)
- Sponsors: OTHER (Academic) 76.5% | INDUSTRY 16.8% | FED 3.6%

### Limb Amputation (n=393)
- COMPLETED: 203 (51.7%) | RECRUITING: 76 (19.3%)
- NA (observational/Device): 292 (74.3%)
- PHASE3: only 3 (0.8%) — critically scarce
- Sponsors: OTHER (Academic) 65.1% | INDUSTRY 20.9% | FED 11.5%

## Latest Active Trials (2024–2026)

| NCT ID | Title | Status | Start |
|--------|-------|--------|-------|
| NCT07613502 | Bio Leg: Advancing Mobility (BAM) | RECRUITING | 2026-06 |
| NCT07094074 | Exploratory Functional Assessment After Amputation | NOT_YET_RECRUITING | 2026-09 |
| NCT07397169 | Adjustable Prosthetic Sockets for Lower Limb | NOT_YET_RECRUITING | 2026-10 |
| NCT06938087 | 3D Printed Prosthetic Foot: Pilot Study | COMPLETED | 2025-05 |
| NCT06635655 | Prosthetic System Impact on Mental Workload | RECRUITING | 2025-02 |
| NCT05831696 | Metabolic Cost: Passive vs. Powered Knees | RECRUITING | 2023-02 |
| NCT07222085 | Glide Control Strategy (Upper Limb) | RECRUITING | 2025-10 |
| NCT07653295 | Típmed™ Revision Hip Prosthesis PMCF | RECRUITING | 2024-03 |
| NCT05902221 | Rifampicin for C. acnes Prosthetic Joint Infections | RECRUITING | 2024-05 |

## Access Gap Summary (Detailed)

| Region | CPO 30km | Nearest CPO | Drive Mi | Drive Hrs | Medicaid | Amp Rate | Hospitals |
|--------|----------|-------------|----------|-----------|----------|----------|-----------|
| WV (Beckley) | 0 | Charleston, WV | ~190 | 3+ | No expanded | High | 3 |
| KY (Pikeville) | 0 | Lexington, KY | ~130 | 3+ | Limited | High | 1 |
| KY (Ashland) | 0 | Lexington, KY | ~140 | 3+ | Limited | High | 3 |
| MS Delta (Greenville) | 0 | Memphis, TN | ~200 | 3+ | Not expanded | Highest US | 2 |
| MS Delta (Clarksdale) | 0 | Memphis, TN | ~150 | 3+ | Not expanded | Highest US | 0 |

### Key Gap Findings
- **Zero CPO providers** within 30 km of any target region
- Nearest CPO is **130–200+ miles away**, requiring 3+ hours of driving
- All regions served only by general/acute-care hospitals with no O&P specialty
- **WV and MS have not expanded Medicaid**; KY has limited expansion
- **Mississippi Delta has the highest amputation rate in the U.S.** (driven by diabetes)
- **No prosthetic clinical trial sites** in WV, KY, or MS despite high amputation rates

## Latest Findings Files

| File | Description |
|------|-------------|
| `README.md` | This overview |
| `FINDINGS_JULY_2026_LATEST.md` | Comprehensive findings with detailed gap analysis |
| `CLINICAL_TRIAL_TRENDS_LATEST.md` | Detailed statistical trends by status, phase, sponsor, geography |
| `access_gap_summary.csv` | Machine-readable CPO coverage gap data |
| `gap_analysis_proximity_data.csv` | Proximity and provider search results for all regions |
| `JULY_2026_UPDATE.md` | Summary of what's new in this update |

## Methods

1. **Clinical Trials:** Searched ClinicalTrials.gov for "prosthetic" and "amputation + prosthetic" conditions. Analyzed by status, phase, sponsor type, and country. Retrieved latest trial listings for 2024–2026 entries.
2. **Provider Mapping:** Geocoded representative cities in three underserved regions (Beckley WV, Pikeville/Ashland KY, Greenville/Clarksdale MS). Searched OSM for healthcare amenities (clinics, hospitals, pharmacies, doctors) within 30–50 km radius.
3. **Gap Analysis:** Compared providers found against population density, amputation rates, Medicaid expansion status, and hospital bed availability.

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License

MIT (Open Access) — free to use for research, policy, and advocacy.

*Built to improve prosthetic care access for all. Open and free.*