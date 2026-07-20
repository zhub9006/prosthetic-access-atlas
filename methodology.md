# Methodology — Prosthetic Access Atlas

> Version: 1.0 | Updated: 2026-07-20

## Data Collection

### ClinicalTrials.gov
- **API endpoint:** `https://clinicaltrials.gov/api/v2/studies`
- **Queries executed:**
  - `query.cond=prosthetic` → **644 studies** (broad: includes joint, heart valve, limb prosthetics)
  - `query.cond=prosthetic limb` → **136 studies** (focused on limb prosthetics/amputation)
  - `query.cond=prosthetic limb + locn=United States` → **86 US studies**
- **Analysis dimensions:** status, phase, country, sponsor type
- **Date:** July 2026
- **Limitations:** The word "prosthetic" captures prosthetic joint, heart valve, and limb prosthetics. Focused amputation studies are a subset of the broad count.

### OpenStreetMap
- **Geocoding:** Used OSM Nominatim to locate representative cities in each underserved region.
  - Rural WV: Beckley (37.78, -81.19)
  - Eastern KY: Pikeville (37.48, -82.52)
  - Mississippi Delta: Greenville (33.41, -91.06)
- **Provider search:** `find_nearby_places` and `search_category` with coordinates and 20–50km radii.
- **Categories searched:** healthcare (clinic, doctor, pharmacy, dentist, hospital), amenity
- **Limitations:** OSM may miss small private CPO practices not mapped as healthcare facilities. The absence of prosthetist/orthotist entries strongly suggests structural gaps but is not absolute proof.

### Limitations
1. OSM data completeness varies by region — rural areas may have fewer mapped facilities.
2. ClinicalTrials.gov "prosthetic" keyword is broad (includes dental, cardiac, joint prosthetics). Focused amputation studies are a subset.
3. Drive times are estimates based on straight-line distance; actual road travel may be longer.
4. Medicaid expansion status refers to adoption of ACA Medicaid expansion, not current coverage details.
5. This analysis does not claim to be exhaustive; it is a snapshot for advocacy and planning purposes.

---

## Corrected/Updated Figures (2026-07-20)

| Metric | Previous (outdated) | Current (verified) |
|--------|---------------------|-------------------|
| Total prosthetic studies (broad) | 1,491 | **644** (narrower, validated query) |
| Focused prosthetic limb studies | 266 | **136** |
| US prosthetic limb studies | 1,022 | **86** |
| Phase 3 trials globally | Unknown | **30 (4.7%)** |
| Studies with unknown status | Unknown | **134 (20.8%)** |
| Region-level CPO providers | Not verified | **0 in all 3 regions** |

---

## Reproducibility

All data can be reproduced using:
1. ClinicalTrials.gov search: `condition:prosthetic` sorted by firstPostDate
2. OSM Overpass query: `[amenity~"hospital|clinic|pharmacy"]` within target coordinates
3. OSM routing: between origin and destination coordinates
4. GitHub: `gh api repos/zhub9006/prosthetic-access-atlas`

---

*Open methodology — corrections and additions welcome via PR.*
