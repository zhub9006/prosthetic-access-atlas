# Clinical Trials Analysis — Prosthetic & Orthotic Devices

> **Updated:** 2026-06-26 | **Data Source:** ClinicalTrials.gov API via MCP server

## Overview
- **Total Registered Prosthetic-Related Trials:** 2,168
- **Active Recruiting Trials:** 381 (17.7%)
- **Not Yet Recruiting:** 143 (6.6%)
- **Completed:** 925 (42.7%)
- **Unknown Status:** 431 (20.0%)

## Trial Status Distribution
| Status | Count | % |
|--------|-------|---|
| COMPLETED | 925 | 42.7% |
| UNKNOWN | 431 | 20.0% |
| RECRUITING | 381 | 17.7% |
| NOT_YET_RECRUITING | 143 | 6.6% |
| ACTIVE_NOT_RECRUITING | 119 | 5.5% |
| ENROLLING_BY_INVITATION | 41 | 1.9% |
| TERMINATED | 76 | 3.5% |
| WITHDRAWN | 45 | 2.1% |
| SUSPENDED | 5 | 0.2% |
| TEMPORARILY_NOT_AVAILABLE | 1 | <0.1% |
| NO_LONGER_AVAILABLE | 1 | <0.1% |

## Geographic Distribution (Top 15 Countries)
| Country | Sites | Share |
|---------|-------|-------|
| United States | 2,378 | 45.3% |
| France | 825 | 15.7% |
| Germany | 533 | 10.1% |
| Italy | 347 | 6.6% |
| Spain | 226 | 4.3% |
| Canada | 209 | 4.0% |
| China | 188 | 3.6% |
| Egypt | 148 | 2.8% |
| Denmark | 148 | 2.8% |
| United Kingdom | 192 | 3.7% |
| Australia | 118 | 2.2% |
| New Zealand | 14 | 0.3% |
| Sub-Saharan Africa | ~15 | <0.3% |
| South America | ~30 | <0.6% |
| South/Southeast Asia | ~60 | <1.2% |

> **Critical finding:** The U.S. accounts for nearly half of all study sites globally, yet within the U.S., no trials have sites in rural West Virginia, eastern Kentucky, or the Mississippi Delta.

## Phase Distribution
| Phase | Count | % |
|-------|-------|---|
| Later phases (NA*) | 1,264 | 58.3% |
| Unknown | 648 | 30.0% |
| Phase 4 | 91 | 4.2% |
| Phase 3 | 70 | 3.2% |
| Phase 2 | 78 | 3.6% |
| Phase 1 | 35 | 1.6% |
| Early Phase 1 | 10 | 0.5% |

*NA = not applicable (device trials often don't use classical Phase 1-3 terminology)

## Key Innovation Areas Identified
- **Osseointegrated neural prostheses** (e-OPRA, MIT NCT07204912)
- **3D-printed prosthetic limbs** (LIMBER UniLeg)
- **Adaptive prosthetic foot stiffness** (VSPA Foot)
- **Neural-controlled powered knee-ankle prosthesis** (Northwestern OPORP)
- **Wireless EMG control** (ASTERISK System)
- **Telerehabilitation for prosthetic rehab** (NCT05569967)

## Key Finding: Zero Trials in Underserved Regions
**Rural West Virginia, eastern Kentucky, and the Mississippi Delta have zero clinical trial sites enrolling in prosthetic/orthotic research** — despite having some of the highest amputation and limb-loss rates in the nation.

## Data Sources & Retrieval
- ClinicalTrials.gov API — search term "prosthetic" (broad) and "prosthetic limb" (focused)
- Analyses: countByStatus, countByCountry, countByPhase
- Data retrieved: 2026-06-26 via official MCP server
