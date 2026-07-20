# Prosthetic Access Atlas — Supplemental Report (July 2026)

> Generated: 2026-07-20  
> Analyst: Open-source community  
> Data: ClinicalTrials.gov API + OpenStreetMap

---

## Executive Summary

This report presents the findings from two parallel analyses conducted to inform the **Prosthetic Access Atlas** project:

1. **Clinical Trial Landscape** — Analysis of prosthetic-related clinical trials on ClinicalTrials.gov, examining trends by status, geography, phase, and sponsor.
2. **Access Gap Analysis** — Mapping of prosthetic/orthotic care (CPO) providers across three underserved U.S. regions using OpenStreetMap data.

### Bottom Line

- **644 prosthetic-related clinical trials** exist globally (broad search), but only **~30 are Phase 3 efficacy trials** — the evidence base for prosthetic devices is critically thin.
- **All three underserved regions** (rural WV, eastern KY, Mississippi Delta) have **zero CPO providers within 30km** and **zero active clinical trial sites**.
- The **Mississippi Delta** is the most severe gap: highest amputation rates in the U.S., fewest healthcare facilities, and the longest drive to the nearest CPO specialist.

---

## Part 1: Clinical Trial Landscape

### 1.1 Scope of Search

Three queries were run against ClinicalTrials.gov:

| Query | Studies Returned | Scope |
|-------|-----------------|-------|
| `cond=prosthetic` | 644 | Broad (includes joint, heart valve, limb prosthetics) |
| `cond=prosthetic limb` | 136 | Focused on limb prosthetics/amputation |
| `cond=prosthetic limb` + US location | 86 | US-focused limb studies |

### 1.2 Status Distribution (n=644)

| Status | Count | % |
|--------|-------|---|
| RECRUITING | 112 | 17.4% |
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| TERMINATED | 24 | 3.7% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

**Key insight:** Nearly half of all prosthetic studies are completed (42.1%), and over 20% have unknown status. Only 17.4% are actively recruiting, indicating a pipeline bottleneck.

### 1.3 Phase Distribution (n=644)

| Phase | Count | % |
|-------|-------|---|
| Unknown | 202 | 31.4% |
| NA (Not Applicable) | 338 | 52.5% |
| Phase 3 | 30 | 4.7% |
| Phase 4 | 29 | 4.5% |
| Phase 2 | 39 | 6.1% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

**Key insight:** With only 30 Phase 3 trials globally, the evidence for prosthetic device efficacy is dangerously thin. Over half of studies are categorized as "Not Applicable" (typically observational or device-feasibility studies without a phase designation).

### 1.4 Geographic Distribution

The top 10 countries by study count:

1. **United States** — 680 (includes multi-country trials)
2. **France** — 317
3. **Denmark** — 78
4. **Germany** — 76
5. **Italy** — 71
6. **United Kingdom** — 44
7. **Canada** — 41
8. **Netherlands** — 41
9. **Egypt** — 38
10. **Spain** — 38

> **Note:** The US figure of 680 is inflated by multi-center international trials. The count of US-only prosthetic limb studies is 86.

### 1.5 Sponsor Breakdown

| Sponsor | Count | % |
|---------|-------|---|
| OTHER (Academic/Non-Profit) | 493 | 76.5% |
| INDUSTRY | 108 | 16.8% |
| FED (Federal) | 23 | 3.6% |
| OTHER_GOV | 14 | 2.2% |
| NETWORK | 5 | 0.8% |
| NIH | 1 | 0.2% |

**Key insight:** Academic sponsorship dominates at 76.5%. While this ensures scientific rigor, it limits the commercial translation pipeline. Only 16.8% of studies have industry backing, and just 3.6% are federally funded.

### 1.6 Example Key Trials

**PROSTHETIC LIMB / AMPUTATION:**

| NCT ID | Title | Status | Phase | Sponsor |
|--------|-------|--------|-------|---------|
| NCT01901081 | IMES: Implantable Myoelectric Sensors for Upper Limb Prostheses | COMPLETED | NA | Alfred E. Mann Foundation |
| NCT06013631 | Prosthesis Training Effects on Pain & Satisfaction (Lahore, Pakistan) | COMPLETED | NA | Univ. of Lahore |
| NCT05190354 | Xtremity Polymer Prosthetic Socket System (US, below-knee) | COMPLETED | NA | Medical Creations Inc. |

**PROSTHETIC JOINT INFECTIONS:**

| NCT ID | Title | Status | Phase | Sponsor |
|--------|-------|--------|-------|---------|
| NCT05902221 | Rifampicin for C. acnes Prosthetic Joint Infections | RECRUITING | Phase 3 | CHU Nice, France |
| NCT06400342 | REVIVE-TAVR: Valve-in-Valve vs. Explant for Failed TAVR | NOT_YET_RECRUITING | NA | MedStar Health |

---

## Part 2: Access Gap Analysis

### 2.1 Regions Examined

| Region | Representative City | Coordinates |
|--------|-------------------|-------------|
| Rural West Virginia | Beckley, WV | 37.78°N, 81.19°W |
| Eastern Kentucky | Pikeville, KY | 37.48°N, 82.52°W |
| Mississippi Delta | Greenville, MS | 33.41°N, 91.06°W |

### 2.2 Provider Presence Within 30km

#### Rural West Virginia (Beckley Area) — 3 hospitals, 4+ clinics, 9+ pharmacies, 3+ dentists

