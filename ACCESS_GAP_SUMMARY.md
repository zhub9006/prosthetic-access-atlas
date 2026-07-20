---
title: Access Gap Summary — July 2026
author: Open-Source Community
updated: 2026-07-20
license: MIT
---

# Access Gap Summary — July 2026

## The Core Problem
People in rural WV, eastern KY, and the MS Delta face **130-200+ drives** to reach a single Certified Prosthetist-Orthotist (CPO). Meanwhile, the MS Delta has **zero healthcare facilities** within 30km — yet the highest amputation rates in the U.S.

## Methodology
- **Geocoding**: OSM `geocode_address` for regional centers (Beckley WV, Pikeville KY, Clarksdale MS)
- **Neighborhood Analysis**: `analyze_neighborhood` (30km radius for WV/KY, 40km for MS)
- **Healthcare Search**: `explore_area` for comprehensive facility counts
- **Gap Metric**: Distance to nearest CPO from regional hub
- **Analysis Date**: July 20, 2026

## Scorecard

| Region | Overall | Walkability | Healthcare | CPO (0km) | CPO (100km) | Nearest CPO | Drive |
|--------|---------|-------------|------------|-----------|-------------|-------------|-------|
| WV Beckley | 6.1 | 0 | 7 | **0** | **0** | Charleston, WV (190mi) | 3+ hrs |
| KY Pikeville | 5.6 | 6 | 11 | **0** | **0** | Lexington, KY (130mi) | 3+ hrs |
| MS Delta | 4.1 | 2 | **0** | **0** | **0** | Memphis, TN (200mi) | 4+ hrs |

## Key Data Points

### WV Beckley
- Healthcare (within 30km): 7 facilities (1 pharmacy, 1 clinic+emergency, 1 medical center, audiology, dialysis, 2+ dental)
- **CPO: NONE** within 30km or 100km
- Public Transit: 0 | Walkability: 0
- Medicaid: WV did NOT expand
- Key Barrier: Even with some healthcare, no CPO exists. 190-mile gap to nearest.

### KY Pikeville
- Healthcare (within 30km): 11+ facilities (PMC Medical Diagnostics, MCHC Elkhorn City, 5 doctors, 6 pharmacies, 2 dentists, 1 optometrist, 1 chiropractic)
- **CPO: NONE** within 30km or 100km. Nearest foot care is NOT a CPO.
- Public Transit: 0 | Walkability: 6
- Medicaid: KY expanded (limited)
- Key Barrier: Appalachian isolation. Even a town with services has zero orthotics/prosthetics.

### MS Delta
- Healthcare (within 30km): **ZERO (0)** — the most alarming finding
- Broader (50km+): 1 hospital campus, multiple clinics, 18+ pharmacies, 6+ dentists
- **CPO: NONE** within 30km or 100km. Nearest: Memphis, TN (~200mi)
- Public Transit: 0 | Walkability: 2
- Medicaid: MS did NOT expand
- Key Barrier: **THE WORST IN THE NATION** — highest amputation rate + zero healthcare in radius + 200mi gap + no Medicaid + no transit. Double crisis.

## Recommended Interventions
1. Mobile Prosthetics Clinics for 200-mile gaps
2. Telehealth Orthotics partnerships
3. Medicaid Expansion Advocacy
4. Community Health Worker Programs
5. NHSC Placement for prosthetics clinicians
6. Clinical Trial diversity mandates