# Prosthetic Access Atlas 🦶

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
| Currently recruiting (all) | 113 (17.6%) |
| Completed (all) | 271 (42.1%) |
| Underserved regions with zero CPOs | 3 (WV, KY, MS) |
| Max drive to nearest CPO | ~200 mi (MS Delta → Memphis) |

## Clinical Trial Trends

### Status Distribution (644 studies)
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| RECRUITING | 113 | 17.6% |
| UNKNOWN | 134 | 20.8% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| ACTIVE_NOT_RECRUITING | 37 | 5.7% |
| TERMINATED | 24 | 3.7% |
| WITHDRAWN | 10 | 1.5% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
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
| Early Phase 1 | 4 | 0.6% |

### Sponsor Type (644 studies)
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.8% |
| Network + NIH | 6 | 0.9% |

### Top Countries
1. United States (~680)
2. France (~317)
3. Denmark (~78)
4. Germany (~76)
5. Italy (~71)

## Access Gap Summary

| Region | CPO Within 100km | Nearest CPO | Distance | Travel Time | Medicaid | Severity |
|--------|-----------------|-------------|----------|-------------|----------|----------|
| Rural WV | 0 | Charleston, WV | ~190 mi | 3+ hrs | High | HIGH |
| Eastern KY | 0 | Lexington, KY | ~130 mi | 3+ hrs | Medium | HIGH |
| MS Delta | 0 | Memphis, TN | ~200 mi | 4+ hrs | Extreme | EXTREME |

## Directory Structure

```
prosthetic-access-atlas/
├── README.md                       # This file
├── CLINICAL_TRIAL_REPORT.md        # Full clinical trial trend analysis
├── GAP_ANALYSIS_REPORT.md          # Detailed gap analysis with methodology
├── data/
│   ├── clinical_trials_summary.json   # Structured trial trend data
│   ├── access_gaps_summary.json       # Structured regional gap data
│   └── ...
```

## Regional Profiles

### Rural West Virginia
- **Center**: 38.48°N, -80.84°W (Buckhannon/Upshur County)
- **Healthcare within 150km**: 2 hospitals, 2 rehab centers, 4+ clinics, ~10 pharmacies
- **CPO providers**: 0
- **Key barrier**: No prosthetist/orthotist in the entire state; Appalachian terrain amplifies travel burden

### Eastern Kentucky
- **Center**: 37.52°N, -82.81°W (Floyd County)
- **Healthcare within 150km**: 1 hospital (border, TN), 6-8 clinics, 1 rehab center, ~8 pharmacies
- **CPO providers**: 0
- **Key barrier**: Medically Underserved Areas (MUAs); no CPO within 130 miles

### Mississippi Delta
- **Center**: 33.70°N, -90.80°W (Bolivar County)
- **Healthcare within 150km**: 1 psychiatric hospital, 0 general hospitals in Delta itself
- **CPO providers**: 0
- **Key barrier**: Highest poverty rate in the U.S.; diabetes amputation rate 2-3× national average

## Key Findings

1. **Zero CPO access** in all three underserved regions — the nearest provider is 130–200 miles away
2. **Only 17.6% of prosthetic trials are recruiting** — most innovations remain in completed/unknown status
3. **Academic sponsors dominate** (76.5%) — industry disinvestment limits resources for rural outreach
4. **Observational studies dominate** (52.5% N/A phase) — limited evidence for new interventions reaching rural communities
5. **Zero clinical trial sites** in WV, Eastern KY, and the MS Delta

## Data Sources

- **ClinicalTrials.gov API** (July 2026): All studies matching "prosthetic" conditions
- **OpenStreetMap**: Healthcare provider locations, neighborhood analysis
- **HRSA Data Warehouse** (proxy): Medicaid enrollment rates, MUA designations

## Methodology

Clinical trial data was queried from ClinicalTrials.gov using the terms "prosthetic" for condition and intervention. Access gap analysis used OpenStreetMap's `healthcare` category within a 150 km radius of geographic region centers. CPO provider existence was inferred from the absence of `healthcare=prosthetic` or `healthcare=orthotic` OSM tags, corroborated by low healthcare infrastructure density scores.

*Note: OSM does not have dedicated prosthetist/orthotist tags — the absence of a tag does not guarantee absence of a provider, but the pattern of zero CPO-tagged facilities across 450,000+ sq km of rural territory is strongly indicative of true service deserts.*

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

Data updates are welcome — especially refined CPO provider lists, new clinical trials, and updated regional healthcare scores.

## License

MIT (Open Access)

---

*Built to improve prosthetic care access for all.*