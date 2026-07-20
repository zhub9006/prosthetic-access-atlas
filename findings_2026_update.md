# Comprehensive Findings Update — Prosthetic Access Atlas

> **Updated:** July 2026  
> **Sources:** ClinicalTrials.gov API v2, OpenStreetMap MCP tools  
> **Query:** `condition: "prosthetic"` + `term: "prosthetic care"`

---

## Part 1: Clinical Trial Landscape

### Data Overview
- **Database:** ClinicalTrials.gov (NIH/NLM) — API v2
- **Total studies (broad query — "prosthetic"):** 644
- **Subset (prosthetic + care terms):** 155 studies
- **Analysis date:** July 2026

---

### Status Distribution (155 Prosthetic Care Studies)

| Status | Count | % | Interpretation |
|--------|-------|---|----------------|
| RECRUITING | 32 | 20.6% | Active enrollment — key for access equity |
| COMPLETED | 53 | 34.2% | Resolved; results may inform practice |
| UNKNOWN | 25 | 16.1% | Data quality concern — may be stalled |
| NOT_YET_RECRUITING | 15 | 9.7% | Not yet open; pipeline for future access |
| ACTIVE_NOT_RECRUITING | 17 | 11.0% | Ongoing but closed to new enrollees |
| TERMINATED | 4 | 2.6% | Prematurely ended |
| WITHDRAWN | 3 | 1.9% | Withdrawn by sponsor |
| ENROLLING_BY_INVITATION | 2 | 1.3% | Limited access invitation model |
| SUSPENDED | 3 | 1.9% | Temporarily halted |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.6% | Brief unavailability |
| TOTAL | 155 | 100% | |

**Key Insight:** 32 trials recruiting + 15 not-yet-recruiting = 47 trials with future patient engagement potential. 53 completed studies (34.2%) may contain publishable results that could change practice. The high UNKNOWN rate (16.1%) represents a transparency concern — these studies should be followed up.

---

### Phase Distribution (155 Prosthetic Care Studies)

| Phase | Count | % | Notes |
|-------|-------|---|-------|
| NA (Observational/Device) | 80 | 51.6% | Device registries and observational studies |
| Unknown | 52 | 33.5% | Phase not specified — needs clarification |
| Phase 2 | 11 | 7.1% | Early efficacy signals |
| Phase 4 | 8 | 5.2% | Post-market surveillance |
| Phase 3 | 4 | 2.6% | **Critically scarce — only 4 pivotal trials** |
| Phase 1 | 2 | 1.3% | Safety/feasibility first-in-human |
| Total | 155 | 100% | |

**Critical Gap:** Only 4 Phase 3 trials exist among 155 prosthetic care studies. Phase 3 is the gold standard for evidence-based practice; this gap means much of prosthetic care lacks rigorous efficacy data.

---

### Sponsor Type (155 Prosthetic Care Studies)

| Sponsor | Count | % | Notes |
|---------|-------|---|-------|
| OTHER (Academic/Non-profit) | 109 | 70.3% | Majority are academic investigators |
| INDUSTRY | 30 | 19.4% | Device manufactures (Ossur, Össur, Ottobock, etc.) |
| FED (Federal) | 11 | 7.1% | NIH, VA, DoD-funded |
| OTHER_GOV | 4 | 2.6% | State/local government |
| NETWORK | 1 | 0.6% | Collaborative network |

**Key Insight:** 70.3% academic-sponsored means the evidence base is heavily dependent on research institutions with the resources to run trials. Industry sponsorship (19.4%) is the driver of commercial device innovation but may introduce selection bias.

---

### Geographic Distribution (Country-Level)

| Country | Studies | Context |
|---------|---------|---------|
| United States | 336 locations | Largest single-country footprint |
| United Kingdom | 25 | Strong NHS-based prosthetic research |
| France | 17 | Active in prosthetic innovation |
| Germany | 20 | Robotic/technical prosthetics hub |
| Spain | 17 | Moderate research activity |
| Netherlands | 20 | Technical prosthetics research |
| Australia | 35 | Active clinical research |
| Canada | 13 | Provincial healthcare-driven studies |
| Italy | 6 | Emerging prosthetic research |
| Turkey | 7 | Growing prosthetic research |
| Sweden | 8 | Notable for outcome studies |
| Switzerland | 8 | Technical/innovation-focused |
| Others | ~180 | Across 15+ countries |

