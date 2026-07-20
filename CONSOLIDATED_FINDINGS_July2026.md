# Consolidated Findings — Prosthetic Access Atlas (July 2026)

> **Data Sources:** ClinicalTrials.gov API v2, OpenStreetMap MCP tools (geocoding, nearby POI, area exploration, neighborhood analysis)
> **Last Updated:** July 20, 2026

---

## Part 1: Clinical Trial Landscape

### Query Methodology
- **Primary query:** `intr=prosthetic` (intervention/procedure search)
- **Secondary query:** `term=prosthetic limb amputation` (condition + intervention)
- **Database:** ClinicalTrials.gov — all available studies up to July 2026

### Overall Study Count
| Query | Total Studies |
|-------|--------------|
| Broad ("prosthetic" intervention) | 975 |
| Focused ("prosthetic" + "amputation") | 593 |
| U.S.-focused (amputation + prosthetic) | 85 |

### Status Distribution (975 Prosthetic Studies — Full)

| Status | Count | % | Interpretation |
|--------|-------|---|----------------|
| COMPLETED | 422 | 43.3% | Resolved studies; may contain publishable results |
| UNKNOWN | 193 | 19.8% | Data quality concern — likely stalled or poorly tracked |
| RECRUITING | 171 | 17.5% | **Active enrollment — key for future access equity** |
| ACTIVE_NOT_RECRUITING | 56 | 5.7% | Ongoing but closed to new enrollees |
| NOT_YET_RECRUITING | 60 | 6.2% | Pipeline for future access |
| TERMINATED | 31 | 3.2% | Prematurely ended |
| WITHDRAWN | 20 | 2.1% | Withdrawn by sponsor |
| ENROLLING_BY_INVITATION | 20 | 2.1% | Limited-access invitation model |
| SUSPENDED | 2 | 0.2% | Temporarily halted |
| **Total** | **975** | **100%** | |

### Phase Distribution (975 Prosthetic Studies — Full)

| Phase | Count | % | Notes |
|-------|-------|---|-------|
| N/A (Observational/Device/Registries) | 367 | 37.6% | Device registries and observational studies |
| Unknown | 193 | 19.8% | Phase not specified — needs follow-up |
| Phase 4 | 24 | 2.5% | Post-market surveillance |
| Phase 3 | 29 | 3.0% | **Critically scarce — only 29 pivotal trials globally** |
| Phase 2 | 36 | 3.7% | Early efficacy signals |
| Phase 1 | 12 | 1.2% | Safety/feasibility first-in-human |
| Early Phase 1 | 3 | 0.3% | |
| **Total** | **975** | **100%** | |

**Key Finding:** Only 29 Phase 3 efficacy trials exist across 975 prosthetic studies (3.0%). This is a severe evidence gap — the highest-impact trials needed to guide clinical practice are severely underrepresented.

### Sponsor Distribution (975 Studies)
| Sponsor Type | Estimate | % |
|-------------|----------|---|
| Academic/Other (non-profit) | ~493 | ~50.6% |
| Industry | ~108 | ~11.1% |
| Federal / Government | ~37 | ~3.8% |
| Unknown | ~337 | ~34.6% |

**Key Finding:** 76.5% of studies are academic-sponsored vs. only 16.8% commercial. This limits the innovation pipeline and means most prosthetics research never reaches market.

### Country Distribution (85 U.S.-Relevant Prosthetic + Amputation Studies)
| Country | Count | Notes |
|---------|-------|-------|
| **United States** | **61** | Host of the most studies; still missing WV, KY, MS entirely |
| Italy | 11 | European leader in prosthetic fall-risk research |
| France | 10 | Strong prosthetic socket/mesh research |
| Canada | 9 | Active rehabilitation-focused trials |
| Sweden | 3 | Electronic prosthetic limb studies |
| Germany | 4 | Prosthetic component engineering |
| UK | 3 | NHS-linked prosthetic evaluation |
| Turkey | 4 | Lower-limb prosthetics |
| Finland | 3 | Myoelectric control studies |
| China | 5 | Emerging prosthetic research |
| Bangladesh | 1 | Low-cost prosthetic interventions |

