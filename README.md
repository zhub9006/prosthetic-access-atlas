# 🦿 Prosthetic Access Atlas

**Open-access resource mapping prosthetic/orthotic clinical trial data and uncovering care gaps in underserved U.S. regions.**

## Overview

This repository compiles:
- **Clinical trial trends** from ClinicalTrials.gov for prosthetic interventions
- **Regional healthcare gap analysis** across rural West Virginia, eastern Kentucky, and the Mississippi Delta
- **Provider mapping** identifying prosthetic & orthotic care deserts

## Key Findings

### Clinical Trial Landscape (as of July 2026)
- **644 total studies** found across ClinicalTrials.gov matching prosthetic conditions
- **113 actively recruiting** / **12 enrolling by invitation** — significant ongoing trials
- **271 completed** studies provide a rich evidence base
- **38 not yet recruiting** — future trials anticipated
- Condition focus: amputation, prosthesis user satisfaction, quality of life, lower-limb prosthetics

### Regional Healthcare Access Scores
| Region | Overall | Healthcare | Groceries | Walkability |
|---|---|---|---|---|
| Rural West Virginia (Beckley, WV) | 4.2/10 | **0/10** 🔴 | 9.9/10 | 2/10 |
| Eastern Kentucky (Floyd County, KY) | 4.9/10 | 9.0/10 🟡 | 9.1/10 | 0/10 |
| Mississippi Delta (Greenville, MS) | 4.4/10 | **2.1/10** 🔴 | 8.9/10 | 2/10 |

### Critical Gaps Identified
1. **Rural West Virginia (Beckley)**: **ZERO** healthcare amenities within 30 km — a full prosthetic care desert
2. **Mississippi Delta**: Only **1 facility** (Southeast Rehabilitation Hospital, Lake Village, AR — 23.6 km away) — no dedicated prosthetic/orthotic providers
3. **Eastern Kentucky**: Better healthcare access (9.0/10), but patients still face significant travel distances to specialized prosthetic providers

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                          # This file
├── data/
│   ├── clinical-trials-summary.md     # Detailed clinical trial data & trends
│   ├── regional-healthcare-scores.md  # Neighborhood analysis scores
│   └── gap-analysis.md                # Underserved region provider mapping
├── maps/                              # Geographic data & visualizations
│   └── provider-locations.md          # Mapped care providers
└── methodology.md                     # Data sources & methodology
```

## How to Use

This data is intended for:
- **Researchers** studying prosthetic care disparities
- **Clinicians** identifying underserved areas for outreach
- **Policy makers** prioritizing resource allocation
- **Community organizations** advocating for local prosthetic services

## Data Sources
- ClinicalTrials.gov API (clinical study registry)
- OpenStreetMap (healthcare facility mapping)
- Neighborhood livability analysis

## License

Open-access — free to use, share, and adapt for nonprofit and research purposes.

---

*Built to bridge the gap between prosthetic innovation and access.*