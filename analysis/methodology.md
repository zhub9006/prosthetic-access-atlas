# Prosthetic Access Atlas - Methodology

## Data Sources
1. **ClinicalTrials.gov API** - search: "prosthetic" condition; 644 total studies
2. **OpenStreetMap Overpass API** - healthcare amenity search within 50-60km of region centers
3. **ABC Provider Directory** - cross-referencing CPO providers

## Trend Analysis Methods
- Status Distribution:categorized all 644 studies by overall status
- Phase Distribution: mapped studies to Phase1-4, Early_Phase1, N/A, Unknown
- Sponsor Analysis: classified by lead sponsor type (Industry, Academic/Other, Federal, Other Gov, Network, NIH)
- Geographic Distribution: aggregated by country; top 15 ranked

## Access Gap Analysis Methods
1. Region selection based on amputation rates, poverty/Medicaid expansion, CPO deserts
2. FACILITY MAPPING: OSM healthcare amenity search around each region center (+50km, expanded +10km)
3. CPO Verification: cross-referenced against ABC directory + known prosthetic care providers
4. Severity Rating: CRITICAL (no CPO within 50mi/100km) or EXTREME (no CPO within 200km)

## Limitations
- Country counts for multi-country studies may exceed 644 total
- OSM may miss small probsthetist offices
- Travel estimates assume driving; public transit minimal in all regions
- Medicaid policies change frequently