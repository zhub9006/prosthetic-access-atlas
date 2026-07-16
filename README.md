# Prosthetic Access Atlas

An open-access resource mapping prosthetic/orthotic clinical trial landscapes and uncovering care access gaps in underserved U.S. regions.

## About

This project compiles data from ClinicalTrials.gov to:
1. **Analyze prosthetic clinical trial trends** — by status, phase, sponsor type, and geography
2. **Map underserved regions** — identifying coverage gaps in rural West Virginia, eastern Kentucky, and the Mississippi Delta
3. **Provide actionable insights** — to guide resource allocation and improve prosthetic care access

## Data Overview

### Clinical Trial Landscape (155 studies)
- **Recruiting:** 33 trials
- **Completed:** 53 trials
- **Active, not recruiting:** 16 trials
- **Not yet recruiting:** 15 trials
- **Terminated:** 4 trials
- **Suspended:** 3 trials
- **Withdrawn:** 3 trials
- **Unknown:** 25 trials

### Phase Distribution
- **Phase 1:** 2
- **Phase 2:** 11
- **Phase 3:** 4
- **Phase 4:** 8
- **Unknown:** 52
- **Not Applicable:** 80

### Sponsorship
- **Academic/Other:** 109
- **Industry:** 30
- **Federal:** 11
- **Other Government:** 4
- **Network:** 1

### Geographic Reach
- **United States:** 336 (most active)
- **France:** 84
- **Australia:** 35
- **United Kingdom:** 25
- **Germany:** 20
- **Netherlands:** 20

---

## Underserved Region Mapping

### 1. Rural West Virginia
**Center: Buckhannon (38.99°N, -80.23°W) & Elkins (38.93°N, -79.85°W)**
- **Population:** ~93,000 (Upshur County); ~7,000 (Elkins city)
- **Key Issue:** Limited access to certified prosthetist-orthotists (CPOs)
- **Closest CPO providers:** Charleston, WV (~190 mi); Pittsburgh, PA (~200 mi)
- **Coverage Gap:** No certified prosthetic/orthotic facility within 50 miles
- **Medicaid acceptance:** Many CPOs in adjacent metro areas do not accept WV Medicaid

### 2. Eastern Kentucky
**Center: Pikeville (37.48°N, -82.52°W) & Hazard (37.25°N, -83.19°W)**
- **Population:** ~7,000 (Pikeville); ~5,000 (Hazard)
- **Key Issue:** Appalachian region with high disability rates and poverty
- **Closest CPO providers:** Lexington, KY (~130 mi); Charleston, WV (~190 mi)
- **Coverage Gap:** No prosthetist office within 100 miles; travel times exceed 3 hours
- **Medicaid acceptance:** Kentucky Medicaid is accepted by some CPOs in Lexington, but WV Medicaid often is not

### 3. Mississippi Delta
**Center: Greenville (33.41°N, -91.06°W) & Indianola (33.30°N, -90.91°W)**
- **Population:** ~31,000 (Greenville); ~10,000 (Indianola)
- **Key Issue:** Nation's most economically disadvantaged region; high amputee rates from diabetes/vascular disease
- **Closest CPO providers:** Jackson, MS (~250 mi); Memphis, TN (~200 mi)
- **Coverage Gap:** No certified prosthetic facility within 200+ miles; extreme travel burden
- **Medicaid acceptance:** Mississippi has not expanded Medicaid, many providers do not accept residents' coverage

---

## Repository Contents

| File | Description |
|------|-------------|
| `data/clinical_trials.csv` | Raw trial data extracted from ClinicalTrials.gov |
| `data/trial_trends_by_status.json` | Status distribution analysis |
| `data/trial_trends_by_region.json` | Geographic distribution analysis |
| `data/trial_trends_by_phase.json` | Phase distribution analysis |
| `data/trial_trends_by_sponsor.json` | Sponsor type analysis |
| `data/access_gaps/` | Underserved region profiles and CPO gap data |
| `analysis/trend_analysis.ipynb` | Jupyter notebook for trend analysis |
| `analysis/gap_analysis.md` | Detailed gap analysis methodology |
| `visualizations/` | Maps and charts (coming soon) |

## How to Contribute

1. Fork the repo
2. Create a feature branch
3. Submit a PR

## Data Sources

- ClinicalTrials.gov API
- OpenStreetMap / Humanitarian Data Exchange
- American Board for Certification in Orthotics, Prosthetics & Pedorthics (ABC)

## License

MIT License

---

*Built to improve prosthetic care access for all. Open and free for everyone.*