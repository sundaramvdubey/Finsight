# Finsight v1 — Local and Portable Use

Finsight is intentionally a **local-first static application**. It does not require an account, database, API key, telemetry service, or paid backend to use the dashboard and its exports. The default portable path is a PWA: open the hosted demo or a local build in a modern browser, choose “Install app” when offered, and use it as a standalone window. The service worker caches the static shell for repeat/offline viewing after the first successful load.

## Run from the repository

```bash
pnpm install
pnpm dev
```

For a production-like local build:

```bash
pnpm build
pnpm start
```

The dashboard is available at `http://localhost:3000`. A static host, GitHub Pages-style host, or any HTTPS file server can host the built `dist/public` contents. Service-worker installation requires `localhost` or HTTPS; opening `index.html` directly from `file://` is not an offline-install path.

## Exports

The CSV and PDF exports run entirely in the browser. CSV contains the verified monthly aggregates, next-quarter projection rows, and top-six ranking rows for each verified month. PDF captures the rendered dashboard, including charts, thesis, caveats, and source notes. No exported file is sent to a server.

## Device support

The PWA is designed for current desktop and mobile Chromium, Safari, and Firefox releases. It is responsive on narrow screens, but the analytical charts are easiest to inspect on a laptop. The app does not currently ship signed Windows, macOS, Linux, Android, or iOS binaries. A native wrapper would add platform-specific build and signing maintenance without improving the core local-first use case, so it remains intentionally out of scope for this release.

## Data and privacy

The bundled data is the project’s verified, source-attributed aggregate table. There are no personal transaction records and no user-entered financial accounts. Browser downloads remain on the user’s device. The source and licensing posture is documented in `docs/DATA_PROVENANCE.md`; review NPCI’s current terms before commercial redistribution or a raw-data mirror.
