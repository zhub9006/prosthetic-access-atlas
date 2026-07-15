# Prosthetic Access Atlas

An open-access resource mapping prosthetic and orthotic care access gaps, clinical trial trends, and underserved regions worldwide. Built to identify where prosthetic care is missing and how to close the gaps.

## 📊 What This Project Does

1. **Clinical Trial Landscape** — Aggregates and analyzes prosthetic-related trials from ClinicalTrials.gov (644 studies)
2. **Coverage Gap Map** — Identifies regions with zero prosthetic/orthotic providers
3. **Travel Burden Analysis** — Calculates actual drive times and economic costs for underserved patients
4. **Infrastructure Scoring** — Neighborhood-level livability scores for gap regions
5. **Intervention Recommendations** — Actionable strategies to close gaps

## 📈 Key Findings

### Clinical Trials
| Metric | Value |
|--------|-------|
| Total prosthetic studies | 644 |
| Currently recruiting | 113 (17.5%) |
| Completed | 271 (42.1%) |
| Unknown status | 134 (20.8%) |

### Care Gap Analysis

| Region | Prosthetic Providers | Nearest Hub | Drive Time |
|--------|---------------------|-------------|------------|
| Beckley, WV | **0** | Charleston, WV | 76 min |
| Pikeville, KY | **0** | Charleston, WV / Lexington, KY | 127 min |
| Greenville, MS | **0** | Memphis, TN | 190 min |

> 🔴 **All three regions have ZERO identified prosthetic or orthotic care providers within a 100km radius.**

### Access Tiers

```
🟢 Tier 1 (Full Access):    Northeast, Midwest metros — <30 min to care
🟡 Tier 2 (Moderate):       Suburban areas — 30 min–1 hr to care  
🟠 Tier 3 (Limited):        Rural Appalachia — 1–2 hr to care
🔴 Tier 4 (Extreme Desert): Beckley, Pikeville, Greenville — 2–3 hr to care
```

### Annual Travel Burden

| Region | Annual Round-Trip Miles | Annual Hours Lost |
|--------|------------------------|-------------------|
| Beckley, WV | ~230 mi | ~5 hours |
| Pikeville, KY | ~520 mi | ~8 hours |
| Greenville, MS | ~750 mi | ~10 hours |

## 🇺🇸 Georgia & the Deep South

| Region | Prosthetic Providers | Nearest Hub | Drive Time |
|--------|---------------------|-------------|------------|
| **Black amputation rate** | 2-3× national avg | Delta region | — |
| **Mississippi** highest diabetes prevalence in the US | — | No Medicaid expansion | — |
| **Rural hospital closures** | Multiple Delta hospitals closed | No replacements | — |

## 📁 Repository Structure

```
prosthetic-access-atlas/
├── ATLAS_FULL_REPORT.md          # Comprehensive report (this project's master document)
├── clinical_trials/
│   ├── summary.md                # Clinical trial landscape analysis
│   ├── key_studies.json          # Structured data on highlighted trials
│   └── data-sources.md           # Data sources and methodology
├── gap_analysis/
│   ├── west_virginia.md          # WV coverage gap report
│   ├── eastern_kentucky.md       # KY coverage gap report
│   ├── mississippi_delta.md      # MS Delta coverage gap report
│   └── methodology.md            # Data collection methodology
├── maps/
│   └── access_disparity_map.md   # Visual and tabular gap mapping with travel distances
├── data/
│   └── sources.md                # Master data sources document
└── README.md                     # This file
```

## 🔬 Recently Identified Clinical Trials

| NCT ID | Title | Status | Sponsor | Enrollment |
|--------|-------|--------|---------|------------|
| NCT06134167 | Transdermal Compress Device for Transfemoral Amputations | RECRUITING | Balmoral Medical | 100 |
| NCT06498245 | MPK-K2: Microprocessor Knee for K2-Level Ambulators | RECRUITING | Univ. Hospital Strasbourg | TBD |
| NCT07519746 | PROINGA: Satisfaction and Quality of Life Among Prosthetic Users in Gaza | COMPLETED | Yeditepe University | 128 |

## 💡 Recommended Interventions

### Immediate (0-6 months)
1. **Mobile prosthetic/orthotic clinic** — Deploy traveling O&P units serving gap regions
2. **Telehealth prosthetics consult line** — Connect rural amputees to academic centers via video
3. **Community health worker training** — Train local workers in basic prosthetics maintenance

### Medium-term (6-18 months)
4. **Partnership with NCT06134167 low-cost socket protocol** — Implement transdermal implant methodology at regional hubs
5. **DME supply chain** — Establish DME suppliers in gap regions
6. **University partnerships** — WVU, Marshall, UK, Shepherd Center outreach programs

### Long-term (18-36 months)
7. **Rural prosthetics fellowship** — PM&R residency tracks focused on rural amputee care
8. **OSM data enrichment** — Ensure all O&P providers are tagged in OpenStreetMap
9. **Clinical trial inclusion** — Advocate for rural gap region sites in upcoming trials

## 📋 How to Contribute

We welcome contributions! Open an issue or pull request to add:

1. **Additional clinical trial datasets** — Update with new trials
2. **Provider location updates** — Add verified prosthetic/orthotic provider directories
3. **New region analyses** — Expand to rural Appalachia, Deep South, Tribal Lands
4. **Visualization tools** — Interactive maps, charts, dashboards
5. **Policy recommendations** — Policy interventions for each gap region
6. **Patient stories** — Anonymized testimonials from underserved prosthetic users

## 📖 About the Data

- **Clinical Trials**: ClinicalTrials.gov API (644 studies)
- **Gap Analysis**: OpenStreetMap (neighborhood analysis + route directions)
- **Infrastructure Scores**: OSM features within 50 km radius
- **Generated**: 2026-07-15

## 📜 License

This project is licensed under the **MIT License** — open access for all users.

## 🔗 Links

- **GitHub**: https://github.com/zhub9006/prosthetic-access-atlas
- **Clone**: `git clone https://github.com/zhub9006/prosthetic-access-atlas.git`

## 🤝 Partners & Acknowledgments

- ClinicalTrials.gov (NIH/NLM)
- OpenStreetMap community
- WVU School of Medicine, Marshall University
- University of Kentucky, Pikeville Medical Center
- Methodist Rehabilitation Center (Jackson, MS)
- Shepherd Center (Atlanta, GA)