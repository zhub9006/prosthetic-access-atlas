# Prosthetic Access Atlas — 🦽 Access Gap Mapper & Clinical Trial Tracker

> **Open-access resource** mapping prosthetic and orthotic care access gaps, clinical trial trends, and underserved regions worldwide. Built from ClinicalTrials.gov and OpenStreetMap data.

---

## Overview

This repository compiles two intersecting data streams:

1. **Clinical Trial Landscape** — From ClinicalTrials.gov API: 2,182+ prosthetic/amputation studies across all phases, sponsors, and countries
2. **Care Gap Analysis** — From OpenStreetMap: Zero prosthetic/orthotic care providers identified within 100km of three medically underserved U.S. regions

---

## Key Findings

### Clinical Trial Landscape
- **2,182 total studies** indexed for prosthetic/amputation conditions
- **Status breakdown:**
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 936 | 43.0% |
| UNKNOWN | 434 | 19.9% |
| RECRUITING | 380 | 17.4% |
| NOT_YET_RECRUITING | 145 | 6.6% |
| TERMINATED | 76 | 3.5% |
| ACTIVE_NOT_RECRUITING | 119 | 5.5% |
- **Phase distribution:** 58.5% NA (device/surgical) | 29.9% Unknown | 7.8% Phase 1-4
- **Sponsor split:** 76.8% Academic | 17.5% Industry | 2.4% Federal
- **Geographic distribution:** U.S. leads (2,393 sites); France (825), Germany (533), Spain (228) follow
- **Critical evidence gap:** **Zero Phase III trials** for lower-limb prosthetic amputation
- **Powered prosthetics:** Only 14 studies globally, mostly European; U.S. rural sites excluded
- **AI in prosthetics:** Only 1 out of 85 osseointegration/prosthetic studies uses AI; rural patients completely excluded

### Highlighted Active Trials
| NCT ID | Title | Status | Location | Significance |
|--------|-------|--------|----------|--------------|
| **NCT06498245** | MPK-K2: Microprocessor Knee for K2 Ambulators | 🔵 RECRUITING | United States | Largest RCT comparing powered vs. conventional knees for community ambulators |
| **NCT06634654** | AI-based Approach in TKA | 🔵 RECRUITING | Italy | Predictive AI for personalized prosthetic outcomes |
| **NCT07574762** | CAN-ARD: Robotic vs. Navigation TKA | 🔵 RECRUITING | France | First robotic prosthetics RCT in Europe |

### Highlighted Completed Trials
| NCT ID | Title | Status | Sponsor |
|--------|-------|--------|---------|
| **NCT07519746** | PROINGA: Prosthetic Satisfaction & QoL in Gaza | ✅ COMPLETED | Yeditepe University |
| **NCT05407545** | MOKI-B: Motorised Prosthetic Knee (Össur Power Knee) | ✅ COMPLETED | VUB / Össur |
| **NCT03726918** | BioPreIOA: Osseointegration Bio-Markers | ✅ COMPLETED | Istituto Ortopedico Rizzoli |
| **NCT04725461** | Low Cost Socket for Lower Limb Amputees | ✅ COMPLETED | Shirley Ryan AbilityLab |
| **NCT03544853** | Computational Socket Design (MIT) | ✅ COMPLETED | MIT / NIBIB |
| **NCT07215442** | Skin Temperature & Prosthetic Thermoregulation | ✅ COMPLETED | VA Puget Sound |
| **NCT03215771** | Myoelectric Orthosis (TBI/Stroke) | ✅ COMPLETED | Northwestern / VA |
| **NCT07032753** | Neuromusculoskeletal Interface (e-OPRA) | ⏳ NOT YET RECRUITING | Shirley Ryan AbilityLab |

---

## Care Gap Analysis

### The Critical Finding: Three Zero-Coverage Regions

| Region | Center Point | Coordinates | O&P Providers (100km) | Nearest Services | Distance |
|--------|-------------|-------------|------------------------|------------------|----------|
| **Rural West Virginia** | Beckley, WV | 37.778°N, 81.188°W | **0** | Charleston, WV | ~100 km |
| **Eastern Kentucky** | Pikeville, KY | 37.479°N, 82.519°W | **0** | Charleston, WV / Lexington, KY | ~150-160 km |
| **Mississippi Delta** | Greenville, MS | 33.411°N, 91.064°W | **0** | Memphis, TN | ~130 km |

### Infrastructure Scores (Neighborhood Analysis)

| Category | Beckley, WV | Pikeville, KY | Greenville, MS |
|----------|-------------|---------------|----------------|
| **Overall** | 4.8 / 10 | 5.3 / 10 | **2.8 / 10** |
| **Healthcare** | **0 / 10** | **0 / 10** | **1.3 / 10** |
| Groceries | 10.0 (68) | 9.2 (46) | 0 / 10 (4) |
| Restaurants | 9.9 (121) | 10.0 (75) | 10.0 (30) |
| Education | 10.0 | 0 | 0 |
| Public Transport | 0 | 0 | 0 |
| Parks | 0 (11) | 8.8 | 9.8 |
| Shopping | 9.7 | 9.6 | 2.0 |

