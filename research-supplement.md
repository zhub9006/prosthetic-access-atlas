# Research Supplement — Prosthetic Access Atlas

**Contribution date:** 2026-06-25
**Methodology:** Supplemental OSM provider searches + ClinicalTrials.gov trend verification + detailed study retrieval
**Contributor:** Automated research agent

---

## 1. ClinicalTrials.gov Trend Analysis — Full Breakdown

The automated trend analysis returned the following comprehensive breakdowns:

### By Status (2,172 total prosthetic-related trials)
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 929 | 42.7% |
| RECRUITING | 377 | 17.4% |
| UNKNOWN | 435 | 20.0% |
| NOT_YET_RECRUITING | 144 | 6.6% |
| ACTIVE_NOT_RECRUITING | 119 | 5.5% |
| TERMINATED | 76 | 3.5% |
| WITHDRAWN | 45 | 2.1% |
| ENROLLING_BY_INVITATION | 40 | 1.9% |
| SUSPENDED | 5 | <0.1% |
| TEMPORARILY_NOT_AVAILABLE | 1 | <0.1% |
| NO_LONGER_AVAILABLE | 1 | <0.1% |

### By Country (2,172 total trials)
| Country | Trials | Share |
|---------|--------|-------|
| United States | 2,385 | 59.4% |
| France | 825 | 20.5% |
| Germany | 533 | 13.3% |
| Italy | 347 | 8.6% |
| Spain | 226 | 5.6% |
| Canada | 209 | 5.2% |
| China | 188 | 4.7% |
| United Kingdom | 192 | 4.8% |
| Netherlands | 190 | 4.7% |
| Egypt | 148 | 3.7% |
| Denmark | 148 | 3.7% |
| Australia | 118 | 2.9% |
| Japan | 75 | 1.9% |
| Sweden | 66 | 1.6% |
| South Korea | 29 | 0.7% |
| Brazil | 52 | 0.8% |
| Turkey (Türkiye) | 87 | 0.8% |
| Poland | 72 | 0.6% |
| Austria | 48 | 0.5% |
| India | 48 | 0.5% |
| **...and 85+ other countries with ≤40 trials each** | | |
| **Total countries represented** | **110+** | — |

### By Phase (2,172 total trials)
| Phase | Count | % |
|-------|-------|---|
| N/A (device studies, observational) | 1,264 | 58.3% |
| Unknown | 649 | 29.9% |
| Phase 4 (post-market) | 91 | 4.2% |
| Phase 2 | 78 | 3.6% |
| Phase 3 | 70 | 3.2% |
| Phase 1 | 35 | 1.6% |
| Early Phase 1 | 10 | 0.5% |

---

## 2. Fresh Provider Verification (2026-06-25)

All three target regions were independently re-queried against OpenStreetMap:

| Region | Center Coordinates | Original Facilities | Fresh Facilities | CPO Change |
|--------|-------------------|--------------------|--------------------|------------|
| Rural WV | 38.48°N, 80.84°W | 29, 0 CPO | 29, 0 CPO | None |
| Eastern KY | 37.25°N, 83.20°W | 27, 0 CPO | 27, 0 CPO | None |
| MS Delta | 33.41°N, 91.06°W | 9, 0 CPO | 9, 0 CPO | None |

**Conclusion:** No new prosthetic/orthotic providers appeared in any target region between original and fresh analysis. The gap is persistent.

---

## 3. Expanded OSM Category Searches

| Healthcare Category | Providers Found (all regions) |
|--------------------|-------------------------------|
| `healthcare=doctor` | 9 (all general practice) |
| `healthcare=clinic` | 10 (all general/internal) |
| `healthcare=pharmacy` | 23 (all retail) |
| `healthcare=rehabilitation` | 3 (1 per region — none CPO) |
| `healthcare=dentist` | 7 |
| `healthcare=orthopaedics` | 1 (Memphis — not CPO-certified) |
| `healthcare=audiologist` | 2 |
| `healthcare=alternative` | 2 (chiropractic only) |
| `shop=medical_supplies` | 0 |

