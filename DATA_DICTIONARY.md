# The Prosthetic Access Atlas

An open-access data project combining ClinicalTrials.gov prosthetic research findings with geographic gap analysis for underserved U.S. regions.

## Purpose

Current prosthetic care access in rural America and the rural South is critically under-documented. This atlas:

1. **Quantifies the clinical trial landscape** for prosthetic care and related conditions
2. **Maps care deserts** in rural West Virginia, eastern Kentucky, and the Mississippi Delta
3. **Identifies actionable policy and practice interventions**
4. **Provides a publicly editable, open-source framework** that anyone can extend

## Why This Matters

- **Rural West Virginia**: 200K+ population, zero CPOs within 100 miles of the center of the region
- **Eastern Kentucky**: 250K+ population, zero CPOs within 100+ miles — deepest prosthetic desert in the contiguous U.S.
- **Mississippi Delta**: 200K+ population, zero CPOs within 250+ miles — highest amputation rates in the nation combined with no accessible care
- **Clinical Trial Gap**: Only 21% of prosthetic trials are recruiting; ZERO trials conducted in any underserved rural region

## Data Sources

| Source | Description | Access |
|--------|-------------|--------|
| ClinicalTrials.gov | Federal clinical trial registry | API (public) |
| ABC (American Board for Certification) | Certified prosthetist-orthotist directory | Subscription |
| OpenStreetMap/Humanitarian Data | POI and facility mapping | CC-BY-SA |
| CDC Wonder | Disease and amputation prevalence data | Public |
| HRSA Data Warehouse | Medically underserved areas | Public |
| US Census Bureau | Demographics and income data | Public |

## Key Metrics

### Clinical Trial Trends (N=155)
- **Recruiting:** 21.3% (33 trials)
- **Completed:** 34.2% (53 trials)
- **Active, not recruiting:** 10.3% (16 trials)
- **Not yet recruiting:** 9.7% (15 trials)
- **Terminated:** 2.6% (4 trials)
- **Unknown:** 16.1% (25 trials)
- **Suspended:** 1.9% (3 trials)
- **Withdrawn:** 1.9% (3 trials)

### Phase Distribution
- **Phase 1:** 1.3% | **Phase 2:** 7.1% | **Phase 3:** 2.6% | **Phase 4:** 5.2%
- **Unknown:** 33.5% | **Not Applicable:** 51.6%

### Geographic Distribution (Global)
- **United States:** 48.5% (336 institution referrals)
- **France:** 12.1% (84)
- **Australia:** 5.1% (35)
- **United Kingdom:** 3.6% (25)
- **Germany:** 2.9% (20)
- **Netherlands:** 2.9% (20)
- **Developing nations:** <2% combined

### Sponsorship
- **Academic/Other:** 70.3%
- **Industry:** 19.4%
- **Federal (NIH/VA):** 7.1%

### Coverage Gap Scores (0-5, 5=best)
| Region | Score | Nearest CPO | Medicaid Status | Amputation Rate |
|--------|-------|-----------|----------------|-----------------|
| Rural WV | 1/5 | ~190 mi (Charleston) | Limited | Above avg |
| Eastern KY | 1/5 | ~130 mi (Lexington) | KY only | 2x national |
| Mississippi Delta | 0/5 | 200-250 mi (Memphis/Jackson) | Not expanded | 3-4x national |

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                    # You are here
├── .gitignore                   # Python/intermediate files
├── DATA_DICTIONARY.md           # Field definitions and data sources
├── CONTRIBUTING.md              # How to contribute
├── LICENSE                      # MIT License
├── data/
│   ├── clinical_trials.csv      # Extracted prosthetic trial data
│   ├── trial_trends_by_status.json   # Trial status distribution
│   ├── trial_trends_by_region.json   # Global geographic distribution
│   ├── trial_trends_by_phase.json    # Trial phase distribution
│   ├── trial_trends_by_sponsor.json  # Sponsorship analysis
│   ├── access_gaps/
│   │   ├── region_profiles.md       # Detailed gap profiles
│   │   └── por_supplier_map.json    # Provider lookup data
│   └── raw/
│       └── clinicaltrials_raw.json  # Raw API response (if available)
├── analysis/
│   ├── trend_analysis.ipynb    # Jupyter notebook for trend exploration
│   └── gap_analysis.md          # Gap scoring methodology
├── visualizations/               # Maps and charts (to be developed)
│   ├── access_gap_map.png
│   └── trial_trend_charts.png
└── docs/
    └── policy_briefs/            # Policy briefs for stakeholders
```

## Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Pandas, Matplotlib, Folium

### Quick Start
```bash
git clone https://github.com/zhub9006/prosthetic-access-atlas.git
cd prosthetic-access-atlas
python analysis/trend_analysis.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) file

## Disclaimer

This is an open-access academic/policy resource. Clinical trial data is sourced from ClinicalTrials.gov and may contain inaccuracies. Provider data is based on publicly available directories and may be outdated. Always verify directly with CPO offices and ClinicalTrials.gov before clinical or policy decisions.

---

*Built for prosthetic care equity. All data is open and free for use, reuse, and redistribution.*