# Prosthetic & Orthotic Care Coverage Gap Map

## Visual Gap Representation

```
RURAL WEST VIRGINIA          EASTERN KENTUCKY             MISSISSIPPI DELTA
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │         │                 │
│   No O&P        │         │   No O&P        │         │   No O&P        │
│   providers     │         │   providers     │         │   providers     │
│   within 30km   │         │   within 30km   │         │   within 30km   │
│                 │         │                 │         │                 │
│   ─ ─ 90km to ─│         │  ─ 120km to ── │         │ ─ 130km to ─── │
│   Charleston    │         │   Lexington     │         │   Memphis       │
│   (WV)          │         │   (KY)          │         │   (TN)          │
└─────────────────┘         └─────────────────┘         └─────────────────┘
  Walkability: 2/10           Walkability: 2/10           Walkability: 2/10
  Healthcare: 9.0*           Healthcare: 0.0 🔴          Healthcare: 2.1 🔴
  *general healthcare only — zero O&P/orthotics
```

## Gap Severity Index

| Region | O&P Providers (30km) | Pop. Est. | Amputation Rate | Healthcare Score | Gap Severity | Nearest O&P |
|--------|---------------------|-----------|-----------------|-----------------|-------------|-------------|
| Rural WV | 0 | ~150,000 | High (vascular) | 9.0 (general) | 🔴 CRITICAL | Charleston (~90km) |
| Eastern KY | 0 | ~120,000 | High (opioid/diabetes) | 0.0 🔴 | 🔴 CRITICAL | Lexington (~120km) |
| Mississippi Delta | 0 | ~200,000 | Very High (diabetes) | 2.1 🔴 | 🔴 CRITICAL | Memphis (~130km) |

## Travel Distance to Nearest Prosthetic Care

```
Czech crescent: 30km ──┐
                       ├── 60km ──┐
                       │          ├── 90km ──┐
                       │          │          ├── 120km ──┐
                       │          │          │          ├── 130km ──┐
                       │          │          │          │          └── 160km
Rural WV ───────► Charleston (90km)
Eastern KY ──────► Lexington (120km)
Mississippi Delta ─► Memphis (130km)
```

## Clinical Trial Access by Region

| Region | Prosthetic Trials | Nearest Trial Site | Travel Distance |
|--------|------------------|-------------------|-----------------|
| Rural WV | 0 | N/A | Unreachable |
| Eastern KY | 0 | U of Louisville (NCT05440032) | ~120km |
| Mississippi Delta | 0 | U of Mississippi Medical Center (NCT02540681) | ~160km |

## Additional At-Risk Corridors (Preliminary)

Based on the same methodology, the following regions likely have similar or worse gaps:
- **Appalachian Ohio** (Athens, Marietta, Chillicothe)
- **Rural Arkansas** (Jonesboro, Pocahontas, Retrieved)
- **Deep South** (Selma, AL; Lufkin, TX; Pine Bluff, AR)
- **Navajo Nation** (Shiprock, Window Rock, AZ)
- **Black Hills region** (Pine Ridge, SD; Rapid City outskirts)

## Data Sources & Limitations

### Primary Sources
- **ClinicalTrials.gov API** — prosthetic condition search, status/country aggregations, detailed trial records
- **OpenStreetMap** — provider location data via MCP tools (geocode, find_nearby_places, search_category, analyze_neighborhood)

### Limitations
1. **OSM data may be incomplete** — smaller O&P businesses may not be mapped
2. **30km radius is a starting point** — in truly rural areas, the nearest O&P may be 60-100+ km away but still the "closest" option
3. **ClinicalTrials.gov only reflects registered studies** — unregistered or industry-only trials may be missed
4. **Neighborhood scores are algorithmic** — real-world access may differ
5. **OSM categories may not capture O&P** — prosthetists/orthotists may be under "shop" or "healthcare" or not mapped at all

### Recommended Cross-References
1. **ABC Directory** (American Board for Certification in Orthotics, Prosthetics & Pedorthics)
2. **NAAO+P** (National Association for the Advancement of Orthotics and Prosthetics)
3. **CMS Medicare O&P Supplier Locator**
4. **State occupational therapy and prosthetics boards**
5. **Hanger Clinic / Össur / Ottobock / Fairride / Clarkson** — major provider networks

## Next Steps
1. ✅ Complete ClinicalTrials.gov data collection and analysis
2. ✅ Map three initial target regions
3. ⬜ Validate OSM provider data with phone calls/ABC directory
4. ⬜ Expand to additional at-risk corridors
5. ⬜ Add interactive Leaflet.js map with plotted provider locations and coverage polygons
6. ⬜ Integrate HCUP/Medicare amputee incidence by county
7. ⬜ Add travel-time isochrone calculations
8. ⬜ Track grant funding and trial enrollment by region