# Methodology & Reproducibility

## How This Data Was Generated

### Step 1: Clinical Trial Harvesting
```
Query: ClinicalTrials.gov API v2
Parameters:
  - cond: prosthetic, amputation, prosthesis
  - term: prosthetic limb, amputation, prosthesis
  - Filters: All statuses, phases, countries
Result: 644 unique studies
```

### Step 2: Trend Analysis
```
Analyzed by:
  - Status (10 categories)
  - Phase (6 categories)
  - Country (50+ countries)
  - Sponsor Type (6 categories)
Tools: ClinicalTrials.gov analyze_trends endpoint
```

### Step 3: Gap Analysis
```
For each underserved region:
  1. Geocode center point (OSM geocoding)
  2. Search OSM within 30km for healthcare providers
  3. Extrapolate to 50-100km for nearest O&P estimation
  4. Cross-reference with known regional hospitals
```

### Step 4: Infrastructure Scoring
```
Neighborhood analysis (OSM):
  - Categories: groceries, restaurants, healthcare, education, parks, transport, shopping
  - Radius: 1km (default), 30km (extended)
  - Output: Composite score 0-10
```

## Reproducibility Checklist

- [x] Clinical trial queries are traceable to API endpoints
- [x] Geographic coordinates are verifiable via OSM
- [x] Provider counts are based on OSM data (open, not proprietary)
- [x] All NCT IDs link to public ClinicalTrials.gov pages
- [x] Data freshness is timestamped

## Known Issues

- OSM data may not capture all small O&P businesses
- ClinicalTrials.gov API had intermittent timeouts during analysis
- Multi-site studies may appear in multiple country counts
- Provider availability is not real-time verified

## Suggestions for Replication

1. Clone this repo and run `git pull` for latest updates
2. Visit ClinicalTrials.gov and verify highlighted NCT IDs
3. Use https://overpass-turbo.eu/ to individually verify O&P providers
4. Cross-reference with HHS Health Professional Shortage Area database
5. Add more regions using the same methodology
