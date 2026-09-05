"""Refresh the typed dashboard data module from processed inputs and cited official pulse data."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TS = ROOT / "client" / "src" / "data" / "finsightData.ts"
PULSE = ROOT / "data" / "raw" / "npci_upi_monthly_2026_27.csv"
BENCHMARK = ROOT / "data" / "processed" / "model_benchmark.json"
APP = ROOT / "data" / "processed" / "upi_monthly_app_FINAL.csv"


def main() -> None:
    raw = TS.read_text()
    start = raw.index("= ") + 2
    end = raw.rindex(" as const;")
    data = json.loads(raw[start:end])

    pulse = pd.read_csv(PULSE, parse_dates=["month_start"]).sort_values("month_start")
    latest = pulse.iloc[-1]
    data["current_pulse"] = {
        "month": latest["month_start"].strftime("%Y-%m-%d"),
        "banks_live": int(latest["banks_live"]),
        "volume_mn": round(float(latest["volume_mn"]), 2),
        "value_cr": round(float(latest["value_cr"]), 2),
        "source_url": str(latest["source_url"]),
        "label": "Official NPCI ecosystem pulse; not mixed into app-wise trend charts",
    }

    benchmark = json.loads(BENCHMARK.read_text())
    data["model_benchmark"] = [
        {
            "method": row["method"],
            "mape_pct": row["mape_pct"],
            "mae_mn": row["mae_mn"],
            "folds": row["folds"],
            "last_forecast_mn": row["last_forecast_mn"],
        }
        for row in benchmark["models"]
    ]

    app = pd.read_csv(APP, parse_dates=["month_start"])
    app["share_pct"] = app["volume_mn"] / app.groupby("month_start")["volume_mn"].transform("sum") * 100
    app["rank"] = app.groupby("month_start")["volume_mn"].rank(method="min", ascending=False).astype(int)
    cred = app[app["app_name"].str.casefold().eq("cred")].sort_values("month_start").copy()
    cred["growth_pct"] = cred["volume_mn"].pct_change() * 100
    data["cred_trend"] = [
        {
            "month_start": row["month_start"].strftime("%Y-%m-%d"),
            "volume_mn": round(float(row["volume_mn"]), 2),
            "share_pct": round(float(row["share_pct"]), 2),
            "rank": int(row["rank"]),
            "growth_pct": None if pd.isna(row["growth_pct"]) else round(float(row["growth_pct"]), 2),
        }
        for _, row in cred.iterrows()
    ]

    metrics = data["metrics"]
    metrics.update({
        "app_latest_month": metrics["latest_month"],
        "app_latest_volume_mn": metrics["latest_volume_mn"],
        "ecosystem_latest_month": latest["month_start"].strftime("%Y-%m-%d"),
        "ecosystem_latest_volume_mn": round(float(latest["volume_mn"]), 2),
        "ecosystem_latest_value_cr": round(float(latest["value_cr"]), 2),
        "rolling_mape_pct": benchmark["models"][0]["mape_pct"],
        "rolling_validation_folds": benchmark["models"][0]["folds"],
        "model_winner": benchmark["winner_by_mape"],
    })

    TS.write_text("export const finsightData = " + json.dumps(data, indent=2) + " as const;\n")
    print(f"wrote {TS}")
    print(f"current official pulse: {latest['month_start']:%Y-%m} / {latest['volume_mn']:.2f} Mn")
    print(f"cred trend rows: {len(data['cred_trend'])}")


if __name__ == "__main__":
    main()
