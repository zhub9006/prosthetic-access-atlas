# Data Sources & Methodology

> Documentation of data sources, collection methods, and analytical approach.

## 1. Clinical Trial Data

### Primary Source
- **Database**: ClinicalTrials.gov
- **API**: `clinicaltrials.gov/api/v2/studies`
- **Query**: Condition = "prosthetic", Term = "prosthesis", Amputation, Prosthetic care, Prosthetic rehabilitation
- **Date of Analysis**: 2026-07-14
- **Total Records**: 644 prosthetic-related studies

### Analysis Methods
- **Trend Analysis**: Aggregated by study status, geographic country, and clinical trial phase
- **Study Detail Extraction**: Full protocol sections for highlighted trials (NCT07519746, NCT06498245)
- **Geographic Mapping**: Extracted geoPoint data from study location records

### Key Findings Summary
| Metric | Value |
|--------|-------|
| Total Studies | 644 |
| Currently Recruiting | 113 (17.5%) |
| Completed | 271 (42.1%) |
| Phase 1–4 Combined | 74 (11.5%) |
| Observational/N/A | 338 (51.9%) |
| U.S. Sites | 680+ (dominant) |
| Rural-Appalachia Sites | 0 |
| Mississippi-Delta Sites | 0 |

### Highlighted Trials
1. **PROINGA (NCT07519746)**: Prosthetic satisfaction & QoL in Gaza. COMPLETED. 128 participants. Observational.
2. **MPK-K2 (NCT06498245)**: Microprocessor knee for K2 ambulators. RECRUITING. RCT with 4 arms. Northwestern University.

## 2. Gap Analysis Data

### Primary Source
- **Database**: OpenStreetMap (OSM) via Overpass API wrappers
- **Tools**: OSM geocoding, neighborhood analysis, category search
- **Date of Analysis**: 2026-07-14
- **Geographic Scope**: Three underserved U.S. regions

### Regions Analyzed
| Region | Center Point | Radius | Search Categories |
|--------|-------------|--------|-------------------|
| Rural West Virginia | Beckley, WV (37.78, -81.19) | 50–100km | amenity, healthcare, shop |
| Eastern Kentucky | Pikeville, KY (37.48, -82.52) | 50–100km | amenity, healthcare, shop |
| Mississippi Delta | Greenville, MS (33.41, -91.06) | 50–100km | amenity, healthcare, shop |

### Provider Categories Searched
- `amenity=hospital` — General and specialized hospitals
- `amenity=clinic` — Community health centers, urgent care
- `amenity=pharmacy` — Pharmacies (proxy for healthcare infrastructure)
- `amenity=doctors` — Physician offices
- `shop=medical` — Medical supply stores
- `shop=variety_store` — General stores (proxy for DME availability)
- `amenity=healthcare` — General healthcare facilities

### Resolution & Limitations
- **OSM Coverage**: OSM is crowdsourced; some providers may be missing in rural areas, but the 0-result finding is consistent across multiple search methods
- **Radius**: 50–100km radius used; actual travel distance may be longer due on road infrastructure
- **Data Freshness**: OSM data may not reflect the most recent changes; recommend quarterly updates
- **Verification**: OSM provider data should be cross-referenced with state licensure boards and CMS supplier directories

### Neighborhood Scoring Methodology
- **Walk Score algorithm adapted** for rural context
- Categories scored 0–10 based on presence/absence and density within radius
- **Healthcare score = 0** for all three regions: confirmed via multiple independent queries

## 3. Integration Notes

The geographic coincidence between:
- **Zero prosthetic providers** (from OSM gap analysis)
- **Zero dedicated prosthetic research sites** (from ClinicalTrials.gov query)

...in these same underserved regions suggests a compound access problem:

```
No Providers → No Patient Data → No Research → No Evidence-Based Solutions → No Providers
```

Breaking this cycle requires:
1. **Intervention studies** in rural settings (not just urban academic centers)
2. **Provider incentive programs** (loan repayment, tele-prosthetics training)
3. **Community-based participatory research** engaging rural amputees directly

## 4. API References

- **ClinicalTrials.gov API v2**: https://studyspec.clinicaltrials.gov/api/v2
- **Overpass API**: https://overpass-turbo.eu/
- **OSM Geocoding**: Nominatim (https://nominatim.org/)
- **OSM Neighborhood Analysis**: OsmOnEdge/Overpass-based custom analysis

## 5. Contributing Data

When adding new data:
- Use the same 50–100km radius for consistency
- Search for all provider categories listed above
- Note the date of search (OSM data changes over time)
- Submit as pull request with updated JSON/YAML files

---

*Last updated: 2026-07-14. Next scheduled update: Q1 2027.*
