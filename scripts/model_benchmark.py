"""Benchmark simple, auditable forecasts with expanding-window one-step validation."""
from pathlib import Path
import json
import math
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "monthly_totals.csv"
OUTPUT_JSON = ROOT / "data" / "processed" / "model_benchmark.json"


def linear_forecast(values: np.ndarray, horizon: int = 1) -> float:
    x = np.arange(len(values), dtype=float)
    slope, intercept = np.polyfit(x, values.astype(float), 1)
    return float(intercept + slope * (len(values) - 1 + horizon))


def drift_forecast(values: np.ndarray) -> float:
    if len(values) < 2:
        return float(values[-1])
    return float(values[-1] + np.mean(np.diff(values)))


def forecast(method: str, values: np.ndarray) -> float:
    if method == "last_value":
        return float(values[-1])
    if method == "rolling_mean_3":
        return float(np.mean(values[-3:]))
    if method == "drift":
        return drift_forecast(values)
    if method == "linear_trend":
        return linear_forecast(values)
    raise ValueError(method)


def main() -> None:
    df = pd.read_csv(INPUT, parse_dates=["month_start"]).sort_values("month_start")
    values = df["volume_mn"].to_numpy(dtype=float)
    methods = ["last_value", "rolling_mean_3", "drift", "linear_trend"]
    min_train = 8
    rows = []
    for method in methods:
        errors = []
        abs_errors = []
        folds = []
        for origin in range(min_train, len(values)):
            train = values[:origin]
            actual = float(values[origin])
            prediction = forecast(method, train)
            if actual == 0:
                continue
            error_pct = abs((actual - prediction) / actual) * 100
            errors.append(error_pct)
            abs_errors.append(abs(actual - prediction))
            folds.append({
                "origin_month": df.iloc[origin]["month_start"].strftime("%Y-%m-%d"),
                "actual_volume_mn": round(actual, 2),
                "predicted_volume_mn": round(prediction, 2),
                "ape_pct": round(error_pct, 4),
            })
        rows.append({
            "method": method,
            "folds": len(errors),
            "mape_pct": round(float(np.mean(errors)), 4),
            "mae_mn": round(float(np.mean(abs_errors)), 2),
            "last_forecast_mn": round(forecast(method, values), 2),
            "fold_details": folds,
        })
    rows.sort(key=lambda item: item["mape_pct"])
    result = {
        "input_start": df.iloc[0]["month_start"].strftime("%Y-%m-%d"),
        "input_end": df.iloc[-1]["month_start"].strftime("%Y-%m-%d"),
        "observations": int(len(values)),
        "validation": "expanding-window one-step-ahead; minimum training window = 8 verified observations",
        "winner_by_mape": rows[0]["method"],
        "models": rows,
    }
    OUTPUT_JSON.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "models"}, indent=2))
    for row in rows:
        print(f"{row['method']}: MAPE={row['mape_pct']:.2f}% MAE={row['mae_mn']:.2f}M folds={row['folds']}")


if __name__ == "__main__":
    main()
