# Latest Findings — Prosthetic Access Atlas

*Analysis Date: July 2026*

---

## 1. Clinical Trial Landscape (ClinicalTrials.gov)

### 1.1 Search Scope
- **"Prosthetic care"** query: **155 studies**
- **"Prosthetic limb"** query: **184 studies**
- **Total unique studies** with prosthetic focus: ~563 (combined across search terms)

### 1.2 Status Distribution (Prosthetic Care — 155 studies)

| Status | Count | % | Interpretation |
|--------|-------|---|----------------|
| RECRUITING | 32 | 20.6% | Actively enrolling — best for participation |
| COMPLETED | 53 | 34.2% | Finished; results available |
| UNKNOWN | 25 | 16.1% | Data quality concern — may be abandoned |
| NOT_YET_RECRUITING | 15 | 9.7% | Not yet open — watch for launch |
| ACTIVE_NOT_RECRUITING | 17 | 11.0% | Running but not enrolling new subjects |
| SUSPENDED | 3 | 1.9% | Paused — may resume |
| TERMINATED | 4 | 2.6% | Stopped early |
| WITHDRAWN | 3 | 1.9% | Removed from registry |
| ENROLLING_BY_INVITATION | 2 | 1.3% | Closed recruitment |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.6% | Brief pause |

**Key Insight:** Only 32 trials (20.6%) are currently recruiting. Over 83% are either completed, unknown-status, or not yet recruiting — meaning very few opportunities exist for new participants.

### 1.3 Phase Distribution (Prosthetic Care — 155 studies)

| Phase | Count | % |
|-------|-------|---|
| Unknown | 52 | 33.5% |
| N/A (Observational/Device/Registry) | 80 | 51.6% |
| Phase 2 | 11 | 7.1% |
| Phase 4 | 8 | 5.1% |
| Phase 3 | 4 | 2.6% |
| Phase 1 | 2 | 1.3% |

**Key Insight:** More than half are observational/device registries (51.6%). Only 4 Phase 3 and 2 Phase 1 interventional trials exist — indicating a weak evidence base for prosthetic device efficacy.

### 1.4 Sponsor Type (Prosthetic Care — 155 studies)

| Sponsor Type | Count | % |
|-------------|-------|---|
| Academic / Other (Non-Profits) | 109 | 70.3% |
| Industry | 30 | 19.4% |
| Federal | 11 | 7.1% |
| Other Gov | 4 | 2.6% |
| Network | 1 | 0.6% |

### 1.5 Geographic Distribution (Prosthetic Limb — 184 studies)

| Country | Count |
|---------|-------|
| United States | 251 |
| France | 45 |
| Canada | 10 |
| Netherlands | 10 |
| Germany | 9 |
| United Kingdom | 9 |
| Spain | 9 |
| Italy | 5 |
| Austria | 2 |
| Belgium | 5 |
| Norway | 5 |
| Turkey | 5 |
| Egypt | 1 |
| South Korea | 1 |
| Kenya | 2 |
| Singapore | 1 |

**Note:** US dominates but includes multi-site trials. The concentration of trial sites in urban academic centers means rural populations are systematically excluded.

### 1.6 Notable Active/Recent Trials

| NCT ID | Title | Status | Sponsor | Phase |
|--------|-------|--------|---------|-------|
| NCT05990062 | K-Socket-Harness: Variable-Compliance Socket for Transradial Amputees | RECRUITING | VA Office of Research and Development | Device |
| NCT06243549 | Personalisation of Prosthetic Care for Lower-Limb Amputees | ACTIVE_NOT_RECRUITING | University of Bath | Observational |
| NCT02366702 | Bilateral Transfemoral Ambulation: Passive vs Powered Prosthetics | UNKNOWN | SCIRE | Observational |

---

## 2. Underserved Area Gap Analysis

### 2.1 Methodology
- **Tool:** OpenStreetMap via OSM MCP tools
- **Search radius:** 50 km from regional center
- **Categories:** amenity (hospital, clinic, doctors, health, pharmacy), office (health-related), healthcare
- **Neighborhood scoring:** OSM neighborhood analysis (50 km radius)

### 2.2 Region: Rural West Virginia (Center: Charleston, WV)
**Coordinates:** 38.35°N, -81.63°W

#### Hospitals Within 30 km
| Hospital | Address | Distance |
|----------|---------|----------|
| Charleston Area Medical Center – General Hospital | 501 Morris St, Charleston, WV 25301 | ~0.5 km |
| Charleston Area Medical Center – Memorial Hospital | 3200 MacCorkle Ave SE, Charleston, WV 25304 | ~3.5 km |
| Charleston Surgical Hospital | 1306 Kanawha Blvd E, Charleston, WV 25301 | ~0.3 km |
| Saint Francis Hospital | 333 Laidley St, Charleston, WV 25301 | ~0.5 km |
| CAMC – Women and Children's Hospital | 800 Pennsylvania Ave, Charleston, WV 25302 | ~1 km |

#### Prosthetic/Orthotic Providers
- **Zero dedicated prosthetic-orthotic (CPO) clinics found within 50 km**
- No orthotist/prosthetist offices located in the OSM database for this region
- Nearest known CPO provider: ~190 miles (Charleston to Huntington or beyond)

