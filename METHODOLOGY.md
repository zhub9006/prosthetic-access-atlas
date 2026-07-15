# Methodology

## Data Collection (2026-07-15)

### 1. ClinicalTrials.gov
- **API:** ClinicalTrials.gov MCP server
- **Query:** `condition=prosthetic` (644 matching studies)
- **Trends:** `countByStatus` and `countByCountry` aggregations
- **Detail:** Full protocol data for 5 representative trials
- **Regional search:** `locn` filter applied for West Virginia, Kentucky, Mississippi

### 2. OpenStreetMap (via OSM MCP)
- **Geocoding:** Resolved Buckhannon WV, Hazard KY, and Greenville MS to precise coordinates
- **Neighborhood Analysis:** `analyze_neighborhood` with 30km radius (walkability, healthcare, education, services scores)
- **Healthcare Search:** `find_nearby_places` with healthcare category filters
- **Category Search:** `search_category` for healthcare subcategories

### 3. Tools Used
| Tool | Purpose |
|------|---------|
| `clinicaltrials_list_studies` | Search/retrieve trial listings |
| `clinicaltrials_analyze_trends` | Aggregate by status, country |
| `clinicaltrials_get_study` | Detailed trial protocol data |
| `geocode_address` | Resolve location names → coordinates |
| `analyze_neighborhood` | Livability/amenity scoring (30km) |
| `find_nearby_places` | POI search by category |
| `search_category` | Area-based feature search |

### Limitations
1. **OSM data may be incomplete** — smaller O&P businesses may not be mapped
2. **30km radius baseline** — in rural areas, nearest O&P may be 60-100+ km away but still "closest" option
3. **ClinicalTrials.gov only reflects registered studies** — unregistered/industry-only trials excluded
4. **Neighborhood scores are algorithmic estimates** — real-world access may differ
5. **OSM categories may not capture O&P** — prosthetists/orthotists may be under different categories or not mapped at all

### Recommended Validation
1. **ABC Directory** (certification board O&P provider locator)
2. **NAAO+P** (professional association)
3. **CMS Medicare O&P Supplier Locator**
4. **State occupational therapy & prosthetics boards**
5. **Major provider networks:** Hanger, Össur, Ottobock, Fairride/Clarkson

### Rate Limits Encountered
- OSM `find_nearby_places` returned 429 (rate limited) on second call for West Virginia — used `search_category` results instead
- Shell limit on `search_category` with complex bounding boxes — reverted to `find_nearby_places` with healthcare category for KY and MS successfully

## Repository Structure
```
prosthetic-access-atlas/
├── README.md                      # Overview and key findings
├── CLINICAL_TRIALS.md             # Detailed trial data (existing)
├── clinical_trials/
│   ├── summary.md                 # Status/country trends (existing)
│   ├── detailed_trials.md         # ← NEW: 5 trial profiles + access gap
│   ├── trials.json                # ← NEW: Structured JSON data
│   └── trials.json                # ← NEW: Trial profiles and regional presence
├── gap_analysis/
│   ├── region_profiles.md          # Regional profiles (existing, enriched)
│   ├── coverage_gap_map.md         # Gap visualization (existing, updated)
│   └── precise_gaps.md             # ← NEW: Precise provider data for 3 regions
├── regions/
│   ├── west_virginia.md            # ← NEW: WV detailed analysis
│   ├── eastern_kentucky.md         # ← NEW: KY detailed analysis
│   └── mississippi_delta.md        # ← NEW: MS detailed analysis
└── METHODOLOGY.md                  # ← NEW: This file
```

## Future Enhancements
1. Interactive Globe/Map (Leaflet.js) with plotted provider locations and coverage polygons
2. Validate OSM provider data against ABC directory and phone verification
3. Expand to additional at-risk corridors (Appalachian Ohio, Rural Arkansas, Deep South, Navajo Nation, Black Hills)
4. Integrate HCUP/Medicare data for amputee incidence by county
5. Add travel-time isochrone calculations from centroid points
6. Track NIH/CDC grant funding and trial enrollment by region
7. Monitor ClinicalTrials.gov for new access/equity-focused prosthetic studies