# Search Methodology Documentation

This document describes the data collection methods, search strategies, and limitations for the Prosthetic Access Atlas.

## 1. Clinical Trials Data

### Source
- Database: ClinicalTrials.gov API
- Retrieval date: 2026-06-17

### Search Strategies

#### Broad Search ("prosthetic")
- Query term: "prosthetic"
- Total studies returned: 2,162
- Analyses performed: countByStatus, countByCountry, countByPhase, countBySponsorType

#### Focused Search ("prosthetic limb")
- Query term: "prosthetic limb"
- Total studies returned: 509
- Purpose: Narrow to studies specifically about prosthetic limb devices

### Why Two Searches?

The broad search reveals the total research infrastructure (rehabilitation, gait training, socket design), while the focused search identifies trials most directly relevant to prosthetic device access. The ratio (2,162 broad vs 509 focused) indicates roughly 77% of prosthetic-related trials address adjacent areas.

### Key Limitations
- AI/ML processing may miss synonyms (e.g., "amputee rehabilitation," "limb loss")
- Multi-country studies counted per site, inflating geographic totals
- "Unknown" status studies (20%) may include paused trials or data errors
- "Prosthetic" may return false positives (e.g., dental prosthetics)

## 2. Provider Gap Analysis

### Source
- Database: OpenStreetMap (OSM) via MCP Geocoding and Search APIs
- Retrieval date: 2026-06-17

### Search Strategy

Three underserved regions via CDC Social Vulnerability Index and Amputee Coalition data:

| Region | Center Point | Coordinates |
|--------|-------------|-------------|
| Rural West Virginia | Beckley, Raleigh County | 37.78N, 81.19W |
| Eastern Kentucky | Pikeville, Perry County | 37.48N, 82.52W |
| Mississippi Delta | Greenville, Washington County | 33.41N, 91.06W |

- Radius: 50 km (31 mi) from center point
- Categories: health, amenity
- Subcategories: hospital, clinic, pharmacy, doctor, rehabilitation, podiatry

### Why These Regions?

1. Rural West Virginia - High coal-mining injury and diabetes rates; persistent poverty
2. Eastern Kentucky - Among highest amputation rates due to diabetes and opioid infections
3. Mississippi Delta - Highest diabetes and amputation rates in nation, especially among Black Americans

### Key Limitations
- OSM data may not capture all private-practice prosthetists
- No validation against state licensure databases or Amputee Coalition directories
- 50 km radius may be too conservative for rural areas
- Seasonal factors not accounted for
- Prosthetic specialists may be classified under general categories

## 3. Data Integration

Cross-referenced to identify:
- Innovation-access disconnect: Where trials happen vs. where need is greatest
- Evidence-to-practice gap: Novel technologies not reaching highest-need populations
- Infrastructure deficit: No clinical trial sites, teaching hospitals, or residency programs in target regions

## 4. Recommended Updates

- State licensure database queries for certified prosthetists/orthotists (CPOs)
- Amputee Coalition provider directory cross-referencing
- Medicaid reimbursement rate analysis by state
- CDC amputation prevalence data by county
- FQHC locations and capabilities
- Transportation route analysis (drive times to nearest prosthetic care)