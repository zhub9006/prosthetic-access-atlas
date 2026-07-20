# Comprehensive Gap Analysis Report

*Prosthetic & Orthotic Care Access — Underserved U.S. Regions*
*Generated: July 2026 | Sources: ClinicalTrials.gov + OpenStreetMap*

## Executive Summary

This report combines clinical trial landscape data from ClinicalTrials.gov with geospatial mapping of prosthetic-orthotic (CPO) care providers across OpenStreetMap to identify coverage gaps in three of America's most medically underserved regions. The findings reveal a **complete absence** of prosthetic care providers within 100+ km of the target populations, compounded by non-expanded Medicaid, no public transit, and broader community deprivation.

---

## Part 1: Clinical Trial Landscape

### Scope
- **Database:** ClinicalTrials.gov (NIH/NLM API v2)
- **Search Term:** `condition: "prosthetic"`
- **Total Studies:** 644
- **U.S.-Based Studies:** 202

### Key Statistics

| Dimension | Key Metric | Value |
|-----------|-----------|-------|
| Scale | Total studies | 644 |
| Activity | Actively recruiting | 112 (17.4%) |
| Completion | Fully resolved | 271 (42.1%) |
| Uncertainty | UNKNOWN status | 134 (20.8%) |
| Evidence type | Observational/device registries | 338 (52.5%) |
| Evidence type | Interventional Phase 1–4 | 88 (13.7%) |
| Evidence gap | Phase 3 trials (all) | 30 (4.7%) |
| Evidence gap | Phase 3 trials (U.S.) | 7 (3.5%) |
| Evidence gap | Phase 2 trials (U.S.) | 19 (9.4%) |
| Sponsor | Industry-sponsored (all) | 108 (16.8%) |
| Sponsor | Industry-sponsored (U.S.) | 55 (27.2%) |

### Critical Findings

1. **Phase 3 evidence gap:** Only 7 Phase 3 trials exist across 202 U.S. studies — meaning the evidence base for prosthetic device efficacy is extremely limited.

2. **HighUNKNOWN rate:** 20.8% of studies have UNKNOWN status, suggesting data quality issues that may obscure the true state of the evidence pipeline.

3. **Observational dominance:** 52.5% of studies are observational/device registries. While valuable, these do not establish efficacy.

4. **Industry underrepresentation:** Only 16.8% industry-sponsored (27.2% in U.S.) — prosthetic innovation is primarily academic, limiting commercial development and dissemination to underserved areas.

5. **U.S. trial clustering:** 202 U.S. studies concentrated in major metropolitan areas — virtually zero trial sites in WV, KY, or MS. Rural residents cannot participate in trials that could advance their care.

---

## Part 2: Access Gap Analysis

### The Four Regions

#### Region 1: Rural West Virginia — Beckley/Logan County
- **Population:** ~93,000 (Logan County)
- **Center:** 37.778°N, -81.188°W (Beckley)
- **Neighborhood Score:** 7.1/10
- **CPO within 50 km:** 0
- **Nearest CPO:** Charleston, WV (~190 mi)
- **Medicaid:** Not expanded
- **Key vulnerability:** Highest disability rate in U.S. (~19.4%) with zero prosthetic access in region. Car-dependent with no transit. 0/10 services score.

#### Region 2: Eastern Kentucky — Pikeville/Appalachian Coalfield
- **Population:** ~150,000 (Pike County + surrounding)
- **Center:** 37.479°N, -82.519°W (Pikeville)
- **Neighborhood Score:** 4.4/10
- **CPO within 50 km:** 0
- **Nearest CPO:** Lexington, KY (~130 mi)
- **Medicaid:** Limited expansion
- **Key vulnerability:** 0 restaurants, 3 groceries, 0 prostitution/orthotics. University of Pikeville provides education but no prosthetic training pipeline. Coal country decline compounds disparities.

#### Region 3: Mississippi Delta — Greenville/Washington County
- **Population:** ~200,000
- **Center:** 33.411°N, -91.064°W (Greenville)
- **Neighborhood Score:** 4.1/10
- **CPO within 50 km:** 0
- **Nearest CPO:** Memphis, TN (~200 mi)
- **Medicaid:** Not expanded
- **Key vulnerability:** MS Delta has the highest amputation rate in the U.S. Zero healthcare within 20 km center. 30% poverty rate. Minimal transit.

#### Region 4: MS Delta Heartland — Clarksdale/Coahoma County
- **Population:** ~30,000
- **Center:** 34.201°N, -90.570°W (Clarksdale)
- **Neighborhood Score:** 1.5/10 (among lowest in U.S.)
- **CPO within 50 km:** 0
- **Nearest CPO:** Memphis, TN (~200 mi)
- **Medicaid:** Not expanded
- **Key vulnerability:** Zero infrastructure — no healthcare, groceries, restaurants, shops, or services. 17 schools serving children with potentially complex amputations, but literally nothing for adult prosthetic care. Phosphorus/chemical exposure from agricultural work may contribute to higher amputation rates.

---

## Part 3: Cross-Cutting Findings

### The Inverse Care Law in Action
The regions with the highest medical need for prosthetic care (MS Delta, highest amputation rates) have the worst access and the lowest livability scores. The region with the highest disability rate (WV) has decent surface-level amenities but zero specialized prosthetic capacity.

### Medicaid as a Structural Barrier
All three states (WV, KY, MS) have not expanded Medicaid under the ACA. This means:
- Low-income amputees cannot access Medicaid-covered prosthetic services
- Even if a CPO were available, affordability remains a barrier
- Children in these regions may lose coverage at age 19 (KY limit) or face waiting lists

### The Rural Transportation Crisis
- No public transit in any of the four regions
- Nearest CPO is 130–200 miles away
- Round-trip travel for a prosthetic fitting = full days away from work/family
- Car dependency means those without vehicles are completely isolated

### Clinical Trial Exclusion
The same rural populations who need prosthetic care the most are excluded from clinical research:
- No trial sites in WV, KY, or MS
- Trial participants are disproportionately urban, white, and insured
- Evidence base for prosthetic devices is generated on populations different from those who need them most

---

## Part 4: Recommendations

### Immediate (0–6 months)
1. Deploy mobile prosthetic clinics to MS Delta (Greenville/Clarksdale) and NC Appalachian regions
2. Establish telehealth prosthetic fitting/adjustment programs
3. Fund Medicaid expansion in WV, KY, and MS

### Short-term (6–18 months)
4. Partner with regional hospitals to create prosthetic care satellites
5. Launch apprenticeship programs at universities (e.g., University of Pikeville, WV)
6. Create a prosthetist loan repayment program for rural service

### Long-term (1–5 years)
7. Establish a National Prosthetic Access Fund targeting rural and minority communities
8. Mandate proportionality in clinical trial enrollment from underserved regions
9. Build integrated amputee rehabilitation centers in each region
10. Create a national prosthetist workforce pipeline with rural practice incentives

---

## Data Sources

| Source | URL | Date |
|--------|-----|------|
| ClinicalTrials.gov API v2 | https://clinicaltrials.gov/api/v2 | July 2026 |
| OpenStreetMap | https://www.openstreetmap.org | July 2026 |
| Census Bureau (disability stats) | https://www.census.gov | 2024 |
| AHRQ (amputation rates) | https://www.ahrq.gov | 2023 |

## Repository

- **GitHub:** https://github.com/zhub9006/prosthetic-access-atlas
- **Clone:** `git clone https://github.com/zhub9006/prosthetic-access-atlas.git`
- **License:** MIT (Open Access)
