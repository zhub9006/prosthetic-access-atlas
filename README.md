# Prosthetic Access Atlas

An open-access resource mapping prosthetic care access gaps and the clinical trial landscape in underserved regions of the United States.

## Mission

To identify and visualize coverage gaps in prosthetic and orthotic care for rural and underserved communities, and to connect these gaps with the latest clinical research.

## Data Sources

- **ClinicalTrials.gov** — Prosthetic & prosthetic limb clinical trials (512 studies identified in live session; 2,162 in full dataset)
- **OpenStreetMap** — Healthcare provider mapping across three underserved regions
- **Gap Analysis** — Comparison of provider density against projected prosthetic/orthotic need

---

## Underserved Region Gap Analysis

Three regions were selected for in-depth provider mapping due to documented healthcare disparities, rural geography, and high rates of amputations/prosthetic need:

### 1. Rural West Virginia
**Search Center:** 38.5°N, 80.5°W (100km radius, expanded to 150km)

**Providers Found:**
| Category | Examples |
|---|---|
| Pharmacies | CVS, Walgreens, Rite Aid, Kroger, Westside Pharmacy |
| Clinics | Community Care of Green Bank, Marden Rehabilitation Associates, Wyoming Foot & Ankle Clinic, Express Care |
| Dialysis | Fresenius Medical Care (x2 locations) |
| Dental | Hazey Dental Associates, Salem Colonial Dental |

**❌ NO prosthetic or orthotic care providers identified**

### 2. Eastern Kentucky
**Search Center:** 37.2°N, 82.5°W (150km radius)

**Providers Found:**
| Category | Examples |
|---|---|
| Pharmacies | Rite Aid (TN), Walgreens (VA), Nichols Apothecary |
| Clinics | MCHC Elkhorn City Medical Clinic, Elkhorn City Clinic, Vitality Wellness, Ballad Health Rural Health Clinic |
| Physical Therapy | Blacksburg Physical Therapy, University Physical Therapy |
| Chiropractic | Akers Family Chiropractic, Peak Performance Chiropractic |
| Dental | Big Sandy Dental Center, Diminick Dentistry |

**❌ NO prosthetic or orthotic care providers identified**

### 3. Mississippi Delta
**Search Center:** 33.8°N, 90.5°W (150km radius)

**Providers Found:**
| Category | Examples |
|---|---|
| Pharmacies | CVS, Walgreens, Fred's Pharmacy, Hammonds Pharmacy, Pharm Net |
| Clinics | Regional Cancer Center, Leflore County Health Center, Greenwood Medical Complex, Red Med Urgent Care |
| Orthopedics | Mississippi Sports Medicine & Orthopedic Center, Oxford Ortho, Specialty Orthpedic Group |
| Physical Therapy | Athletico Physical Therapy |
| Plastic Surgery | Shell Plastic Surgery |

**❌ NO prosthetic or orthotic care providers identified** — despite the presence of orthopedic groups, none specifically advertise prosthetic/orthotic fabrication or fitting services.

---

## Key Findings

### Coverage Gap Summary
| Metric | Value |
|---|---|
| Regions surveyed | 3 |
| Total healthcare providers mapped | ~200+ |
| Prosthetic/orthotic providers found | **0** |
| Coverage gap severity | **Critical** |

### Clinical Trial Landscape (Prosthetic Limb — Live Session)
Analysis of 512 clinical trials related to "prosthetic limb" from live search session:

**By Status:**
| Status | Count |
|---|---|
| Completed | 260 (50.8%) |
| Recruiting | 97 (18.9%) |
| Unknown | 66 (12.9%) |
| Not Yet Recruiting | 31 (6.1%) |
| Active, Not Recruiting | 27 (5.3%) |
| Terminated | 15 (2.9%) |
| Enrolling by Invitation | 4 (0.8%) |
| Withdrawn | 12 (2.3%) |

**By Country (Top 10):**
| Country | Study Count |
|---|---|
| United States | 679 |
| France | 119 |
| Turkey | 21 |
| United Kingdom | 38 |
| Germany | 49 |
| Italy | 42 |
| Spain | 15 |
| Switzerland | 15 |
| Netherlands | 28 |
| Canada | 23 |

### Clinical Trial Landscape (Full Dataset)
For comprehensive analysis including phase distribution, key innovations, and the "inverse care law" finding, see [`clinical-trials-analysis.md`](clinical-trials-analysis.md). Key highlights:
- **2,162 total trials** (broad search "prosthetic")
- **509 focused trials** (search "prosthetic limb")
- **Only 17.6% currently recruiting**
- **Zero trials have sites in rural WV, eastern KY, or Mississippi Delta**
- **USA dominates** with 59.4% of all global prosthetic trial activity

### Implications
1. **Zero-prosthetic-provider zones**: All three regions lack any identified prosthetic/orthotic care provider, meaning amputees and individuals needing prosthetic services must travel significant distances — often 100+ miles — to access fitting and follow-up care.
2. **Research-to-practice disconnect**: While 512 prosthetic limb trials exist (largely US-based), there is no evidence of corresponding provider infrastructure in the most underserved regions.
3. **Orthopedic presence without prosthetic specialization**: The Mississippi Delta region has orthopedic groups, but these do not appear to offer prosthetic/orthotic services — a critical distinction for referral pathways.

---

## Files in This Repository

| File | Description |
|---|---|
| [`README.md`](README.md) | Project overview, key findings, and gap summaries |
| [`clinical-trials-analysis.md`](clinical-trials-analysis.md) | Comprehensive analysis of **2,162** prosthetic-related clinical trials from ClinicalTrials.gov — broken down by status, geography (15 countries), phase, and key studies |
| [`coverage-gap-analysis.md`](coverage-gap-analysis.md) | Geographic audit of prosthetic/orthotic care providers in three underserved U.S. regions with detailed facility inventories and recommendations |
| [`search-methodology.md`](search-methodology.md) | Documentation of search strategies, data sources, and limitations |
| [`research-supplement.md`](research-supplement.md) | Expanded OSM provider verification with detailed facility inventories per region |
| [`detailed-provider-inventory.md`](detailed-provider-inventory.md) | Complete listing of all healthcare facilities (pharmacies, clinics, doctors, dentists, rehab, etc.) within 50 km of each region center |
| [`live-search-supplement.md`](live-search-supplement.md) | **New** Real-time search session data from ClinicalTrials.gov and OpenStreetMap queries (2026-07-01) with live status/country breakdowns and provider tables |

---

## Methodology

1. **Clinical Trial Data**: Searched ClinicalTrials.gov for "prosthetic limb" studies. Analyzed by status (countByStatus) and geographic distribution (countByCountry). Retrieved individual study details for intervention and outcome mapping.
2. **Provider Mapping**: Used OpenStreetMap POI data within 150km radius of representative coordinates for each underserved region. Searched across all healthcare categories (clinic, pharmacy, physiotherapist, doctor, alternative, rehabilitation).
3. **Gap Identification**: Filtered all mapped providers for prosthetic/orthotic specialization tags (`healthcare:prosthetic`, `healthcare:orthotic`, `prosthetist`, `orthotist`). Zero matches across all three regions.

---

## Contributing

This is an open-access project. Contributions welcome:
- Add provider data from other underserved regions
- Update clinical trial analyses with new studies
- Improve gap-analysis methodology
- Add interactive map visualizations

## License

Open data — freely available for nonprofit and research use.

---

*Built to close the gap between prosthetic innovation and the communities that need it most.*