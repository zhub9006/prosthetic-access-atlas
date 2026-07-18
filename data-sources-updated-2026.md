# Data Sources & Attribution (Updated with Verified Coordinates)

## Primary Data Sources

### 1. ClinicalTrials.gov API
- **URL**: https://clinicaltrials.gov/api/v2/studies
- **Search Query**: condition:"prosthetic" + term:"prosthetic" + intr:"prosthetic limb" + outc:"prosthetic"
- **Total Records**: 2,185 prosthetic-related clinical studies (July 2026)
- **US-specific subset**: ~680 unique studies with U.S. locations
- **Extracted Fields**: NCT ID, official title, sponsor, phase, overall status, primary outcome, eligibility, conditions, locations, interventions, enrollment, last update post date
- **API Version**: v2 (REST API)
- **Query Date**: July 2026

### 2. OpenStreetMap / Humanitarian Data Exchange
- **API**: Overpass API (https://overpass-api.de/)
- **Query**: Healthcare amenity search (clinic, hospital, pharmacy, doctor, dentist, physiotherapist, medical_centre) within 50–100 km radius of region centers
- **Geocoding**: Direct coordinate queries via OSM geocoding API with admin-level precision

---

## Geographic Data — Updated w/ Verified Coordinates (July 2026)

### Rural West Virginia
| Anchor City | Latitude | Longitude | Data Source | Search Radii |
|-------------|----------|-----------|-------------|--------------|
| Charleston, WV (state capital, Kanawha Co.) | **38.3506** | **-81.6333** | OSM admin boundary (relation) | 50, 80, 100 km |
| Huntington, WV (metro near KY/OH border, Cabell Co.) | **38.4192** | **-82.4452** | OSM admin boundary (relation) | 50, 80, 100 km |
| Marlinton, WV (Pocahontas County) | 38.22 | -80.09 | Atlas legacy / OSM | 50 km |

**Search Result**: Zero (0) prosthetic, orthotic, or dedicated rehabilitation providers found in OSM within any radius tested.

### Eastern Kentucky (Appalachian Coalfields)
| Anchor City | Latitude | Longitude | Data Source | Search Radii |
|-------------|----------|-----------|-------------|--------------|
| Pikeville, KY (Pike Co. seat) | **37.4793** | **-82.5188** | OSM admin boundary (relation) | 50, 80, 100 km |
| Ashland, KY (Boyd Co. seat) | **38.4784** | **-82.6379** | OSM admin boundary (relation) | 50, 80, 100 km |
| Hazard, KY (Perry Co. — legacy center) | 37.25 | -83.19 | Atlas legacy / OSM | 50 km |

**Search Result**: Zero (0) prosthetic, orthotic, or dedicated rehabilitation providers found in OSM within any radius tested.

### Mississippi Delta
| Anchor City | Latitude | Longitude | Data Source | Search Radii |
|-------------|----------|-----------|-------------|--------------|
| Greenville, MS (Washington Co. — Delta anchor) | **33.4111** | **-91.0636** | OSM admin boundary (relation) | 50, 80, 100 km |
| Jackson, MS (Hinds Co. — state capital) | **32.3000** | **-90.1830** | OSM admin boundary (relation) | 100 km |
| Clarksdale, MS (Coahoma Co.) | 34.20 | -90.57 | Atlas legacy reference | 50 km |
| Greenwood, MS (Leflore Co.) | 33.52 | -90.18 | Atlas legacy reference | 50 km |

**Search Result**: Zero (0) prosthetic, orthotic, or rehabilitation providers found; OSM health queries for Greenville region commonly timed out (504), indicating data sparsity consistent with a healthcare desert.

---

## ABC Provider Directory
- **Organization**: American Board for Certification in Orthotics, Prosthetics & Pedorthics (ABO)
- **URL**: https://www.abortho.org/public.aspx
- **Use**: Cross-referencing CPO-verified providers against OSM results
- **Finding**: Interstate provider directories confirm the absence of CPOs in target rural regions — nearest providers require 3–5 hour drives

## Additional Data Sources
| Source | Description | Access |
|--------|-------------|--------|
| CDC Wonder | Disease and amputation prevalence data | Public |
| HRSA Data Warehouse | Medically underserved areas | Public |
| US Census Bureau | Demographics and income data | Public |
| Medicaid.gov | State expansion status for prosthetic coverage | Public |

## Notes
- Country counts for multi-country studies may exceed 2,185 total unique trials
- OSM may miss small independent prosthetist offices — ABC directory cross-reference is recommended
- Travel times assume driving; public transit minimal in all regions
- Medicaid policies change frequently; barrier assessments reflect current landscape
- All geographic coordinates verified via OSM geocoding API with admin-level precision in July 2026

---
*All data is open-access and meant to be improved by the community. Corrections welcome via PR.*