### What Gets Covered vs. What Doesn't
| Available | Missing |
|-----------|---------|
| Pharmacies (CVS, Walgreens, Rite Aid) | **Prosthetists / CPOs** |
| Primary care clinics | **Orthotists** |
| Community health centers (FQHCs) | **PM&R / Physiatry** |
| Dental offices | **DME (prosthetics specialists)** |
| Some hospitals (Charleston, Huntington) | **Prosthetic training / rehab** |
| Pharmacy chains | **O&P outpatient clinics** |
| | **Telerehabilitation programs** |

---

## Access Disparity Map

```
                         PROSTHETIC CARE ACCESS
                         ======================

    Northeast ──── Dense provider network (Boston, NYC, Philly)
         │         50+ prosthetics clinics within 50km
         │         Major academic centers with prosthetics R&D
         │
    Midwest ──── Moderate clusters (Chicago, Detroit, Minneapolis)
         │         15-30 providers within 50km
         │         Some rural gaps between cities
         │
    South ──── Sparse; major gaps in Delta, Appalachia
         │         Atlanta, Nashville have moderate coverage
         │         Rural AL/GA/MS/KY/SC have small gaps
         │
    Appalachia ──── ZERO providers within 100km of Beckley, Pikeville
         │         WV: 3M people, ~0 CPOs in 3 counties
         │         KY: High amputation rates, no local trials
         │         VA border: Some limited VA prosthetics (Blacksburg)
         │
    Mississippi Delta ──── ZERO providers within 100km of Greenville
         │         MS: Highest diabetes rate in the nation
         │         AR/LA Delta: Similar gaps along the river
         │         No clinical trial sites for prosthetics in MS

    West ──── Sparse; only urban coastal presence
              L.A., S.F. have some providers
              Vast rural West has zero coverage
```

### Travel Distance to Nearest Prosthetic Care
| From | To | Distance | Time |
|------|-----|----------|------|
| Beckley, WV | Charleston, WV | ~100 km | 1.5 hrs |
| Pikeville, KY | Charleston, WV / Lexington, KY | 150-160 km | 2+ hrs |
| Rolling Fork, MS | Greenville, MS | ~30 km | 45 min |
| Greenville, MS | Memphis, TN | ~130 km | 2 hrs |
| Hazard, KY | Lexington, KY | ~120 km | 2 hrs |

---

## Repository Structure

```
prosthetic-access-atlas/
├── README.md                       ← You are here — overview & key findings
├── ATLAS_FULL_REPORT.md            ← Comprehensive report with all sections
├── clinical-trials-data.md         ← ClinicalTrials.gov trend analysis (status, phase, country, sponsor)
├── gap-analysis.md                 ← Detailed gap analysis: WV, KY, MS Delta profiles
├── key-studies.md                  ← Deep dives into 12 highlighted clinical trials
├── data-sources.md                 ← Methodology, API parameters, limitations
├── METHODOLOGY.md                  ← Full methodology documentation
├── MAP_access_disparity.md         ← Visual map and travel distance table
└── regions/                        ← Individual regional profiles
    ├── beckley_wv.md               ← Rural WV — profile & interventions
    ├── pikeville_ky.md             ← Eastern KY — profile & interventions
    └── greenville_ms_delta.md      ← Mississippi Delta — profile & interventions
```

---

## Data Sources

| Source | URL | Type |
|--------|-----|------|
| ClinicalTrials.gov API | https://clinicaltrials.gov/api/v2/studies | REST API |
| OpenStreetMap Overpass | https://overpass-api.de/api/ | Geospatial Query |
| OSM Geocoding | https://nominatim.openstreetmap.org/ | Geocoding |
| GitHub Repo | https://github.com/zhub9006/prosthetic-access-atlas | Repository |

---

## License

MIT — Open Access. See [LICENSE](LICENSE) file.

## Contributing

Contributions welcome! Please open an issue or pull request to add:
- Additional clinical trial datasets
- Provider location updates for uncovered areas
- New region analyses
- Visualization tools and map overlays
- AI-driven access prediction models
- Transportation assistance maps for patients

## Acknowledgments

- **ClinicalTrials.gov** — Open clinical trial registry
- **OpenStreetMap** — Community-sourced geospatial data
- **U.S. Census Bureau & CDC** — Demographic and health data references
- **Affected communities** — The people of Appalachia and the Mississippi Delta who bear the highest amputation burdens

---

*Built: 2026-07-15 | Updated: 2026-07-15 | Authors: Open-access community*