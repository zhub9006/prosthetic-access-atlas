# Data Sources & Methodology

## Clinical Trial Data
- **Source:** ClinicalTrials.gov API v2
- **Query:** `cond=amputation, term=prosthesis`
- **Date collected:** July 20, 2026
- **Total studies found:** 459 (focused search); 644 (broad search, `cond=prosthetic`)
- **API Limitations:** Significant timeouts and 500 errors during collection; data represents what was retrievable
- **Analysis types:** countByStatus, countByPhase, countBySponsorType, countByCountry

## Gap Analysis (OSM)
- **Source:** OpenStreetMap via OSM MCP tools
- **Search method:** `find_nearby_places` and `search_category` with 30-50 km radii
- **Center points:**
  - Rural West Virginia: Huntington, WV (38.42°N, -82.45°W)
  - Eastern Kentucky: Pikeville, KY (37.48°N, -82.52°W)
  - Mississippi Delta: Greenville, MS (33.41°N, -91.06°W)
- **Categories searched:** healthcare (clinic, doctor, hospital, pharmacy, physiotherapist, rehabilitation), shop
- **Limitations:** Each search limited to ~50 results; some requests timed out (504/429 rate limits); OSM data completeness varies by region

## CPO Distance Estimation
- Estimated based on known CPO locations in metropolitan areas (Charleston, WV; Lexington, KY; Memphis, TN)
- Not verified against actual provider directories for every small town
- Recommendation: validate with state prosthetic societies and Medicare provider data

## Key Definitions
- **CPO:** Certified Prosthetist-Orthotist — board-certified provider of prosthetic and orthotic devices
- **DME:** Durable Medical Equipment — includes prostheses, orthoses, wheelchairs
- **Care gap:** Defined as zero CPO providers within 30 km radius of the representative town

## Recommended Quarterly Refresh Cycle
1. Re-query ClinicalTrials.gov API
2. Re-run OSM nearby-places searches
3. Update country and phase distributions
4. Validate CPO distances against state provider directories
5. Check for new Medicaid expansion updates

## API Endpoints Used
- ClinicalTrials.gov: `https://clinicaltrials.gov/api/v2/studies`
- OpenStreetMap Nominatim: `https://nominatim.openstreetmap.org/search`
- OpenStreetMap Overpass: `https://overpass-api.de/api/interpreter`

## Data Quality
- **Clinical trials:** Retrieved with gaps (API timeouts); 459 focused + 644 broad baseline
- **OSM geographic data:** Successfully retrieved for all three regions
- **CPO provider data:** OSM has limited specialized medical provider coverage; distances are estimates
- **Neighborhood scores:** Some API timeouts; scores may be approximate

*Last updated: July 20, 2026*