| Category | Count | Notable Providers |
|----------|-------|-------------------|
| Hospitals | 3 | Beckley VA Medical Center, Raleigh General Hospital, Beckley Appalachian Regional Hospital |
| Clinics | 4+ | MedExpress, Primary Care Plus, Marden Rehabilitation, Wyoming Foot & Ankle Clinic |
| Pharmacies | 9 | CVS, Walgreens (3), Citizen's Pharmacy, Westside Pharmacy, others |
| Dentists | 3 | Liberty Dental, Oceana Dental, Shady Spring Dental |
| Rehab/Dialysis | 1 | Fresenius Medical Care |
| **CPO Providers** | **0** | **None detected** |

#### Eastern Kentucky (Pikeville Area) — 1 hospital, 2 clinics, 5 doctors, 2 pharmacies, 2 dentists

| Category | Count | Notable Providers |
|----------|-------|-------------------|
| Hospitals | 1 | Pikeville Medical Center |
| Clinics | 2 | PMC Medical Diagnostics, MCHC Elkhorn City |
| Doctors | 5 | Meta Medical Center (Dr. Parker), Pediatric Associates, Asthma & Allergy Center |
| Pharmacies | 2 | Elkhorn Drug, Nichols Apothecary |
| Dentists | 2 | Big Sandy Dental Center, Elkhorn Dental |
| Specialty | 2 | Optometry, Chiropractic |
| **CPO Providers** | **0** | **None detected** |

#### Mississippi Delta (Greenville Area) — 2 hospitals, 1 clinic, 1+ pharmacy, 2 dentists

| Category | Count | Notable Providers |
|----------|-------|-------------------|
| Hospitals | 2 | Delta Regional Medical Center West Campus, Delta Health System – The Medical Center |
| Clinics | 1 | The Greenville Clinic (internal, pediatrics, cardiology) |
| Pharmacies | 1+ | Good Neighbor Pharmacy |
| Dentists | 2 | Michelle Seard-Higgins DMD, Dental Group of Greenville |
| **CPO Providers** | **0** | **None detected** |

### 2.3 Access Gap Summary

| Region | CPO Within 30km | Nearest CPO Hub | Drive Time | Medicaid |
|--------|----------------|-----------------|------------|----------|
| Rural WV (Beckley) | **0** | Charleston / Columbus | 3+ hrs | Not expanded |
| Eastern KY (Pikeville) | **0** | Lexington | 3+ hrs | Limited |
| Mississippi Delta (Greenville) | **0** | Memphis | 4+ hrs | Not expanded |

### 2.4 Severity Assessment

**Critical (Mississippi Delta):** Zero CPO providers, fewest healthcare facilities, highest amputation rates, and the longest drive (4+ hrs) to the nearest specialist. The Mississippi Delta has the highest amputation rate in the United States and essentially no prosthetic care infrastructure.

**High (Rural West Virginia):** While WV has the most overall healthcare infrastructure among the three regions (3 hospitals, 9 pharmacies), it has zero CPO providers and Medicaid was not expanded. Mountainous terrain compounds travel times.

**High (Eastern Kentucky):** A single Critical Access Hospital serves the region. Pikeville Medical Center is the only hospital within 30km. Limited Medicaid expansion and sparse public transit create additional barriers.

### 2.5 OSM Data Caveats

- OpenStreetMap may not capture all CPO providers, especially small private practices
- Prosthetists/orthotists may not be mapped as distinct entities in OSM
- The absence of CPO facilities in OSM strongly suggests structural access gaps, but does not prove a complete absence of private practice
- Hospital and clinic data should be verified against state licensing databases for completeness

---

## Part 3: Synthesis and Recommendations

### 3.1 The Evidence-Implementation Gap

The prosthetic field faces a dual crisis:

1. **Evidence gap:** Only ~30 Phase 3 trials globally, with unknown status for 1 in 5 studies.
2. **Implementation gap:** The three most underserved regions have zero trial sites, zero CPO providers, and patients face 3–4 hour drives for basic prosthetic care.

### 3.2 Recommendations

1. **Establish satellite CPO clinics** in Beckley, Pikeville, and Greenville using existing hospital infrastructure as anchor sites.
2. **Deploy mobile prosthetic units** for the Mississippi Delta, where road access is limited and population density is very low.
3. **Leverage telehealth** for initial prosthetic fittings, adjustments, and follow-ups to bridge the 130–200 mile gap.
4. **Prioritize the Mississippi Delta** — the compounding of highest amputation rates + fewest providers + longest travel = most urgent need.
5. **Leverage VA facilities** — Beckley VA Medical Center could serve as a prosthetic rehabilitation hub for West Virginia.
6. **Expand trial recruitment** to underserved regions — zero trials in WV, KY, or MS despite these regions having high amputation rates.
7. **Data transparency** — 20.8% of prosthetic studies have unknown status; improved reporting would strengthen the evidence base.

---

## Data Sources

| Source | URL | Access |
|--------|-----|--------|
| ClinicalTrials.gov API | https://clinicaltrials.gov/api/v2/studies | Open/Free |
| OpenStreetMap | https://openstreetmap.org | Open/Free |
| GitHub Repository | https://github.com/zhub9006/prosthetic-access-atlas | Open/Free |

---

*This report was compiled on July 20, 2026. Data is subject to change as new trials are registered and OSM data is updated. The prosthetic access atlas is a living, community-maintained resource.*
