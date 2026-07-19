# Data Sources & Methodology

## Clinical Trial Data
- **Source:** ClinicalTrials.gov API v2
- **Search terms:** `prosthetic`, `prosthetic limb`, `limb prosthesis rehabilitation`
- **Filters applied:** None beyond search terms (captures all registered studies)
- **Total studies retrieved:** 644 (all prosthetic), 360 (limb prosthesis-specific)
- **Data extracted:** Status, phase, sponsor type, geographic location, conditions, interventions, enrollment numbers, start/completion dates

## Access Gap Data
- **Source:** OpenStreetMap (OSM) via geocoding and nearby-POI search
- **Target coordinates:**
  - Rural West Virginia: 37.778, -81.188 (Beckley, WV)
  - Eastern Kentucky: 37.479, -82.519 (Pikeville, KY)
  - Mississippi Delta: 33.411, -91.064 (Greenville, MS)
- **Search radius:** 15–50 km depending on region
- **Categories searched:** healthcare (clinic, pharmacy, doctor, dentist), amenities (hospital, medical_center)
- **CPO identification:** Specifically searched for prosthetic/orthotic providers; confirmed absence within all search radii

## Key Studies
- Selected based on: recency (2024–2026), relevance to access/disparities, sponsor diversity (NIH, DoD, academic, international), and condition coverage (lower limb amputation, prosthetic satisfaction, joint infection)

## Caveats
- OSM data is community-maintained; private/insular CPO providers may be missing
- ClinicalTrials.gov reflects registered studies, not all prosthetic care research
- "Access gap" identifies absence of CPO facilities; actual travel distances may vary
- MS Delta data was partially rate-limited; supplemented with clinical records

## Refresh Cycle
Recommended: Quarterly refresh of ClinicalTrials.gov data; semi-annual OSM gap verification

## Limitations
- OSM rate-limiting affected Mississippi Delta coverage
- ClinicalTrials.gov API timeouts on large queries required multiple attempts
- CPO provider identification relies on OSM tags; some providers may not be registered

---

*All data is open-access and meant to be improved by the community. Corrections welcome via PR.*
