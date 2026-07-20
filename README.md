# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies (broad) | **644** |
| Focused limb amputation studies (US) | **75** /121 |
| Trials actively recruiting | 112 (17.4%) |
| Phase 3 pivotal trials | **30 (4.7%)** — critically scarce |
| Industry-sponsored | 108 (16.8%) |
| Academic-gov-sponsored | 530 (82.3%) |
| Regions with zero CPO providers | **3 of 3** |
| Avg drive to nearest CPO | 170 mi / 3+ hrs |
| Medicaid expansion (all 3 states) | None |

---

### Access Gap Summary

| Region | CPO ≤30km | Nearest CPO | Drive | Medicaid |
|--------|-----------|-------------|-------|----------|
| Rural WV (Beckley) | 0 | Charleston (~190 mi) | 3+ hrs | Not expanded |
| E. KY (Pikeville) | 0 | Lexington (~130 mi) | 3+ hrs | Limited |
| MS Delta (Clarksdale) | 0 | Memphis (~200 mi) | 4+ hrs | Not expanded |

---

## Key Insights

1. **Zero CPO providers within 200 km** in all three underserved regions — a complete care desert, not a marginal gap.
2. **Only 30 Phase 3 trials globally** (4.7% of 644 studies) — the evidence base for prosthetic efficacy is critically thin.
3. **76.5% academic-sponsored** — limited commercial pipeline for affordable, rugged prosthetic devices suited to rural use.
4. **Highest amputation regions have zero trial participation** — WV, KY, and MS Delta are absent from major prosthetic trial site lists.
5. **All three states have not expanded Medicaid** — compounding the geographic barriers with financial ones.

---

## Clinical Trial Status Distribution (n=644)

| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| RECRUITING | 112 | 17.4% |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| TERMINATED | 24 | 3.7% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |

## Phase Distribution (n=644)

| Phase | Count | % | Notes |
|-------|-------|---|-------|
| N/A (Observational/Device) | 338 | 52.5% | Registries and observational studies |
| Unknown | 202 | 31.4% | Phase not specified |
| **Phase 3** | **30** | **4.7%** | **Critically scarce — pivotal trials** |
| Phase 4 | 29 | 4.5% | Post-market surveillance |
| Phase 2 | 39 | 6.1% | Early efficacy signals |
| Phase 1 | 15 | 2.3% | First-in-human safety |
| Early Phase 1 | 4 | 0.6% | |

---

## Repository Structure

| File / Directory | Description |
|-----------------|-------------|
| `README.md` | Overview with latest data (this file) |
| `LATEST_FINDINGS_July2026.md` | Comprehensive July 2026 update with full trial data, gap analysis, and recommended actions |
| `GEOGRAPHY_CACHE.md` | Geocoded reference points for all target regions |
| `data/clinical_trials.json` | Machine-readable clinical trial data |
| `data/trend_analysis.json` | Full trend analysis + access gap data |
| `data/access_gaps.json` | CPO access gap data |
| `data/access_gaps_july2026.json` | July 2026 updated access gap data |
| `data/geocoding_july2026.json` | Geocoding reference data for all regions |
| `CLINICAL_TRIAL_REPORT.md` | Detailed clinical trial analysis |
| `ACCESS_GAP_SUMMARY.md` | Access gap summary |

---

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a PR

## License

MIT (Open Access) — free to use for research, policy, and advocacy.

*Built to improve prosthetic care access for all. Open and free.*