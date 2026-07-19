# Prosthetic Access Atlas

An open-access resource mapping prosthetic clinical trial landscapes and uncovering care access gaps in underserved U.S. regions.

## Overview

This repository compiles:
- **Clinical trial trends** from ClinicalTrials.gov (644 prosthetic-related studies)
- **Access gap analysis** for three underserved regions: Rural West Virginia, Eastern Kentucky, and the Mississippi Delta
- **Data files** for reproducible research

## Key Findings

### Clinical Trial Trends
- **644 total studies** across all phases
- **42.1% completed**; only 17.6% actively recruiting
- **76.5% academic-sponsored** — limited commercial investment
- **52.5% observational/device studies** — early-stage research ecosystem

### Access Gaps (Critical Finding)
| Region | CPOs Within 100km | Nearest CPO | Travel Time |
|--------|-------------------|-------------|-------------|
| Rural WV | **0** | Charleston, WV | 2+ hrs |
| Eastern KY | **0** | Lexington, KY | 2.7 hrs |
| MS Delta | **0** | Memphis, TN | 1.6 hrs |

**All three regions are prosthetic care deserts.**

## Repository Structure

| Path | Description |
|------|-------------|
| `ATLAS_REPORT.md` | Full comprehensive report |
| `data/clinical_trials_trends.json` | Trial trend data (status, phase, sponsor) |
| `data/access_gaps.json` | Regional gap profiles |
| `data/key_studies.md` | Detailed study profiles |
| `data/clinical_trials_data.md` | Raw trial listings |
| `analysis/gap_analysis.md` | Detailed gap analysis methodology |
| `data-sources.md` | Source attributions |

## Getting Started

```bash
git clone https://github.com/zhub9006/prosthetic-access-atlas.git
cd prosthetic-access-atlas
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

MIT (Open Access) — free to use, modify, and share.

---

*Built to improve prosthetic care access for all.*
