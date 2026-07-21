# Methodology — Prosthetic Access Atlas (Updated July 2026)

## Data Collection

### ClinicalTrials.gov Data
- **API version:** ClinicalTrials.gov API v2
- **Query dates:** July 20–21, 2026
- **Search queries:**
  1. `cond=prosthetic` + `term=prosthetic care` → 155 results
  2. `cond=prosthetic limb` + `term=prosthetic rehabilitation` → 32 results
  3. `cond=upper limb amputation` + `term=prosthetic` → 88 results
  4. `cond=lower limb amputation` + `term=prosthetic` → 176 results
  5. `cond=prosthetic limb amputation` + `term=prosthetic` → 117 results
- **Analyses performed:** `countByStatus`, `countByCountry`, `countByPhase`, `countBySponsorType`
- **Fields extracted:** NCTId, BriefTitle, OverallStatus, Condition, Phase, StartDate

### OpenStreetMap Data
- **Geocoding:** OSM search for "Beckley, West Virginia", "Pikeville, Kentucky", "Greenville, Mississippi"
- **Region coordinates:**
  - Rural WV (Beckley): 37.78°N, 81.19°W
  - Eastern KY (Pikeville): 37.48°N, 82.52°W
  - Mississippi Delta (Greenville): 33.41°N, 91.06°W
- **Nearby-place searches:** 10–30 km radii, categories: amenity, health, medical
- **Hospital/provider lookups:** OSM geocode for hospitals and CPO facilities in each region
- **Proximity analysis date:** July 2026

## Key Metrics (July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic trials (broad search) | 155 |
| Limb-amputation prosthetic trials | 117 |
| Upper limb prosthetic trials | 88 |
| Lower limb prosthetic trials | 176 |
| Actively recruiting (limb amputation) | 26 (22.2%) |
| Completed (limb amputation) | 58 (49.6%) |
| Phase 3 trials (all prosthetics) | 4 (broad) / ~30 (global) |
| CPO providers within 30km (all 3 regions) | 0 |
| Nearest CPO distance | 130–200+ miles |

## Gap Analysis Summary

| Region | CPO 30km | Nearest CPO | Drive | Medicaid | Amputation Rate |
|--------|----------|-------------|-------|----------|----------------|
| WV (Beckley) | 0 | Charleston, WV | ~190 mi | Not expanded | High |
| KY (Pikeville) | 0 | Lexington, KY | ~130 mi | Limited | High |
| MS Delta (Greenville) | 0 | Memphis, TN | ~200 mi | Not expanded | Highest US |

## Limitations

1. **OSM data may be incomplete** in rural areas — some CPO providers may not appear in OpenStreetMap.
2. **ClinicalTrials.gov data reflects registered studies only** — unreported or private trials are excluded.
3. **Status classifications are self-reported** by sponsors; "UNKNOWN" status may indicate abandoned or poorly maintained records.
4. **Drive times are estimates** based on straight-line distances to nearest major cities.
5. **The three regions were selected** based on known rural/underserved characteristics; other underserved regions may exist.

## Tools Used

- ClinicalTrials.gov MCP Server (clinical trial data)
- OpenStreetMap MCP Server (geocoding, nearby places, routing)
- GitHub API (repository management and file publishing)

## License

MIT — open access for research, policy, and advocacy.
