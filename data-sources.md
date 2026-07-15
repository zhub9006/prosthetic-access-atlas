# Data Sources & Methodology

> How this atlas was built — transparent, reproducible, and open.

## ClinicalTrials.gov Data

- **API version**: ClinicalTrials.gov v2 API
- **Query**: `"prosthetic"` with term filters for `prosthetic care OR prosthetics OR orthotics`
- **Analyses performed**: `countByStatus`, `countByCountry`
- **Retrieval date**: 2026-07-15
- **Total matched studies**: 192

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

## OpenStreetMap Data

- **API**: Overpass API via OSM-MCP server
- **Geocoding**: `geocode_address` for region centers
- **Nearby search**: `find_nearby_places` with `healthcare` category
- **Radius**: 50 km for urban areas, 30 km for rural
- **Retrieval date**: 2026-07-15

### Healthcare Categories Searched
- `clinic` — community health centers, urgent care
- `hospital` — inpatient facilities
- `pharmacy` — drug stores
- `doctor` — general practitioners, specialists
- `dentist` — dental providers
- `rehabilitation` — rehab hospitals and centers
- `optometrist` — vision care
- `chiropractic` — musculoskeletal care
- `prosthetist` / `orthotist` / `O&P` — **not found**

### Regions Analyzed
| Region | Center Point | Radius |
|--------|-------------|--------|
| Rural West Virginia | 38.48°N, 80.84°W | 30 km |
| Eastern Kentucky | 37.48°N, 82.52°W | 50 km |
| Mississippi Delta | 33.41°N, 91.06°W | 50 km |

## Limitations

1. **OSM completeness**: Private O&P clinics may not maintain OSM entries. Absence suggests a gap but does not prove non-existence.
2. **ClinicalTrials.gov scope**: The API may not index all prosthetics-related trials; some use different condition terminology.
3. **Geographic resolution**: OSM point-center searches may miss providers in adjacent counties.
4. **Temporal validity**: OSM data is community-edited and may be outdated.

## Tools Used

| Tool | Purpose |
|------|---------|
| `clinicaltrials_analyze_trends` | Aggregate studies by status, country |
| `clinicaltrials_list_studies` | Retrieve recent trial details |
| `osm_geocode_address` | Convert region names to coordinates |
| `osm_find_nearby_places` | Search healthcare amenities near each center |
| `github_create_repository` | Create public atlas repository |
| `github_push_files` | Compile all outputs into structured files |

---

*Last updated: 2026-07-15*
