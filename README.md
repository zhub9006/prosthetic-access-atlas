# Prosthetic Access Atlas

An open-access resource mapping prosthetic clinical trial landscapes and uncovering care access gaps in underserved U.S. regions.

## Clinical Trial Trends (644 Total Studies)

### Status Distribution
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

### Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 4 | 29 | 4.5% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

### Sponsor Type
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.8% |
| Network + NIH | 6 | 0.9% |

### Top Countries
1. United States (~680) | 2. France (~317) | 3. Denmark (~78) | 4. Germany (~76) | 5. Italy (~71)

## Access Gap Summary
| Region | CPO Within 50km | Nearest CPO | Travel | Medicaid |
|--------|----------------|-------------|--------|----------|
| Rural WV | None | Charleston (~190 mi) | 3+ hrs | High |
| Eastern KY | None | Lexington (~130 mi) | 3+ hrs | Medium |
| MS Delta | None | Memphis (~200 mi) | 4+ hrs | Extreme |

## Repository Structure
| File | Description |
|------|-------------|
| ATLAS_REPORT.md | Full comprehensive report |
| data/clinical_trials.csv | Active trial data extract |
| data/key_studies.md | Detailed study profiles |
| data/trial_trends_by_status.json | Status distribution |
| data/trial_trends_by_region.json | Geographic data |
| data/trial_trends_by_phase.json | Phase analysis |
| data/trial_trends_by_sponsor.json | Sponsor analysis |
| data/access_gaps/*.json | Regional CPO gap profiles |
| data/access_gap_summary.csv | Gap summary table |
| analysis/methodology.md | Methodology & caveats |
| analysis/gap_analysis.md | Detailed gap analysis |
| data-sources.md | Data source attributions |

## Contributing
1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License
MIT (Open Access)

---
*Built to improve prosthetic care access for all. Open and free.*