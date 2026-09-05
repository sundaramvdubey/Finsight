# Contributing to Finsight

Finsight is an open-source, local-first analytics dashboard. Contributions are welcome when they make the evidence trail clearer, the analysis more reproducible, or the interface more useful without overstating what the data can support.

## Before opening a change

Read `README.md`, `docs/DATA_PROVENANCE.md`, `docs/FEATURE_SCOPE.md`, and `docs/V1_2_AUDIT.md`. Keep the distinction between the 19-month app-wise analysis and the separately sourced official NPCI ecosystem pulse explicit. Do not silently combine datasets with different grains, dates, or provenance.

## Data and analysis standards

Use primary or clearly citable sources. Never add simulated values, fabricated reviews, or unsupported app-level observations. Preserve source lineage in processed files. If a month is excluded, name the reason and update the validation logic and documentation together. Any forecast should state its validation design, fold count, metric, sample size, and known limitations.

## Local checks

From the repository root, run:

```bash
python3 scripts/validate_data.py
python3 scripts/model_benchmark.py
pnpm install
pnpm check
pnpm test
pnpm build
```

If you change processed inputs, regenerate the dashboard module with `python3 scripts/build_dashboard_data.py` and include the generated file in the same change. The dashboard is a static React application; keep new features browser-local unless the scope is explicitly changed.

## Pull requests

Describe the user-facing change, the source or method behind it, and the checks you ran. Include screenshots for visual changes. Keep claims proportional to the evidence and update provenance or release notes when a source window, metric, or model changes.

## License and attribution

Code contributions are released under the MIT License. The underlying data may have separate source terms; contributors are responsible for retaining the attribution and usage notes required by the source.
