# Data Sources

## ClinicalTrials.gov
- API endpoint: https://clinicaltrials.gov/api/v2/studies
- Search terms: "prosthetic" AND "amputation" with prosthetic focus
- Data extraction: status, phase, sponsor, country, NCT ID, title, dates
- Retrieval date: September 2026

## OpenStreetMap (OSM)
- Geocoding: Nominatim API
- Provider search: Overpass API (amenity=healthcare)
- Categories searched: hospital, clinic, health_centre, pharmacy
- Limitation: OSM API experienced connectivity issues during September 2026 data pull; provider data supplemented with known regional information

## Supplemental
- Kaiser Family Foundation: Medicaid expansion status by state (2026)
- CDC/HRSA: Amputation rate estimates by region
- U.S. Census Bureau: Population density, uninsured rates

## Funnel of Evidence
1. ClinicalTrials.gov → trial counts, status, phase, geography
2. OSM/Geocoding → provider locations, distances
3. Public datasets → socioeconomic context (Medicaid, amputation rates, demographics)
4. Synthesis → gap identification and intervention recommendations
