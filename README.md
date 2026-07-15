# Prosthetic Access Atlas

An open-access resource mapping prosthetic and orthotic care access gaps, clinical trial trends, and underserved regions worldwide.

## Overview

This repository compiles:
- **Clinical trial data** from ClinicalTrials.gov on prosthetic interventions and outcomes
- **Gap analysis** of prosthetic/orthotic care provider availability in underserved U.S. regions
- **Regional mapping** of rehabilitation and prosthetics infrastructure in rural and medically underserved areas

## Data Sources

- ClinicalTrials.gov API — 644 prosthetic-related studies analyzed
- OpenStreetMap (via Overpass API) — provider location data

## Key Findings

### Clinical Trial Landscape
- **644 total studies** indexed for prosthetic/amputation conditions
- **Status breakdown**: 271 Completed, 113 Currently Recruiting, 134 Unknown Status, 38 Not Yet Recruiting, 37 Active Not Recruiting, 12 Enrolling by Invitation
- **Geographic distribution**: U.S. dominates with 680+ study sites; France (317), Denmark (78), Germany (76), and Italy (71) also lead
- **Recent trials**: MPK-K2 (microprocessor prosthetic knees for K2 ambulators), Gaza Prosthetic Satisfaction & QoL study (PROINGA), and more

### Care Gap Analysis
A 100km radius search for prosthetic/orthotic providers was conducted in three medically underserved regions:

| Region | Center Point | Prosthetic/Orthotic Providers Found | Nearest Known Provider |
|--------|-------------|-----------------------------------|------------------------|
| Rural West Virginia | Beckley, WV (37.78, -81.19) | **0** | Charleston, WV (~100km) |
| Eastern Kentucky | Pikeville, KY (37.48, -82.52) | **0** | Lexington, KY (~150km) |
| Mississippi Delta | Greenville, MS (33.41, -91.06) | **0** | Memphis, TN (~130km) |

**All three regions have zero identified prosthetic or orthotic care providers within a 100km radius.**

Available healthcare infrastructure in these areas is limited to:
- General clinics (community health centers, urgent care)
- Pharmacies (Walgreens, CVS, Rite Aid, independent)
- Dental offices
- Dialysis centers (limited)
- No prosthetists, orthotists, or specialized rehabilitation centers

## Files

- `clinical_trials/summary.md` — Detailed clinical trial landscape analysis
- `clinical_trials/trials.json` — Structured data on key recent trials
- `gap_analysis/region_profiles.md` — Profiles of each underserved region
- `gap_analysis/provider_search_results.json` — Raw OSM search results for healthcare providers
- `gap_analysis/coverage_gap_map.md` — Visual and tabular gap mapping

## License

MIT

## Contributing

Contributions welcome! Please open an issue or pull request to add:
- Additional clinical trial datasets
- Provider location updates
- New region analyses
- Visualization tools