# Data Sources & Methodology

## Clinical Trial Data

- **Source:** ClinicalTrials.gov API v2
- **Query Date:** July 2026
- **Queries Used:**
  - `cond=prosthetic` (broad): 644 studies, 421 with geographic data
  - `cond=prosthetic limb` (filtered): 184 studies, 136 clinical
  - `term=prosthetic limb amputation`: supplemental
- **Analysis Endpoints:**
  - `countByStatus` — filtered by RECRUITING, COMPLETED, ACTIVE_NOT_RECRUITING
  - `countByPhase` — full phase distribution
  - `countBySponsorType` — industry vs academic vs federal
  - `countByCountry` — geographic distribution (recruiting + completed only)
- **Note:** API experienced intermittent 500 errors and timeouts during data collection; results represent best-effort accumulation across multiple attempts

## Geographic Data

- **Source:** OpenStreetMap (via OSM MCP tools)
- **Geocoding:** `geocode_address` for region centroids
- **Provider Search:** `find_nearby_places` with categories [healthcare, amenity]
- **Route Data:** `get_route_directions` (car mode) from representative rural coordinates to nearest major city
- **Search Radius:** 30–50 km from representative town coordinates
- **Regions Searched:**
  - Rural West Virginia (Dille: 38.48, -80.84; Beckley: 37.78, -81.19)
  - Eastern Kentucky (Pikeville: 37.48, -82.52; Elkhorn City: 37.30, -82.35)
  - Mississippi Delta (Greenville: 33.41, -91.06; Indianola: 33.45, -90.66)

## Key Definitions

- **CPO:** Certified Prosthetist-Orthotist — the primary provider for prosthetic/orthotic care
- **30 km threshold:** roughly 19 miles, representing a reasonable access radius for routine prosthetic follow-up
- **Gap:** A region with zero CPO providers within 30 km of the representative coordinate
- **Drive time:** Calculated via OSM routing engine (car mode) from representative rural point to nearest major city with hospital

## Limitations

1. ClinicalTrials.gov API experienced service disruptions (500 errors, timeouts) — some trend data may be incomplete
2. OSM data reflects only what is mapped; some providers may be missing, especially unlisted CPOs
3. Distance calculations are road-based estimates; actual travel times may vary by season/conditions
4. This analysis identifies *structural* gaps; individual patient experiences may differ
5. Medicaid expansion status was checked as of 2026 — both WV and KY have not expanded
6. The "Mississippi Delta" region is defined broadly; micro-regions within it may have different access profiles