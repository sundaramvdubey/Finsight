# Finsight v1.2.0

Finsight v1.2 strengthens the original UPI Growth Story capstone without changing its central question: UPI is growing, but distribution remains concentrated.

## Included

The release keeps the verified app-wise window from November 2023 through October 2025, makes all five excluded months explicit, and adds a separately sourced official NPCI ecosystem pulse through August 2026. The dashboard does not mix the two grains.

The projection section now labels the January 2026 output as a linear scenario. A reproducible expanding-window benchmark compares last value, three-point rolling mean, drift, and linear trend across 11 one-step folds. Linear trend leads at 3.22% MAPE on the 19-observation sequence, but the result remains directional.

The CRED lens now includes a verified-month trend chart plus latest share, rank, and volume readouts. Its boundary remains October 2025 because a matching official app-wise refresh could not be established from the current NPCI public table.

The repository adds `citation.cff`, `CONTRIBUTING.md`, official-pulse validation, a deterministic dashboard-data generator, benchmark output, and a frontend contract test. The public positioning now describes Finsight as a reproducible analytics dashboard rather than an AI-driven product.

## Verification

```text
python3 scripts/validate_data.py  -> PASS
python3 scripts/model_benchmark.py -> PASS
pnpm check                        -> PASS
pnpm test                         -> PASS
pnpm build                        -> PASS
```

The dashboard remains static and local-first. It requires no login, database, paid API, or backend. Code is MIT-licensed; NPCI source data remains attributed and subject to its current terms.
