# Data Sources

| Source | URL | Type | Date Used |
|--------|-----|------|-----------|
| ClinicalTrials.gov API | https://clinicaltrials.gov/api/v2/studies | REST API | 2026-07-13, 2026-07-15 |
| OpenStreetMap Overpass | https://overpass-api.de/api/ | Geospatial Query | 2026-07-15 |
| OSM Geocoding | https://nominatim.openstreetmap.org/ | Geocoding | 2026-07-15 |
| GitHub Repo | https://github.com/zhub9006/prosthetic-access-atlas | Repository | 2026-07-15 |
| U.S. Census Bureau | https://www.census.gov/ | Demographics | Reference |
| CDC Diabetes Atlas | https://www.cdc.gov/diabetes/data/ | Health Data | Reference |

## API Parameters
### ClinicalTrials.gov
- Query cond: `prosthetic`
- Query term: `prosthetic limb amputation`
- Analyses: `countByStatus`, `countByCountry`
- Page size: 10-50
- Fields: NCTId, BriefTitle, OverallStatus, StartDate, CompletionDate, Location, StudyType, Enrolled

### OpenStreetMap
- Geocoding: `geocode_address` for Beckley WV, Pikeville KY, Greenville MS
- Reverse: `reverse_geocode` for address confirmation
- Neighborhood: `analyze_neighborhood` (25-30km radius)
- Categories: amenity=hospital, clinic, doctors, pharmacy, health_centre, dentist

## Limitations
1. OSM may not capture all private O&P clinics
2. ClinicalTrials.gov may not index all prosthetics trials
3. OSM point-center searches may miss adjacent county providers
4. OSM data is community-edited and may be outdated

*Last updated: 2026-07-15*