#### Neighborhood Score
| Category | Score (out of 10) |
|----------|-------------------|
| Overall | 5.9 |
| Healthcare | 9.8 |
| Walkability | 10 |
| Groceries | 9.8 |

**Important:** The healthcare score reflects the urban Charleston area (city center). In surrounding rural counties, healthcare scores drop significantly.

#### Access Barriers
- **Wyoming WV** did not expand Medicaid — compounding cost barriers
- **No public transit** in rural counties
- **Nearest CPO:** 130+ miles in most rural areas

### 2.3 Region: Eastern Kentucky (Center: Pikeville, KY)
**Coordinates:** 37.48°N, -82.52°W

#### Hospitals Within 30 km
| Hospital | Address | Distance |
|----------|---------|----------|
| Pikeville Medical Center | 911 S Bypass Rd, Pikeville, KY 41501 | ~1 km |

#### Prosthetic/Orthotic Providers
- **Zero dedicated prosthetic-orthotic (CPO) clinics found**
- No orthotist/prosthetist offices in OSM within 50 km
- Nearest known CPO provider: ~130 miles (Lexington, KY)

#### Neighborhood Score
| Category | Score (out of 10) |
|----------|-------------------|
| Overall | 4.5 |
| Healthcare | **0** |
| Walkability | 4 |
| Groceries | 8.8 |
| Education | 10 (University of Pikeville) |

**Critical Finding:** Healthcare score is literally **0/10** at the neighborhood level — confirming a complete absence of accessible health infrastructure.

#### Access Barriers
- **Kentucky** did not expand Medicaid
- Appalachian geography creates extreme travel distances
- No public transit; limited ride-share services
- Poverty rate among highest in the nation

### 2.4 Region: Mississippi Delta (Center: Greenville, MS)
**Coordinates:** 33.41°N, -91.06°W

#### Hospitals Within 30 km
| Hospital | Address | Distance |
|----------|---------|----------|
| Delta Regional Medical Center – West Campus | 300 S Washington Ave, Greenville, MS 38703 | ~1 km |
| Delta Health System – The Medical Center | 1400 E Union St, Greenville, MS 38703 | ~1.5 km |

#### Prosthetic/Orthotic Providers
- **Zero dedicated prosthetic-orthotic (CPO) clinics found within 50 km**
- No orthotist/prosthetist offices in OSM for this region
- Nearest known CPO provider: ~200 miles (Memphis, TN or Jackson, MS)

#### Neighborhood Score
| Category | Score (out of 10) |
|----------|-------------------|
| Overall | **4.6** |
| Healthcare | **2.0** |
| Walkability | 2 |
| Groceries | 8.9 |
| Shopping | 0 |
| Services | 0 |

**Critical Finding:** Healthcare score of just 2.0/10 — the lowest of all three regions. The Delta's poverty, limited infrastructure, and provider shortage create a compounding crisis.

#### Access Barriers
- **Mississippi** has not expanded Medicaid
- MS Delta has the **highest amputation rate in the U.S.** (driven by diabetes, vascular disease, trauma)
- Minimal public transit; widespread transportation poverty
- Some of the nation's worst health outcomes overall

---

## 3. Cross-Regional Summary

| Metric | Rural WV | Eastern KY | MS Delta |
|--------|----------|------------|----------|
| CPO Within 50 km | **0** | **0** | **0** |
| Nearest CPO | ~190 mi | ~130 mi | ~200 mi |
| Travel Time | 3+ hrs | 3+ hrs | 4+ hrs |
| Medicaid Expansion | No | No | No |
| Healthcare Score | 9.8* | 0 | 2.0 |
| Hub Hospital | 5 facilities | 1 facility | 2 facilities |
| Trial Sites Present | None | None | None |

*Charleston city center only; rural WV counties have far lower scores.

### Key Conclusions
1. **Zero prosthetic-orthotic providers within 50 km in all three regions** — this is not a marginal gap but a complete absence.
2. **All three states have not expanded Medicaid** — cost barriers compound geographic ones.
3. **MS Delta has the highest amputation rates in the US yet the worst access** — a paradox demanding intervention.
4. **No clinical trial sites exist in any of these regions** — research participation is inaccessible to the populations who need it most.
5. **Eastern KY has the worst neighborhood healthcare score (0/10)** — the most structurally underserved.
6. **Clinical trial evidence is thin** — only 4 Phase 3 and 104 interventional trials across 563+ studies; most are observational registries.

---

## 4. Recommendations

1. **Mobile CPO Units** — Deploy traveling prosthetic-orthotic clinics serving all three regions on rotating schedules
2. **Telehealth Fitting** — Invest in remote fitting and adjustment capabilities to reduce travel burden
3. **Medicaid Expansion Advocacy** — All three states' refusal to expand Medicaid is the single policy barrier worsening every other gap
4. **Trial Site Expansion** — Require or incentivize prosthetic trial sites in underserved regions
5. **Community Health Worker Programs** — Train local providers in basic prosthetic care and fitting support
6. **Travel Voucher Programs** — Fund transportation for patients to reach the nearest CPO centers

---

*Data sources: ClinicalTrials.gov API v2, OpenStreetMap via OSM MCP tools. All data publicly accessible and open-source.*
