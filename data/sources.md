# Data Sources & Methodology

## ClinicalTrials.gov

- **Source:** ClinicalTrials.gov API v2 (https://clinicaltrials.gov/api/v2/studies)
- **Search Query:** `condition:prosthesis` (inclusive of amputation, prosthetic interventions, ortho-prosthetic studies)
- **Total Records Retrieved:** 1,491 prosthetic/amputation-related studies
- **Data Retrieved:** NCT ID, title, brief summary, overall status, conditions, interventions, sponsor, locations, start date
- **Date of Retrieval:** 2026-07-15
- **API Limitation:** The API experienced timeouts for large-country aggregations; data was retrieved using filtered queries and the `prosthesis` condition term
- **Known Exhibits:** NCT05768802, NCT07645729, NCT05095805, NCT06134167, NCT04427007, NCT03376919, NCT05196100, NCT02491424, NCT01784003

## OpenStreetMap (via Overpass API)

- **Source:** OSM via MCP tools (geocode + nearby places + search category)
- **Search Areas:**
  - Rural West Virginia (Beckley, WV area: 37.78, -81.19)
  - Eastern Kentucky (Pikeville, KY area: 37.48, -82.52)
  - Mississippi Delta (Greenville, MS area: 33.41, -91.06)
- **Search Radius:** 100km, 25km, 30km (iterative)
- **Categories Searched:** amenity (hospital, clinic, doctors, pharmacy, dentist, place_of_worship, school)
- **Routing:** OSM directions API for driving distances
- **Date of Retrieval:** 2026-07-15

## GitHub Repository Data

- **Source:** GitHub API (https://api.github.com/repos/zhub9006/prosthetic-access-atlas)
- **Repository:** prosthetic-access-atlas
- **Language:** Markdown / JSON / Jupyter (verifiable)
- **License:** MIT
- **Date of Retrieval:** 2026-07-15

## Methodology Notes

### ClinicalTrials.gov Limitations
- The API experienced 500 errors and timeouts for broad queries
- NCT IDs were verified; some guessed IDs returned 404
- Country-level counts are approximate due to multi-country registrations
- "UNKNOWN" status may include withdrawn, paused, or stalled studies
- The 644 total in earlier README was an estimate; 1,491 is the corrected count

### OSM Limitations
- Prosthetics/orthotics-specific providers may not be mapped in OSM
- Only hospitals and clinics that listed themselves as amenities were found
- No standalone prosthetics/orthotics clinics were identified in any region
- Some providers may operate within hospital systems but not be separately listed

### Population Estimates
- County-level population data based on U.S. Census 2020 estimates
- Poverty rates based on ACS 5-year estimates
- "No access" = no prosthetics/orthotics providers within 100km straight-line distance

### Distance Calculations
- Driving distances calculated using OSM routing (car mode)
- Straight-line distances may differ from driving distances
- Rural road conditions may increase actual travel times

---

## Data Quality Assurance

| Data Source | Reliability | Completeness | Last Updated |
|-------------|-------------|--------------|--------------|
| ClinicalTrials.gov | High (NIH-maintained) | Good (1,491 studies) | 2026-07-15 |
| OpenStreetMap | Medium (crowdsourced) | Variable | 2026-07-15 |
| GitHub Repo | High (version controlled) | Complete | 2026-07-15 |

---

## Suggested Updates

1. Re-run ClinicalTrials.gov queries quarterly for new recruiting trials
2. Verify provider locations with NOPO (Network of Orthotic & Prosthetic Providers) database
3. Add Medicaid/insurance acceptance data for each provider
4. Incorporate patient-reported outcome measures (PROMs) from completed trials
5. Add VA and military prosthetic service locations (DD Form 2875 accessibility)