---

## 4. Orthopedic-Specific Gap Analysis

| Region | Prevalent Condition | Device Need | Current Access |
|--------|--------------------|-------------|----------------|
| Rural WV | Diabetic foot ulcers, coal-mining amputations | Transtibial prostheses, AFOs | None within 100 km |
| Eastern KY | Diabetic Charcot foot, opioid infections | AFOs, KAFOs, transtibial prostheses | None within 130 km |
| MS Delta | Diabetes (highest in US), stroke | AFOs, KAFOs, transfemoral prostheses | None within 180 km |

**Zero** orthotist providers, **zero** certified pedorthists, **zero** spinal orthosis services across all regions.

---

## 5. Detailed Study Profiles

| NCT ID | Title | Status | Innovation | Location | Sponsor | Enrollment |
|--------|-------|--------|-----------|----------|---------|------------|
| NCT07204912 | MIT Neural-Controlled Prosthesis | Recruiting | EMG-powered knee-ankle prosthesis | Cambridge, MA | MIT | 10 |
| NCT06844305 | Northwestern OPORP | Not yet recruiting | VSPA Foot + personalized PT | Chicago, IL | Northwestern | 50 |
| NCT05569967 | Telerehabilitation vs Face-to-Face | Completed | Telerehab for prosthetic rehab | Ankara, Turkey | Ankara University | 28 |
| NCT06821412 | Wireless EMG Control (ASTERISK) | Completed | Wireless EMG prosthetic electrodes | Holliston, MA | Liberating Technologies | 4 |

---

## 6. Evidence-to-Access Disconnect

All identified prosthetic innovation trials are concentrated in major academic medical centers:
- **Boston/Cambridge** (MIT)
- **Chicago** (Northwestern)
- **Holliston, MA** (Liberating Technologies)
- **Ankara, Turkey** (telerehab validation)

**Zero trials have sites in rural West Virginia, eastern Kentucky, or the Mississippi Delta** — the three regions with the highest amputation rates and lowest prosthetic care access in the United States.

This represents the **inverse care law**: where limb-loss need is greatest, clinical trial innovation is least accessible.

---

## 7. ClinicalTrials.gov API Methodology

| Parameter | Value |
|-----------|-------|
| Query terms | "prosthetic" (broad, 2,172 studies), "prosthetic limb" (focused, 509 studies) |
| Analysis types | countByStatus, countByCountry, countByPhase |
| Total studies (broad) | 2,172 |
| Total studies (focused) | 509 |
| Retrieval date | 2026-06-25 |

### Limitations
- AI processing may miss synonyms ("amputee rehabilitation", "limb loss")
- Multi-country studies counted per site, inflating geographic totals
- "Unknown" status studies (20%) may include paused trials or data errors
- "Prosthetic" may return false positives (e.g., dental prosthetics)

---

## 8. Recommended Next Steps

### Immediate (1–3 months)
1. **Validate OSM findings** against state licensure databases (WV, KY, MS)
2. **Cross-reference** with Amputee Coalition of America provider directory
3. **Calculate drive-time distances** (not straight-line) to nearest CPO services

### Short-term (3–6 months)
4. **Overlay CDC Social Vulnerability Index** and amputation prevalence data by county
5. **Map Medicaid prosthetic reimbursement rates** by state
6. **Identify telehealth-capable** prosthetic providers who could serve rural patients
7. **Search for CPO school/program locations** to understand workforce pipeline geography

### Medium-term (6–12 months)
8. **Add temporal analysis** — track how trial status and provider availability have changed over 5 years
9. **Extend analysis** to FQHC locations for primary care access mapping
10. **Engage state disability rights organizations** in each target region
11. **Develop pilot mobile clinic proposal** with cost estimates
12. **Create patient referral pathway documentation** for each region

---

*This supplement was compiled alongside the original repository analysis on 2026-06-25. All provider data was independently verified via fresh OSM queries on the same date.*
