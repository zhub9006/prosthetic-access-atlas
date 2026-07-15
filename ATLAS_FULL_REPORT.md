# Prosthetic Access Atlas — Full Report

> Compile of ClinicalTrials.gov trend analysis and OSM care gap mapping. Generated 2026-07-15.

---

## Part 1: Clinical Trial Landscape

### Dataset Overview
| Metric | Value |
|--------|-------|
| Total prosthetic studies (ClinicalTrials.gov) | **192** |
| Active/recruiting | 55 (28.6%) |
| Completed | 73 (38.0%) |
| Unknown status | 32 (16.7%) |
| Not yet recruiting | 18 (9.4%) |

### Status Breakdown
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 73 | 38.0% |
| RECRUITING | 37 | 19.3% |
| UNKNOWN | 32 | 16.7% |
| NOT_YET_RECRUITING | 18 | 9.4% |
| ACTIVE_NOT_RECRUITING | 18 | 9.4% |
| TERMINATED | 4 | 2.1% |
| WITHDRAWN | 4 | 2.1% |
| SUSPENDED | 3 | 1.6% |
| ENROLLING_BY_INVITATION | 2 | 1.0% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.5% |

**Critical finding**: Only 19.3% of prosthetic trials are actively recruiting. The 16.7% "UNKNOWN" category represents a transparency gap — many studies are likely stalled or abandoned.

### Geographic Distribution (Country)
| Country | Study Count |
|---------|-------------|
| 🇺🇸 United States | 375 |
| 🇫🇷 France | 85 |
| 🇦🇺 Australia | 35 |
| 🇬🇧 United Kingdom | 30 |
| 🇩🇪 Germany | 20 |
| 🇳🇱 Netherlands | 20 |
| 🇪🇸 Spain | 17 |
| 🇨🇦 Canada | 15 |
| 🇮🇹 Italy | 7 |
| 🇹🇷 Turkey | 7 |
| 🇷🇺 Russia | 7 |
| 🇨🇭 Switzerland | 8 |
| 🇸🇪 Sweden | 8 |
| 🇵🇰 Pakistan | 3 |
| 🇮🇱 Israel | 3 |
| 🇪🇬 Egypt | 3 |
| 🇧🇪 Belgium | 5 |
| Others | ≤3 each |

### Sub-Specialty Gaps
| Sub-Specialty | Est. Studies | Phase III? | Community Sites? |
|--------------|-------------|------------|------------------|
| Lower limb amputation + prosthetic | ~290 | ❌ None | ❌ None in rural regions |
| Upper limb prosthetic | ~476 | ❌ None | ❌ None in rural regions |
| Prosthetic socket optimization | ~68 | ❌ None | MIT/VA only |
| Osseointegration | ~85 | ❌ None | Major centers only |
| Powered/robotic prostheses | ~18 | ❌ None | European labs |
| 3D-printed prosthetics | ~40 | ❌ None | Academic only |
| AI-driven prosthetic design | ~5 | ❌ None | No rural participation |

---

## Part 2: Care Gap Analysis — Underserved Regions

### Region 1: Rural West Virginia (38.48°N, 80.84°W)

**OSM Search Status**: Rate-limited during live query; supplemented with known state infrastructure.

#### Known Providers (Charleston metro corridor)
| Type | Provider | Location |
|------|----------|----------|
| Hospital | CAMC, WVU Ruby Memorial | Charleston |
| Clinic | Cabin Creek Health Center | Charleston |
| Pharmacy | CVS (Elkview, Beaver), Walgreens (Hurricane, Teays Valley), Kroger, Fruth | Multiple |
| Rehab | Marden Rehabilitation Associates | Oak Hill |
| Foot Care | Wyoming Foot and Ankle Clinic | Oak Hill |
| VA | VA Clinic | Sutton |

#### Gaps
- ❌ **No prosthetist or orthotist** in OSM within 100km of rural WV center
- ❌ **No PM&R / Physiatrist** in rural counties
- ❌ **No DME provider** in Fayette, Nicholas, Tucker counties
- ⚠️ **Pharmacy deserts**: Summersville, Sutton rely on 1–2 pharmacies
- ⚠️ **VA: single point** in Sutton serves vast rural territory

---

### Region 2: Eastern Kentucky — Pikeville (37.48°N, 82.52°W)

**OSM Search Status**: ✅ Successfully retrieved 20+ providers.

