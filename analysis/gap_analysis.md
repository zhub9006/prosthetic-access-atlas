# Gap Analysis Methodology

## Methodology

### Data Collection
- **Clinical Trial Source:** ClinicalTrials.gov API (search: prosthetic care, prosthetic limb)
- **Provider Source:** OpenStreetMap, ABC Directory, Hanger Clinic network
- **Demographic Source:** CDC, HRSA, US Census Bureau

### Gap Scoring (0-5 scale)
| Factor | Weight | Scoring |
|--------|--------|---------|
| CPO distance | 30% | 0=within 20 mi, 3=50-100 mi, 5=100+ mi |
| Medicaid acceptance | 20% | 0=widely accepted, 3=limited, 5=none |
| Amputation rate | 20% | 0=below avg, 3=2x avg, 5=3x+ avg |
| Public transit | 15% | 0=available, 5=none |
| Inpatient rehab | 15% | 0=within 50 mi, 5=none |

### Scoring Results
- **Rural WV:** 1/5 (CPO ~190 mi away, but WV Medicaid limited coverage)
- **Eastern KY:** 1/5 (CPO ~130 mi away, but KY Medicaid accepted in Lexington; deep isolation)
- **Mississippi Delta:** 0/5 (CPO 200-250 mi away; MS no Medicaid expansion; highest amputations)

### Limitations
- OSM provider data may be incomplete; ABC directory verification needed
- Amputation rates vary by county; state-level data used as proxy
- Medicaid policies change; verify current status
- Cultural and socioeconomic factors not fully captured in numbers

### Next Steps
1. Conduct on-the-ground CPO provider verification in each region
2. Collect patient testimony for qualitative data
3. Update provider map quarterly
4. Advocate for mobile prosthetic clinics with health policy stakeholders
5. Partner with VA and HRSA for evidence-based intervention design
6. Submit manuscript to JAMA or Archives of PM&R