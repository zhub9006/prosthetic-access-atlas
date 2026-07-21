# Prosthetic Access Atlas — README Update (July 21, 2026)

This document summarizes the latest additions to the atlas from ClinicalTrials.gov and OSM gap-mapping.

---

## Latest ClinicalTrials.gov Data (July 2026)

- **644 total prosthetic studies** identified (broad search: `cond=prosthetic`)
- **176 studies** for lower limb amputation + prosthetic
- **117 studies** for prosthetic limb amputation (focused intersection)
- **15 studies** for prosthetic care access specifically

### Key Trend Findings

| Metric | Value |
|--------|-------|
| Studies actively recruiting (all prosthetics) | 112 / 644 (17.4%) |
| Studies with UNKNOWN status | 134 (20.8%) |
| Phase 3 trials | 30 (4.7%) |
| Academic-sponsored studies | 493 (76.5%) |
| Industry-sponsored studies | 108 (16.8%) |
| Unknown-phase (observational) | 338 (52.5%) |
| Top country | United States (680 entries, 52.4%) |
| 2nd country | France (317 entries, 24.4%) |

### Newest Active Trials (2026)

1. **NCT07592325** — Access Socket Flexible Socket for Transtibial Prosthesis (France, RECRUITING)
2. **NCT07613502** — Bio Leg: Advancing Mobility / BAM (Univ. of Florida, RECRUITING)
3. **NCT07397169** — Adjustable Prosthetic Sockets (NTR, NOT_YET_RECRUITING)
4. **NCT07094074** — Exploratory Functional Assessment After LLA (NTR)

---

## Gap-Analysis Updates (July 2026)

3 target regions confirmed with **zero CPO providers within 30 km**, plus an expanded 4th check point:

| Region | Nearest CPO | Drive | Medicaid |
|--------|-------------|-------|----------|
| WV (Beckley) | Charleston, WV | ~190 mi / 3+ hrs | Not expanded |
| KY (Pikeville) | Lexington, KY | ~130 mi / 3+ hrs | Limited |
| MS Delta (Greenville) | Memphis, TN | ~200 mi / 3+ hrs | Not expanded |
| MS Delta (Clarksdale) | Memphis, TN | ~150 mi / 3+ hrs | Not expanded |

---

## New Files Added (July 21, 2026)

| File | Description |
|------|-------------|
| `TRIAL_TRENDS_UPDATED.md` | Rich trend tables: status, phase, country, sponsor, newest trials |
| `GAP_SUMMARY_UPDATED.csv` | Machine-readable gap summary for all 4 regions |
| `PROXIMITY_ANALYSIS_UPDATED.csv` | Full proximity data with coordinates and drive metrics |

---

## Repository Structure (Updated)

```
prosthetic-access-atlas/
├── README.md                       # Main overview
├── FINDINGS_JULY_2026_LATEST.md    # Detailed findings (existing, to be refreshed)
├── CLINICAL_TRIAL_TRENDS_LATEST.md # Trend analysis (existing, to be refreshed)
├── TRIAL_TRENDS_UPDATED.md         # New: 644-study trend dataset (Jul 21)
├── GAP_SUMMARY_UPDATED.csv         # New: gap data for 4 regions
├── PROXIMITY_ANALYSIS_UPDATED.csv  # New: proximity & drive-time data
├── access_gap_summary.csv          # Original gap summary
├── gap_analysis_proximity_data.csv # Original proximity data
├── [many other existing files...]
```

---

*Open-access resource. Built to improve prosthetic care access for all.*