---

# Data Sources & Methodology

## Clinical Trial Data

- **Source:** ClinicalTrials.gov API
- **Query:** Condition = "prosthetic" (broad)
- **Total studies retrieved:** 644
- **Date of retrieval:** July 2025
- **Method:** Programmatic query using `clinicaltrials_list_studies` and `clinicaltrials_analyze_trends` for status, country, phase, and sponsor breakdowns.

## Access Gap Data

- **Source:** OpenStreetMap (via OSM MCP tools)
- **Geocoding:** Place-based geocoding of region representative towns
- **Nearby searches:** `find_nearby_places` (30–100 km radius) and `explore_area` (30–100 km radius)
- **Route directions:** `get_route_directions` for driving distance/time to nearest metro areas
- **Categories searched:** amenity, shop, office, health
- **Subcategories of interest:** hospital, clinic, health_center, pharmacy, doctors, prosthetics, orthotics

## Key Assumptions & Limitations

1. OSM data may not capture all small or newly opened providers.
2. Prosthetic/orthotic providers may be listed under general medical categories without explicit prosthetics tags.
3. Driving distances assume road access; actual travel time varies with weather and road conditions.
4. "Care desert" classification requires that NO providers exist within 100 km — near-miss areas are flagged for monitoring.
5. The ClinicalTrials.gov query uses the broad condition "prosthetic" which may include dental prosthetics and joint prostheses alongside limb prosthetics.

---

*Compiled for open-access use under MIT License.*
