# Clinical Trial Trends — Updated July 2026

> Compiled from ClinicalTrials.gov API v2 | July 20, 2026

## Search Methodology
- **Primary search:** `amputation + prosthesis` (clinicaltrials.gov API v2)
- **Total studies returned:** 459 (specific)
- **Broad search count (repo baseline):** 644 studies
- **API status during collection:** Intermittent timeouts and 500 errors; data represents what was retrievable

## Status Distribution (n=459 prosthesis+amputation studies)

| Status | Count | % | Interpretation |
|--------|-------|---|----------------|
| COMPLETED | 235 | 51.2 | Far end of pipeline; results available |
| UNKNOWN | 63 | 13.7 | Data quality concern |
| RECRUITING | 80 | 17.4 | Active enrollment — most relevant for access gap |
| NOT_YET_RECRUITING | 28 | 6.1 | Planning phase |
| ACTIVE_NOT_RECRUITING | 22 | 4.8 | Ongoing but not enrolling |
| TERMINATED | 15 | 3.3 | Stopped before completion |
| WITHDRAWN | 12 | 2.6 | Removed from registry |
| ENROLLING_BY_INVITATION | 4 | 0.9 | Limited access by invitation |

**Note:** The repo baseline (644 studies, broader search) shows slightly different distributions due to wider query scope. The 459 studies above use a focused `amputation + prosthesis` query.

## Phase Distribution (n=459)

| Phase | Count | % | Significance |
|-------|-------|---|--------------|
| N/A (Observational/Device) | 316 | 68.9 | Registries and observational studies |
| Unknown | 117 | 25.5 | Phase not recorded — data gap |
| Phase 2 | 9 | 2.0 | Safety/efficacy exploration |
| Phase 1 | 7 | 1.5 | First-in-human safety |
| Phase 3 | 4 | 0.9 | **Pivotal efficacy trials — extremely scarce** |
| Early Phase 1 | 6 | 1.3 | Initial safety testing |
| Phase 4 | 3 | 0.7 | Post-market surveillance |

**Key Insight:** Only 13 withdrew studies are interventional (Phase 1-4). The vast majority are observational/registries. Phase 3 trials (n=4) are critically scarce — this is the evidence gap for prosthetic device efficacy.

## Sponsor Type Analysis (n=459)

| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 324 | 70.6% |
| Industry | 78 | 17.0% |
| Federal | 44 | 9.6% |
| Other Government | 12 | 2.6% |
| Network | 1 | 0.2% |

**Key Insight:** 70.6% academic-sponsored, only 17.0% industry. Federal funding accounts for ~10%. Limited commercial innovation pipeline.

## International Country Distribution (n=459, multi-country registrations counted per country)

| Country | Study Count | Notes |
|---------|------------|-------|
| United States | 500 | Highest (includes multi-country registrations) |
| France | 83 | Strong prosthetic research tradition |
| Turkey | 41 | Growing prosthetic research |
| Italy | 19 | Falls/balance prosthesis research |
| United Kingdom | 18 | Prosthetic limb registries |
| Canada | 19 | VA-linked prosthetic studies |
| Belgium | 11 | Prosthetic knee/device research |
| Netherlands | 14 | Rehabilitation prosthetics |
| Ukraine | 8 | War-related amputation prosthetics |
| Australia | 4 | Indigenous health prosthetics |

**Key Insight:** U.S. dominates but many studies are multi-country registrations. France and Turkey have notable prosthetic research programs.

## Notable Individual Trials (July 2026)

### NCT03433300 — Microprocessor Knees in Early Rehabilitation
- **Status:** COMPLETED
- **Sponsor:** University of Washington + DoD + Otto Bock
- **Population:** 19 transfemoral amputees (4-16 weeks post-amputation)
- **Intervention:** Microprocessor knee (Ottobock Kenevo/C-Leg) vs. non-microprocessor knee (Ottobock 3R60/3R62)
- **Key outcomes:** Falls, step activity, balance confidence, mobility, QoL, community integration
- **Relevance:** Directly applicable to early prosthetic rehabilitation access

### NCT06883942 — MOTU++ pedane (Fall Risk in Prosthesis Wearers)
- **Status:** COMPLETED (2025)
- **Sponsor:** Fondazione Don Carlo Gnocchi ETS
- **Population:** 8 transfemoral/trans-tibial amputees
- **Intervention:** Fall detection algorithm validation on sliding/stumbling platforms
- **Relevance:** Safety assessment for prosthetic users; fall risk biomarkers

## Data Quality Notes
- ClinicalTrials.gov API experienced significant timeouts during collection; some searches returned 500 errors
- The broader repo baseline (644 studies) used a wider `cond=prosthetic` query
- Country counts exceed 459 total because multi-country registrations are counted per participating country
- For the most current data, re-query the ClinicalTrials.gov API v2

## Comparison with Repo Baseline (n=644, broad search)

| Metric | Broad Search (644) | Focused Search (459) |
|--------|-------------------|---------------------|
| COMPLETED | 271 (42.1%) | 235 (51.2%) |
| RECRUITING | 112 (17.4%) | 80 (17.4%) |
| UNKNOWN | 134 (20.8%) | 63 (13.7%) |
| Phase 3 | 29 (4.7%) | 4 (0.9%) |
| Industry-sponsored | 108 (16.8%) | 78 (17.0%) |

*Updated: July 20, 2026*
