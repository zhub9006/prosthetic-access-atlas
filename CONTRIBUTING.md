# Contributing to Prosthetic Access Atlas

## How to Contribute

### 1. Report Data Issues
- Check if the data on ClinicalTrials.gov is outdated
- Verify CPO provider information through ABC directory or direct contact
- Open an issue with the `[DATA]` label

### 2. Add Regional Profiles
- Duplicate an existing profile that is similar in scope
- Update coordinates, demographics, and provider data
- Include gap scoring with methodology notes
- Submit a PR for review

### 3. Add Visualizations
- Fork the repo
- Create a new branch for your visualization
- Add charts, maps, or dashboards in `visualizations/`
- Ensure all outputs are version-controlled

### 4. Add Policy Briefs
- Write evidence-based briefs in `docs/policy_briefs/`
- Include citations and gap analysis data
- Target audience: HRSA, CMS, state Medicaid offices, VA

### 5. Fix bugs or improve code
- Python scripts and Jupyter notebooks live in `analysis/`
- Use virtual environments
- Add unit tests where appropriate

## Code of Conduct

- Be respectful and inclusive
- Default to open data sharing
- Credit original data sources
- Do not include protected health information

## Documentation Standards

- All markdown files use ATX headers
- JSON files must be valid (validate with `python -m json.tool`)
- CSV files include header rows
- All figures and maps must include source attribution

## Review Process

1. Fork and branch
2. Open PR against `main`
3. At least one maintainer review
4. CI check (if any) must pass
5. Merge

---

We welcome contributions from clinicians, researchers, policymakers, patients, and advocates.