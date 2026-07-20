# Clinical Trial Trend Analysis — Data Sources

## Queries Executed

### 1. Status Distribution (155 Prosthetic Care Studies)
- **Query:** `condition: "prosthetic"` + `term: "prosthetic care"`
- **Total:** 155 studies
- **Key results:**
  - RECRUITING: 32 (20.6%)
  - COMPLETED: 53 (34.2%)
  - UNKNOWN: 25 (16.1%)
  - NOT_YET_RECRUITING: 15 (9.7%)
  - ACTIVE_NOT_RECRUITING: 17 (11.0%)
  - TERMINATED: 4 (2.6%)
  - WITHDRAWN: 3 (1.9%)
  - ENROLLING_BY_INVITATION: 2 (1.3%)
  - SUSPENDED: 3 (1.9%)
  - TEMPORARILY_NOT_AVAILABLE: 1 (0.6%)

### 2. Phase Distribution (155 Prosthetic Care Studies)
- **Query:** `condition: "prosthetic"` + `term: "prosthetic care"`
- **Total:** 155 studies
- **Key results:**
  - NA (Observational/Device): 80 (51.6%)
  - Unknown: 52 (33.5%)
  - Phase 2: 11 (7.1%)
  - Phase 4: 8 (5.2%)
  - Phase 3: 4 (2.6%) *** — critically scarce
  - Phase 1: 2 (1.3%)

### 3. Sponsor Type (155 Prosthetic Care Studies)
- **Query:** `condition: "prosthetic"` + `term: "prosthetic care"`
- **Total:** 155 studies
- **Key results:**
  - OTHER: 109 (70.3%)
  - INDUSTRY: 30 (19.4%)
  - FED: 11 (7.1%)
  - OTHER_GOV: 4 (2.6%)
  - NETWORK: 1 (0.6%)

### 4. Geographic Distribution (155 Prosthetic Care Studies)
- **Query:** `condition: "prosthetic"` + `term: "prosthetic care"`
- **Total:** 155 studies
- **Top countries:**
  - United States: locations in 336+ studies
  - UK: 25 studies
  - France: 17 studies
  - Germany: 20 studies
  - Spain: 17 studies

## Broader Query Results
- **Query:** `condition: "prosthetic"` (broad)
- **Total:** 644 studies
- Used as the primary dataset in the existing README

## APIs Used
- ClinicalTrials.gov API v2 via MCP tools
- OpenStreetMap via OSM MCP tools
