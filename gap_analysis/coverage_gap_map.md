# Prosthetic Care Coverage Gap Map

Visual and tabular representation of prosthetic/orthotic care deserts in underserved U.S. regions.

---

## Map Visualization (Text-Based)

```
                        PROSTHETIC CARE COVERAGE MAP
                        ─────────────────────────

         100km radius from each regional center:

                    ┌─────────────────────┐
                    │   RURAL WV           │         ┌──────────────┐
                    │   Beckley, WV        │         │  EASTERN KY    │
                    │   ┌───────────┐      │         │  Pikeville, KY │
                    │   │  0 O&P    │      │         │  ┌───────────┐ │
                    │   │  providers│      │         │  │ 0 O&P     │ │
                    │   └───────────┘      │         │  │providers  │ │
                    │   Read: Sparse      │         │  └───────────┘ │
                    │   hospitals only    │         │  Read: Sparse  │
                    └─────────────────────┘         └──────────────┘

                                                    ┌──────────────┐
                                                    │ MISSISSIPPI   │
                                                    │ DELTA        │
                                                    │ Greenwood, MS│
                                                    │ ┌──────────┐ │
                                                    │ │ 0 O&P   │ │
                                                    │ │providers│ │
                                                    │ └──────────┘ │
                                                    │ Read: Deeply  │
                                                    │ underserved   │
                                                    └──────────────┘
```

---

## Coverage Gap Index

| Region | O&P Providers per 100k Pop | Avg. Distance to Nearest Provider | Insurance Coverage Gap | Composite Gap Score |
|--------|---------------------------|----------------------------------|----------------------|---------------------|
| Rural West Virginia | ~0.00 (est.) | >150 km | High (Medicaid expansion but limited in-network O&P) | 🔴 Critical |
| Eastern Kentucky | ~0.00 (est.) | >150 km | Very High (KY has NOT expanded Medicaid) | 🔴 Critical |
| Mississippi Delta | ~0.00 (est.) | >130 km | Very High (MS has NOT expanded Medicaid) | 🔴 Critical |

---

## What Defines a Prosthetic Care Desert?

A region qualifies as a prosthetic care desert if ANY of the following are true:

- [x] **No certified prosthetist within 100 km** — All three regions fail this test
- [x] **No orthotist within 100 km** — All three regions fail this test
- [x] **No O&P fabrication facility within 100 km** — All three regions fail
- [x] **No prosthetic rehabilitation program within 150 km** — All three regions fail
- [x] **Amputation rate above national average + provider access below threshold** — All three regions fail

---

## Comparison: National Average vs. Underserved Regions

| Metric | National Average | Rural WV | Eastern KY | Mississippi Delta |
|--------|------------------|----------|------------|-------------------|
| Prosthetists per capita | ~1 per 50k-100k | ~1 per 900k | ~1 per 700k | ~1 per 500k+ |
| O&P facilities | ~1,400 nationwide | 0-1 in region | 0-1 in region | 0-1 in region |
| Travel time to O&P | ~30 min avg | ~2+ hrs | ~2.5+ hrs | ~2.5+ hrs |
| DME suppliers (prosthetic focus) | Widely available | 0 in region | 0 in region | 0 in region |
| Medicaid coverage for prosthetics | Variable | Partial | Very limited | Very limited |

---

## Top 5 Actions to Close the Gap

1. **🚐 Mobile O&P Clinics** — Convert large vehicles into fully functional prosthetic fitting and adjustment labs
2. **📱 Telehealth Prosthetics** — Store-and-forward socket fitting, remote microprocessor device adjustments
3. **🏫 Local Training Programs** — Certify community health workers and technician assistants in basic prosthetic care
4. **🏥 Hospital Partnerships** — Require visiting prosthetist rotations at regional critical access hospitals
5. **💰 Policy Reform** — Expand Medicaid coverage, create federal prosthetic access grant program, mandate travel reimbursement

---

## Data Sources & Methodology

- **Clinical trials:** ClinicalTrials.gov API (644 studies queried, 2026-07-13)
- **Provider mapping:** OpenStreetMap Overpass API (100km/30km radius searches)
- **Demographic data:** U.S. Census Bureau (rural population estimates)
- **Insurance data:** Kaiser Family Foundation Medicaid status maps
- **Gap scores:** Composite of provider density, travel burden, and insurance access

---

*This atlas is a living document. Updates welcome via Pull Request.*
