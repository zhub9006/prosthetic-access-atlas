# Prosthetic Access Atlas 🦿

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions.

## Overview

This repository compiles:
- **Clinical trial trends** from ClinicalTrials.gov (644 prosthetic studies, 360 limb-prosthesis-specific)
- **Access gap analysis** for three underserved regions: Rural West Virginia, Eastern Kentucky, and the Mississippi Delta
- **Key study profiles** of recent and notable prosthetic research
- **Geospatial data** on CPO (Certified Prosthetic-Orthotic) provider deserts

## Quick Stats

| Metric | Value |
|--------|-------|
| Total prosthetic studies | 644 |
| Limb prosthesis studies | 360 |
| Currently recruiting (all) | 112 (17.5%) |
| Completed (all) | 271 (42.1%) |
| Underserved regions with zero CPOs | 3 (WV, KY, MS) |
| Max drive to nearest CPO | ~200 min (MS Delta → Memphis) |

## Clinical Trial Trends

### Status Distribution (644 studies)
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| RECRUITING | 112 | 17.5% |
| UNKNOWN | 134 | 20.8% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| TERMINATED | 24 | 3.7% |
| SUSPENDED | 4 | 0.6% |

### Phase Distribution (644 studies)
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 4 | 29 | 4.5% |
| Phase 1 | 15 | 2.3% |

### Sponsor Type (644 studies)
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.8% |
| Network + NIH | 6 | 0.9% |

## Access Gap Summary

| Region | CPO Within 50km | Nearest CPO | Travel | Medicaid |
|--------|-----------------|-------------|--------|----------|
| Rural WV (Beckley) | **None** | Charleston (~190 mi) | 3+ hrs | High |
| Eastern KY (Pikeville) | **None** | Lexington (~130 mi) | 3+ hrs | Medium |
| MS Delta (Greenville) | **None** | Memphis (~200 mi) | 4+ hrs | Extreme |

**Key Finding:** All three regions are **CPO deserts** — zero certified prosthetic-orthotic providers within 50 km.

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                  # This file
├── ATLAS_REPORT.md            # Comprehensive analysis report
├── data/
│   ├── clinical_trial_trends.json    # Full trend data by status/phase/sponsor/region
│   ├── access_gaps.json              # Regional CPO gap profiles
│   └── key_studies.json              # Recent & notable trial profiles
├── analysis/
│   ├── gap_analysis.md           # Detailed gap analysis with implications
│   └── clinical_trial_trends.md  # Detailed trends analysis
└── data-sources.md           # Data source attributions & methodology
```

## Key Studies Highlighted

1. **PROSPER (NCT06419920)** — RECRUITING — Uneven terrain walking for lower limb prosthesis users (UNLV + NIH + DoD)
2. **EPJIC (NCT02424903)** — Prosthetic joint infection cohort (Pro-Implant Foundation, 5,000 participants)
3. **Gaza QoL Study (NCT07519746)** — COMPLETED — Patient satisfaction and quality of life (128 participants)

## Data Sources

- **ClinicalTrials.gov** — API v2 for all trial data
- **OpenStreetMap** — Healthcare facility mapping
- **Geocoding** — Target coordinates for Beckley WV, Pikeville KY, Greenville MS

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License

MIT (Open Access)

---

*Built to improve prosthetic care access for all. Open and free.*
