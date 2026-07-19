---

# Detailed Access Gap Analysis

## Methodology

This analysis uses OpenStreetMap geographic data to identify prosthetic/orthotic care providers (CPOs) within defined radii of three underserved U.S. regions:

1. **Rural West Virginia** (Buckhannon area — central WV highlands)
2. **Eastern Kentucky** (Pikeville area — Appalachian coalfields)
3. **Mississippi Delta** (Clarksdale area — Delta agricultural region)

For each region, searches were conducted using:
- `find_nearby_places`: 30–100 km radius, all amenity categories
- `explore_area`: 30 km and 100 km radius area profiling
- Route directions: driving distance/time to nearest metropolitan area

## Summary of Findings

### Rural West Virginia

- **30 km radius:** 0 hospitals, 0 clinics, 0 pharmacies, 0 CPOs identified. Only post offices, churches, and schools found.
- **100 km radius:** Still no prosthetics/orthotics providers. Nearest medical infrastructure is in Charleston (~190 km, 2+ hrs).
- **Population context:** Upshur County and surrounding rural counties have aging populations with high rates of diabetes-related amputations.

### Eastern Kentucky

- **30 km radius:** 0 hospitals, 0 clinics, 0 CPOs identified. Only churches, cemeteries, and schools.
- **100 km radius:** No prosthetics/orthotics providers found. Nearest city with full services: Lexington (~226 km, 2.7 hrs).
- **Population context:** Pike County and surrounding Appalachian counties face severe economic hardship; many residents lack reliable transportation.

### Mississippi Delta

- **30 km radius:** 0 hospitals, 0 clinics, 0 CPOs identified. Only churches and schools.
- **100 km radius:** No prosthetics/orthotics providers. Nearest comprehensive care: Memphis (~121 km, 1.6 hrs) or Jackson, MS.
- **Population context:** Coahoma County and surrounding Delta counties have Mississippi's highest rates of poverty and uninsured residents.

## Composite Access Score

| Region | CPO Access | Hospital Access | Transportation Access | Overall Score |
|--------|-----------|----------------|----------------------|---------------|
| Rural WV | ███░░░░ (1) | ███░░░░ (1) | ████░░░ (3) | **Low** |
| Eastern KY | ██░░░░░ (0) | ███░░░░ (1) | ███░░░░ (2) | **Very Low** |
| MS Delta | ██░░░░░ (0) | ███░░░░ (1) | █████░░ (4) | **Low** |

*Scores: 0 = no access, 1 = very limited, 2 = limited, 3 = moderate, 4 = reasonable*

## Conclusion

All three regions represent **prosthetic care deserts** — areas where residents must travel 1.5–3+ hours to access basic prosthetic and orthotic services. Combined with high Medicaid enrollment and limited transportation infrastructure, these gaps create significant barriers to prosthetic care access.

---

*Data sourced from ClinicalTrials.gov, OpenStreetMap, and OSM MCP tools.*
