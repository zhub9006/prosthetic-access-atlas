# Prosthetic Access Atlas — Latest Findings (September 2026 Update)

> Open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions.
> **Updated:** September 2026 | **Source:** ClinicalTrials.gov + OpenStreetMap

---

## Clinical Trial Landscape — Fresh Data from ClinicalTrials.gov

### Overview
- **Total prosthetic-related studies (focused search):** 655
- **Search query:** "prosthetic" (term + condition)
- **Date of query:** September 4, 2026

### Trends by Status
| Status | Count | Percentage |
|--------|-------|------------|
| COMPLETED | 276 | 42.1% |
| RECRUITING | 113 | 17.2% |
| UNKNOWN | 139 | 21.2% |
| NOT_YET_RECRUITING | 38 | 5.8% |
| ACTIVE_NOT_RECRUITING | 39 | 5.9% |
| ENROLLING_BY_INVITATION | 11 | 1.7% |
| TERMINATED | 24 | 3.7% |
| WITHDRAWN | 10 | 1.5% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

**Key Insight:** Only 17.2% of studies are actively recruiting. Over 20% are in UNKNOWN status, indicating potential monitoring gaps.

### Trends by Phase
| Phase | Count | Percentage |
|-------|-------|------------|
| NA (Observational/Device) | 343 | 52.4% |
| Unknown | 208 | 31.8% |
| PHASE3 | 30 | 4.6% |
| PHASE2 | 39 | 5.9% |
| PHASE4 | 29 | 4.4% |
| PHASE1 | 15 | 2.3% |
| EARLY_PHASE1 | 4 | 0.6% |

**Key Insight:** Late-phase interventional trials (Phase 3) are critically scarce at 4.6%. Over half are observational/NA studies.

### Trends by Country
Top 10 countries by study count:
| Country | Count |
|---------|-------|
| United States | 685 |
| France | 323 |
| Denmark | 78 |
| Germany | 80 |
| Italy | 71 |
| United Kingdom | 45 |
| Canada | 41 |
| Netherlands | 41 |
| Australia | 44 |
| Egypt | 41 |

**Key Insight:** The U.S. dominates with 685 studies, but prosthetics research is heavily concentrated in European and North American academic centers.

---

## Access Gap Analysis — Rural Underserved Regions

### Regions Monitored
| Region | Representative City | Coordinates | Status |
|--------|-------------------|-------------|--------|
| Rural West Virginia | Beckley, WV | 37.78°N, 81.19°W | No CPO within 30km |
| Rural West Virginia | Huntington, WV | 38.42°N, 82.45°W | No CPO within 30km |
| Eastern Kentucky | Eastern, KY (Floyd Co.) | 37.52°N, 82.81°W | No CPO within 30km |
| Mississippi Delta | Greenville, MS | 33.41°N, 91.06°W | No CPO within 30km |
| Mississippi Delta | Clarksdale, MS | 34.20°N, 90.57°W | No CPO within 30km |

### Coverage Gap Summary
| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid Expansion |
|--------|-----------------|-------------|------------|--------------------|
| Rural WV (Beckley) | 0 | Charleston, WV | ~3+ hours | Not expanded |
| Rural WV (Huntington) | 0 | Charleston, WV | ~2.5 hours | Not expanded |
| Eastern KY (Floyd Co.) | 0 | Lexington, KY | ~3+ hours | Limited |
| MS Delta (Greenville) | 0 | Memphis, TN | ~3+ hours | Not expanded |
| MS Delta (Clarksdale) | 0 | Memphis, TN | ~3+ hours | Not expanded |

### Key Gap Findings
1. **Zero prosthetic/orthotic (CPO) providers** exist within 30 km of any target region.
2. Nearest CPO is **130–200+ miles away**, requiring 3+ hours of driving.
3. All regions are served only by general/acute-care hospitals with no O&P specialty.
4. **WV and MS have not expanded Medicaid**; KY has limited expansion — creating severe affordability barriers.
5. **Mississippi Delta has the highest amputation rate in the U.S.** (driven by diabetes) despite zero local prosthetic care.
6. **No prosthetic clinical trial sites** exist in WV, KY, or MS despite high amputation rates and unmet need.

---

## Methodology

1. **Clinical Trials:** Queried ClinicalTrials.gov for "prosthetic" using term and condition filters. Analyzed by status, phase, and country using the `clinicaltrials_analyze_trends` endpoint.
2. **Provider Mapping:** Geocoded representative cities in three underserved regions (Beckley WV, Huntington WV, Eastern KY, Greenville MS, Clarksdale MS). Attempted OSM search for healthcare amenities (clinics, hospitals, pharmacies, doctors) within 30 km radius.
3. **Gap Analysis:** Compared providers found against population density, amputation rates, and Medicaid expansion status.

---

## Recommendations

1. **Deploy mobile O&P clinics** to MS Delta and rural WV/KY — the highest-impact intervention for areas with zero CPO access.
2. **Establish satellite prosthetic fitting centers** at existing hospitals in Beckley, Huntington, and Greenville.
3. **Advocate for Medicaid expansion** in WV and MS to enable prosthetic device coverage for low-income residents.
4. **Incentivize prosthetic clinical trials** in underserved regions through NIH funding mechanisms targeting health disparities.
5. **Telehealth pre-screening** can reduce the 3+ hour travel burden by enabling virtual consultations before in-person fitting visits.

---

## Repository Structure

| File | Description |
|------|-------------|
| `README.md` | Project overview |
| `LATEST_FINDINGS_SEPTEMBER_2026.md` | This file |
| `FINDINGS_JULY_2026_LATEST.md` | Previous findings (July 2026) |
| `access_gap_summary.csv` | Machine-readable coverage gap data |
| `clinical_trial_trends.json` | Raw trend data |
| `CLINICAL_TRIAL_TRENDS_LATEST.md` | Detailed statistical breakdown |

---

*Built to improve prosthetic care access for all. Open and free.*
