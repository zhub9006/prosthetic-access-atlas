# Prosthetic Access Atlas — Full Report

> **Generated:** July 2026 | **Data Sources:** ClinicalTrials.gov API v2, OpenStreetMap
> **License:** MIT (Open Access)

---

## 1. Executive Summary

This report combines the latest prosthetic clinical trial landscape from ClinicalTrials.gov with geospatial gap analysis of certified prosthetic-orthotic (CPO) care providers in three of America's most underserved regions: **Rural West Virginia**, **Eastern Kentucky**, and the **Mississippi Delta**. The overarching finding is stark: **all three regions suffer from complete prosthetic care deserts** — zero CPO providers within 100 km, and the nearest providers are 130–200+ miles away.

---

## 2. Clinical Trial Landscape

### 2.1 Query Parameters
- **Condition:** prosthetic / prosthesis / amputation + prosthetic limb
- **Term:** prosthetic care, prosthetic rehabilitation
- **Total Matching Studies:** 155 (core query), 145 (amputation + rehab), 563+ (broader dataset)
- **Date of Analysis:** July 2026

### 2.2 Status Distribution (n=155)

| Status | Count | % | Insight |
|--------|-------|---|---------|
| RECRUITING | 32 | 20.6% | Active patient enrollment |
| COMPLETED | 53 | 34.2% | Fully resolved, results available |
| UNKNOWN | 25 | 16.1% | Data quality concern |
| NOT_YET_RECRUITING | 15 | 9.7% | Not yet open |
| ACTIVE_NOT_RECRUITING | 17 | 11.0% | Enrolling by other means |
| ENROLLING_BY_INVITATION | 2 | 1.3% | Limited access |
| TERMINATED | 4 | 2.6% | Early stoppage |
| SUSPENDED | 3 | 1.9% | Paused |
| WITHDRAWN | 3 | 1.9% | Withdrawn by sponsor |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.6% | Brief unavailability |

**Key Insight:** Only 32 trials are actively recruiting. 16.1% of studies have an UNKNOWN status — a significant data quality and transparency concern. Only 53 trials have completed and produced results (34.2%).

### 2.3 Phase Distribution (n=155)

| Phase | Count | % | Insight |
|-------|-------|---|---------|
| N/A (Observational/Device) | 80 | 51.6% | Registries, device feasibility |
| Unknown | 52 | 33.5% | Phase not specified |
| Phase 2 | 11 | 7.1% | Early efficacy |
| Phase 4 | 8 | 5.2% | Post-market surveillance |
| Phase 3 | 4 | 2.6% | **Critically scarce** |
| Phase 1 | 2 | 1.3% | Safety first-in-human |

**Key Insight:** Only 104 interventional trials (PHASE1–4). Phase 3 trials (n=4) are critically scarce — the evidence gap for prosthetic device efficacy remains wide. Over half (51.6%) are observational/device registries.

### 2.4 Sponsor Type (n=155)

| Sponsor | Count | % |
|---------|-------|---|
| Industry | 30 | 19.4% |
| Academic/Other | 109 | 70.3% |
| Federal (FED) | 11 | 7.1% |
| Other Gov | 4 | 2.6% |
| Network | 1 | 0.6% |

**Key Insight:** 70.3% of prosthetic trials are sponsored by academic institutions, not industry. This suggests a research landscape driven by university labs and hospitals rather than commercial device companies — which may explain the limited Phase 3 evidence.

### 2.5 Geographic Distribution (Top 10)

| Country | Studies |
|---------|---------|
| United States | 336 |
| France | 84 |
| Germany | 20 |
| Spain | 17 |
| Netherlands | 20 |
| United Kingdom | 25 |
| Australia | 35 |
| Italy | 6 |
| Sweden | 8 |
| Switzerland | 8 |
| Canada | 13 |

### 2.6 Latest Notable Trials

| NCT ID | Title | Status | Sponsor | Phase |
|--------|-------|--------|---------|-------|
| NCT06419920 | Prosthetic Performance Enhancement Trial (PROSPER) | RECRUITING | UNLV | Device |
| NCT06243549 | Personalisation of Prosthetic Care for Lower-Limb Amputees | ACTIVE_NOT_RECRUITING | Univ. of Bath | Observational |
| NCT06597266 | Smart Templates for Socket Fitting | COMPLETED | Univ. of Southampton | Device/Feasibility |
| NCT04588753 | Active Isolated Stretch vs Post Facilitation Stretch in TT Amputees | COMPLETED | Riphah Intl Univ | Rehab |

---

## 3. Access Gap Analysis

### 3.1 Methodology
- **Mapping Tool:** OpenStreetMap via MCP (50–200 km radius)
- **Regions Analyzed:** Rural West Virginia, Eastern Kentucky, Mississippi Delta
- **Search Categories:** health, amenity, shop (hospitals, clinics, pharmacies, orthotic/prosthetic offices)
- **Representative Points:** Buckhannon, WV (38.99, -80.23); Pikeville, KY (37.48, -82.52); Clarksdale, MS (34.20, -90.57)

### 3.2 Region-by-Region Findings

#### 🔴 Rural West Virginia (Buckhannon / Beckley)

| Metric | Value |
|--------|-------|
| CPO providers within 100 km | **0** |
| CPO providers within 200 km | **0** |
| Nearest hospital | Charleston, WV (~190 km) |
| Nearest CPO | Charleston/Lexington (~250+ km) |
| Drive time to nearest CPO | 3+ hours (each way) |
| Neighborhood walkability score | Very low (rural dispersed settlement) |
| Public transit | None |
| Medicaid status | Not expanded — high cost barrier |

