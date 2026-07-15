# Methodology

> How this atlas was built — transparent, reproducible, and open.

## Clinical Trial Data Collection
- Source: ClinicalTrials.gov API (api/v2/studies)
- Query: `cond=prosthetic` and related terms
- Analyses: `countByStatus`, `countByCountry`
- Retrieval date: 2026-07-15
- Total matched studies: 2,182

### Data Fields Used
| Field | Source |
|-------|--------|
| NCT ID, Brief Title, Official Title | `protocolSection.identificationModule` |
| Overall Status | `protocolSection.statusModule.overallStatus` |
| Start/Completion Dates | `protocolSection.statusModule.startDateStruct` |
| Sponsor | `protocolSection.sponsorCollaboratorsModule.leadSponsor` |
| Conditions | `protocolSection.conditionsModule.conditions` |
| Study Type | `protocolSection.designModule.studyType` |
| Enrollment | `protocolSection.designModule.enrollmentInfo.count` |
| Locations | `protocolSection.contactsLocationsModule.locations` |
| Brief Summary | `protocolSection.descriptionModule.briefSummary` |

## Geospatial Gap Analysis
- Source: OpenStreetMap (Overpass API)
- Geocoding: `geocode_address` for region centers
- Nearby search: `find_nearby_places` with healthcare category
- Reverse geocode: `reverse_geocode` for location confirmation
- Neighborhood analysis: `analyze_neighborhood` for livability scoring
- Search radius: 50-100km around each region

### Healthcare Categories
- `clinic`, `hospital`, `pharmacy`, `doctor`, `dentist`, `rehabilitation`
- `prosthetist`, `orthotist`, `O&P` — **not found**

### Regions
| Region | Center Point | Coordinates | Radius |
|--------|-------------|-------------|--------|
| Rural WV | Beckley, WV | 37.778°N, 81.188°W | 25 km |
| Eastern KY | Pikeville, KY | 37.479°N, 82.519°W | 25 km |
| MS Delta | Greenville, MS | 33.411°N, 91.064°W | 25 km |

## Limitations
1. OSM may not capture all private O&P clinics
2. ClinicalTrials.gov may not index all prosthetics-related trials
3. OSM point-center searches may miss adjacent county providers
4. OSM data is community-edited and may be outdated

## Tools
| Tool | Purpose |
|------|---------|
| `clinicaltrials_analyze_trends` | Aggregate by status, country |
| `clinicaltrials_list_studies` | Retrieve trial details |
| `clinicaltrials_get_study` | NCT-specific summaries |
| `osm_geocode_address` | Region coordinates |
| `osm_reverse_geocode` | Address lookup |
| `osm_find_nearby_places` | Search amenities |
| `osm_analyze_neighborhood` | Livability scoring |

*Last updated: 2026-07-15*