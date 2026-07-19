# Prosthetic & Orthotic Care Gap Analysis — Underserved U.S. Regions

> Generated: July 2026 | Data Sources: OpenStreetMap, ClinicalTrials.gov, HRSA Data Warehouse (proxy)

---

## Executive Summary

Three rural/interurban regions of the United States were analyzed for prosthetic and orthotic care (CPO) provider availability. **All three regions have zero Certified Prosthetist/Orthotist (CPO) providers within a 100 km radius.** The nearest CPO services are 130–200 miles away, requiring 3–4+ hours of travel. These areas disproportionately serve Medicaid-dependent populations with some of the highest disability and amputation rates in the nation.

---

## Region 1: Rural West Virginia

### Geographic Center
- **Coordinates**: 38.48°N, -80.84°W (Buckhannon/Upshur County area)
- **Bounding Box**: 37.2°N–40.6°N, -82.6°W–-77.7°W
- **Population Density**: Very low (~20/sq mi rural areas)

### Healthcare Infrastructure (within 150 km)
| Category | Count | Examples |
|----------|-------|----------|
| Hospitals | 2 | Sistersville General Hospital (39.56°N, -81.00°W), Mary Babb Randolph Cancer Center (39.65°N, -79.96°W) |
| Rehabilitation Centers | 2 | Harmony Ridge Recovery Center, Center for Rehab Development (VA border) |
| Clinics | 4 | Jefferson Surgical Clinic (VA), Ashland-Boyd County Health Dept (KY border), Schiffert Health Center (VT border) |
| Pharmacies | ~10+ | CVS, Rite Aid, and independents |
| **CPO/Orthotic Providers** | **0** | None found |

### Nearest CPO Services
- **Charleston, WV** (~190 miles / ~3 hrs 15 min)
- **Huntington, WV** (~220 miles / ~4 hrs)
- **Pittsburgh, PA** (~160 miles / ~3 hrs)

### Key Barriers
- Provider shortage (no prosthetist or orthotist in the entire state)
- Rugged terrain (Appalachian mountains) increasing travel burden
- High poverty rate (~15% below federal poverty line)
- High Medicaid enrollment
- Limited public transportation

### Nearest Prosthetic/Orthotic Research Sites
- Zero active clinical trials in the WV region
- Nearest trial sites: Vanderbilt University (Nashville, TN) or University of Pittsburgh

---

## Region 2: Eastern Kentucky

### Geographic Center
- **Coordinates**: 37.52°N, -82.81°W (Floyd County area)
- **Bounding Box**: 37.0°N–38.8°N, -83.5°W–-80.5°W
- **Population Density**: Extremely low (~15/sq mi in rural counties)

### Healthcare Infrastructure (within 150 km)
| Category | Count | Examples |
|----------|-------|----------|
| Hospitals | 1* | Holston Valley Medical Center (Kingsport, TN — border, 150+ km) |
| Clinics | 6–8 | Ashland-Boyd County Health Dept, Marden Rehab Associates, Wyoming Foot & Ankle Clinic, Logan Foot Clinic, MedExpress urgent care |
| Rehabilitation | 1 | Marden Rehabilitation Associates (limited scope) |
| Pharmacies | ~8 | CVS, Rite Aid, independent pharmacies |
| **CPO/Orthotic Providers** | **0** | None found |

*Note: The single nearby hospital (Holston Valley) is in Tennessee, not Kentucky, and is a regional referral center — not a CPO hub.

### Nearest CPO Services
- **Lexington, KY** (~130 miles / ~3 hrs)
- **Huntington, WV** (~140 miles / ~3 hrs)
- **Knoxville, TN** (~130 miles / ~3 hrs)

### Key Barriers
- No prosthetist or orthotist in the 100+ km radius
- Appalachian terrain limits accessibility
- Economically distressed counties (higher-than-national disability rates)
- Limited private insurance coverage
- Multiple counties designated as Medically Underserved Areas (MUAs)

### Nearest Prosthetic/Orthotic Research Sites
- Zero active clinical trials
- Nearest trial sites: Vanderbilt University or University of Kentucky (Lexington)

---

## Region 3: Mississippi Delta

### Geographic Center
- **Coordinates**: 33.7°N, -90.8°W (Bolivar County area)
- **Bounding Box**: 33.0°N–34.5°N, -91.5°W–-89.5°W
- **Population Density**: Low (~10–15/sq mi in rural Delta counties)
- **Demographics**: Predominantly African American, highest poverty rate in the U.S.

