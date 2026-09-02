# Finsight local-first feature contract

Finsight’s expanded product layer adds usability around the existing capstone analysis. It does not add new models, new source datasets, bank-wise splits, personal finance account connections, or commercial features.

| Feature | User value | Local-only behavior |
|---|---|---|
| CSV report | Inspect or reuse verified rows and derived sections | Browser generates a file; nothing uploads |
| PDF report | Share a readable evidence packet with charts and caveats | Browser captures the rendered dashboard |
| Download center | Makes export contents explicit | No account or server state |
| PWA install | Opens like a lightweight app on desktop/mobile | Service worker caches static shell |
| Month selector and chart toggle | Inspect the evidence instead of accepting one headline | Data is bundled and deterministic |
| Guided walkthrough | Helps first-time users understand the read | In-dashboard content plus recordable script |

The portable distribution default is an installable static web app rather than a native binary. That choice keeps the project cross-platform, free to run, easy to audit, and compatible with GitHub-based contribution. A future native wrapper would be a packaging convenience only; it would not change the analysis or data model.

## Non-goals

Finsight does not ingest bank statements, connect to UPI accounts, personalize financial advice, accept payments, or claim to be a production forecasting system. It remains an evidence-first public analysis product.
