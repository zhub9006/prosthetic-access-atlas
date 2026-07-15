# Data Sources & Methodology

## Clinical Trial Data

### Source
- **Database:** ClinicalTrials.gov
- **API:** CTAPI v2 (latest)
- **Query:** `condition: prosthetic`
- **Date:** July 13, 2026
- **Total Records:** 644 unique studies

### Analysis Methods
1. **Status Analysis:** Counted studies grouped by `overallStatus` field
2. **Country Analysis:** Counted studies by lead sponsor country (using `location.country`)
3. **Phase Analysis:** Counted studies by trial phase (`phase` field)
4. **Key Trial Retrieval:** Fetched detailed metadata for most recently submitted studies

### Limitations
- ClinicalTrials.gov may not capture all prosthetic studies (some are industry-sponsored and may not register)
- "Unknown" status affects 20.8% of studies
- Geographic counts may double-count multi-site studies

---

## Gap Analysis Data

### Source
- **Database:** OpenStreetMap (via Overpass API)
- **Search Categories:** amenity = hospital, clinic, pharmacy, doctors, health_centre, nursing_home, community_health_centre
- **Search Terms:** prosthetic, orthotic, prosthetist, orthotist, O&P, 'prosthetic services'
- **Regions Searched:** Rural West Virginia, Eastern Kentucky, Mississippi Delta
- **Date:** July 13, 2026

### Methodology
1. For each region, identified a representative center point
2. Searched within 30km and 100km radius for healthcare facilities
3. Filtered results for prosthetic/orthotic specialization
4. Verified absence of O&P providers through cross-referencing

### Limitations
- **OSM tagging is incomplete:** Prosthodontists and orthotists are often not tagged in OSM at all
- **Radius may be insufficient:** Some rural residents may need to travel >150km
- **OSM data ≠ ground truth:** Absence of a tag doesn't definitively prove absence of a provider
- **Recommended validation:** Cross-reference with AOPA (American Orthotic & Prosthetic Association) directory and state licensing boards

---

## Recommended Validation Steps

1. Cross-reference with AOPA Member Directory (aopa.org)
2. Check state prosthetics/orthotics licensing boards (WV, KY, MS)
3. Search CMS Physician Compare for O&P providers in these regions
4. Contact State Vocational Rehabilitation agencies for on-the-ground data
5. Verify rural hospital capabilities via CMS Care Compare

---

## Citation Format

If using this data in academic or policy publications:

```
Prosthetic Access Atlas. (2026). Clinical Trial Landscape Analysis 
and Underserved Region Coverage Gaps. Retrieved from
https://github.com/zhub9006/prosthetic-access-atlas
```
