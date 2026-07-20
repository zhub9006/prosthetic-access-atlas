# Prosthetic Access Atlas — July 2026 Update

## What's New

### Clinical Trial Data
Added latest trends from ClinicalTrials.gov (July 2026):
- 644 total prosthetic studies analyzed
- Status, phase, country, and sponsor breakdowns
- 86 active US-based studies
- 117 amputation-focused studies
- Only 29 Phase 3 trials globally — critically scarce

### Access Gap Analysis
Mapped three underserved regions:
1. **Rural West Virginia** (Charleston hub, 38.35, -81.63)
2. **Eastern Kentucky** (Pikeville hub, 37.48, -82.52)
3. **Mississippi Delta** (Greenville hub, 33.41, -91.06)

Key finding: **All three regions have ZERO CPO providers within 100 km.**

### Files Added
- `data/ct_trends_latest.json` — Structured clinical trial trend data
- `data/clinical-trial-trends.json` — Earlier trend data with counts
- `clinical-trial-findings.md` — Summaries of recent US-based trials
- `gap_analysis/underserved_regions.md` — Detailed provider gap analysis

## Methodology
- ClinicalTrials.gov API v2: `countByStatus`, `countByPhase`, `countByCountry`, `countBySponsorType`
- OpenStreetMap: Geocoding, nearby-place searches, area exploration (30–100 km radius)
- Gap metric: Distance to nearest Certified Prosthetist-Orthotist (CPO)

## How to Use This Data
1. Clone: `git clone https://github.com/zhub9006/prosthetic-access-atlas.git`
2. Review `data/` for structured trend data
3. Review `gap_analysis/` for regional coverage gaps
4. Review `clinical-trial-findings.md` for recent trial summaries
5. Contribute: Fork, branch, PR

---
*Open access — free to use for research, policy, and advocacy.*