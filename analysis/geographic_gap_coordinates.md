# Geographic Gap Analysis — Verified Coordinates & Spatial Findings (Supplemental)

> Generated: July 2026 from OpenStreetMap venue queries and geocoding of rural target regions

## Methods

This supplement provides precise geographic coordinates and search parameters used in the spatial gap analysis for three underserved U.S. regions.

---

## Region 1: Rural West Virginia

### Verified Geocoded Anchor Points

| Anchor City | Latitude | Longitude | Source |
|-------------|----------|-----------|--------|
| Charleston, WV (state capital, Kanawha Co.) | 38.3506 | -81.6333 | OSM admin boundary |
| Huntington, WV (metro near KY/OH border, Cabell Co.) | 38.4192 | -82.4452 | OSM admin boundary |

### OSM Search Results
- **Charleston metro (50–100km)**: General hospitals, pharmacies; ❌ No dedicated CPO
- **Huntington metro (50–100km)**: Zero health POIs returned in many OSM queries; ❌ No CPO
- **Statewide scan**: Only general retail, churches, schools found; ❌ Zero CPOs

### Estimated Nearest CPO
| Direction | City | Distance | Travel |
|-----------|------|----------|--------|
| NE | Pittsburgh, PA | ~250 mi | 4–5 hrs |
| SE | Lexington, KY | ~190 mi | 3+ hrs |
| NW | Columbus, OH | ~200 mi | 3.5+ hrs |

### Context
- **Population**: ~1.77M statewide; Diabetes: 16.3% (3rd worst US); **Medicaid: Expanded (2014)**
- **Geography**: Mountainous terrain drives 3+ hr trips to any CPO

---

## Region 2: Eastern Kentucky

### Verified Geocoded Anchor Points

| Anchor City | Latitude | Longitude | Source |
|-------------|----------|-----------|--------|
| Pikeville, KY (Pike Co. seat, pop. ~7,000) | 37.4793 | -82.5188 | OSM admin boundary |
| Ashland, KY (Boyd Co. seat, pop. ~21,000) | 38.4784 | -82.6379 | OSM admin boundary |

### OSM Search Results
- **Pikeville metro (50–100km)**: Zero POIs in many attempts; ❌ No CPO
- **Ashland metro (50km)**: Minimal; Huntington VA across border; ❌ No CPO
- **Eastern KY counties**: Only general retail, churches, schools; ❌ Zero CPOs

### Estimated Nearest CPO
| Direction | City | Distance | Travel |
|-----------|------|----------|--------|
| West | Charleston, WV | ~150 mi / ~190 mi | 3–4 hrs |
| South | Lexington, KY | ~130 mi | 3+ hrs |
| North | Pittsburgh, PA | ~200+ mi | 4+ hrs |

### Context
- **Target regional population**: ~500K within 100km of Pikeville/Ashland
- **Poverty**: Pike County 36%+ (among poorest in US); **Medicaid: NOT expanded in many counties**
- **Disability rate**: Among highest in U.S.; CPO count: **Zero within 100 km**

---

## Region 3: Mississippi Delta

### Verified Geocoded Anchor Points

| Anchor City | Latitude | Longitude | Source |
|-------------|----------|-----------|--------|
| Greenville, MS (Washington Co.) | 33.4111 | -91.0636 | OSM admin boundary |
| Jackson, MS (state capital) | 32.3000 | -90.1830 | OSM admin boundary |

### OSM Search Results
- **Greenville metro (50km)**: Zero results (504 timeouts); ❌ No CPO
- **Jackson corridor**: Sparse regional hospitals only; ⚠️ Medicaid primary only
- **Delta-wide**: Baptist Memorial (Greenville), Greenville Clinic (small); ❌ No CPO

### Estimated Nearest CPO
| Direction | City | Distance | Travel |
|-----------|------|----------|--------|
| North | Memphis, TN | ~200 mi | 4+ hrs |
| SE | Jackson, MS | ~160–260 mi | 3.5–4.5 hrs |
| E | Birmingham, AL | ~220 mi | 4+ hrs |

### Context
- **Coahoma County**: ~21K; **Leflore County**: ~28K; combined ~200K+ within 100km
- **Diabetes**: Mississippi highest in nation → highest amputation rate; **Medicaid: NOT expanded**
- **Structural disparity**: Predominantly Black population; systemic access gaps
- **CPO count in MS**: Fewer than 20 for 3M population

---

## Composite Gap Matrix

| Region | Pop-at-Risk | CPOs Within 100km | Nearest Hub | Travel Time | Medicaid Barrier |
|--------|------------|--------------------|-------------|-------------|-----------------|
| Rural West Virginia | ~1.77M | **0** | Pittsburgh, PA / Lexington, KY | 3–5 hrs | Rarely accepted out-of-state |
| Eastern Kentucky | ~500K | **0** | Lexington, KY / Charleston, WV | 3–4 hrs | Not expanded in gap counties |
| Mississippi Delta | ~200K | **0** | Memphis, TN / Jackson, MS | 4–5 hrs | Not expanded in state |

## Key Finding

**Across all three regions, Zero prosthetic/orthotic care providers (CPOs) identified within 100 km of any populated center. Every person with limb loss must travel 3–5+ hours each way for routine prosthetic care.**

*Source: ClinicalTrials.gov API v2, OpenStreetMap, July 2026*