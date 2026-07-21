# Contributing to the Prosthetic Access Atlas

## How to Contribute

This is an open-access resource. We welcome contributions to improve prosthetic care access.

### Types of Contributions

1. **Data updates** — Refresh ClinicalTrials.gov data or OSM provider searches
2. **New regions** — Add underserved areas for gap analysis
3. **Methodology improvements** — Enhance data collection and analysis approaches
4. **Bug fixes** — Fix errors in data or documentation

### Adding a New Region

1. Geocode the target area (central town/city)
2. Search for CPO (Certified Prosthetist/Orthotist) providers within 30 km
3. Search for nearby hospitals and healthcare facilities using OSM
4. Run ClinicalTrials.gov queries for prosthetic trials in that region
5. Run trend analyses: `countByStatus`, `countByCountry`, `countByPhase`, `countBySponsorType`
6. Document findings in `FINDINGS_JULY_2026_LATEST.md` or create a new findings file
7. Update `access_gap_summary.csv` with the new region data

### Commit Guidelines

- Use clear commit messages describing the update
- Update the README.md Quick Facts section when data changes
- Keep CSV files clean with headers
- Use JSON for machine-readable data
- Update METHODOLOGY.md when methods change

### Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes with a descriptive message
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request with a description of your changes

## Code of Conduct

Be respectful and constructive. This is a research and advocacy resource.

## License

MIT — open and free.

*Together we can map and close prosthetic care gaps.*
