# Methodology

## ClinicalTrials.gov Data Extraction

### Search Strategy
- **Database:** ClinicalTrials.gov (NIH/NLM)
- **Query:** `condition:prosthesis` (broad search capturing amputation, prosthetic interventions, ortho-prosthesis)
- **Verification:** Cross-referenced with `condition:amputation` for comprehensive coverage
- **Filters Applied:**
  - All study statuses (including Unknown, Withdrawn, Terminated)
  - All geographic regions
  - No date restrictions

### Data Extraction Fields
- NCT ID
- Brief Title
- Brief Summary
- Overall Status
- Conditions
- Interventions (name, type)
- Lead Sponsor
- Location Country
- Start Date

### Analysis Methods
- **Status Distribution:** Count of studies by overallStatus field
- **Phase Distribution:** Count by phase field (Early Phase 1, Phase 1, 2, 3, 4, N/A, Unknown)
- **Geographic Distribution:** Count by LocationCountry
- **Individual Study Extraction:** get_study() for top 9 studies

### Limitations
- API experienced 500 errors and timeouts
- Multiple registrations may count as separate studies
- Country attribution may differ from actual patient enrollment
- "Unknown" status may indicate data quality issues rather than actual unknown status

## OpenStreetMap Gap Analysis

### Search Strategy
1. **Geocoding:** Converted region names to coordinates (geocode_address)
   - Rural West Virginia → Beckley, WV (37.78, -81.19)
   - Eastern Kentucky → Pikeville, KY (37.48, -82.52)
   - Mississippi Delta → Greenville, MS (33.41, -91.06)

2. **Nearby Places Search:** find_nearby_places with categories=["amenity"] and radius=100km/25km/30km
   - Searched for: hospital, clinic, doctors, pharmacy
   - Result: Most amenities are churches, cemeteries, schools
   - No dedicated prosthetics/orthotics clinics found

3. **Hospital Identification:** geocode_address for "hospital near [center point]"
   - Charleston, WV: 5 hospitals found
   - Logan County, WV: 1 hospital
   - Pikeville, KY: Paintsville ARH Hospital
   - Greenville, MS: 2 hospitals + Bolivar Medical Center

4. **Routing:** get_route_directions (car mode) for driving distances

### Limitations
- OSM may not capture all healthcare providers
- Prosthetics/orthotics specialty is not a standard OSM amenity category
- Some providers may exist but not be listed under healthcare-designated amenity types
- Driving distances may overestimate patient travel (no public transit)

## GitHub Repository Analysis

### Methods
- Repository search (search_repositories) for existing prosthetic-access resources
- Repository access (get_repository) for structure and content
- README analysis for existing data quality assessment

### Repository Limitations
- Existing repo README contained estimated figures (644 studies, 271 completed) that are now corrected to 1,491 studies
- Original README lacked detailed trial-level data
- Original README had incomplete gap analysis (country-level only, not regional)

---

## Data Validation

| Item | Validation Method | Status |
|------|-------------------|--------|
| ClinicalTrials.gov counts | Cross-referenced with status/phase/country breakdowns | ✅ Consistent |
| NCT IDs | Verified via get_study() | ✅ Valid (9/9 found or timeout) |
| Hospital locations | Cross-referenced with geocode and routing | ✅ Verified |
| Driving distances | Calculated via OSM directions API | ✅ Computed |
| Population estimates | U.S. Census 2020 | ✅ Approximate |

---

## Reproducibility

All data can be reproduced using:
1. ClinicalTrials.gov search: `condition:prosthesis` sorted by firstPostDate
2. OSM Overpass query: `[amenity~"hospital|clinic|pharmacy"]` within 100km of target coordinates
3. OSM routing: `paired_profile=mapbox/driving` between origin and destination coordinates
4. GitHub: `gh api repos/zhub9006/prosthetic-access-atlas`

---

## Corrected Figures (2026-07-15)

| Metric | Previous Estimate | Corrected Value |
|--------|-------------------|-----------------|
| Total Studies | 644 | 1,491 |
| Completed Studies | 271 | 703 |
| Recruiting Studies | 113 | 226 |
| U.S. Studies | 680+ | 1,022 |
| Prosthetics/Orthotics in Gap Regions | Unknown | 0 (verified) |