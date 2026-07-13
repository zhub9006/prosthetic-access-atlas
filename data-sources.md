# Data Sources & Methodology

## ClinicalTrials.gov Data

- **API**: ClinicalTrials.gov v2 (MCP server interface)
- **Query terms used**:
  - `prosthetic` (broad)
  - `upper limb prosthetic`
  - `lower limb prosthetic amputation`
  - `orthotic prosthetic rehabilitation`
  - `prosthetic socket fit`
  - `osseointegration prosthetic`
  - `prosthetic training rehabilitation amputee`
  - `bionic prosthesis upper limb`
  - `3D printed prosthetic`
  - `prosthesis rehabilitation`
  - `prosthetic rehabilitation amputee driving`
  - `microwave prosthesis`
- **Analyses performed**:
  - `countByStatus` — distribution across trial lifecycle stages
  - `countByPhase` — breakdown of trial phases (I–IV, NA, Unknown)
  - `countByCountry` — geographic distribution of trial locations
  - `countBySponsorType` — sponsor landscape (academic, industry, federal)
- **Individual study summaries** retrieved for 8 landmark trials
- **Retrieval date**: 2026-07-13

## OpenStreetMap (OSM) Healthcare Data

- **Geocoding**: Used OSM Nominatim geocoder to find coordinates for:
  - Rural West Virginia (Charleston, Beckley, Oak Hill, Clarksburg, Sutton, Summersville, WV State Center)
  - Eastern Kentucky (Pikeville, Hazard, Elkhorn City, Eastern KY)
  - Mississippi Delta (Greenville, Leland, Rolling Fork, Clarksdale, Cleveland, Indianola, Greenwood, Delta)
- **Nearby-place searches**: Queried `healthcare` category at each coordinate with radii of 30–60 km
- **Provider categories extracted**:
  - `hospital`
  - `clinic`
  - `doctors`
  - `pharmacy`
  - `optometrist`
  - `dentist`
  - `dialysis`
  - `alternative` (chiropractic)
- **Note on prosthetist/orthotist data**: OSM does not currently classify providers as `healthcare=prosthetist` or `healthcare=orthotist` in any of these regions. This absence is itself a finding.
- **OSM License**: PDDL (Open Database License)

## Gap Analysis Methodology

- Provider counts were aggregated by category and geographic region
- Coverage maps were generated using OSM administrative boundary and point-of-interest data
- Gap severity ratings:
  - **Severe**: Zero providers of any kind within 40 km
  - **High**: One or fewer providers of a critical specialty
  - **Moderate**: Limited or inconsistent access
  - **Low**: Adequate urban-standard access

## ClinicalTrials.gov API Limitations

- The `fields` parameter has strict naming requirements (e.g., `NCTId` not `nctId`, `BriefTitle` not `briefTitle`)
- Sort ordering requires specific string-based field/order pairs
- Some search queries return 400 errors if invalid field names are included
- The MCP server wraps the REST API and adds validation layers

## Known Limitations

1. **OSM completeness**: Not all healthcare providers are in OSM. Small private O&P clinics, VA prosthetics services, and university-based clinics may be missing.
2. **Clinical trial relevance**: Some "prosthetic" trials are dental/implant-related (e.g., peri-implant mucositis). We filtered these out in summary tables.
3. **Temporal snapshot**: Data reflects a single day (2026-07-13). Trial statuses and counts will change over time.
4. **Geographic resolution**: OSM searches are centered on town coordinates; some rural providers may be just outside the search radius.

## Recommended Updates

- Re-run ClinicalTrials.gov queries quarterly
- Refresh OSM searches after each major healthcare facility opening/closing dataset
- Cross-reference with HHS Health Resources & Services Administration (HRSA) Medically Underserved Area (MUA) designations
- Add NPI (National Provider Identifier) lookup for confirmed prosthetist/orthotist gaps

---

Last updated: 2026-07-13 | Repository: [prosthetic-access-atlas](https://github.com/zhub9006/prosthetic-access-atlas)