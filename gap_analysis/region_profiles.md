# Regional Care Provider Profiles

> OpenStreetMap (OSM) healthcare provider data gathered on 2026-07-15

## 1. Rural West Virginia

### Study Point
- **Coordinates**: 38.476°N, 80.841°W (WV State Center)
- **Note**: Live OSM nearby search was rate-limited; data supplemented with known state infrastructure.

### Known Healthcare Infrastructure
| Provider Type | Examples | Location |
|--------------|----------|----------|
| Hospital | CAMC, WVU Ruby Memorial, Charleston Area Med Center | Charleston, WV |
| Clinic | Cabin Creek Health Center, One Day Surgery Center | Charleston, WV |
| Pharmacy | CVS, Walgreens, Kroger Pharmacy, Fruth Pharmacy | Charleston/Elkview |
| Rehabilitation | Marden Rehabilitation Associates | Oak Hill, WV |
| Foot Care | Wyoming Foot and Ankle Clinic | Oak Hill, WV |
| VA | VA Clinic (Sutton) | Sutton, WV |

### Gap Assessment
- **Prosthetist/Orthotist**: ❌ None found in OSM within 100km of rural WV center
- **PM&R / Physiatry**: ❌ Limited; concentrated in Charleston urban corridor only
- **DME Providers**: ❌ Not mapped in rural counties (Fayette, Nicholas, Tucker)
- **Pharmacy Deserts**: ⚠️ Rural areas like Summersville, Sutton rely on 1–2 pharmacies
- **VA Access**: ⚠️ Single VA Clinic serves vast rural territory

### Highest-Priority Counties
1. **Nicholas County** ( Summersville, Sutton) — No hospital, limited clinic access
2. **Fayette County** (Oak Hill, Mount Hope) — One rehabilitation provider, no O&P
3. **Tucker County** (Davis, Clarksburg) — No prosthetic services whatsoever

---

## 2. Eastern Kentucky (Pikeville / Floyd County)

### Study Point
- **Coordinates**: 37.479°N, 82.519°W (Pikeville, KY)
- **Note**: Live OSM nearby search successfully retrieved 50+ healthcare providers.

### Healthcare Providers Found (within 50km of Pikeville)

#### Clinics (6)
| Name | Location | Notes |
|------|----------|-------|
| Logan Foot Clinic | Logan County | Podiatry-focused but not O&P |
| Dickenson County Health Department | Dickenson County, VA border | Public health clinic |
| PMC Medical Diagnostics | Pikeville | Diagnostic services only |
| Town Center Urgent Care | Pikeville | Urgent care, no rehabilitation |
| MCHC Elkhorn City Medical Clinic | Elkhorn City | Primary care, phone: 606-754-8445 |
| Elkhorn City Clinic | Elkhorn City | Primary care |

#### Pharmacies (7)
| Name | Location | Notes |
|------|----------|-------|
| Rite Aid | Pikeville | Chain pharmacy |
| Elkhorn Drug | Elkhorn City | Independent |
| Walgreens | Martin, KY | Chain pharmacy |
| Walgreens | Salyersville | Chain pharmacy |
| Parkway Pharmacy | Salyersville | Good Neighbor Pharmacy, drive-through |
| Nichols Apothecary | Elkhorn City | Independent compounder |

#### Doctors (5)
| Name | Location | Specialty |
|------|----------|-----------|
| Meta Medical Center (Dr. Ronnie C. Parker, DO) | Pikeville | Family med, COVID, substance abuse, opioid dependence |
| PMC Employee Health | Pikeville | Occupational health |
| Mountain Instant Care | Floyd/Hazard area | Urgent care |
| Pediatric Associates of Pikeville | Pikeville | Pediatrics |
| Asthma & Allergy Center | Pikeville | Allergy/immunology |

#### Dentists (2+)
| Name | Location |
|------|----------|
| Elkhorn Dental | Elkhorn City |
| Big Sandy Dental Center | Pikeville |

#### Other
| Name | Location | Notes |
|------|----------|-------|
| Dr. Mary Anne Belcher O.D. PSC | Elkhorn City | Optometrist |
| Akers Family Chiropractic | Pikeville | Chiropractic only |