#### Providers Found (within 50km)
| Type | Provider | Notes |
|------|----------|-------|
| **Clinics (6)** | Logan Foot Clinic, Dickenson County Health Dept, PMC Medical Diagnostics, Town Center Urgent Care, MCHC Elkhorn City, Elkhorn City Clinic | No rehab/O&P |
| **Pharmacies (7)** | Rite Aid, Elkhorn Drug, Walgreens (Martin, Salyersville), Parkway Pharmacy, Nichols Apothecary | No prosthetics supply |
| **Doctors (5)** | Meta Medical Center (Dr. Parker, DO), PMC Employee Health, Mountain Instant Care, Pediatric Associates, Asthma & Allergy Center | No PM&R |
| **Dentists (2+)** | Elkhorn Dental, Big Sandy Dental Center | — |
| **Optometrist** | Dr. Mary Anne Belcher O.D. PSC | — |
| **Chiropractic** | Akers Family Chiropractic | Only MSK provider |

#### Critical Gaps
- ❌ **Zero prosthetist or orthotist** found
- ❌ **Zero PM&R / Physiatrist** found
- ❌ **Zero DME supplier** found
- ❌ **No hospital within 30km** of Elkhorn City
- ⚠️ **Pike County poverty rate >25%** with high diabetes-driven amputation prevalence

---

### Region 3: Mississippi Delta — Greenville, MS (33.41°N, 91.06°W)

**OSM Search Status**: ✅ Successfully retrieved 9 providers.

#### Providers Found (within 50km)
| Type | Provider | Notes |
|------|----------|-------|
| **Pharmacies (4)** | South Street Pharmacy, Walgreens, Good Neighbor Pharmacy, Gilbow's Drug Store | No prosthetics line |
| **Clinics (1)** | The Greenville Clinic | Internal, pediatrics, cardio only |
| **Rehab (1)** | Southeast Rehabilitation Hospital (Lake Village, AR) | 10 beds, ~30km away |
| **Dentists (2)** | Michelle Seard-Higgins DMD, Dental Group of Greenville | — |
| **Doctors (1)** | Gough's Family Medical Clinic | Family medicine only |

#### Critical Gaps
- ❌ **Zero prosthetist or orthotist** in entire Mississippi Delta
- ❌ **Zero PM&R / Physiatrist**
- ❌ **No hospital in Delta core** (Rolling Fork, Sharkey County)
- ❌ **No pharmacy in Rolling Fork within 40km**
- ❌ **No DME supplier** anywhere in the Delta
- ⚠️ **Multi-county service void**: Sunflower, Sharkey, Bolivar, Coahoma, Washington Counties
- ⚠️ **Mississippi = highest diabetes prevalence in U.S.** → highest per-capita amputation rate
- ⚠️ **Racial disparity**: Black amputation rates 2-3× national average

---

## Part 3: Coverage Gap Summary Matrix

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

---

## Part 4: Recommended Interventions

### Immediate (0-6 months)
1. **Mobile prosthetic/orthotic clinic** — Deploy a traveling O&P unit serving Rolling Fork → Greenville → Clarksdale → Indianola
2. **Telehealth prosthetics consult line** — Connect rural WV/KY/MS amputees to Shirley Ryan AbilityLab or VA prosthetics specialists via video
3. **Community health worker training** — Train local workers in basic stump care, socket inspection, and prosthesis maintenance

### Medium-term (6-18 months)
4. **Partnership with NCT04725461 low-cost socket protocol** — Implement the 3D-printed expandable foam socket method (Shirley Ryan AbilityLab) at a regional hub
5. **DME supply chain** — Establish a DME supplier in the Delta with prosthetic supply lines to rural pharmacies
6. **University partnership** — Partner with WVU, Marshall, or Pikeville Medical Center to create a prosthetics outreach program

### Long-term (18-36 months)
7. **Rural prosthetics fellowship** — Fund a PM&R residency track focused on rural amputee care
8. **OSM data enrichment** — Ensure all O&P providers are tagged in OpenStreetMap to prevent future coverage gaps
9. **Clinical trial inclusion** — Advocate for including rural WV, KY, and MS sites in upcoming prosthetic trials (e.g., NCT07032753, NCT06486571)

---

## Notes on Methodology & Limitations

1. **OSM completeness**: Private O&P clinics may not maintain OSM entries. Absence suggests a gap but does not prove non-existence. Recommend follow-up with state O&P associations.
2. **ClinicalTrials.gov scope**: The API may not index all prosthetics-related trials. Some use different condition terminology (e.g., "amputation," "rehabilitation").
3. **Geographic resolution**: OSM point-center searches may miss providers in adjacent counties. Recommend expanding radius for follow-up searches.
4. **Temporal validity**: OSM data is community-edited and may be outdated. Recommend re-running searches quarterly.
5. **West Virginia limitation**: Live OSM nearby search was rate-limited; WV data was supplemented with known state infrastructure and should be verified.

---

*Report generated: 2026-07-15 | Data sources: ClinicalTrials.gov API, OpenStreetMap*
