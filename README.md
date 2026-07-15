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

**644 total studies** indexed for prosthetic/amputation conditions. Status breakdown across all 644 studies:

| Status | Count | Percentage |
|--------|-------|------------|
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| RECRUITING | 113 | 17.5% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| ACTIVE_NOT_RECRUITING | 37 | 5.7% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| TERMINATED | 24 | 3.7% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

**Geographic distribution** (by study site count): U.S. dominates with 680+ sites; France (317), Denmark (78), Germany (76), and Italy (71) also lead.

### Featured Trials

**NCT07519746 — PROINGA**: Patient Satisfaction & Quality of Life Among Lower Limb Prosthetic Users in Gaza (COMPLETED, n=128)

**NCT07103798 — MPK-K2**: Effect of a Microprocessor-Controlled Prosthetic Knee Joint on K2 Level Ambulators (NOT_YET_RECRUITING, VA-sponsored, estimated July 2026 start)

### Care Gap Analysis

A **100km radius** search for prosthetic/orthotic providers was conducted in three medically underserved regions:

| Region | Center Point | O&P Providers Found | Nearest Known Provider |
|--------|-------------|-------------------|------------------------|
| Rural West Virginia | Beckley, WV (37.78, -81.19) | **0** | Charleston, WV (~100km) |
| Eastern Kentucky | Pikeville, KY (37.48, -82.52) | **0** | Lexington, KY (~150km) |
| Mississippi Delta | Greenville, MS (33.41, -91.06) | **0** | Memphis, TN (~130km) |

**All three regions have zero identified prosthetic or orthotic care providers within a 100km radius.** Available healthcare is limited to general clinics, pharmacies, dentists, and dialysis — no prosthetists or orthotists.

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                          # This file
├── clinical_trials/
│   ├── summary.md                     # Detailed clinical trial landscape analysis
│   └── trials.json                    # Structured data on key recent trials
└── gap_analysis/
    ├── region_profiles.md             # Profiles of each underserved region
    ├── coverage_gap_map.md            # Visual and tabular gap mapping
    ├── provider_search_results.json   # Raw OSM search results
    └── nearest_providers_reference.md # Nearest known O&P providers
```

## How to Use

1. Explore trials: See `clinical_trials/summary.md` for the full landscape analysis
2. Understand gaps: See `gap_analysis/region_profiles.md` for detailed profiles
3. View the gap map: `gap_analysis/coverage_gap_map.md` for visual representation
4. Find nearest providers: `gap_analysis/nearest_providers_reference.md` for referral data

## Contributing

This is an open-access project. Contributions welcome:
- Add more clinical trial data for specific conditions
- Expand geographic gap analysis to additional regions
- Propose interventions for underserved areas
- Share local prosthetic/orthotic provider data

## Data Sources

- ClinicalTrials.gov API (NLM/NIH)
- OpenStreetMap / Overpass API (geographic & amenity data)

## License

Open access — all data is available for reuse.
