# Prosthetic Access Atlas

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions.

## Overview

This project combines data from ClinicalTrials.gov with geographic analysis to identify where prosthetic and orthotic care is missing — and where research is happening (or not) in those same regions.

## Key Findings

### 1. Clinical Trial Landscape
- **644 total prosthetic-related trials** currently registered on ClinicalTrials.gov
- **155 trials** focus specifically on "prosthetic care"
- **Status Breakdown:**
  - COMPLETED: 53 (34%)
  - RECRUITING: 33 (21%)
  - UNKNOWN: 25 (16%)
  - NOT_YET_RECRUITING: 15 (10%)
  - ACTIVE_NOT_RECRUITING: 16 (10%)
  - TERMINATED: 4, SUSPENDED: 3, WITHDRAWN: 3 (13%)

### 2. Geographic Distribution of Trials
- United States: 336 trials
- France: 84
- Australia: 35
- United Kingdom: 25
- Germany: 20
- Spain: 17
- Netherlands: 20
- Other nations: ~49 combined

**Key Gap**: No clinical trials are registered from any of the three underserved regions analyzed.

### 3. Care Gap Analysis

| Region | Overall Score | Healthcare Score | Facilities Within 30km | Walkability | Key Issue |
|--------|---------------|------------------|------------------------|-------------|-----------|
| Pocahontas County, WV | 3.6/10 | **0** | **0** | 0 | No healthcare at all |
| Breathitt County, KY | 4.8/10 | 5.5 | Limited (no prosthetics) | 0 | Nearest care at Jackson/Hazard (25+ km) |
| Mississippi Delta, MS | ~3/10 (est.) | ~2/10 (est.) | Very limited | Low | Deep rural poverty, AMTRAC dependency |

### Featured Trial: PROINGA (NCT07519746)
- Title: Patient Satisfaction and Quality of Life Among Lower Limb Prosthetic Users in Gaza During War
- Status: COMPLETED (Sep 2025 -- Mar 2026)
- Sponsor: Yeditepe University / Al-Azhar University -- Gaza
- Enrollment: 128 participants
- Focus: Prosthetic satisfaction, QoL, rehabilitation outcomes in conflict zones

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                          # This file
├── data/
│   ├── clinical_trials.json           # Raw ClinicalTrials.gov query results
│   ├── status_breakdown.json          # Trial status distribution
│   ├── country_distribution.json      # Geographic distribution by country
│   └── featured_trials.json           # Detailed study summaries
├── gap_analysis/
│   ├── west_virginia.json             # Pocahontas County, WV analysis
│   ├── kentucky.json                  # Breathitt County, KY analysis
│   ├── mississippi_delta.json         # MS Delta region analysis
│   └── combined_gap_report.md         # Merged gap findings
└── src/
    └── analysis_notes.md              # Methodology and toolchain notes
```

## How to Use

1. Explore trials: Browse `data/clinical_trials.json` for the full query results
2. Understand gaps: See `gap_analysis/combined_gap_report.md` for the merged findings
3. Re-run the analysis: Data was gathered via ClinicalTrials.gov API and OpenStreetMap/Overpass queries

## Contributing

This is an open-access project. Contributions welcome:
- Add more clinical trial data for specific conditions
- Expand geographic gap analysis to additional regions
- Propose interventions for underserved areas
- Share local prosthetic/orthotic provider data

## Data Sources

- ClinicalTrials.gov API (NLM/NIH)
- OpenStreetMap / Overpass API (geographic & amenity data)
- OSM Nightly build (neighborhood livability scores)

## License

Open access — all data is available for reuse.
