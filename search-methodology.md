# Search Methodology Documentation

This document describes the data collection methods, search strategies, and limitations for the Prosthetic Access Atlas.

## 1. Clinical Trials Data

### Source
- Database: ClinicalTrials.gov API
- Retrieval dates: 2026-06-17 (trend analysis), 2026-06-25 (study detail retrieval)

### Search Strategies

#### Broad Search ("prosthetic")
- Query term: "prosthetic"
- Total studies returned: 2,169
- Analyses performed: countByStatus, countByCountry, countByPhase

#### Focused Search ("prosthetic limb")
- Query term: "prosthetic limb"
- Total studies returned: 509
- Purpose: Narrow to studies most directly relevant to prosthetic device access

### Why Two Searches?

The broad search reveals the total research infrastructure (rehabilitation, gait training, socket design), while the focused search identifies trials most directly relevant to prosthetic device access. The ratio (2,162 broad vs 509 focused) indicates roughly 77% of prosthetic-related trials address adjacent areas.

### Additional Analysis Types Performed

- **countByCountry**: 2,169 trials across 110+ countries
- **countByPhase**: N/A (58.3%), Unknown (29.9%), Phase 4 (4.2%), Phase 2 (3.6%), Phase 3 (3.2%), Phase 1 (1.6%), Early Phase 1 (0.5%)
- **Detailed study retrieval**: Full protocol data for NCT07204912, NCT06844305, NCT05569967, NCT06821412

### Key Limitations
- AI/ML processing may miss synonyms (e.g., "amputee rehabilitation," "limb loss")
- Multi-country studies counted per site, inflating geographic totals
- "Unknown" status studies (20%) may include paused trials or data errors
- "Prosthetic" may return false positives (e.g., dental prosthetics)

## 2. Provider Gap Analysis

### Source
- Database: OpenStreetMap (OSM) via MCP Geocoding and Search APIs
- Retrieval dates: 2026-06-25 (provider searches), 2026-06-25 (geocoding for Greenville MS)

### Search Strategy

Three underserved regions via CDC Social Vulnerability Index and Amputee Coalition data:

| Region | Center Point | Coordinates |
|--------|-------------|-------------|
| Rural West Virginia | Beckley, Raleigh County | 37.78N, 81.19W |
| Eastern Kentucky | Pikeville, Perry County | 37.52N, 82.81W |
| Mississippi Delta | Greenville, Washington County | 33.41N, 91.06W |

- Radius: 50 km (31 mi) from center point
- Categories: healthcare
- Subcategories: hospital, clinic, pharmacy, doctor, rehabilitation, podiatry, denton, dialysis
- Route analysis: distance verification from region centers to nearest major referral hubs

### Why These Regions?

1. **Rural West Virginia** — High coal-mining injury and diabetes rates; persistent poverty and healthcare deserts
2. **Eastern Kentucky** — Among highest amputation rates in the US due to diabetes and opioid infections
3. **Mississippi Delta** — Highest diabetes prevalence and amputation rates in the nation, especially among Black Americans

### Data Collected Per Region

| Region | Total Facilities | Pharmacies | Clinics | Doctors | Dentists | Rehabilit. | Dialysis | Audiology |
|--------|-----------------|------------|---------|---------|----------|-----------|----------|-----------|
| Rural WV | 29 | 13 | 5 | 2 | 3 | 1 | 1 | 1 |
| Eastern KY | 27 | 7 | 3-4 | 4 | 2 | 1 | 0 | 0 |
| MS Delta | 9+ (50km) / ~20+ (80km) | 4+ | 2-4 | 3-4 | 2-3 | 1 | 1 | 1 |

### Key Limitations
- OSM healthcare data may not capture all private-practice prosthetists/orthotists
- No validation against state licensure databases or Amputee Coalition directories
- 50 km radius may be too conservative for rural areas
- Seasonal factors (weather, road conditions) not accounted for
- Prosthetic specialists may be classified under general categories
- Straight-line distances vs. actual drive times

## 3. Data Integration

Cross-referenced to identify:
- **Innovation-access disconnect**: Where trials happen vs. where need is greatest
- **Evidence-to-practice gap**: Novel technologies not reaching highest-need populations
- **Infrastructure deficit**: No clinical trial sites, teaching hospitals, or residency programs in target regions
- **Comprehensive false-coverage**: Regions have healthcare infrastructure that creates false sense of adequacy, but zero CPO-certified providers

## 4. New Files Added (2026-06-25 Update)

- `active-studies-detail.md` — Detailed profiles of 4 current/recent prosthetic clinical trials
- Updated `clinical-trials-analysis.md` — Full status/country/phase breakdowns with study profiles
- Updated `coverage-gap-analysis.md` — Verified facility counts from OSM searches
- Updated `detailed-provider-inventory.md` — Complete facility listings with contact info
- Updated `research-supplement.md` — Comprehensive verification and methodology documentation

## 5. Recommended Updates

- State licensure database queries for certified prosthetists/orthotists (WV, KY, MS)
- Amputee Coalition provider directory cross-referencing
- Medicaid reimbursement rate analysis by state
- CDC amputation prevalence data by county
- FQHC locations and capabilities
- Transportation route analysis (drive times to nearest prosthetic care)
- Drive-time vs. straight-line distance calculations
- Temporal trend tracking (5-year changes)
