import { describe, expect, it } from "vitest";
import { finsightData } from "./finsightData";

describe("Finsight v1.2 analytical contract", () => {
  it("keeps the official ecosystem pulse separate from the app-wise record", () => {
    expect(finsightData.metrics.latest_month).toBe("2025-10-01");
    expect(finsightData.current_pulse.month).toBe("2026-08-01");
    expect(finsightData.current_pulse.volume_mn).toBe(24508.96);
    expect(finsightData.current_pulse.label).toContain("not mixed");
  });

  it("contains a comparable multi-method benchmark and CRED trend", () => {
    expect(finsightData.model_benchmark).toHaveLength(4);
    expect(finsightData.model_benchmark[0].method).toBe("linear_trend");
    expect(finsightData.metrics.rolling_validation_folds).toBe(11);
    expect(finsightData.metrics.rolling_mape_pct).toBeCloseTo(3.22, 2);
    expect(finsightData.cred_trend).toHaveLength(19);
    expect(finsightData.cred_trend.at(-1)?.month_start).toBe("2025-10-01");
  });
});