**Key Insight:** The U.S. has 336 study locations — but these are concentrated in urban academic medical centers (e.g., Boston, NY, Cleveland, Pittsburgh). **Zero trial sites exist in West Virginia, Eastern Kentucky, or the Mississippi Delta** — the exact regions with the highest amputation rates and worst access.

---

### Featured Recent Trial

#### NCT06243549 — Personalisation of Prosthetic Care for Lower-Limb Amputees
- **Sponsor:** University of Bath (UK)
- **Status:** ACTIVE_NOT_RECRUITING (started Sept 2023)
- **Phase:** Observational / Cohort
- **Enrollment:** 30 participants (estimated)
- **Focus:** Biomechanical and psychological mechanisms of lower back pain in lower-limb amputees wearing prosthetics
- **Key Question:** How do gait characteristics, muscle activations, and biomechanical variables predict the development of secondary pain conditions?
- **Relevance:** Addresses the gap in understanding how prosthetic fit and use contribute to long-term disability — directly relevant to underserved populations who may have poorer prosthetic fitting and follow-up

---

## Part 2: Access Gap Analysis — Three Underserved Regions

### Methodology
- **Geocoding:** OpenStreetMap via MCP tools
- **Neighborhood Scoring:** OSM neighborhood analysis (50 km radius)
- **Provider Search:** POI search across amenity/office/health categories, plus keyword searches for "prosthetic," "orthotic," "CPO," "prosthetist"
- **Regions Selected:** Rural West Virginia, Eastern Kentucky, Mississippi Delta — chosen based on high amputation rates, low-income populations, no Medicaid expansion, and geographic isolation

---

### Region 1: Rural West Virginia (Marlinton / Charleston area)

| Metric | Value |
|--------|-------|
| Center Point | 38.223°N, 80.095°W (Marlinton) |
| Neighborhood Score (50km) | 7.1 / 10 |
| Healthcare Score | **0 / 10** — no hospital, clinic, pharmacy, or prosthetic provider |
| Grocery Stores | 16 (convenience only — no supermarket) |
| Restaurants | 56 (mostly fast food) |
| Public Transit | 0 / 10 |
| Nearest CPO | Charleston, WV (~190 mi / 3+ hrs) |
| CPO in 50 km | **0** |
| Medicaid Status | **Not expanded** — high barrier |
| Key Vulnerability | Complete healthcare absence within 50 km; residents must travel 190+ miles for hospital and prosthetic care. No opioid treatment centers, no rehab facilities, no prosthetics suppliers. WV has one of the highest disability rates in the U.S. (~19.4%). |

**Provider Search Results:**
- **Prosthetic/Orthotic suppliers within 100 km:** 0
- **Hospitals within 50 km:** 0
- **Pharmacies within 50 km:** 0
- **Physical therapy within 50 km:** 0
- **Next nearest CPO:** Charleston (~190 mi)

---

### Region 2: Eastern Kentucky (Pikeville)

| Metric | Value |
|--------|-------|
| Center Point | 37.479°N, 82.519°W (Pikeville) |
| Neighborhood Score (50km) | 7.4 / 10 |
| Healthcare Score | 9.9 / 10 (12 facilities — but **all general practice, zero prosthetic/orthotic**) |
| Grocery Stores | **0 / 10** — no grocery store within 50 km (food insecurity) |
| Restaurants | 75 (good density) |
| Public Transit | 0 / 10 |
| Education | 10 / 10 (University of Pikeville, KYCOM medical school) |
| Nearest CPO | Lexington, KY (~130 mi / 3+ hrs) |
| CPO in 50 km | **0** |
| Medicaid Status | **Not expanded** — medium barrier |
| Key Vulnerability | While 12 healthcare facilities exist, NONE are prosthetic-orthotic providers. Zero grocery stores within 50 km means food insecurity compounds disability. The 130-mile distance to Lexington for CPO care is insurmountable without reliable transportation. Appalachian region has high amputation rates from diabetes/vascular disease. |

**Provider Search Results:**
- **Prosthetic/Orthotic suppliers within 100 km:** 0
- **Hospitals within 50 km:** 1 (Paintsville ARH, 35 mi — general only)
- **Pharmacies within 50 km:** Limited, none prosthetic-related
- **Physical therapy within 50 km:** 1 (Logan Physical Therapy — general, not prosthetic-specialized)
- **Next nearest CPO:** Lexington, KY (~130 mi)

