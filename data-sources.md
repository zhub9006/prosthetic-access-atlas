# Data Sources & Attribution

## Primary Data Sources

### 1. ClinicalTrials.gov API
- **URL:** https://clinicaltrials.gov/api/v2/studies
- **Search Query:** condition:"prosthetic" + term:"prosthetic" + intr:"prosthetic limb" + outc:"prosthetic"
- **Total Records:** 644 prosthetic-related clinical studies
- **Extracted Fields:** NCT ID, official title, sponsor, phase, overall status, primary outcome, eligibility, locations, interventions, enrollment, last update post date
- **API Version:** v2 (REST API)
- **Query Date:** July 2025

### 2. OpenStreetMap / Humanitarian Data Exchange
- **API:** Overpass API (https://overpass-api.de/)
- **Query:** Healthcare amenity search (clinic, hospital, pharmacy, doctor, dentist, physiotherapist) within 50-60km radius of region centers
- **Search Areas:**
  - Rural WV: Marlinton (38.22N, -80.09W) — Pocahontas County
  - Eastern KY: Hazard (37.25N, -83.19W) — Perry County
  - MS Delta: Greenville (33.41N, -91.06W) — Washington County
- **Limitations:** OSM data is crowdsourced; prosthetic/orthotic-specific facilities may be underrepresented. CPO facilities are distinct from general clinics.

### 3. ABC Provider Directory
- **Organization:** American Board for Certification in Orthotics, Prosthetics & Pedorthics
- **URL:** https://www.abortho.org/public.aspx
- **Use:** Cross-referencing CPO-verified providers against OSM results

## Geographic Data
- **West Virginia Center:** Marlinton, WV (38.22°N, 80.09°W) — Pocahontas County
- **Eastern Kentucky Center:** Hazard, KY (37.25°N, 83.19°W) — Perry County
- **Mississippi Delta Center:** Greenville, MS (33.41°N, 91.06°W) — Washington County

## Notes
- Country counts for multi-country studies may exceed 644 total
- OSM may miss small independent prosthetist offices
- Travel times assume driving; public transit minimal in all regions
- Medicaid policies change frequently; barrier assessments reflect current landscape

---*
All data is open-access and meant to be improved by the community. Corrections welcome via PR.