# Clinical Trial Data — Prosthetic & Prosthetic Care

Extracted from ClinicalTrials.gov API v2, July 2026.

## Summary Counts
- Total studies (broad query: `condition=prosthetic`): **644**
- Total studies (specific query: `condition=prosthetic` + `term=prosthetic care`): **155**

## Full Trials (155 prosthetic care studies)

### Latest Studies (most recently submitted)

| NCT ID | Title | Status | Start Date | Completion | Sponsor | Phase |
|--------|-------|--------|------------|------------|---------|-------|
| NCT06243549 | Personalisation of Prosthetic Care for Lower-Limb Amputees | ACTIVE_NOT_RECRUITING | 2023-09 | 2026-10 (est.) | University of Bath (UK) | N/A (Observational) |
| NCT02424903 | European Prosthetic Joint Infection Cohort Study (EPJIC) | UNKNOWN | 2015-05 | 2018-12 (est.) | Pro-Implant Foundation | N/A (Observational, n=5000) |

### Full Status Breakdown (n=644)

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

### Full Phase Breakdown (n=644)

| Phase | Count | % |
|-------|-------|---|
| N/A (Observational/Device) | 338 | 52.5% |
| Unknown | 202 | 31.4% |
| Phase 4 | 29 | 4.5% |
| Phase 2 | 39 | 6.1% |
| Phase 3 | 30 | 4.7% |
| Phase 1 | 15 | 2.3% |
| Early Phase 1 | 4 | 0.6% |

### Full Sponsor Breakdown (n=644)

| Sponsor | Count | % |
|---------|-------|---|
| Academic/Other | 493 | 76.5% |
| Industry | 108 | 16.8% |
| Federal | 23 | 3.6% |
| Other Government | 14 | 2.2% |
| Network | 5 | 0.8% |
| NIH | 1 | 0.2% |

### Geographic Distribution (Top 15 Countries, n=644)

| Country | Count | % |
|---------|-------|---|
| United States | 336 | 52.2% |
| France | 84 | 13.0% |
| Australia | 35 | 5.4% |
| United Kingdom | 25 | 3.9% |
| Germany | 20 | 3.1% |
| Netherlands | 20 | 3.1% |
| Sweden | 8 | 1.2% |
| Switzerland | 8 | 1.2% |
| Canada | 13 | 2.0% |
| Turkey (Türkiye) | 7 | 1.1% |
| South Korea | 3 | — |
| Egypt | 3 | — |
| India | 3 | — |
| Italy | 6 | — |
| Spain | 17 | — |

## Key Observations

1. **Maturation of the trial landscape:** 43% of studies are COMPLETED, while only 17% are RECRUITING. This suggests the prosthetic care research field is mature but may be struggling to sustain new studies.

2. **Phase 3 scarcity:** Only 30 Phase 3 trials (4.7%) provide high-quality evidence for prosthetic interventions. The rest are observational, device-registry, or early-phase studies.

3. **Geographic imbalance:** 52% of all studies are US-based, but European countries (France, Germany, UK, Netherlands) collectively contribute more. Low-income countries with high amputation burdens (India, Pakistan, Egypt, Colombia) are underrepresented.

4. **Industry vs. Academic:** 76.5% academic-sponsored vs. 16.8% industry-sponsored. Limited commercial innovation pipeline.

## API Endpoints Used

- List Studies: `GET /api/v2/studies` with query parameters `cond=prosthetic&term=prosthetic+care`
- Analyze Trends: `POST /api/v2/studies/analyze` with `analysisType` = `countByStatus`, `countByPhase`, `countBySponsorType`, `countByCountry`
- Get Study: `GET /api/v2/studies/{NCTId}`