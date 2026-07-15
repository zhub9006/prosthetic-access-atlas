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
- **Status breakdown**: 271 Completed | 113 Currently Recruiting | 134 Unknown Status | 38 Not Yet Recruiting | 37 Active Not Recruiting | 12 Enrolling by Invitation | 4 Suspended | 10 Withdrawn
- **Phase distribution**: N/A (observational) | Phase 1 | Phase 2 (39) | Phase 3 (30) | Phase 4 (29) | Early Phase 1 (4)
- **Geographic distribution**: U.S. dominates with 680+ study sites; France (317), Denmark (78), Germany (76), and Italy (71) also lead
- **Recent highlighted trials**:
  - **PROINGA (NCT07519746)** — Prosthetic Satisfaction & Quality of Life Among Lower Limb Users in Gaza (Yeditepe University / Al-Azhar Gaza). COMPLETED. 128 participants. Cross-sectional observational study using SAT-PRO, PEQ, TAPES, EQ-5D-5L, and SWLS instruments.
  - **MPK-K2 Trial** — Microprocessor Knee for K2-Level Ambulators (NCT06498245). Currently RECRUITING. Randomized controlled trial comparing microprocessor prosthetic knees to conventional knees for community ambulators. Conducted in the U.S.

### Care Gap Analysis
A 50–100km radius search for prosthetic/orthotic providers was conducted in three medically underserved regions:

| Region | Center Point | Coordinates | Prosthetic/Orthotic Providers Found | Nearest Known Services |
|--------|-------------|-------------|-----------------------------------|------------------------|
| **Rural West Virginia** | Beckley, WV | 37.78, -81.19 | **0** | Charleston, WV (~100km) |
| **Eastern Kentucky** | Pikeville, KY | 37.48, -82.52 | **0** | Charleston, WV (~150km) or Lexington, KY (~160km) |
| **Mississippi Delta** | Greenville, MS | 33.41, -91.06 | **0** | Memphis, TN (~130km) |

**All three regions have zero identified prosthetic or orthotic care providers within a 100km radius.**

Available healthcare infrastructure in these areas is limited to:
- General clinics (community health centers, urgent care)
- Pharmacies (Walgreens, CVS, Rite Aid, independent)
- Dental offices
- Dialysis centers (limited)
- **No prosthetists, orthotists, or specialized rehabilitation centers**

### Infrastructure Scores (Neighborhood Analysis)

| Category | Beckley, WV | Pikeville, KY | Greenville, MS |
|----------|-------------|---------------|----------------|
| Groceries | 10.0 (68 locations) | 9.2 (46 locations) | 0 (0 locations) |
| Restaurants | 9.9 (121 locations) | 10.0 (75 locations) | 10.0 (30 locations) |
| Healthcare | **0** | **0** | **0** |
| Education | 10.0 | 0 | 0 |
| Public Transport | 0 | 0 | 0 |
| Parks | 0 | 8.8 | 9.8 |
| Shopping | 9.7 | 9.6 | 2.0 |
| Overall Score | 4.8 | 5.3 | 2.8 |

## Access Disparity Map

```
                               PROSTHETIC CARE ACCESS
                               ======================

    Northeast ──── Dense provider network (Boston, NYC, Philly)
         │
    Midwest ──── Moderate clusters (Chicago, Detroit, Minneapolis)
         │
    South ──── Sparse; major gaps in Delta, Appalachia
         │
    Appalachia ──── ZERO providers within 100km of Beckley, Pikeville
         │
    Mississippi Delta ──── ZERO providers within 100km of Greenville
```

## Files

- `clinical_trials/summary.md` — Detailed clinical trial landscape analysis
- `clinical_trials/key_studies.json` — Structured data on highlighted trials
- `gap_analysis/region_profiles.md` — Profiles of each underserved region
- `gap_analysis/coverage_gap_map.md` — Visual and tabular gap mapping with travel distances
- `data/sources.md` — Data sources, methodology, and API references

## How to Use

1. **Explore trials**: Browse `clinical_trials/summary.md` for phase, status, and geographic trends
2. **Identify gaps**: Check `gap_analysis/` for regional coverage maps
3. **Add data**: Open a PR with additional trial data or provider updates
4. **Visualize**: Use `gap_analysis/` JSON files to build custom maps

## License

MIT

## Contributing

Contributions welcome! Please open an issue or pull request to add:
- Additional clinical trial datasets
- Provider location updates
- New region analyses
- Visualization tools

## Links

- **GitHub**: https://github.com/zhub9006/prosthetic-access-atlas
- **Clone**: `git clone https://github.com/zhub9006/prosthetic-access-atlas.git`
