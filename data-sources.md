# Data Sources & Methodology

> How this atlas was built — transparent, reproducible, and open.

## ClinicalTrials.gov Data

- **API version**: ClinicalTrials.gov v2 API
- **Query**: `"prosthetic"` with term filters for `prosthetic care OR prosthetics OR orthotics`
- **Analyses performed**: `countByStatus`, `countByCountry`, `countByPhase`
- **Retrieval date**: 2026-07-15
- **Total matched studies**: 2,182 (across all prosthetic sub-queries)

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

### Status Breakdown (from query: "prosthetic")
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 936 | 43.0% |
| UNKNOWN | 434 | 19.9% |
| RECRUITING | 380 | 17.4% |
| NOT_YET_RECRUITING | 145 | 6.6% |
| TERMINATED | 76 | 3.5% |
| ACTIVE_NOT_RECRUITING | 119 | 5.5% |
| WITHDRAWN | 45 | 2.1% |
| ENROLLING_BY_INVITATION | 40 | 1.8% |
| SUSPENDED | 5 | 0.2% |

### Phase Breakdown
| Phase | Count | % |
|-------|-------|---|
| NA (Not Applicable) | 1,273 | 58.5% |
| Unknown | 653 | 29.9% |
| PHASE4 | 91 | 4.2% |
| PHASE3 | 69 | 3.2% |
| PHASE2 | 78 | 3.6% |
| PHASE1 | 35 | 1.6% |
| EARLY_PHASE1 | 10 | 0.5% |

### Geographic Reach (Top Countries)
| Country | Count |
|---------|-------|
| United States | 2,393 |
| France | 825 |
| Germany | 533 |
| Spain | 228 |
| Italy | 347 |
| Canada | 209 |
| Netherlands | 194 |
| United Kingdom | 193 |
| Japan | 75 |
| Australia | 118 |

### Sponsor Types
| Sponsor Type | Count | % |
|-------------|-------|---|
| OTHER (academic/clinical) | 1,676 | 76.8% |
| INDUSTRY | 382 | 17.5% |
| FED (federal/government) | 52 | 2.4% |
| NETWORK | 23 | 1.1% |
| OTHER_GOV | 46 | 2.1% |
| NIH | 2 | 0.1% |

## OpenStreetMap Data

- **API**: Overpass API via OSM-MCP server
- **Geocoding**: `geocode_address` for region centers
- **Nearby search**: `find_nearby_places` with `healthcare` category
- **Reverse geocode**: `reverse_geocode` for location confirmation
- **Neighborhood analysis**: `analyze_neighborhood` for livability scoring
- **Radius**: 50 km for urban areas, 30 km for rural

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
| Region | Center Point | Coordinates | Radius |
|--------|-------------|-------------|--------|
| Rural West Virginia | Beckley, WV | 37.778°N, 81.188°W | 25 km |
| WV (State Center) | Charleston, WV | 38.419°N, 82.445°W | 30 km |
| Eastern Kentucky | Pikeville, KY | 37.479°N, 82.519°W | 25 km |
| KY (Ashland) | Ashland, KY | 38.478°N, 82.638°W | 30 km |
| Mississippi Delta | Greenville, MS | 33.411°N, 91.064°W | 25 km |
| MS Delta (Clarksdale) | Clarksdale, MS | 34.201°N, 90.570°W | 30 km |

## Limitations

1. **OSM completeness**: Private O&P clinics may not maintain OSM entries. Absence suggests a gap but does not prove non-existence.
2. **ClinicalTrials.gov scope**: The API may not index all prosthetics-related trials; some use different condition terminology.
3. **Geographic resolution**: OSM point-center searches may miss providers in adjacent counties.
4. **Temporal validity**: OSM data is community-edited and may be outdated.
5. **Rate limits**: Some API calls were rate-limited (429/504), which may have affected the completeness of nearby-place searches.

## Tools Used

| Tool | Purpose |
|------|---------|
| `clinicaltrials_analyze_trends` | Aggregate studies by status, phase, country, sponsor |
| `clinicaltrials_list_studies` | Retrieve recent trial details |
| `clinicaltrials_get_study` | Detailed study summaries (NCT-specific) |
| `osm_geocode_address` | Convert region names to coordinates |
| `osm_reverse_geocode` | Reverse coordinate lookup for addresses |
| `osm_find_nearby_places` | Search healthcare amenities near each center |
| `osm_analyze_neighborhood` | Livability scoring (healthcare, amenities, transport) |
| `github_create_repository` | Create public atlas repository |
| `github_push_files` | Compile all outputs into structured files |

---

*Last updated: 2026-07-15*