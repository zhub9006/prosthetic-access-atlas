# Methodology

## Data Sources

### 1. ClinicalTrials.gov
- **API**: ClinicalTrials.gov API v2 (via MCP server)
- **Query**: Condition = "prosthetic", Term = "prosthetic care"
- **Filters**: All statuses, all countries
- **Analysis**: Count by status, count by country
- **Date of extraction**: July 2026

### 2. OpenStreetMap (OSM)
- **Tools**: OSM MCP server (geocode, find_nearby_places, analyze_neighborhood, search_category)
- **Query radius**: 30 km from representative center points
- **Categories searched**: amenity (hospital, clinic, doctors, pharmacy, health_centre, physiotherapist)
- **Neighborhood analysis**: Overall livability scores across 8 categories
- **Date of extraction**: July 2026

### 3. Regional Center Points
- **Rural West Virginia**: Beckley, WV (37.7782, -81.1882) — county seat of Raleigh County
- **Eastern Kentucky**: Eastern/Hindman, Floyd County, KY (37.5170, -82.8060)
- **Mississippi Delta**: Greenville, Washington County, MS (33.4111, -91.0636) — county seat

## Limitations

1. **OSM coverage bias**: Healthcare facilities in rural areas may be under-tagged or missing entirely
2. **Specialty granularity**: OSM tags "hospital" or "clinic" but rarely specify "prosthetic" or "orthotic" as a specialty — our gap analysis may overestimate available services
3. **Travel barriers**: OSM data doesn't capture route difficulty (mountain roads, flooding in Delta) — effective accessibility is likely worse than straight-line distance suggests
4. **Dynamic landscape**: Provider availability changes over time; this is a point-in-time snapshot
5. **Clinical trial focus**: The trials search may miss studies with more specific prosthetic sub-terms (e.g., "myoelectric", "osseointegration")

## Recommendations for Improvement

- Augment OSM data with the Open Doors / O&M Provider Directory
- Add CMS HPC (Healthcare Provider Certification) data for prosthetic suppliers
- Include VA prosthetics data (VHA prosthetists at VA medical centers)
- Pattern-match OSM tags for "prosthetist", "orthotist", "O&P" in facility names and descriptions
- Use claims data to identify actual utilization rates vs. provider counts

## Tools Used

| Tool | Purpose |
|---|---|
| ClinicalTrials.gov MCP | Search and analyze clinical trial registry data |
| OSM MCP Server | Geocode, search nearby places, neighborhood analysis |
| GitHub API | Repository creation and content publishing |

---

*Built with open data and open tools. Contributions welcome!*