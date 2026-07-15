# Data Sources & Methodology

## Clinical Trial Data

### Source: ClinicalTrials.gov API
- **API Endpoint**: `https://clinicaltrials.gov/api/v2/studies`
- **Date of Analysis**: July 2026
- **Query Parameters**:
  - Condition: `prosthetic`, `amputation`, `prosthesis`
  - Term: `prosthetic limb`, `amputation`, `prosthesis`
  - Filters: All statuses, all phases, all countries
- **Total Studies Retrieved**: 644 (unique studies)
- **Methodology Notes**:
  - Analysis performed using ClinicalTrials.gov v2 API
  - Trend aggregation across status, phase, country, and sponsor dimensions
  - Studies with multiple conditions/locations may be counted multiple times

### Analyzed Dimensions
- **Status**: COMPLETED, RECRUITING, UNKNOWN, NOT_YET_RECRUITING, etc.
- **Phase**: EARLY_PHASE1, PHASE1, PHASE2, PHASE3, PHASE4, N/A
- **Country**: Geographic distribution of study sites
- **Sponsor Type**: Academic/Government vs. Industry vs. Federal

### Key Study Data
- **MIRA Trial** (NCT05768802): Full structured data from ClinicalTrials.gov
- **PROINGA** (NCT07519746): Gaza conflict-zone lower-limb satisfaction study
- **MPK-K2** (NCT06498245): Microprocessor knee RCT for K2-level ambulators

---

## Gap Analysis Data

### Source: OpenStreetMap (via Overpass API)
- **Method**: Geographic bounding-box and radius searches around target regions
- **Search Radius**: 30km for detailed healthcare; 50-100km for gap extrapolation
- **Categories Searched**: `healthcare`, `amenity`, `pharmacy`, `hospital`, `clinic`
- **Providers Specifically Searched For**:
  - Prosthetist
  - Orthotist
  - O&P (Orthotics & Prosthetics) clinic
  - Certified Orthotic Fitter
  - Rehab hospital (for prosthetic rehab programs)

### Results
| Region | Prosthetic/Orthotic Providers Found | Nearest O&P (estimated) |
|--------|-------------------------------------|-------------------------|
| Beckley, WV | 0 | Charleston, WV (~100km) |
| Hazard/Pikeville, KY | 0 | Lexington, KY (~160km) |
| Cleveland/Greenville, MS | 0 | Memphis, TN (~130km) |

### Identified Infrastructure (non-O&P)

**Beckley, WV (37.78, -81.19)**:
- Raleigh General Hospital (37.787808, -81.201766)
- MedExpress urgent care (37.8027516, -81.1837815)
- Anchor Medical LLC (37.7932784, -81.117786)
- CVS Pharmacy, Beaver (37.750599, -81.1360385)
- Walgreens, Beaver (37.7484415, -81.1350834)
- CVS Pharmacy, Fayetteville (38.032451, -81.1242828)
- Walgreens, Oak Hill (37.9845446, -81.1377133)
- Primary Care Plus (37.7699869, -81.1576383)
- Liberty Dental Centers (37.8017549, -81.1781779)

**Greenville, MS (33.41, -91.06)**:
- The Greenville Clinic (33.3819143, -91.0291499)
- Southeast Rehabilitation Hospital, Lake Village AR (33.3147629, -91.2903316)
- Shelby Drug Store (33.9478467, -90.767517)
- Michelle Seard-Higgins DMD PLLC (33.4062507, -91.0305699)
- Dental Group of Greenville (33.3481607, -91.0431873)

**Hindman/Pikeville, KY (37.34, -82.98)**:
- No healthcare infrastructure captured in 30km search (extremely rural)
- Regional referral centers in Hazard, Pikeville, and Hindman

---

## Methodology

1. **Clinical Trial Harvesting**:
   - Query ClinicalTrials.gov for all studies tagged with `prosthetic`, `amputation`, or `prosthesis`
   - Aggregate by status, phase, country, and sponsor
   - Identify most recent and active studies

2. **Geographic Gap Analysis**:
   - Select representative towns in each underserved region
   - Geocode to precise coordinates
   - Search OpenStreetMap within 30km radius for healthcare providers
   - Extrapolate to 50-100km radius for nearest O&P estimation
   - Cross-reference with known regional referral centers

3. **Infrastructure Scoring**:
   - Use neighborhood analysis (OSM) to score amenities
   - Categories: groceries, restaurants, healthcare, education, parks, transport, shopping
   - Composite score on 0-10 scale

4. **Gap Severity Classification**:
   - Red (Critical): 0 providers within 100km; high disease burden
   - Orange (Severe): 0-1 providers within 100km; moderate burden
   - Yellow (Moderate): 1-3 providers; reasonable but limited
   - Green (Adequate): 3+ providers; local access feasible

---

## Limitations

- OSM data may not capture all providers (especially smaller O&P businesses)
- ClinicalTrials.gov data may include studies that have since been terminated or unknown
- Counts may overlap (multi-site studies counted in multiple countries)
- Radius analysis is proxy; actual O&P access depends on insurance, referral patterns, and device availability
- Real-time provider availability is not verified

---

## API References

- ClinicalTrials.gov API: https://clinicaltrials.gov/api/v2/studies
- OpenStreetMap Overpass API: https://overpass-turbo.eu/
- GitHub Repository: https://github.com/zhub9006/prosthetic-access-atlas
