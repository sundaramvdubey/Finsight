# Project 3: CRED - The UPI Growth Story
## 5-Person Team Plan | 5-Day Sprint

---

## 1. The Brief (from the handbook)

**Question:** Is UPI's growth broadening across apps and banks, or concentrating into a duopoly?

**You must produce, end to end:**
1. A database + SQL script (window functions, CTEs) analyzing 24–36 months of NPCI UPI data
2. A cleaned dataset + Python/pandas exploration (trends, seasonality, concentration)
3. One linear regression model projecting next-quarter transaction volume
4. A published dashboard (Tableau Public or equivalent)
5. A one-page decision memo answering the strategy question directly
6. An AI Workflow Appendix (prompts used, one AI mistake you caught, your judgment calls)
7. A GitHub README + 3-minute recorded walkthrough

**Scope bounds (don't blow past these):** 24–36 months, top apps + a "long tail" bucket for the rest, exactly one model. The insight is in the *shares and concentration*, not forecasting precision.

**What "good" looks like:** the handbook's rubric grades every part on Solid → Strong → Standout. Strategy: get a rough, complete, ugly version of the *entire* pipeline done by Day 2–3 (Solid), then spend remaining time polishing toward Strong/Standout. Never leave any one part unfinished while another is gold-plated.

---

## 2. Where You Actually Start (Day 0, before splitting up)

Before anyone touches data or code, spend **1 hour together**:

1. **Pick the data source.** NPCI publishes monthly UPI statistics at [npci.org.in](https://www.npci.org.in) → "UPI Product Statistics" (bank-wise) and NPCI's app-wise CSVs are also mirrored on sites like [Kaggle](https://www.kaggle.com) and in RBI/press releases for the same period. Confirm you can get **app-wise** (PhonePe, GPay, Paytm, CRED, others) and **bank-wise** monthly volume + value for ~30 months (e.g., Jan 2023–Jun 2026 or similar recent window).
2. **Agree on the database.** SQLite or PostgreSQL — SQLite is fastest to set up for a 5-day sprint (no server, just a file everyone can share).
3. **Agree on the churn-style definition equivalent here:** decide up front what counts as "top apps" vs. "long tail" (e.g., top 5 apps by volume get their own rows, everyone else bucketed as "Others"). This is your version of Mamaearth's churn-threshold decision — document it, defend it.
4. **Set up one shared GitHub repo** with folders: `/data`, `/sql`, `/notebooks`, `/dashboard`, `/memo`, `/ai-appendix`, `README.md`. Everyone pushes here — this becomes deliverable #1 automatically.
5. **Share a single AI prompt log** (a shared doc or `ai-appendix/prompts.md`) that all 5 people append to as they work — don't reconstruct it on Day 5.

---

## 3. The 5 Roles (mapped to the 5 pipeline stages)

| # | Role | Owns | Maps to rubric row |
|---|------|------|---------------------|
| 1 | **Data Engineer** | Sourcing NPCI files, schema design, loading into DB | The SQL (setup half) |
| 2 | **SQL/Analytics Lead** | Window functions, CTEs, market-share & concentration queries | The SQL (analysis half) |
| 3 | **Data Cleaner / EDA Lead** | pandas cleaning, trend/seasonality charts, concentration curve | The cleaning + exploration |
| 4 | **Modeler** | Linear regression, projection, error reporting, honest limitations | The model |
| 5 | **Dashboard & Memo Lead** | Tableau dashboard, one-page memo, ties findings to CRED's strategic question | The dashboard + memo |

Two people should double up on the **README, walkthrough video, and AI appendix** at the end — that's a group effort, not one person's job.

This split works because the pipeline is genuinely sequential (Data Engineer → SQL Lead → Cleaner → Modeler → Dashboard/Memo), but with a 5-day timeline you can't wait for each stage to fully finish before the next starts. The schedule below overlaps them deliberately.

---

## 4. Day-by-Day Schedule

### **Day 1 — Foundation (everyone touches this)**
- **Data Engineer:** Download/scrape NPCI monthly app-wise + bank-wise stats for 24–36 months. Normalize into 2 CSVs (`app_wise.csv`, `bank_wise.csv`). Design schema: `transactions(month, app, bank, volume, value)`. Load into SQLite/Postgres.
- **SQL Lead:** While data loads, drafts the query list needed (see Section 5) so they're ready to write SQL the moment tables exist.
- **Cleaner:** Inspects raw files for the "months won't all look the same" problem the handbook warns about — different column names, merged app categories, format shifts. Starts a `cleaning_log.md`.
- **Modeler:** Researches what "events" might break a UPI growth projection (pricing changes, new entrants like CRED/WhatsApp Pay, RBI regulation, market-share caps) — this becomes the caveats section later. Sketches the regression approach (features: month index, seasonality flag, maybe app-level or aggregate volume).
- **Dashboard/Memo Lead:** Drafts the memo skeleton and the one strategic question it must answer. Sets up Tableau Public account, decides on dashboard layout (3 views: volume/share trend, concentration curve, projection).
- **End of Day 1 goal:** Data loaded into DB, everyone knows the plan. This is your version of "get a rough but complete pipeline going."

### **Day 2 — SQL + Cleaning (core engine)**
- **SQL Lead:** Writes the core queries — market share by app per month (window function), month-on-month growth (`LAG`), rankings (`RANK`/`DENSE_RANK`), and a CTE-based concentration analysis (e.g., top-N share, HHI-style concentration index). Hands query outputs to Cleaner/Modeler as CSVs.
- **Data Engineer:** Now free — helps SQL Lead validate joins, or starts assembling the "long tail" bucket logic, or pairs with Cleaner on messy months.
- **Cleaner:** Pulls SQL outputs into pandas. Fixes duplicates, naming/format inconsistencies, missing months. Documents every decision in `cleaning_log.md`.
- **Modeler:** Finalizes feature plan based on what SQL Lead's queries actually produce.
- **Dashboard/Memo Lead:** Starts pulling early SQL outputs into a first (ugly) Tableau draft — trend and share lines only.
- **End of Day 2 goal:** Clean, query-able dataset with market share, growth, and rankings computed.

### **Day 3 — Exploration + Modeling**
- **Cleaner:** Finishes EDA — seasonality (festive-month spikes like Diwali), the concentration curve across apps, descriptive stats. Each chart makes one point (per rubric).
- **Modeler:** Trains the linear regression on total (or top-app) transaction volume to project next quarter. Reports error (MAPE/RMSE), checks for overfitting (train/test split by time), and starts drafting "what could break this projection" using the events researched Day 1.
- **SQL Lead + Data Engineer:** Free to help wherever bottlenecked — usually Cleaner or Modeler by this point. Also start writing the SQL script comments/structure so "another analyst could extend it" (Standout-level SQL).
- **Dashboard/Memo Lead:** Adds the concentration view and projection view to the dashboard using outputs as they arrive.
- **End of Day 3 goal:** Full Solid-level pipeline exists: data → SQL → clean → EDA → model → rough dashboard. This is the safety checkpoint — nothing left un-started.

### **Day 4 — Decision-Ready Outputs**
- **Dashboard/Memo Lead:** Finalizes the dashboard (publish to Tableau Public), writes the one-page memo answering broadening-vs-concentrating directly, with evidence and implications for CRED as a challenger.
- **Modeler:** Writes the honest limitations section for the model (where it breaks, what data would improve it).
- **Cleaner:** Writes the data-quality note (what was wrong in the raw NPCI files, what was done, what remains imperfect).
- **SQL Lead:** Polishes SQL script structure and comments.
- **Data Engineer:** Starts the README draft (question, data, approach, findings, limitations — business impact first).
- **Everyone:** Contributes to the shared AI appendix — flag at least one moment AI was confidently wrong and how it was caught.
- **End of Day 4 goal:** All 7 deliverables exist in at least Solid form.

### **Day 5 — Polish, Review, Record**
- **Morning:** Whole team reviews against the rubric table (SQL, cleaning, exploration, model, dashboard, memo, AI appendix, README) and pushes the biggest gaps from Solid → Strong.
- **Afternoon:** Finalize README, record the 3-minute walkthrough (rotate who presents, or have the Dashboard/Memo Lead present since they own the "so-what"), final commit to GitHub.
- **End of Day 5 goal:** Fully submitted, reviewed, recorded.

---

## 5. Core SQL Queries to Plan For (SQL Lead's checklist)

- Monthly market share by app: `volume / SUM(volume) OVER (PARTITION BY month)`
- Month-on-month growth: `LAG(volume) OVER (PARTITION BY app ORDER BY month)`
- Rankings: `RANK() OVER (PARTITION BY month ORDER BY volume DESC)`
- Concentration (CTE): top-N apps' combined share per month, or a simple HHI-style sum of squared shares
- Long-tail bucket: aggregate everything outside top 5 into "Others" before ranking

---

## 6. Risks to Watch

- **Data assembly is the biggest time sink** — NPCI's raw files are inconsistent month to month. Don't let this eat into Day 2–3; if a month's data is unusable, drop it and note it rather than stall the team.
- **Don't add a second model.** Scope bounds say one regression — resist the urge to also try ARIMA or classification.
- **The memo is the deliverable a hiring manager reads first.** Don't leave it to the last hour.
