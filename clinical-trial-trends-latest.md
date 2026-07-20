# Clinical Trial Trends — Prosthetic & Prosthetic Care (July 2026)

Data sourced from ClinicalTrials.gov API v2.

## Search Parameters
- Query: `condition=prosthetic` + `term=prosthetic care`
- Total matching studies: **644** (broad), **155** (prosthetic care specific)
- Analysis date: July 2026

## Status Distribution (n=644)

| Status | Count | % |
|--------|-------|---|
| COMPLETED | 271 | 42.1% |
| UNKNOWN | 134 | 20.8% |
| RECRUITING | 112 | 17.4% |
| ACTIVE_NOT_RECRUITING | 38 | 5.9% |
| NOT_YET_RECRUITING | 38 | 5.9% |
| TERMINATED | 24 | 3.7% |
| ENROLLING_BY_INVITATION | 12 | 1.9% |
| WITHDRAWN | 10 | 1.6% |
| SUSPENDED | 4 | 0.6% |
| TEMPORARILY_NOT_AVAILABLE | 1 | 0.2% |

**Key Insight:** 271 completed vs. only 112 recruiting — nearly 2.5x completed-to-recruiting ratio, indicating a maturation of the trial landscape but also a recruitment challenge for new studies.

## Phase Distribution (n=644)

| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 4 | 29 | 4.5% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

**Key Insight:** Only 69 trials (10.7%) are interventional (Phases 1–4). The majority (338) are observational or device-registry studies. **Only 30 Phase 3 efficacy trials** exist across the entire landscape — a critical gap for evidence-based prosthetic care.

## Sponsor Type Distribution (n=644)

| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal | 23 | 3.6% |
| Other Government | 14 | 2.2% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

**Key Insight:** 76.5% academic-sponsored, only 16.8% industry-sponsored. Limited commercial innovation pipeline for prosthetic devices.

## Geographic Distribution (Top 10 Countries)

| Country | Count | % |
|---------|-------|---|
| United States | 336 | 52.2% |
| France | 84 | 13.0% |
| Australia | 35 | 5.4% |
| United Kingdom | 25 | 3.9% |
| Spain | 17 | 2.6% |
| Germany | 20 | 3.1% |
| Netherlands | 20 | 3.1% |
| Sweden | 8 | 1.2% |
| Switzerland | 8 | 1.2% |
| Canada | 13 | 2.0% |

**Key Insight:** The US dominates (52%), but European nations collectively contribute more trials (130+). Low-income countries (India, Pakistan, Egypt, Colombia) have minimal representation despite high amputation burdens.

## Notable Studies

1. **NCT06243549** — *Personalisation of Prosthetic Care for Lower-Limb Amputees* (University of Bath, UK)
   - Status: ACTIVE_NOT_RECRUITING
   - Type: Observational cohort, 12-month prospective
   - 30 participants; exploring biomechanical and psychological pathways of lower back pain post-amputation
   - Key focus: gait parameters, muscle activation, pain development

2. **NCT02424903** — *European Prosthetic Joint Infection Cohort Study (EPJIC)*
   - Status: UNKNOWN
   - Type: Observational, 5,000 planned
   - Multi-center across Europe; evaluating treatment approaches for prosthetic joint infections
   - Sponsor: Pro-Implant Foundation, Charité Berlin

## Data Sources
- ClinicalTrials.gov API v2: https://clinicaltrials.gov/api/v2/studies
- Analysis endpoint: analyzeTrends (countByStatus, countByPhase, countBySponsorType, countByCountry)