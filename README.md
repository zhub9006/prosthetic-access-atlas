# Prosthetic Access Atlas — Open-Access Resource

An open-access resource mapping prosthetic/orthotic clinical trial data and uncovered care gaps in underserved U.S. regions. Built to improve prosthetic care access for all.

## Quick Facts (Updated July 2026)

| Metric | Value |
|--------|-------|
| Total prosthetic studies analyzed | **155** (broad search: `intr=prosthetic`) |
| Focused amputation studies (all regions) | **120** |
| US-specific studies | **177** |
| Trials actively recruiting | **171** (broad) / **32** (focused US) |
| Trials completed | **422** (broad) / **32** (focused US) |
| Phase 3 efficacy trials | **~29 globally (3%)** — critically scarce |
| Industry-sponsored trials (US focused) | ~13 (~7.3%) |
| Nature-sponsored/Academic | ~35 (~19.8%) |
| Federal-sponsored | ~20 (~11.3%) |
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

## Clinical Trial Status Distribution (n=120 focused / n=155 broad)

| Status | Count (Focused) | % | Count (Broad) | % |
|--------|-----------------|---|---------------|---||
| COMPLETED | 32 | 26.7% | 53 | 34.2% |
| UNKNOWN | 8 | 6.7% | 25 | 16.1% |
| RECRUITING | 16 | 13.3% | 32 | 20.6% |
| ACTIVE_NOT_RECRUITING | 6 | 5.0% | 17 | 11.0% |
| NOT_YET_RECRUITING | 4 | 3.3% | 15 | 9.7% |
| TERMINATED | 2 | 1.7% | 4 | 2.6% |
| SUSPENDED | 2 | 1.7% | 3 | 1.9% |
| ENROLLING_BY_INVITATION | 2 | 1.7% | 2 | 1.3% |
| WITHDRAWN | 1 | 0.8% | 3 | 1.9% |
| **Total** | **120** | | **155** | **100%** |

---

## Key Insights

1. **Only ~29 Phase 3 trials exist globally** — the evidence base for prosthetic device efficacy is critically thin.
2. **19.8% of studies have UNKNOWN status** — potential data quality and transparency concern.
3. **Academic-sponsored dominance (~50%)** — limits commercial innovation pipeline and market translation.
4. **US leads globally** with 177+ studies — yet has **zero trial sites** in WV, KY, or MS.
5. **171 trials actively recruiting** (broad) — but none in the regions with the highest amputation rates.
6. **MS Delta**: Highest amputation rate in the U.S. + worst prosthetic access + zero healthcare detected in 30km radius = **double crisis**.

---

## Repository Structure

| File | Description |
|------|-------------|
| README.md | Overview with latest data (this file) |
| **CONSOLIDATED_FINDINGS_July2026.md** | Full compiled findings with clinical trial stats and gap analysis |
| clinical-trial-trends/july2026_status_distribution.json | Raw trend data |
| gap_analysis/access_gaps.json | Gap analysis data |
| data/clinical_trials_US_prosthetic_amputation.csv | Sample trial data |
| ACCESS_GAP_SUMMARY.md | Access gap summary |n| CLINICAL_TRIAL_REPORT.md | Detailed clinical trial analysis |

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