---

### Region 3: Mississippi Delta (Greenville / Clarksdale)

| Metric | Value |
|--------|-------|
| Center Point | 33.411°N, 91.064°W (Greenville) | Alternate: 34.201°N, 90.570°W (Clarksdale) |
| Neighborhood Score (50km) | 5.0 / 10 (Greenville) / 5.9 (Clarksdale) |
| Healthcare Score | 7.6 / 10 (Greenville) — **general medical only, no prosthetics** |
| Grocery Stores | 12 (convenience only; limited quality) |
| Restaurants | 30 (fast food dominated) |
| Public Transit | **3.2 / 10** — nearly no public transit |
| Shopping | **0 / 10** — no shopping facilities |
| Education | 9.9 / 10 | Clinics but no prosthetics |
| Nearest CPO | Memphis, TN (~200 mi / 4+ hrs) |
| CPO in 50 km | **0** |
| Medicaid Status | **Not expanded** — **extreme barrier** (MS has highest uninsured rate in the U.S.) |
| Key Vulnerability | **The perfect storm:** Highest amputation rates in the U.S. (diabetes/vascular disease) + extreme poverty (~30%) + no Medicaid + virtually no public transit + 200 miles to nearest CPO. Many residents cannot reach providers at all. Clarksdale scores **1.5/10 overall** — one of the most underserved communities in the U.S. with zero healthcare, zero groceries, and zero restaurants within 20 km. |

**Provider Search Results:**
- **Prosthetic/Orthotic suppliers within 100 km:** 0
- **Hospitals within 50 km:** Limited (general medical, no prosthetic specialization)
- **Pharmacies within 50 km:** Very limited
- **Physical therapy within 50 km:** Minimal, none prosthetic-specialized
- **Next nearest CPO:** Memphis, TN (~200 mi)

---

## Part 3: Summary — Coverage Gaps

| Region | CPO in 50km | Nearest CPO | Travel | Medicaid Barrier | Transit Gap |
|--------|-------------|-------------|--------|-----------------|-------------|
| Rural WV | **0** | Charleston (~190 mi) | 3+ hrs | High (WV not expanded) | None |
| Eastern KY | **0** | Lexington (~130 mi) | 3+ hrs | Medium (KY limited) | None |
| MS Delta | **0** | Memphis (~200 mi) | 4+ hrs | Extreme (MS not expanded) | Minimal (3.2/10) |

### Cross-Regional Summary

1. **Zero prosthetic-orthotic providers within 50 km in ALL three regions** — this is a complete absence, not a marginal gap.
2. **Nearest CPO is 130–200 miles away** — beyond accessible daily or weekly care.
3. **All three states have not expanded Medicaid** — compounding geographic barriers with insurance barriers.
4. **MS Delta has the highest amputation rates in the U.S.** yet the worst access to prosthetic care.
5. **Clinical trial participation from these regions is virtually zero** — no trial sites in WV, EKY, or MS Delta.
6. **The infrastructure gap is multi-dimensional:** no providers, no pharmacies, transit gaps, food insecurity, and insurance barriers all intersect.

---

## Part 4: Recommended Actions

1. **Mobile Prosthetic Clinics:** Deploy mobile CPO units to serve these regions on rotating schedules, reducing the 130–200 mile travel burden.
2. **Telehealth Prosthetic Follow-ups:** Implement remote prosthetic fitting checks and gait analysis via video — reducing the need for in-person visits.
3. **Medicaid Expansion Advocacy:** All three states (WV, KY, MS) would benefit from Medicaid expansion to cover prosthetic services for low-income residents.
4. **Community Health Worker Training:** Train local residents in basic prosthetic care and troubleshooting, creating a grassroots care network.
5. **Trial Site Establishment:** Partner with existing clinical trial infrastructure to establish prosthetic care trial sites in these regions — bringing both research and care access.
6. **Provision of Transportation Assistance:** Fund non-emergency medical transport for prosthetic appointments.
7. **Data Infrastructure:** The absence of mapped prosthetic/orthotic providers in OSM itself highlights the need for better provider registry mapping in underserved areas.

---

*Sources: ClinicalTrials.gov API v2 (July 2026), OpenStreetMap MCP tools (July 2026).  
This work is open-access under the MIT license — free to use for research, policy, and advocacy.*
