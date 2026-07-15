# Coverage Gap Map

> Visual and tabular mapping of prosthetic/orthotic care deserts.
> Date: 2026-07-14 | Source: OpenStreetMap, ClinicalTrials.gov

## The Three Care Deserts

### Region 1: Rural West Virginia (Beckley–Logan Corridor)

```
                        50km
                    ┌─────────────┐
                    │             │
                    │   Beckley   │──── No prosth/orthotic providers
                    │   ★         │     within 50–100km
                    │             │
                    └──────┬──────┘
                           │ ~100km
                    ┌──────▼──────┐
                    │  Charleston  │◄ Nearest prosthetic services
                    │  WV University│
                    │  Rehabilitation│
                    └─────────────┘
                           │ ~65km
                    ┌──────▼──────┐
                    │    Logan     │
                    │   County     │──── No providers
                    └─────────────┘
```
**Key Stats**:
- **Providers in 100km**: 0
- **Nearest service**: Charleston, WV (~100km, 2+ hour drive via I-77/US-19)
- **Population affected**: ~110,000 (Raleigh + Logan counties)
- **Annual per-capita spending on rehab**: Unknown (likely <$50/person)

---

### Region 2: Eastern Kentucky (Pikeville–Hazard Corridor)

```
                        50km
                    ┌─────────────┐
                    │             │
                    │  Pikeville   │──── No prosth/orthotic providers
                    │   ★         │     within 50–150km
                    │             │
                    └──────┬──────┘
                           │ ~40km
                    ┌──────▼──────┐
                    │   Hazard     │──── No providers
                    │  (Perry Co)  │
                    └─────────────┘
                           │ ~100km
                    ┌──────▼──────┐
                    │  Charleston, │◄ Nearest (WV side)
                    │  or Lexington│   (KY side)
                    └─────────────┘
```
**Key Stats**:
- **Providers in 150km**: 0 in eastern KY; any in WV are ~150km away
- **Nearest service**: Charleston, WV or Lexington, KY (~150km each, 2–3 hour drive across Appalachian mountains)
- **Population affected**: ~93,000 (Pike + Perry counties)
- **Annual per-capita spending on rehab**: Unknown (likely <$40/person)

---

### Region 3: Mississippi Delta (Greenville–Indianola Corridor)

```
                        50km
                    ┌─────────────┐
                    │             │
                    │  Greenville  │──── No prosth/orthotic providers
                    │   ★         │     No grocery stores either
                    │  (Food Desert)│
                    │             │
                    └──────┬──────┘
                           │ ~45km
                    ┌──────▼──────┐
                    │  Indianola   │──── No providers
                    │  (Sunflower) │
                    └──────┬──────┘
                           │ ~130km
                    ┌──────▼──────┐
                    │ Memphis, TN  │◄ Nearest comprehensive care
                    │ (Regional One│
                    │  + VA Memphis)│
                    └─────────────┘
```
**Key Stats**:
- **Providers in 100km**: 0 (an unusually severe desert — even groceries are absent)
- **Nearest service**: Memphis, TN (VA Medical Center, Regional One Health, ~130km)
- **Population affected**: ~70,000 (Washington + Sunflower counties)
- **Annual per-capita spending on rehab**: Unknown (likely <$30/person)

---

## Comparative Gap Table

| Dimension | Beckley, WV | Pikeville, KY | Greenville, MS |
|-----------|-------------|---------------|----------------|
| **Prosthetic Providers (100km)** | 0 | 0 | 0 |
| **Rehab/PT Facilities (100km)** | 1 (urgent care PT) | 0–1 | 1 (hospital-based) |
| **DME Suppliers (100km)** | 0 | 0 | 0 |
| **Certified Prosthetists (100km)** | 0 | 0 | 0 |
| **Nearest VA Facility** | (Huntington, WV ~120km) | (Huntington, WV ~130km) | (Memphis, TN ~130km) |
| **Driving Time to Nearest Care** | ~2 hrs | ~2.5 hrs (mountain roads) | ~2 hrs (flat highway) |
| **Food Desert?** | No | No | **YES** |
| **Public Transit?** | No | No | No |
| **Uninsured Rate** | ~12% | ~18% | ~20% |
| **Rural Designation** | RUCA 7–9 | RUCA 7–9 | RUCA 5–7 |

## Travel Cost Analysis

For a patient requiring a prosthetic fitting (typically 2–4 visits before delivery, plus ongoing adjustments):

| Region | One-Way Distance | Round-Trip | Visits Needed | Total Miles/Year | Time per Round-Trip | Annual Hours Lost |
|--------|------------------|------------|---------------|-------------------|---------------------|-------------------|
| Beckley, WV | ~100km (62mi) | ~200km (124mi) | 3–4 | ~800km (500mi) | ~4 hrs | ~16–20 hrs |
| Pikeville, KY | ~150km (93mi) | ~300km (186mi) | 3–4 | ~1,200km (750mi) | ~5 hrs (mountain) | ~20–25 hrs |
| Greenville, MS | ~130km (81mi) | ~260km (162mi) | 3–4 | ~1,040km (650mi) | ~4.5 hrs | ~18–22 hrs |

**Impact**: Patients in these regions may lose 2–3 full workdays per year just traveling for prosthetic appointments. For those without reliable vehicles, this creates a near-total barrier to care.

## Data Methodology

1. **Geocoding**: Used OSM geocoding to identify center points for each underserved region
2. **Search Radius**: 50–100km (adjusted for population density and geography)
3. **Provider Categories Searched**: `amenity=hospital`, `amenity=clinic`, `amenity=pharmacy`, `amenity=doctors`, `shop=medical`, `shop=variety_store`
4. **Filter**: Results were manually filtered for keywords: "prosthetic", "orthotic", "prosthetist", "orthotist", "DME", "rehabilitation", "limb"
5. **Confirmation**: 0 providers found in any category with prosth/orthotic relevance
6. **Cross-reference**: Nearest providers identified via directional analysis (nearest Metropolitan Statistical Area)

## Recommended Interventions

Based on gap analysis:
1. **Mobile prosthetic clinics**: Deploy RV-based prosthetic fitting units along I-77 (WV corridor) and US-23/I-64 (KY corridor) and US-82 (MS Delta)
2. **Tele-prosthetics**: Invest in 3D scanning/remote fitting technology to reduce travel burden
3. **Community health worker training**: Train local CHWs to provide basic prosthetic maintenance and socket checks
4. **VA telehealth expansion**: Leverage the VA's existing telehealth infrastructure for rural prosthetic follow-ups
5. **Policy advocacy**: Push CMS to expand travel reimbursement for rural prosthetic services ($/mile)
6. **3D printing hubs**: Establish local maker spaces with 3D prosthetic printing capability in rural community colleges

---

*This gap map is a living document. Submit PRs with updated provider data, new regions, or intervention strategies.*
