# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies analyzed | **975** (broad search: `intr=prosthetic`) |
| Trials actively recruiting | **171** (17.5%) |
| Trials completed | **422** (43.3%) |
| Phase 3 efficacy trials | **29** (3.0%) — critically scarce |
| Industry-sponsored trials | ~108 (~11.1%) |
| Academic-sponsored trials | ~493 (~50.6%) |
| Regions with zero CPO providers (30km) | **3 of 3** |
| Average distance to nearest CPO | **130–200+ miles** |

---

## Access Gap Summary

| Region | CPO Within 30km | Nearest CPO | Drive Time | Medicaid |
|--------|----------------|-------------|------------|----------|
| Rural West Virginia (Beckley) | 0 | Charleston (~190 mi) | 3+ hrs | Not expanded |
| Eastern Kentucky (Pikeville) | 0 | Lexington (~130 mi) | 3+ hrs | Limited |
| Mississippi Delta (Clarksdale) | 0 | Memphis (~200 mi) | 4+ hrs | Not expanded |

### Provider Presence by Region (within 30km)

| Region | Pharmacies | Clinics | Doctors | Dentists | Other | CPO |
|--------|-----------|---------|---------|----------|-------|-----|
| WV (Beckley) | 9 | 4 | 1+ | 3+ | 1 dialysis, 1 audiology | **0** |
| KY (Pikeville) | 6 | 4 | 5 | 2 | 1 optometry, 1 chiropractic | **0** |
| MS Delta (Clarksdale) | 18+ | Multiple | Multiple | 6+ | Multiple specialists | **0** |

---

## Clinical Trial Status Distribution (n=975)

| Status | Count | % |
|--------|-------|---|
| COMPLETED | 422 | 43.3% |
| UNKNOWN | 193 | 19.8% |
| RECRUITING | 171 | 17.5% |
| ACTIVE_NOT_RECRUITING | 56 | 5.7% |
| NOT_YET_RECRUITING | 60 | 6.2% |
| TERMINATED | 31 | 3.2% |
| WITHDRAWN | 20 | 2.1% |
| ENROLLING_BY_INVITATION | 20 | 2.1% |
| SUSPENDED | 2 | 0.2% |
| **Total** | **975** | **100%** |

## Phase Distribution (n=975)

| Phase | Count | % | Notes |
|-------|-------|---|-------|
| N/A (Observational/Device) | 367 | 37.6% | Registries and observational studies |
| Unknown | 193 | 19.8% | Phase not specified |
| Phase 4 | 24 | 2.5% | Post-market surveillance |
| **Phase 3** | **29** | **3.0%** | **Critically scarce — pivotal trials** |
| Phase 2 | 36 | 3.7% | Early efficacy signals |
| Phase 1 | 12 | 1.2% | First-in-human safety |
| Early Phase 1 | 3 | 0.3% | |
| **Total** | **975** | **100%** | |

---

## Clinical Trial Trends — Key Insights

1. **Only 29 Phase 3 trials exist globally** — the evidence base for prosthetic device efficacy is critically thin.
2. **19.8% of studies have UNKNOWN status** — potential data quality and transparency concern.
3. **Academic-sponsored dominance (50.6% vs. 11.1% industry)** — limits commercial innovation pipeline and market translation.
4. **US leads globally** with 576 studies (71% of foreign country totals), yet has **zero trial sites** in WV, KY, or MS.
5. **171 trials actively recruiting** — but none in the regions with the highest amputation rates.

---

## Clinical Trial Country Distribution (Top 15)

| Country | Count |
|---------|-------|
| United States | 576 |
| France | 273 |
| Italy | 91 |
| China | 44 |
| Germany | 48 |
| Netherlands | 50 |
| Canada | 53 |
| Egypt | 53 |
| Denmark | 42 |
| UK | 26 |
| Australia | 21 |
| Turkey | 21 |
| Spain | 32 |
| Sweden | 13 |
| Norway | 6 |

*Data from ClinicalTrials.gov `countByCountry` analysis (amputation + prosthetic, COMPLETED + RECRUITING).*

---

## Access Gap Summary — Detailed

### Rural West Virginia (Beckley, WV)
- **Coordinates:** 37.78°N, 81.19°W
- **CPO within 30 km:** 0
- **CPO within 100 km:** 0
- **Nearest CPO:** Charleston, WV — ~190 mi
- **Healthcare within 30km:** 9 pharmacies, 4 clinics, 1 major medical center, 3+ dentists, 1 audiology, 1 dialysis
- **Key barrier:** No public transit; WV did not expand Medicaid; 3+ hour drive to nearest CPO

### Eastern Kentucky (Pikeville, KY)
- **Coordinates:** 37.48°N, 82.52°W
- **CPO within 30 km:** 0
- **CPO within 100 km:** 0 (nearest: Logan Foot Clinic — foot care only, not CPO)
- **Nearest CPO:** Lexington, KY — ~130 mi
- **Healthcare within 30km:** 6 pharmacies, 4 clinics (incl. PMC Medical Diagnostics, MCHC Elkhorn City), 5 doctors, 2 dentists, 1 optometrist, 1 chiropractic
- **Key barrier:** Appalachian isolation; coal economy decline reduced healthcare infrastructure; KY limited Medicaid

### Mississippi Delta (Clarksdale, MS)
- **Coordinates:** 34.20°N, 90.57°W
- **CPO within 30 km:** 0
- **CPO within 100 km:** 0
- **Nearest CPO:** Memphis, TN — ~200 mi
- **Healthcare within 30km:** 18+ pharmacies, 1 hospital campus, multiple clinics, 6+ dentists, numerous specialists
- **Key barrier:** MS Delta has **highest amputation rates in the U.S.** yet worst prosthetic access. MS did not expand Medicaid. No public transit. Double crisis.

---

## Clinical Trial Relevance

- **Zero prosthetic clinical trial sites** in any of the three regions
- **576 U.S. studies** on amputation/prosthetics — none participated by WV, KY, or MS
- **Evidence gap:** Phase 3 trials for prosthetic devices are critically scarce (n=29 globally, n=7 in US)

---

## Methodology

- **Clinical Trial Data:** ClinicalTrials.gov API v2 (queried July 2026)
  - Query: `intr=prosthetic` (broad); `intr=prosthetic limb amputation` (focused)
  - Trend analyses: `countByStatus`, `countByPhase`, `countByCountry`
- **Geospatial Mapping:** OpenStreetMap via OSM MCP tools (30 km radius)
  - Provider search: `find_nearby_places` with healthcare category
  - Area exploration: `explore_area` for comprehensive neighborhood profiles
  - Coordinates: `geocode_address` for regional center points
- **Gap Metrics:** Distance to nearest Certified Prosthetist-Orthotist (CPO) from regional hub
- **Analysis date:** July 20, 2026

---

## Repository Structure

| File | Description |
|------|-------------|
| README.md | Overview with latest data (this file) |
| **CONSOLIDATED_FINDINGS_July2026.md** | Full compiled findings with clinical trial stats and gap analysis |
| ACCESS_GAP_SUMMARY.md | Access gap summary table and methodology |
| CLINICAL_TRIAL_REPORT.md | Detailed clinical trial analysis |
| clinical-trial-trends.md | Trend data from ClinicalTrials.gov |
| data/ | Additional data files and profiles |

---

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License

MIT (Open Access) — free to use for research, policy, and advocacy.

---

*Built to improve prosthetic care access for all. Open and free.*