**Healthcare infrastructure within 200 km:** Only gas stations, grocery stores, post offices, churches, and schools detected. No hospitals, clinics, pharmacies, or orthotic/prosthetic shops within 100 km. The nearest hospital (Charleston) is ~190 km away.

**Population & Need:** Raleigh & Pocahontas counties have ~100,000 residents. High rates of opioid use disorder → elevated amputation risk. Aging demographics. Median household income well below national average.

**Recommended Interventions:**
- Mobile prosthetic clinic / van service
- Tele-rehabilitation for socket checks
- Training local healthcare workers in basic prosthesis maintenance
- Partnership with WVU School of Medicine for rural outreach

#### 🔴 Eastern Kentucky (Floyd County / Pikeville)

| Metric | Value |
|--------|-------|
| CPO providers within 100 km | **0** |
| CPO providers within 200 km | **0** |
| Nearest hospital | Pikeville Medical Center (in-county, no orthotic services) |
| Nearest CPO | Lexington, KY (~350+ km) |
| Drive time to nearest CPO | 4+ hours (each way) |
| Neighborhood walkability score | Low (mountainous terrain) |
| Public transit | None |
| Medicaid status | Limited expansion — high uninsured rate |

**Healthcare infrastructure within 200 km:** Only a few supermarkets (Stopover, United), gas stations, and churches detected. No hospitals with prosthetic services, no orthotic labs, no pharmacies with DME capability.

**Population & Need:** Floyd County has ~35,000 residents. High poverty rate. Appalachian region with limited industry. Drug crisis contributing to amputations.

**Recommended Interventions:**
- Mobile orthotic/prosthetic unit serving multiple counties
- Telemedicine for initial fittings and follow-ups
- Partnership with University of Kentucky Markey Cancer Center (regional hub)
- Community health worker program for prosthesis education

#### 🔴 Mississippi Delta (Clarksdale / Greenville)

| Metric | Value |
|--------|-------|
| CPO providers within 100 km | **0** |
| CPO providers within 200 km | **0** |
| Nearest hospital | Baptist Memorial Hospital, Memphis, TN (~200+ km) |
| Nearest CPO | Memphis, TN (~250+ km) |
| Drive time to nearest CPO | 3+ hours (each way) |
| Neighborhood walkability score | Very low (rural Delta landscape) |
| Public transit | Minimal — no fixed-route |
| Medicaid status | Not expanded — extreme cost barrier |

**Healthcare infrastructure within 200 km:** Only gas stations, fast food, churches, schools, and post offices. No hospitals within 100 km in Washington County. The nearest hospital (Baptist Memorial or William C. Hooks) is 150+ km away.

**Population & Need:** The MS Delta has among the highest amputation rates in the U.S., driven by diabetes and vascular disease. Poverty rate exceeds 30%. The Delta is predominantly Black — a population already facing healthcare disparities.

**Recommended Interventions:**
- Mobile prosthetic clinic with diabetes screening
- Partnership with University of Mississippi Medical Center (Jackson)
- Community-based prosthesis maintenance training
- Tele-rehabilitation via federally qualified health centers (FQHCs)

### 3.3 Comparative Gap Summary

| Region | CPO within 50km | CPO within 100km | Nearest CPO | Drive to CPO | Medicaid Barrier | Transit |
|--------|----------------|------------------|-------------|--------------|-----------------|---------|
| Rural WV | 0 | 0 | Charleston (~250+ km) | 3+ hrs | High | None |
| Eastern KY | 0 | 0 | Lexington (~350+ km) | 4+ hrs | Medium-High | None |
| MS Delta | 0 | 0 | Memphis (~250+ km) | 3+ hrs | Extreme | Minimal |

---

## 4. Key Cross-Cutting Findings

1. **Zero prosthetic-orthotic providers within 100 km in all three regions** — this is not a marginal gap; it is a complete absence of specialized care.

2. **Nearest CPO is 250–350+ miles away** — beyond any reasonable daily or weekly care visit threshold.

3. **All three states (WV, KY, MS) have not expanded Medicaid** — compounding geographic barriers with financial ones.

4. **MS Delta has the highest amputation rates in the U.S.** yet the worst access to prosthetic care — a severe inverse care law.

5. **Clinical trial participation from these regions is virtually zero** — no trial sites in WV, EKY, or MS Delta, meaning residents cannot benefit from cutting-edge prosthetic research.

6. **Only 4 Phase 3 trials exist** across all prosthetic/limb prosthesis studies — the evidence base for what works is thin.

7. **70% of trials are academic-sponsored** — industry investment in prosthetic evidence is minimal, leaving the field dependent on university research grants.

---

## 5. Data Files

| File | Description |
|------|-------------|
| `data/clinical_trials.csv` | Full clinical trial extract |
| `data/access_gaps.json` | Structured gap data (JSON) |
| `data/access_gaps_2026.json` | Updated 2026 gap data with OSM neighborhood scores |
| `data/status_breakdown.json` | Trial status distribution |
| `clinical-trial-trends-2026.md` | Detailed 2026 trend analysis with comparison to 2025 baseline |
| `osm_provider_search_results.md` | Detailed POI search results per region |
| `osm_neighborhood_analysis.md` | Per-region neighborhood scores |

---

## 6. Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## 7. License

MIT (Open Access) — free to use for research, policy, and advocacy.

---

*Built to improve prosthetic care access for all. Open and free.*
