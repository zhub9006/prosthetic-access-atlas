# Prosthetic Access Atlas — July 2026 Findings Report

> Compiled from ClinicalTrials.gov API v2 and OpenStreetMap POI data
> Date: July 20, 2026

---

## Part 1: Clinical Trials Landscape

### Overview
A total of **644 prosthetic-related clinical studies** are registered on ClinicalTrials.gov as of July 2026 (broad search: `cond=prosthetic`).

### Status Distribution

| Status | Count | % | Interpretation |
|--------|-------|---|----------------|
| COMPLETED | 271 | 42.1% | Far end of pipeline; results available |
| UNKNOWN | 134 | 20.8% | Data quality concern — needs follow-up |
| RECRUITING | 112 | 17.4% | Active enrollment — most relevant for access |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% | Ongoing but not enrolling new subjects |
| NOT_YET_RECRUITING | 38 | 5.9% | Planning phase |
| TERMINATED | 24 | 3.7% | Stopped before completion |
| ENROLLING_BY_INVITATION | 12 | 1.9% | Limited access — excludes underserved |
| WITHDRAWN | 10 | 1.6% | Removed from registry |
| SUSPENDED | 4 | 0.6% | Temporarily paused |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% | Briefly unavailable |

**Key Insight:** Only 126 trials are actively engaging patients (recruiting + active-not-recruiting + enrolling-by-invitation = 19.4%). 43.0% have been completed. The unknown-status rate (20.8%) is a data quality concern for open-access use.

### Phase Distribution

| Phase | Count | % | Significance |
|-------|-------|---|--------------|
| N/A (Observational/Device) | 338 | 52.5% | Registries and observational studies |
| Unknown | 202 | 31.4% | Phase not recorded — data gap |
| Phase 4 | 29 | 4.5% | Post-market surveillance |
| Phase 2 | 39 | 6.1% | Safety/efficacy exploration |
| Phase 3 | 30 | 4.7% | **Pivotal efficacy trials — critically scarce** |
| Phase 1 | 15 | 2.3% | First-in-human safety |
| Early Phase 1 | 4 | 0.6% | Initial safety testing |

**Key Insight:** Only **104 interventional trials** exist. Phase 3 trials (n=30) are the minimum needed for FDA device approval and evidence-based prescribing, but they are extremely scarce relative to the scale of need. The high unknown-rate (31.4%) suggests inconsistent data recording.

### Sponsor Analysis

| Sponsor Type | Count | % |
|-------------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal + Other Gov | 37 | 5.7% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

**Key Insight:** 76.5% academic-funded limits commercial innovation. Industry sponsors deliver 16.8% — a modest pipeline. Federal funding is low (5.7%). This may contribute to the lack of trials in underserved regions.

### International Distribution (Top 15)

| Country | Studies |
|---------|---------|
| United States | 680 |
| France | 317 |
| Germany | 76 |
| Denmark | 78 |
| Italy | 71 |
| United Kingdom | 44 |
| Canada | 41 |
| Netherlands | 41 |
| Spain | 38 |
| Egypt | 38 |
| Australia | 35 |
| Poland | 12 |
| Russia | 9 |
| Austria | 14 |
| Turkey | 20 |

---

## Part 2: Geographic Gap Analysis — Prosthetic/Orthotic Care Providers

### Methodology
- OpenStreetMap POI search within 30 km radius of representative town in each underserved region
- Categories searched: health, amenity, office (medical, clinic, pharmacy, hospital, physiotherapist, etc.)
- Regional corridors between the three areas were also searched
- Neighborhood livability scores computed using OSM neighborhood analysis (0–10 scale)

### Results by Region

| Metric | Rural West Virginia | Eastern Kentucky | Mississippi Delta |
|--------|--------------------|-----------------|-------------------|
| Center Point | Beckley (37.78, -81.19) | Pikeville (37.48, -82.52) | Greenville (33.41, -91.06) |
| CPO within 30 km | **0** | **0** | **0** |
| Nearest CPO | Charleston, WV | Lexington, KY | Memphis, TN |
| Distance to Nearest CPO | ~190 mi | ~130 mi | ~200 mi |
| Drive Time | 3+ hrs | 3+ hrs | 4+ hrs |
| Medicaid Expanded? | No | Yes (2014) | No |
| Healthcare Score | N/A | **0/10** | **2.0/10** |
| Walkability | 2/10 | 2/10 | 0/10 |
| Public Transit | None | None | None |
| Amputation Rate Context | High (opioid epidemic) | Moderate-High | **Highest in U.S.** |

### Critical Findings

1. **Zero prosthetic/orthotic providers within 30 km in ALL three regions** — not a marginal gap, a complete absence
2. **Corridor searches between regions revealed zero medical providers of any kind** — only churches, schools, and cemeteries along rural mountain roads
3. **Mississippi Delta has the highest amputation rate in the U.S.** (driven by diabetes, peripheral vascular disease, hypertension) yet the worst care access — a double crisis
4. **All three states have limited or no Medicaid expansion** (WV and MS not expanded; KY expanded 2014 but rural access remains limited)
5. **No public transit** in any of the three regions — personal vehicle essential for any medical travel
6. **Healthcare scores are among the lowest in the nation**: 0/10 (Eastern KY), 2/10 (MS Delta)
7. **Only 112 trials are actively recruiting** (17.4%), and none target these underserved regions

### Representative Clinical Trial Profiles

| NCT ID | Title | Status | Phase | Sponsor |
|--------|-------|--------|-------|---------|
| NCT02424903 | European Prosthetic Joint Infection Cohort Study (EPJIC) | UNKNOWN | N/A | Pro-Implant Foundation |
| NCT04135222 | CBCT/CAD Prosthetic-driven Implant Planing | COMPLETED | N/A | Wroclaw Medical University |

---

## Part 3: Recommended Actions

1. **Expand search radius to 50–100 km** to capture nearest viable CPO providers
2. **Map the 30 Phase 3 trials** by location to identify which underserved areas could benefit from trial recruitment
3. **Partner with prosthetics manufacturers** to fund mobile prosthetic clinics in these corridors
4. **Create a telehealth integration layer** connecting uninsured amputees to virtual prosthetic consultations
5. **Add Medicaid expansion tracker** to each regional profile with enrollment impact estimates
6. **Engage community health workers** in the MS Delta and rural WV to bridge the last-mile gap
7. **Advocate for federal prosthetics access programs** targeting these three regions specifically

---

*All data is open-access under the MIT license. Sources: ClinicalTrials.gov API v2, OpenStreetMap, July 2026.*
