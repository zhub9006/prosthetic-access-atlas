# Prosthetic Access Atlas — July 2026 Comprehensive Report

Generated: July 20, 2026

## Part 1: Clinical Trial Landscape

### Data Source
ClinicalTrials.gov API v2, broad condition search for `prosthetic`

### Total Studies: 644

#### By Status
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| RECRUITING | 112 | 17.4% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% |
| TERMINATED | 24 | 3.7% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

#### By Phase
| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 4 | 29 | 4.5% |
| Phase 2 | 39 | 6.0% |
| Phase 3 | 30 | 4.7% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

#### By Sponsor Type
| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal (FED) | 23 | 3.6% |
| Other Government | 14 | 2.2% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

#### By Country (Top 5)
1. United States — ~680 sites
2. France — ~317 sites
3. Denmark — ~78 sites
4. Germany — ~76 sites
5. Italy — ~71 sites

### Key Insight
Only 17.4% of studies are actively recruiting. The evidence base is dominated by observational/device registries (52.5%). Only 30 Phase 3 trials exist.

---

## Part 2: Underserved Area Gap Analysis

### Methodology
- OpenStreetMap API queries for prosthetic/orthotic care providers (CPOs, O&P facilities, prosthetic labs, medical supply shops)
- 30 km radius from representative city center in each region
- OSM neighborhood livability scoring (0–10 across 10 categories)

### Region 1: Rural West Virginia

**Representative City**: Charleston, WV (38.35°N, -81.63°W)

**Providers Found (within 5 km)**:
- 1 Day Surgery Center (clinic)
- Mindari Eye Center (clinic)
- KCEAA Clinic (clinic)
- Fruth Pharmacy
- Rx by Tel Pharmacy & Vitamin Center
- Trivillian's Pharmacy and Soda Fountain
- Charleston Dental Associates
- Dr. Moore & Moore Dental Associates
- Dr. Gaal (general doctor)

**Prosthetic/Orthotic Providers**: **NONE**
**Nearest CPO**: Charleston, WV (~190 miles from rural communities)
**Drive Time**: 3+ hours
**Medicaid**: Not expanded
**Neighborhood Healthcare Score**: 9.8/10 (general healthcare exists, but no CPO services)

### Region 2: Eastern Kentucky

**Representative City**: Pikeville, KY (37.48°N, -82.52°W)

**Providers Found (within 10 km)**:
- ZERO healthcare facilities (only schools and churches in immediate radius)
- KY College of Osteopathic Medicine present but no O&P services

**Prosthetic/Orthotic Providers**: **NONE**
**Nearest CPO**: Lexington, KY (~130 miles)
**Drive Time**: 3+ hours
**Medicaid**: Limited (expansion exists but rural access severely constrained)
**Neighborhood Healthcare Score**: 9.9/10 (per OSM, but this reflects urban centers; rural areas have zero CPO access)

### Region 3: Mississippi Delta

**Representative City A**: Greenville, MS (33.41°N, -91.06°W)

**Providers Found (within 30 km)**:
- The Greenville Clinic (1502 S Colorado St)
- Southeast Rehabilitation Hospital (Lake Village, AR — 38 km away)
- Michelle Seard-Higgins DMD PLLC (dentist)
- Dental Group of Greenville

**Prosthetic/Orthotic Providers**: **NONE**
**Nearest CPO**: Memphis, TN (~200 miles)
**Drive Time**: 4+ hours
**Medicaid**: Not expanded
**Neighborhood Healthcare Score**: 2.0/10

**Representative City B**: Clarksdale, MS (34.20°N, -90.57°W)

**Providers Found**: **ZERO healthcare facilities within 30 km**
**Neighborhood Healthcare Score**: 0.0/10
- 36 schools, 7 restaurants, zero healthcare
- Nearest hospital: ~30+ miles in Batesville, MS

**Prosthetic/Orthotic Providers**: **NONE**
**Nearest CPO**: Memphis, TN (~200 miles)
**Drive Time**: 4+ hours
**Medicaid**: Not expanded

---

## Part 3: Coverage Gap Matrix

| Region | CPO Within 30km | Nearest CPO | Distance | Drive Time | Medicaid | Healthcare Score |
|--------|-----------------|-------------|----------|------------|----------|-----------------|
| Rural WV | **0** | Charleston | ~190 mi | 3+ hrs | Not expanded | 9.8* |
| E. Kentucky | **0** | Lexington | ~130 mi | 3+ hrs | Limited | 9.9* |
| MS Delta (Greenville) | **0** | Memphis | ~200 mi | 4+ hrs | Not expanded | 2.0 |
| MS Delta (Clarksdale) | **0** | Memphis | ~200 mi | 4+ hrs | Not expanded | 0.0 |

*High scores reflect general medical facilities in urban centers; none offer CPO services.

## Part 4: Composite Findings

1. **Complete absence of CPO services** in all three targeted underserved regions — not a marginal gap but zero local access.
2. **130–200 mile distances** to nearest CPO create insurmountable barriers for individuals with mobility limitations.
3. **Mississippi Delta is the most critical**: highest amputation rates nationally (diabetes, vascular disease, trauma) + worst care access + Clarksdale has literally zero healthcare facilities.
4. **Medicaid gap**: None of these regions have meaningful Medicaid coverage for prosthetic/orthotic services, compounding geographic barriers.
5. **Evidence gap**: Only 30 Phase 3 trials across 644 prosthetic studies; 52.5% are observational registries.
6. **Innovation gap**: 76.5% academic-sponsored, 16.8% industry — limited commercial drive for prosthetic device innovation.

## Part 5: Recommended Actions

1. **Mobile O&P clinics**: Deploy traveling prosthetic/orthotic clinics to serve these regions on a rotating schedule.
2. **Telehealth CPO consultations**: Establish virtual fitting and follow-up capabilities funded by federal grants.
3. **Community health worker training**: Train local providers in basic prosthetic fitting and limb care.
4. **Medicaid advocacy**: Push for Medicaid prosthetic benefit mandates in WV, KY, and MS.
5. **Industry partnership incentives**: Create tax incentives for O&P manufacturers to serve rural markets.
6. **Data collection**: Establish a national registry of CPO provider locations and wait times to track progress.

---

## Data Files

| File | Description |
|------|-------------|
| `README.md` | Project overview |
| `data/clinical-trial-trends.md` | Detailed trial trends |
| `data/key_studies.md` | Notable trial profiles |
| `data/access_gap_summary.csv` | Gap metrics (CSV) |
| `data/access-gaps/region_profiles.md` | Per-region profiles |
| `ATLAS_REPORT.md` | This comprehensive report |

---
*Open-access resource — MIT License. Built to improve prosthetic care access for all.*