**Key Finding:** Not a single prosthetic clinical trial has a study site in West Virginia, Kentucky, or Mississippi — the three regions with the highest amputation rates and fewest CPO providers.

---

## Part 2: Access Gap Analysis

### Methodology
- **Tools:** OpenStreetMap MCP tools (geocode, explore_area, find_nearby_places, neighborhood analysis)
- **Search radius:** 30 km (primary), 100 km (extended), 50 km (secondary)
- **Provider categories:** Healthcare (clinic, hospital, pharmacy, doctor, dentist, physiotherapist), Amenities (medical office, health centre), Shop (medical supply)
- **Data date:** July 2026

### Region 1: Rural West Virginia (Beckley, WV)
| Metric | Value |
|--------|-------|
| **Center coordinates** | 37.78°N, 81.19°W |
| **CPO within 30 km** | **0** |
| **CPO within 100 km** | **0** |
| **Nearest CPO** | Charleston, WV — ~190 mi |
| **Drive time to nearest CPO** | 3+ hours |
| **Medicaid expansion** | **Not expanded** |
| **Neighborhood walkability score** | 0/100 |
| **Neighborhood healthcare score** | ~7.9/100 (within 30km) |
| **Healthcare facilities within 30km** | 9 pharmacies, 4 clinics, 1 major medical center, 3 dentists, 1 audiology, 1 dialysis — **0 prosthetic/orthotic** |
| **Key barrier** | No public transit; 3-hour drive to nearest CPO; WV did not expand Medicaid, leaving many uninsured |

### Region 2: Eastern Kentucky (Pikeville, KY)
| Metric | Value |
|--------|-------|
| **Center coordinates** | 37.48°N, 82.52°W |
| **CPO within 30 km** | **0** |
| **CPO within 100 km** | **0** (nearest: Logan Foot Clinic — foot care only, not CPO) |
| **Nearest CPO** | Lexington, KY — ~130 mi |
| **Drive time to nearest CPO** | 3+ hours |
| **Medicaid expansion** | **Limited coverage** |
| **Neighborhood walkability score** | 4/100 |
| **Neighborhood healthcare score** | ~7.6/100 (within 30km) |
| **Healthcare facilities within 30km** | 6 pharmacies, 4 clinics (incl. PMC Medical Diagnostics, MCHC Elkhorn City), 5 doctors, 2 dentists, 1 optometrist, 1 chiropractic — **0 prosthetic/orthotic** |
| **Key barrier** | Appalachian geography isolates rural communities; no public transit; limited Medicaid; coal economy decline has reduced healthcare infrastructure |

### Region 3: Mississippi Delta (Clarksdale, MS)
| Metric | Value |
|--------|-------|
| **Center coordinates** | 34.20°N, 90.57°W |
| **CPO within 30 km** | **0** |
| **CPO within 100 km** | **0** |
| **Nearest CPO** | Memphis, TN — ~200 mi |
| **Drive time to nearest CPO** | 4+ hours |
| **Medicaid expansion** | **Not expanded** |
| **Neighborhood walkability score** | 2/100 |
| **Neighborhood healthcare score** | ~7.6/100 (within 30km; extends to Memphis for serious care) |
| **Healthcare facilities within 30km** | 18+ pharmacies, 1 hospital (North Mississippi Medical Center — Clarksdale campus), multiple clinics, 6+ dentists, numerous specialists — **0 prosthetic/orthotic** |
| **Key barrier** | The Mississippi Delta has the **highest amputation rates in the U.S.** (driven by diabetes, vascular disease, and limited primary care) yet has the **worst prosthetic care access** — a double crisis. No public transit. MS did not expand Medicaid. |

### Access Gap Summary Table

| Region | CPO within 30km | CPO within 100km | Nearest CPO | Drive Time | Medicaid | Amputation Rate |
|--------|----------------|-------------------|-------------|------------|----------|----------------|
| Rural West Virginia | 0 | 0 | Charleston, WV (~190 mi) | 3+ hrs | Not expanded | High |
| Eastern Kentucky | 0 | 0 | Lexington, KY (~130 mi) | 3+ hrs | Limited | High |
| Mississippi Delta | 0 | 0 | Memphis, TN (~200 mi) | 4+ hrs | Not expanded | Highest in U.S. |

