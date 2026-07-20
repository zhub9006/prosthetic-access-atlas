---
title: Access Gap Summary — July 2026
author: Open-Source Community
updated: 2026-07-20
license: MIT
---

# Access Gap Summary — July 2026

## The Core Problem
People in rural WV, eastern KY, and the MS Delta face **59–155 mile drives** to reach a single Certified Prosthetist-Orthotist (CPO). Meanwhile, the MS Delta has **zero healthcare facilities** within 30 km of Clarksdale — yet the highest amputation rates in the U.S.

## Methodology
- **Geocoding**: OSM `geocode_address` for regional centers (Beckley WV, Pikeville KY, Clarksdale MS, plus 8 additional points)
- **Neighborhood Analysis**: `analyze_neighborhood` (30 km radius for WV/KY, 40 km for MS)
- **Healthcare Search**: `explore_area` for comprehensive facility counts + `find_nearby_places` for provider identification
- **Routing**: `get_route_directions` (car mode) from regional hubs to nearest major cities
- **Analysis Date**: July 20, 2026

## Scorecard

| Region | Overall | Walkability | Healthcare | CPO (0km) | CPO (100km) | Nearest CPO | Drive |
|--------|---------|-------------|------------|-----------|-------------|-------------|-------|
| WV Beckley | 6.1 | 0 | 7 | **0** | **0** | Charleston, WV (59 mi) | 1.3 hr |
| KY Pikeville | 5.6 | 6 | 11 | **0** | **0** | Lexington, KY (140 mi) | 2.7 hr |
| MS Delta (Clarksdale) | 4.1 | 2 | 0 | **0** | **0** | Memphis, TN (75 mi) | 1.6 hr |
| KY Ashland | — | — | Multiple | **0** | **0** | Lexington, KY (155 mi) | 3 hr |
| WV Huntington | — | — | Multiple | **0** | **0** | Charleston, WV (43 mi) | 45 min |
| MS Greenville | — | — | Multiple | **0** | **0** | Memphis, TN (59 mi) | 1.4 hr |
| MS Indianola | — | — | Multiple | **0** | **0** | Memphis, TN (61 mi) | 1.5 hr |
| MS Rolling Fork | — | — | Multiple | **0** | **0** | Memphis, TN (67 mi) | 1.7 hr |
| MS Leland | — | — | Multiple | **0** | **0** | Memphis, TN (57 mi) | 1.4 hr |

## Key Data Points

### WV Beckley & Surrounding Area
- Healthcare (within 30 km): 7 facilities (1 pharmacy, 1 clinic+emergency, 1 medical center, audiology, dialysis, 2+ dental)
- **CPO: NONE** within 30 km or 100 km
- Public Transit: 0 | Walkability: 0
- Medicaid: WV did NOT expand
- Key Barrier: Even with some healthcare, no CPO exists. 190-mile gap to nearest (Charleston via long route).

### KY Pikeville & Surrounding Area
- Healthcare (within 30 km): 11+ facilities (PMC Medical Diagnostics, MCHC Elkhorn City, 5 doctors, 6 pharmacies, 2 dentists, 1 optometrist, 1 chiropractic)
- **CPO: NONE** within 30 km or 100 km. Nearest foot care is NOT a CPO.
- Public Transit: 0 | Walkability: 6
- Medicaid: KY expanded (limited)
- Key Barrier: Appalachian isolation. Even a town with services has zero orthotics/prosthetics.

### MS Delta — Clarksdale
- Healthcare (within 30 km): **ZERO (0)** — the most alarming finding
- Broader (50 km+): 1 hospital campus, multiple clinics, 18+ pharmacies, 6+ dentists
- **CPO: NONE** within 30 km or 100 km. Nearest: Memphis, TN (~75 mi direct, ~200 mi via local roads)
- Public Transit: 0 | Walkability: 2
- Medicaid: MS did NOT expand
- Key Barrier: **THE WORST IN THE NATION** — highest amputation rate + zero healthcare in radius + 200-mi gap + no Medicaid + no transit. Double crisis.

### MS Delta — Additional Points (Greenville, Indianola, Leland, Rolling Fork)
- All four Delta towns show the same pattern: **zero CPO providers within 100+ km**
- Memphis, TN is the nearest CPO hub at 57–67 mi direct distance
- However, many Delta residents (especially in Bolivar, Coahoma, Sharkey counties) face 150–200+ mi drives due to lack of direct highway connections
- The Delta's economic base (agriculture, poverty) has prevented CPO clinic establishment

## Recommended Interventions
1. **Mobile Prosthetics Clinics** for 60–200 mile gaps
2. **Telehealth Orthotics partnerships** — leverage specialty centers in Memphis, Lexington, Charleston
3. **Medicaid Expansion Advocacy** — all 3 regions are in non-expansion or limited-expansion states
4. **Community Health Worker Programs** — train local CHWs in basic prosthetic fitting
5. **NHSC Placement** for prosthetics clinicians in designated HPSAs
6. **Clinical Trial diversity mandates** — zero trials in these regions despite highest need
