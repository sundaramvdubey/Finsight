# Finsight — The UPI Growth Story
**One-page memo | Window: Nov 2023–Oct 2025 (19 of 24 months verified) | Basis: transaction volume**

## The question
Is UPI's growth broadening across apps, or hardening into a PhonePe/Google Pay duopoly — and what does that mean for a challenger like CRED?

## The answer: broadening, after a concentration peak in mid-2024

Market concentration (HHI, volume-share basis) **rose** from 3,738 in Nov 2023 to a peak of **3,942 in Jun 2024**, then **fell steadily** to a low of **3,535 in Sep 2025** before ticking up slightly to 3,577 in Oct 2025. PhonePe + Google Pay's combined share tracks the same arc: 84.1% → peak 87.4% (Aug 2024) → 83.0% (Oct 2025).

**Read:** the "PhonePe/GPay duopoly" narrative was more true in mid-2024 than it is today. The last five quarters of this window show real, if modest, broadening — driven by Navi's rise (near-zero share to ~3% by Oct 2025) and steady erosion at the very top, not by any single new leader.

*(See `notebooks/figures/02_concentration_curve.png` and `04_top_apps_share.png`.)*

## So what, for CRED

CRED's own volume share has stayed roughly flat across the window (~0.5–1%, `sql/queries.sql` query 5) — it has **not** captured share of the broadening. The apps that gained (Navi, Fampay, super.money) share a common trait CRED doesn't lean on as hard: they're default-use payment apps, not credit-card-management-first apps with UPI as an add-on. The broadening is real, but it's happening around CRED, not through it. This is the central strategic tension worth putting in front of leadership — not a data-supported prediction of what CRED should do about it, but the fact pattern it needs to reconcile.

## Next-quarter projection (linear regression on total volume)

| Month | Projected volume | 95% band |
|---|---|---|
| Nov 2025 | 20,219 Mn | 19,311 – 21,126 |
| Dec 2025 | 20,590 Mn | 19,682 – 21,498 |
| Jan 2026 | 20,961 Mn | 20,054 – 21,869 |

Model: linear regression on total monthly volume vs. calendar-month index, fit on 19 verified months. Test error (last 4 months held out) was **1.69% MAPE**, in line with train error (2.15%) — no overfitting.

## Risks to the projection
- **No seasonality term** — a straight line can't capture the festive-season swings visible in the data (e.g. the Oct/Nov 2024 spike-then-drop); Nov/Dec 2025 could miss the band in either direction.
- **19 months, not 24** — see limitation below; the true forecast uncertainty is wider than the ±908 Mn shown, which only reflects in-sample residual spread.
- **Pending regulation** — NPCI's proposed 30% per-app volume cap, if enacted inside this window, would restructure PhonePe/GPay volumes directly and break the trend assumption.
- **New-entrant composition risk** — Navi, super.money, and WhatsApp (onboarding cap lifted Dec 2024) are still scaling; the total-volume trend could hold even as its composition shifts further.

## Data limitation, stated plainly
5 of the original 24 months (Dec 2023, Feb 2024, Mar 2024, Sep 2024, Jul 2025) were duplicate copies of the adjacent month in the source export — confirmed via an independent cross-check against reported NPCI aggregates, not assumed. No verified app-wise replacement data could be sourced in the time available, so these 5 months were excluded rather than patched. Full detail in `DECISIONS.md` and `data/cleaning_notes.md`.

## Recommendation
Treat the "PhonePe/GPay lock-in" framing as dated by about a year. The live strategic question for CRED isn't whether the market is opening up — it is — but why the apps capturing that opening aren't CRED, and whether that's a positioning problem or a product-surface problem.
