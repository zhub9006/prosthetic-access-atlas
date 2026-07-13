# Prosthetic Access Atlas

An open-access resource mapping prosthetic/orthotic clinical trial landscape and care access gaps in underserved U.S. regions.

## Key Findings (642 Trials)
- **Recruiting**: 114 (17.8%) | **Completed**: 269 (41.9%) | **Unknown**: 134 (20.9%)
- **Phase 1-3**: 84 trials total (13.1%) | **No/Unknown Phase**: 538 (83.8%)
- **U.S. studies**: 680 (multi-country arms) | **NIH-funded**: 1 trial only!
- **Sponsor**: 492 Other/Academic | 107 Industry | 23 Federal | 1 NIH

## Regional Gap Analysis

| Region | Center | O&P Providers Found in OSM | Nearest Major O&P Center |
|---|---|---|---|
| Rural West Virginia | 38.5°N, 80.5°W | **0** | Charleston, WV (+out-of-state) |
| Eastern Kentucky | 37.5°N, 83.0°W | **0** | Lexington, KY (~161 km) |
| Mississippi Delta | 33.4°N, 90.2°W | **0** | Memphis, TN (~161 km) |

### Three Universal Barriers:
1. Zero certifiable prosthetist/orthotist providers mapped in 150 km radius around any region center
2. Rural hospital closures + long travel distances prevent regular O&P follow-up
3. High diabetes/vascular disease/trauma rates create greater limb-loss need than in most regions

## Data Files
- `data/clinicaltrials_trends.json` — raw statistical output from ClinicalTrials.gov
- `data/regions_gtfs.json` — region metadata (coordinates, barriers, pop estimates)
- `ANALYSIS/full_trials_summary.md` — complete trial analysis
- `ANALYSIS/region_gap_analysis.md` — detailed regional care gap analysis

## How to Contribute
- Map certified ABC/CPO providers into these gap zones
- Add patient navigation resources for trial enrollment
- Update recruitment status as ClinicalTrials.gov data refreshes
- Submit regional commute/time-to-care routing data

## License
Open Access