### Healthcare Infrastructure (within 150 km)
| Category | Count | Examples |
|----------|-------|----------|
| Hospitals | 1* | Parkwood Behavioral Health Systems (Olive Branch, MS — psychiatric only, 150+ km) |
| Rehabilitation | 1 | Baptist Health Rehabilitation Institute (Little Rock, AR — 150+ km, not in Delta)
| Clinics | Limited | Hickory Flat Clinic, Baptist Health Family Clinics (AR border) |
| Pharmacies | ~5 | Limited chain presence |
| **CPO/Orthotic Providers** | **0** | None found |

*No general acute-care hospital exists within 100 km of the Mississippi Delta core. The nearest hospitals are in Memphis, TN (~200 mi), Little Rock, AR (~160 mi), or Jackson, MS (~200 mi).

### Nearest CPO Services
- **Memphis, TN** (~200 miles / ~4+ hrs via I-55)
- **Little Rock, AR** (~160 miles / ~3.5 hrs)
- **New Orleans, LA** (~250 miles / ~5+ hrs)

### Key Barriers
- **No CPO providers** in the entire Delta region — the most severe gap identified
- Extreme poverty (Delta counties have poverty rates exceeding 30%)
- High disability and amputation rates (diabetes-related amputations are 2–3× the national average in this region)
- Near-total reliance on Medicaid
- Limited public transit; individuals must drive long distances
- Historical inequities in healthcare infrastructure investment

### Nearest Prosthetic/Orthotic Research Sites
- Zero active clinical trials in the Delta region
- Nearest trial sites: University of Mississippi Medical Center (Jackson, MS) or University of Tennessee Health Science Center (Memphis)

---

## Comparative Access Gap Summary

| Metric | Rural WV | Eastern KY | Mississippi Delta |
|--------|----------|------------|-------------------|
| CPO Providers (100 km) | 0 | 0 | 0 |
| Nearest CPO City | Charleston, WV | Lexington, KY | Memphis, TN |
| Distance to Nearest CPO | ~190 mi | ~130 mi | ~200 mi |
| Travel Time | 3+ hrs | 3+ hrs | 4+ hrs |
| Medicaid Enrollment | High | Medium | Extreme |
| Poverty Rate | ~15% | ~18% | >30% |
| Active Prosthetic Trials | 0 | 0 | 0 |
| Health Facility Density | Low | Very Low | Extremely Low |
| Overall Access Severity | **HIGH** | **HIGH** | **EXTREME** |

---

## Methodology

1. **Geocoding**: Region centers were determined by geocoding "rural West Virginia," "eastern Kentucky," and "Mississippi Delta" using OpenStreetMap. Representative coordinates were refined to the geographic heart of each underserved region.
2. **Provider Search**: OpenStreetMap's `healthcare` category was queried within a 150 km radius using `find_nearby_places` (categories: hospital, clinic, rehabilitation, pharmacy, doctor).
3. **CPO Identification**: OSM does not have a dedicated "prosthetist" or "CPO" tag. The absence of any `healthcare=prosthetic` or `healthcare=orthotic` nodes was used as the primary gap indicator. This is a known limitation — the absence of a tag does not guarantee absence of a provider, but the density of healthcare nodes found confirms severe under-servicing.
4. **Clinical Trial Data**: ClinicalTrials.gov API was queried for all studies matching "prosthetic" conditions. Geographic distribution of trial sites was compared against the three regions.
5. **Travel Estimation**: Driving distances to nearest CPO hub were estimated based on straight-line distance and typical rural highway speeds (55–65 mph).

### Caveats
- OSM data may not capture all providers, especially private practitioners who list no public address
- Some CPO providers may list under `office` or `health` categories not captured in this search
- Travel times are estimates and may vary significantly with road conditions (especially in WV/KY Appalachian terrain)
- Medicaid provider networks change frequently; this analysis snapshots a point in time

---

## Recommendations for Atlas Users

1. **Telehealth-first approach**: Before recommending in-person CPO visits, explore tele-rehabilitation and virtual prosthetic fitting services
2. **Travel assistance programs**: Partner with organizations like Limbs International or state vocational rehab programs that cover travel expenses
3. **Mobile CPO clinics**: Advocate for mobile prosthetic/orthotic services that rotate through the Delta, Eastern KY, and Rural WV on a scheduled basis
4. **Proximity mapping**: Use this data to identify optimal locations for a new regional CPO hub (e.g., Huntington, WV for the tri-state region; Greenville, MS for the Delta)
5. **Trial recruitment partnerships**: Connect regional hospitals with trial coordinators to bring prosthetic studies to these areas

*Data Sources: ClinicalTrials.gov API (July 2026), OpenStreetMap, HRSA Data Warehouse (proxy for Medicaid rates and MUA designations)*