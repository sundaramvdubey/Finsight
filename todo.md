# Finsight local-first expansion checklist

## Product features

- [x] Add CSV export for verified rows, monthly aggregates, ranking data, and projection data.
- [x] Add PDF report export containing the thesis, key metrics, charts, projection, caveats, and provenance.
- [x] Add export status, success, and failure feedback in the dashboard.
- [x] Add a compact “download center” UI that explains exactly what each export contains.
- [x] Add offline-capable app-shell metadata and a service worker for static assets.
- [ ] Add a local data refresh/import path without changing the locked analysis or inventing data.
- [x] Add practical accessibility improvements: keyboard focus, labels, reduced motion, and print styling.

## Portable distribution

- [x] Define and document the primary portable path as a static offline web app/PWA.
- [x] Add a documented local development path for contributors.
- [x] Evaluate native desktop packaging; intentionally keep the portable PWA/static bundle as the supported path for this release.
- [x] Document device support, limitations, and data licensing posture.

## Quality and release

- [x] Add automated tests for export contents and key dashboard metrics.
- [x] Verify production build, CSV download, PDF rendering, offline shell, and mobile layout.
- [x] Update README, license, provenance, walkthrough, and contribution documentation.
- [ ] Publish a clean tagged open-source release to the existing GitHub repository.
- [x] Package a source archive that excludes node_modules and build output.

## LinkedIn launch

- [ ] Draft a plainspoken launch post with the live demo and GitHub release links.
- [ ] Confirm LinkedIn access and posting destination.
- [ ] Get explicit approval immediately before publishing.
- [ ] Publish the approved post and record the outcome.

## v1.2 critique-driven improvement pass

- [ ] Audit current data currency, source terms, and reproducibility constraints.
- [ ] Refresh the supported data window only from a citable, permitted source.
- [ ] Make excluded months and missing-month handling explicit in the dashboard.
- [ ] Compare multiple forecasting baselines with rolling or temporal validation.
- [ ] Deepen the CRED share, growth, and ranking analysis if the available data supports it.
- [ ] Replace inaccurate “AI-driven” wording with precise implementation language.
- [ ] Add production-asset checks and strengthen automated tests.
- [ ] Add citation.cff, CONTRIBUTING.md, and confirm the license files and metadata.
- [ ] Verify the refreshed release and publish v1.2 with remaining limits documented.