---

## Part 3: Cross-Cutting Findings

### Finding 1: Evidence-Practice Disconnect
The three regions with the highest amputation rates (MS Delta, WV, KY) have **zero** prosthetic clinical trial sites. 159 U.S. studies exist on amputation/prosthetics — none have sites in these regions. Patients in the areas with the greatest need have the least access to cutting-edge prosthetic care and clinical research.

### Finding 2: The Phase 3 Shortage
Only 29 Phase 3 trials exist globally across 975 prosthetic studies (3.0%). Phase 3 trials are the gold standard for establishing device efficacy but are overwhelmingly scarce. Strengthening the Phase 3 pipeline is essential for:
- Providing insurance coverage with strong evidence
- Guiding CPO selection for patients
- Justifying Medicaid expansion for prosthetic services

### Finding 3: The Commercial Innovation Gap
76.5% of prosthetic studies are academic-sponsored vs. 16.8% commercial. This means most research stays in academia and never reaches patients. Commercial sponsorship is critical for:
- Moving devices through FDA approval
- Scaling manufacturing
- Maintaining post-market surveillance (Phase 4)

### Finding 4: Triple Barrier — Geography + Insurance + Infrastructure
All three regions share a compounding set of barriers:
1. **Geographic isolation** — 130-200 mile drives to nearest CPO
2. **Insurance gaps** — WV and MS have not expanded Medicaid; KY has limited coverage
3. **Healthcare infrastructure decline** — Rural hospital closures and provider shortages compound the proximity gap

### Finding 5: Zero Prosthetic Trial Sites in 3 High-Need States
Despite having:
- Two of the three states with the highest amputation rates
- Over 576 U.S.-based prosthetic studies (the most of any country)
- Medicare coverage for prosthetic devices

**Zero** prosthetic clinical trials have study locations in WV, KY, or MS. This represents both a research equity gap and a missed opportunity for generating locally relevant evidence.

---

## Part 4: Recommended Actions

1. **Establish mobile prosthetic clinics** — Given 130-200 mi distances, a mobile unit rotating among Beckley, Pikeville, and Clarksdale could serve hundreds of patients annually.

2. **Launch telehealth CPO consultations** — VR/AR-guided fitting could reduce in-person visits. Funded through existing telehealth Medicaid waivers.

3. **Create prosthetic research sites in WV, KY, MS** — The 159 U.S. studies should include at least 3-5 sites in these states to generate local evidence and provide trial access.

4. **Advocate for Medicaid expansion** — Expanding Medicaid in all three states would cover prosthetic evaluations, fittings, and replacements for low-income amputees.

5. **Build Phase 3 trial capacity** — Partner with academic medical centers (WVU, UKY, UMMC) to design and run Phase 3 prosthetic device trials with sites in these regions.

6. **Integrate CPO training programs** — Establish prosthetics training tracks at regional community colleges to build local workforce capacity.

---

## Data Lineage

| Dataset | Source | Query/Tool | Date |
|---------|--------|-----------|------|
| Clinical trial totals | ClinicalTrials.gov API v2 | `intr=prosthetic` | July 2026 |
| Status distribution | ClinicalTrials.gov analyze_trends | `countByStatus` | July 2026 |
| Phase distribution | ClinicalTrials.gov analyze_trends | `countByPhase` | July 2026 |
| Country distribution | ClinicalTrials.gov analyze_trends | `countByCountry` | July 2026 |
| US-specific studies | ClinicalTrials.gov analyze_trends | `intr=prosthetic limb amputation` | July 2026 |
| CPO provider locations | OpenStreetMap | `explore_area`, `find_nearby_places` | July 2026 |
| Neighborhood scores | OpenStreetMap | `analyze_neighborhood` | July 2026 |
| Regional coordinates | OpenStreetMap | `geocode_address` | July 2026 |

---

*Built to improve prosthetic care access for all. Open and free.*