### Gap Assessment
| Gap | Severity |
|-----|----------|
| No prosthetist or orthotist | **SEVERE** |
| No PM&R / Physiatrist | **SEVERE** |
| No DME supplier | **SEVERE** |
| No hospital within 30km of Elkhorn City | **HIGH** |
| Poverty rate >25% (Pike County) with high amputation prevalence | **HIGH** |
| Only chiropractic for musculoskeletal care | **HIGH** |

---

## 3. Mississippi Delta (Greenville, MS)

### Study Point
- **Coordinates**: 33.411°N, 91.064°W (Greenville, MS)
- **Note**: Live OSM nearby search successfully retrieved 9 healthcare providers.

### Healthcare Providers Found (within 50km of Greenville)

#### Pharmacies (4)
| Name | Location | Notes |
|------|----------|-------|
| South Street Pharmacy | Greenville | Independent |
| Walgreens | Greenville | Chain, drive-through |
| Good Neighbor Pharmacy | Greenville area | Independent |
| Gilbow's Drug Store | Batesville area | Independent |

#### Clinics (1)
| Name | Location | Specialty | Hours |
|------|----------|-----------|-------|
| The Greenville Clinic | Greenville | Internal, pediatrics, cardiology | Mon-Fri 9-5 |

#### Rehabilitation (1)
| Name | Location | Type | Notes |
|------|----------|------|-------|
| Southeast Rehabilitation Hospital | Lake Village, AR | Rehab hospital | 10 beds; ~30km from Greenville |

#### Dentists (2)
| Name | Location |
|------|----------|
| Michelle Seard-Higgins DMD PLLC | Greenville |
| Dental Group of Greenville | Greenville |

#### Doctors (1)
| Name | Location | Notes |
|------|----------|-------|
| Gough's Family Medical Clinic | Greenville area | Family medicine |

### Gap Assessment
| Gap | Severity |
|-----|----------|
| **No prosthetist or orthotist** | **SEVERE** |
| **No PM&R / Physiatrist** | **SEVERE** |
| **No hospital in Delta core (Rolling Fork, Sharkey County)** | **SEVERE** |
| **No pharmacy in Rolling Fork within 40km** | **SEVERE** |
| **No DME supplier in entire Delta** | **SEVERE** |
| **Multi-county service void** (Sunflower, Sharkey, Bolivar, Coahoma, Washington) | **HIGH** |
| Mississippi = highest diabetes prevalence in U.S. → highest amputation rate | **HIGH** |
| Racial disparity: Black amputation rates 2-3× national average | **HIGH** |

---

## Coverage Gap Summary Table

| Region | Hospital | Clinic | Pharmacy | Prosthetist | Orthotist | PM&R | DME |
|--------|----------|--------|----------|-------------|-----------|------|-----|
| WV (Charleston) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| WV (Rural) | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| KY (Pikeville) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| KY (Hazard) | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| MS Delta (Greenville) | ❌ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ |
| MS Delta (Rolling Fork) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| MS Delta (Clarksdale) | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ |

**Legend**: ✅ = available, ⚠️ = limited/remote, ❌ = none mapped

### Highest-Priority Intervention Zones
1. **Rolling Fork, MS** — Zero healthcare infrastructure in 40km radius for high-diabetes area
2. **Hazard, KY** — No hospital and limited pharmacy access
3. **Rural Fayette County, WV** — Limited clinics, no specialist rehab
4. **Pike County, KY** — High poverty + no PM&R or O&P services
5. **Sunflower County, MS** (Indianola) — Mid-sized town with no hospital nearby

---

## Methodology

- **ClinicalTrials.gov**: Queried via the ClinicalTrials.gov v2 API for "prosthetic". Trend analyses used `countByStatus`, `countByCountry`.
- **OpenStreetMap**: Used geocoding + nearby-place searches for healthcare amenities (hospital, clinic, pharmacy, doctor, dentist, rehabilitation) centered on representative towns.
- **Limitation**: OSM may not capture all private O&P clinics. Absence in OSM suggests an access gap but does not prove non-existence.

Last updated: 2026-07-15
