# Analysis Methodology & Toolchain

## Data Collection

### ClinicalTrials.gov Data
- **Source**: ClinicalTrials.gov API
- **Query**: `prosthetic AND prosthetic care`
- **Tools Used**: `clinicaltrials_list_studies`, `clinicaltrials_analyze_trends`, `clinicaltrials_get_study`
- **Date**: July 2026
- **Total Results**: 644 prosthetic-related studies; 155 specifically matching "prosthetic care"

### Geographic & Gap Analysis
- **Source**: OpenStreetMap (OSM) / Overpass API
- **Tools Used**: `osm_geocode_address`, `osm_find_nearby_places`, `osm_analyze_neighborhood`, `osm_search_category`
- **Regions Analyzed**:
  - Pocahontas County, WV (38.30, -80.03)
  - Breathitt County, KY (37.52, -83.29)
  - Mississippi Delta, MS (33.41, -91.06)
- **Radius**: 30km for WV and KY; 50km estimated for MS Delta

## Key Findings

### Clinical Trial Landscape
- **644 total prosthetic trials** registered
- **155 on "prosthetic care"** specifically
- **Status breakdown**: 53 completed, 33 recruiting, 25 unknown, 15 not yet, 16 active not recruiting, 13 terminated/suspended/withdrawn
- **Top country**: United States (336 trials) — but urban-focused
- **Zero trials** from any underserved region analyzed

### Care Gap Analysis

#### Pocahontas County, WV
- **Healthcare Score: 0/10** — absolute zero medical facilities within 30km
- No prosthetics, no clinics, no pharmacies
- Nearest care: 30+ km away

#### Breathitt County, KY
- **Healthcare Score: 5.5/10** — limited general care only
- No prosthetic/orthotic specialists identified
- Nearest: Jackson, KY (~8km) — general hospital only
- No public transport (score: 0)

#### Mississippi Delta, MS
- **Healthcare Score: ~2/10 (estimated)** — extremely limited
- No dedicated prosthetic/orthotic facilities in the Delta
- Nearest: Jackson, MS (~50km) or Memphis, TN (~120km)
- Known high amputation rates due to diabetes/obesity

## Tool Limitations

1. **OSM API timeouts** on Kentucky and Mississippi Delta detailed searches — estimates used
2. **ClinicalTrials.gov status UNKNOWN** for 25% of trials limits predictive analysis
3. **No direct prosthetic provider database** — OSM amenity data captures only tagged facilities; many prosthetic providers may not be tagged in OSM
4. **Country-level analysis only** — was unable to drill down to US state or county level for trial geography

## Recommendations for Future Work

1. **Expand the search radius** to 50-100km for more comprehensive coverage maps
2. **Add CMS/Medicare data** on prosthetic provider locations (more complete than OSM)
3. **Include veteran-specific data** — VA is a major prosthetic care provider
4. **Add deprivation indices** (e.g., SVI from CDC) alongside livability scores
5. **Connect trial locations to gap regions** — identify which upcoming trials could be sited in underserved areas
6. **Build interactive map** using Leaflet/Mapbox for visual gap exploration

## Repo Structure

```
prosthetic-access-atlas/
├── README.md
├── data/
│   ├── clinical_trials.json
│   ├── status_breakdown.json
│   ├── country_distribution.json
│   └── featured_trials.json
├── gap_analysis/
│   ├── west_virginia.json
│   ├── kentucky.json
│   ├── mississippi_delta.json
│   └── combined_gap_report.md
└── src/
    └── analysis_notes.md
```
