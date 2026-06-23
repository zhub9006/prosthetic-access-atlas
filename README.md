# Prosthetic Access Atlas

**An open-access resource mapping prosthetic clinical trials and care provider gaps in underserved U.S. regions.**

---

## 🎯 Mission

Globally, 35–40 million people need prosthetics or assistive devices, yet only 5–15% have access. This project combines clinical trial intelligence with geographic coverage analysis to identify where innovation is happening — and where it isn't reaching.

---

## 📊 What's Inside

| File | Description |
|------|-------------|
| [`clinical-trials-analysis.md`](clinical-trials-analysis.md) | Comprehensive analysis of **2,162** prosthetic-related clinical trials from ClinicalTrials.gov — broken down by status, geography (15 countries), phase, and key studies |
| [`coverage-gap-analysis.md`](coverage-gap-analysis.md) | Geographic audit of prosthetic/orthotic care providers in three underserved U.S. regions: Rural West Virginia, Eastern Kentucky, and the Mississippi Delta |
| [`search-methodology.md`](search-methodology.md) | Documentation of search strategies, data sources, and limitations |

---

## 🔑 Key Findings

### Clinical Trial Landscape — Broad Search ("prosthetic")

| Metric | Value |
|--------|-------|
| **Total registered trials** | **2,162** |
| **Completed** | 42.7% (923 trials) |
| **Recruiting** | 17.4% (378 trials) |
| **Unknown status** | 20.0% (431 trials) |
| **Not yet recruiting** | 6.6% (142 trials) |
| **Active, not recruiting** | 5.5% (119 trials) |
| **Terminated** | 3.5% (76 trials) |
| **Withdrawn** | 2.1% (45 trials) |

### Clinical Trial Landscape — Focused Search ("prosthetic limb")

| Metric | Value |
|--------|-------|
| **Total registered trials** | **509** |
| **Completed** | 51.1% |
| **Recruiting** | 18.7% |
| **Unknown status** | 12.8% |

### Geographic Dominance

- **United States** leads with 2,378 site-locations (includes multi-country studies)
- **France** (821), **Germany** (533), **Italy** (346), **Spain** (225) follow
- **No trials have sites in rural West Virginia, eastern Kentucky, or Mississippi Delta**
- **Low- and middle-income countries dramatically underrepresented** — most of Africa, South America, and Southeast Asia have minimal presence

### Key Innovations Identified
- Osseointegrated neural prostheses (e-OPRA)
- 3D-printed prosthetic limbs (LIMBER UniLeg)
- Adaptive prosthetic foot stiffness (VSPA Foot)
- Neural-controlled powered knee-ankle prosthesis (MIT)
- Wireless EMG control (ASTERISK System)
- Telerehabilitation for prosthetic rehab (NCT05569967)

### Coverage Gap Crisis
- **Zero prosthetic or orthotic care providers** identified within 50 km of any of the three target regions
- Rural WV (Beckley area): 29 healthcare facilities, none prosthetic-specific
- Eastern KY (Pikeville area): 27 healthcare facilities, none prosthetic-specific
- Mississippi Delta (Greenville, MS area): Only 9 healthcare facilities total, none prosthetic-specific
- The closest relevant services are general rehabilitation or foot/ankle clinics — not certified prosthetic care

### Distance to Nearest Prosthetist
| Region | Estimated Distance |
|--------|--------------------|
| Rural West Virginia | ~100 km |
| Eastern Kentucky | ~130 km |
| Mississippi Delta | ~180 km |

---

## 🗺️ Target Regions

| Region | Center Point | Healthcare Facilities (50 km) | Prosthetic/Orthotic Providers |
|--------|-------------|------------------------------|------------------------------|
| Rural West Virginia | 37.78°N, 81.19°W | 29 | **0** |
| Eastern Kentucky | 37.48°N, 82.52°W | 27 | **0** |
| Mississippi Delta | 33.41°N, 91.06°W | 9 | **0** |

---

## 📋 Data Sources

- **Clinical Trials**: [ClinicalTrials.gov](https://clinicaltrials.gov/) API — searched with terms "prosthetic" (broad, 2,162 studies) and "prosthetic limb" (focused, 509 studies)
- **Provider Locations**: [OpenStreetMap](https://www.openstreetmap.org/) — healthcare category search within 50 km radius
- **Trend Analysis**: countByStatus, countByCountry, countByPhase aggregations

---

## 🤝 How to Contribute

1. Fork this repository
2. Add new regions or update existing data
3. Submit a pull request

---

## 📜 License

This project is released under an open-access license to maximize impact for underserved communities.

---

*Built to close the gap between prosthetic innovation and the communities that need it most.*