# Data Sources & Methodology

## Clinical Trial Data

**Source:** ClinicalTrials.gov API v2  
**Query Date:** July 15, 2026  
**Query Parameters:**
- Condition: `prosthetic`
- Sort: Last update post date
- Result count: 10 studies (detail mode), full trend analysis (644 total)
- Additional analyses: status, phase, sponsor type, country

### API Endpoints Used
```
GET /api/v2/studies?query.cond=prosthetic&sort=lastUpdatePostDate&pageSize=10
GET /api/v2/studies/vis/analyze?analysisType=countByStatus&query.cond=prosthetic
GET /api/v2/studies/vis/analyze?analysisType=countByPhase&query.cond=prosthetic
GET /api/v2/studies/vis/analyze?analysisType=countByCountry&query.cond=prosthetic
GET /api/v2/studies/vis/analyze?analysisType=countBySponsorType&query.cond=prosthetic
```

**Limitations:**
- ClinicalTrials.gov API experienced intermittent timeouts (504) and service errors (500)
- Country-level data may have overlapping counts (studies can have multiple sites)
- "Unknown" status indicates records with insufficient metadata
- Only 10 of 644 studies were individually verified; remaining data from trend analysis

## Geographic / Provider Data

**Source:** OpenStreetMap (Overpass API) via OSM MCP Server  
**Query Date:** July 15, 2026  

### Methodology
1. **Geocode** regional center points:
   - Beckley, WV → (37.778, -81.188)
   - Pikeville, KY → (37.479, -82.519)
   - Greenville, MS → (33.411, -91.064)
   - Huntington, WV → (38.419, -82.445)
   - Cleveland, MS → (33.744, -90.725)

2. **Search** for healthcare amenities within 20,000-50,000m radius:
   - Categories: `healthcare` (clinic, doctor, pharmacy, dentist, optometrist)
   - Also searched: `shop` → `medical_equipment` (no results found)

3. **Neighborhood analysis** for livability scores:
   - Radius: 10,000m for each center
   - Categories scored: healthcare, education, groceries, restaurants, parks, shopping, public_transport, services

**Limitations:**
- OSM Overpass API returned HTTP 429 (rate limit), 504 (timeout), and 400 (bad request) errors
- Healthcare category search was the only reliable query; many location-based searches failed
- OSM may underreport prosthetic/orthotic-specific providers (many small O&P shops are not tagged)
- Prosthetists/orthotists may be listed under generic "clinic" or "doctor" tags without specialty annotation
- No commercial provider directories (e.g., American Board for Certification in Orthotics, Prosthetics & Pedorthics) were queried

## Gap Scoring Methodology

Each region scored on:
1. **Provider Density**: Count of prosthetic/orthotic providers per 100k population
2. **Travel Burden**: Average distance to nearest O&P provider
3. **Insurance Access**: Medicaid expansion status + specialty coverage
4. **Infrastructure Score**: Healthcare, education, public transport, services availability

**Gap Severity:**
- 🔴 Critical: 0 providers within 100km + Medicaid non-expansion
- 🟠 High: 1-2 providers within 100km + partial coverage
- 🟡 Moderate: 3-5 providers within 100km
- 🟢 Low: 5+ providers within 50km

## Neighborhood Analysis

Tool: `osm-mcp-server_analyze_neighborhood` (10km radius)

### Beckley, WV Results:
- Healthcare: 8.1/10 (4 features: pharmacy ×3, doctor ×1)
- Education: 9.8/10 (15 schools)
- **No pharmacies or doctors specializing in prosthetics/orthotics**

### Pikeville, KY Results:
- Healthcare: 8.6/10 (4 features within 10km)
- Education: 9.9/10 (20 schools including U. of Pikeville)
- **No prosthetics/orthotics providers**

### Greenville, MS Results:
- Healthcare: 0/10 (0 features within 10km)
- Education: 9.6/10 (18 schools)
- Restaurants: 10.0/10 (14 locations)
- **Only 3 healthcare facilities found in 20km radius — all dentists or general clinic**

---

*Methodology document updated 2026-07-15. Data is current as of this date.*