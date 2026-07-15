# Prosthetic Access Atlas 🦿

An open-access resource mapping prosthetic and orthotic care access gaps, clinical trial trends, and underserved regions worldwide.

## Overview

This repository compiles:
- **Clinical trial data** from ClinicalTrials.gov on prosthetic interventions and outcomes
- **Gap analysis** of prosthetic/orthotic care provider availability in underserved U.S. regions
- **Regional mapping** of rehabilitation and prosthetics infrastructure in rural and medically underserved areas

## Key Findings

### Clinical Trial Landscape
- **644 total studies** indexed for prosthetic/amputation conditions
- **Status breakdown**: 271 Completed | 113 Currently Recruiting | 134 Unknown Status
- **Phase distribution**: Device Feasibility (338) | Phase 2 (39) | Phase 3 (30) | Phase 4 (29)
- **Geographic distribution**: U.S. dominates with 680+ study sites; France, Denmark, Germany also lead
- **Recent highlighted trials**:
  - **MIRA (NCT05768802)** — Implantable EMG array for prosthetic hand control (University of Pittsburgh)
  - **PROINGA (NCT07519746)** — Prosthetic satisfaction in Gaza conflict zone (128 participants)
  - **MPK-K2 (NCT06498245)** — Microprocessor knee RCT for community ambulators

### Care Gap Analysis

| Region | Center Point | O&P Providers Found | Nearest Services |
|--------|-------------|---------------------|------------------|
| **Rural West Virginia** | Beckley, WV | **0** | Charleston, WV (~100km) |
| **Eastern Kentucky** | Pikeville, KY | **0** | Lexington, KY (~160km) |
| **Mississippi Delta** | Greenville, MS | **0** | Memphis, TN (~130km) |

**All three regions have zero identified prosthetic or orthotic care providers within 100km.**

### Infrastructure Scores

| Score | Beckley, WV | Hazard, KY | Greenville, MS |
|-------|-------------|------------|----------------|
| Overall | 4.8 | 5.3 | 2.8 |
| Healthcare | 0 | 0 | 0 |
| Groceries | 68 | 46 | 0 |

---

## Files

- `clinical_trials/summary.md` — Detailed clinical trial landscape analysis
- `clinical_trials/key_studies.json` — Structured data on highlighted trials
- `gap_analysis/region_profiles.md` — Profiles of each underserved region
- `gap_analysis/coverage_gap_map.md` — Visual and tabular gap mapping
- `data/sources.md` — Data sources, methodology, and API references

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
