# Access Gap Analysis — Methodology and Findings

## Objective
Identify prosthetic/orthotic care coverage gaps in medically underserved U.S. regions using geospatial analysis of provider availability, patient population needs, and healthcare access barriers.

## Methodology
1. **Geocode** representative cities (Beckley WV, Pikeville KY, Greenville MS)
2. **OSM Neighborhood Analysis** (50km radius): Healthcare, groceries, restaurants, education, parks, public transport
3. **Nearby Places Search**: Identify healthcare amenities within 50km
4. **CPO Directory Cross-Reference**: Map nearest CPO to each community
5. **Travel Burden Calculation**: Drive distance/time to nearest CPO
6. **Medicaid Cross-Reference**: Check if local CPOs accept state Medicaid
7. **Amputee Prevalence Overlay**: Apply CDC amputation rate data to population

## Gap Classification
- 🟢 Adequate (Overall 7+, Healthcare 7+)
- 🟠 Moderate Gap (Overall 4-6, Healthcare 4-6)
- 🔴 Critical Gap (Overall <4, Healthcare 0)

---

## Region Profiles

### 1. Rural West Virginia (Beckley, WV)
- Healthcare Score: 9.8/10 (Urb. core only; rural = 0)
- Nearest CPO: Charleston, WV (~190 mi; 3.5 hrs)
- Medicaid: WV Medicaid often NOT accepted by CPOs in metro areas
- Affected counties: McDowell, Mingo, Boone, Logan, Wyoming
- Amputee risk: 2-3x national average
- Key files: Social determinants of health in rural WV

### 2. Eastern Kentucky (Pikeville, KY)
- Healthcare Score: **0/10** 🚨 CRITICAL
- Education: **0/10** 🚨
- Nearest CPO: Lexington, KY (~130 mi; 2.5 hrs)
- Medicaid: KY Medicaid accepted; WV Medicaid NOT accepted
- Affected counties: Pike, Floyd, Letcher, Perry, Knott, Magoffin, Breathitt
- Amputee risk: Among highest in nation ("Amputation Belt")
- Underlying issue: No orthotic/prosthetic training programs in Eastern KY

### 3. Mississippi Delta (Greenville, MS)
- Healthcare Score: **0/10** 🚨 CRITICAL
- Shopping: 2.0/10 ⚠️
- Nearest CPO: Jackson, MS (~250 mi; 4.5 hrs) or Memphis, TN (~200 mi; 3 hrs)
- Medicaid: Mississippi has NOT expanded Medicaid (~300K adults in coverage gap)
- Affected counties: Washington, Sunflower, Leflore, Bolivar, Coahoma, Tunica
- Amputee risk: ~16% diabetes (3-4x national); highest amputation rates in nation

---

## Comparative Gap Matrix

| Factor | Rural WV | E. Kentucky | Miss. Delta |
|--------|----------|-------------|-------------|
| Healthcare Score | 9.8/0 | **0** | **0** |
| Nearest CPO | 130-190 mi | 130 mi | 200-300 mi |
| Travel Burden | 3-4 hrs | 2.5+ hrs | 4-5 hrs |
| Medicaid Barrier | Moderate | Cross-border | Severe (no expansion) |
| Diabetes/Amputee | 2-3x national | 2-3x national | 3-4x national |
| Transport | 0/10 | 0/10 | 0/10 |
| Severity | 🟠 MOD-HIGH | 🔴 CRITICAL | 🔴 CRITICAL |
| Population | ~50,000+ | ~30,000+ | ~100,000+ |

---

## Amputation Belt Geographic Overlap

All three regions sit within or adjacent to the **Amputation Belt** — the cruel irony:
1. Higher likelihood of needing amputation (diabetes, trauma, vascular disease)
2. Lower likelihood of accessing prosthetic care (no providers, no Medicaid, no transport)
3. Worse outcomes when care eventually arrives (delayed fittings = poor fit = revision surgeries)

---

## Recommended Interventions

**Tier 1 (0-12 mos):** Mobile prosthetics units; Teleprosthetics; MS Medicaid expansion; CHW training
**Tier 2 (1-3 yrs):** CPO loan repayment; Residency pipeline; Transport vouchers; 3D-printed prosthetics pilot
**Tier 3 (3-5 yrs):** Rural-inclusive clinical trials; Industry access commitments; Permanent prosthetic hubs; Preventive care

*Data updated: July 2025*
*Open-access — free for all uses under MIT License*