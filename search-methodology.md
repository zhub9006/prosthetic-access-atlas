# Search Methodology Documentation

This document describes the data collection methods, search strategies, and limitations for the Prosthetic Access Atlas.

## 1. Clinical Trials Data

### Source
- Database: ClinicalTrials.gov API (v2)
- Retrieval dates: 2026-06-23, 2026-06-26

### Search Strategies

#### Broad Search ("prosthetic")
- Query term: "prosthetic"
- Total studies returned: **2,168** (as of 2026-06-26)
- Analyses performed: countByStatus, countByCountry, countByPhase

#### Focused Search ("prosthetic limb")
- Query term: "prosthetic limb"
- Total studies estimated: ~500
- Purpose: Narrow to studies most directly relevant to prosthetic device access

### Why Two Searches?

The broad search reveals the total research infrastructure (rehabilitation, gait training, socket design), while the focused search identifies trials most directly relevant to prosthetic device access. The broad search captures ~4× more studies than device-specific ones, indicating that most "prosthetic" trials address adjacent areas like patient-reported outcomes, gait analysis, and rehabilitation.

### Key Limitations
- AI/ML processing may miss synonyms (e.g., "amputee rehabilitation," "limb loss," "osseointegration")
- Multi-country studies counted per site, inflating geographic totals
- "Unknown" status studies (20%) may include paused trials or data errors
- "Prosthetic" may return false positives (e.g., dental prosthetics)
- List-studies endpoint has sort/field validation constraints; trend analysis via dedicated analyze endpoints was used instead

## 2. Provider Gap Analysis

### Source
- Database: OpenStreetMap (OSM) via MCP Geocoding and Search APIs
- Retrieval dates: 2026-06-23, 2026-06-26

### Search Strategy

Three underserved regions identified via CDC Social Vulnerability Index and Amputee Coalition prevalence data:

| Region | Center Point | Coordinates | Radius Range |
|--------|-------------|-------------|-------------|
| Rural West Virginia | Beckley, Raleigh County | 38.48°N, 80.84°W | 50 / 100 / 150 km |
| Eastern Kentucky | Hazard, Perry County | 37.25°N, 83.20°W | 50 / 100 / 150 km |
| Mississippi Delta | Clarksdale/Greenville | 33.41°N, 91.06°W | 50 / 100 / 150 km |

- Categories searched: all healthcare subcategories (hospital, clinic, pharmacy, doctor, rehabilitation, physiotherapy, occupational therapy, dental, audiologist, optometrist, mental health)
- **Result: zero prosthetic/orthotic providers found at any radius in any region**

### Why These Regions?

1. **Rural West Virginia** — High coal-mining injury and diabetes rates; persistent poverty; no trauma centers with prosthetic services
2. **Eastern Kentucky** — Among highest amputation rates due to diabetes and opioid infections; no prosthetist within any reasonable radius
3. **Mississippi Delta** — Highest diabetes and amputation rates in nation, especially among Black Americans; virtually no healthcare infrastructure

### Key Limitations
- OSM data may not capture all private-practice prosthetists (many classify under "medical supplier" or "durable medical equipment")
- No validation against state licensure databases (WV DOH, KY CSS, MS DOH) or Amputee Coalition directories
- 50 km radius may be too conservative for some rural areas where travel is already normalized
- Mountain terrain in WV/KY means driven distances exceed straight-line distances
- Prosthetic specialists may use non-standard OSM tags ("medical supplier", "shop", etc.) that were not searched
- Seasonal factors not accounted for

## 3. Data Integration

Cross-referenced to identify:
- **Innovation-access disconnect**: Where trials happen (mostly urban/wealthy areas) vs. where need is greatest (rural poor)
- **Evidence-to-practice gap**: Novel technologies (neural prostheses, 3D printing) not reaching highest-need populations
- **Infrastructure deficit**: No clinical trial sites, teaching hospitals, or residency programs in target regions
- **Provider type gaps**: Even general rehabilitation, occupational therapy, and physical therapy are absent from these regions

## 4. Recommended Updates

- Query state licensure databases (WV, KY, MS) for certified prosthetists/orthotists (CPOs)
- Cross-reference Amputee Coalition provider directory
- Analyze Medicaid reimbursement rates by state (WV, KY, MS vs. national average)
- Pull CDC amputation prevalence data by county
- Identify FQHC locations and capabilities in target regions
- Map drive-time contours from nearest CPO-certified centers
- Search OSM for "medical supplier" / "durable medical equipment" tags in target regions
- Assess broadband/telehealth readiness in each region

---

*Methodology v2.1 — Updated 2026-06-26*
