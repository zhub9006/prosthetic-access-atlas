# Mapped Care Providers & Gaps

## Geographic Coordinates & Nearby Providers

### Region 1: Rural West Virginia (Beckley, WV)
- **Center**: 37.7782°N, 81.1882°W
- **Providers Found**: 0
- **Nearest Hospital**: Raleigh General Hospital (est. ~5 km, unverified in OSM)
- **Nearest VA Prosthetic Center**: Louisburg, NC or Lexington, KY (both >150 km)
- **Nearest Academic O&P**: Washington University in St. Louis (>300 km)

### Region 2: Eastern Kentucky (Floyd County, KY)
- **Center**: 37.5170°N, 82.8060°W
- **Providers Found**: General healthcare (score 9.0), but no specialized O&P data
- **Nearest Possible Facilities**:
  - King's Daughters Medical Center, Ashland, KY (~30 km, 37.77, -82.60)
  - Regional facilities likely in Pikeville, Prestonsburg, or Williamson
- **Estimated Distance to Specialized O&P Lab**: 60–120 km

### Region 3: Mississippi Delta (Greenville, MS)
- **Center**: 33.4111°N, 91.0636°W
- **Providers Found**: 1 (Southeast Rehabilitation Hospital, Lake Village, AR)
  - **Address**: 905 Borgognoni Drive, Lake Village, AR 71653
  - **Phone**: +1 870 265 4333
  - **Type**: Rehabilitation hospital (10 beds)
  - **Distance**: 23.6 km
  - **Website**: https://atrp.ar.gov/places/southeast-rehabilitation-hospital
- **Nearest Comprehensive Amputee Centers**:
  - University of Mississippi Medical Center (Jackson, MS) — ~100 km
  - Regional Amputee Coalition services (Memphis, TN) — ~120 km

## Coverage Gap Visualization (Text-Based)

```
WEST VIRGINIA          KENTUCKY               MISSISSIPPI DELTA
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  ·  ·  ·  ·  │       │     ~O~      │       │     ····      │
│  ·  ·  ·  ·  │       │    ···       │       │     ····      │
│  ·  ·  ·H·  │       │   ···        │       │     ·····      │
│  ·  ·  · ·   │       │   ···        │       │     ····      │
│  JO Empty    │       │  (Some       │       │  No provider  │
│  (No care    │       │   exists)    │       │  in 30km      │
│   zones)     │       │              │       │               │
└──────────────┘       └──────────────┘       └──────────────┘
  0 providers             Sparse                 1 provider
  30km radius             30km radius            30km radius
```

## Awareness Gaps

1. **Veterans in rural WV**: Many WV veterans access VA prosthetic services via the Louisburg, NC VA or the Lexington, KY VA — but these are >150 km away. Rural terrain and weather make this nearly impossible for regular follow-ups.
2. **Underinsured in MS Delta**: Large uninsured population means even where providers exist, affordability is a secondary barrier.
3. **Appalachian stigma**: Mental health and disability stigma in rural Appalachia may prevent patients from seeking prosthetic services even when they exist.

## Data Limitations

- OpenStreetMap data may not capture all small private O&P practices
- Some providers may exist but not be tagged as prosthetic/orthotic specific
- Mobile/ traveling providers are typically not mapped
- Private for-profit O&P companies may have limited OSM presence

## Future Data Enrichment

- Cross-reference with American Board for Certification in Orthotics, Prosthetics & Pedorthics (ABC) directory
- Add VA prosthetic centers in proximity
- Layer in CMS supplier data for prosthetic providers
- Incorporate patient travel-time analysis using actual road network data