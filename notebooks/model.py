import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

sns.set_theme(style="whitegrid")

df = pd.read_csv('/home/claude/finsight/data/processed/monthly_totals.csv')
df['month_start'] = pd.to_datetime(df['month_start'])
df = df.sort_values('month_start').reset_index(drop=True)

# Time feature: actual calendar months since Nov 2023 (handles the 5 gaps correctly,
# unlike a plain row index which would compress the gaps)
base = pd.Timestamp('2023-11-01')
df['months_since_start'] = ((df['month_start'].dt.year - base.year) * 12 +
                             (df['month_start'].dt.month - base.month))

X = df[['months_since_start']].values
y = df['volume_mn'].values

# Train/test split: hold out the LAST 4 real months as test (temporal split,
# not random — random would leak future info into training for a time series)
n_test = 4
X_train, X_test = X[:-n_test], X[-n_test:]
y_train, y_test = y[:-n_test], y[-n_test:]

model = LinearRegression().fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_mae = mean_absolute_error(y_train, train_pred)
test_mae = mean_absolute_error(y_test, test_pred)
train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

train_mape = np.mean(np.abs((y_train - train_pred) / y_train)) * 100
test_mape = np.mean(np.abs((y_test - test_pred) / y_test)) * 100

print("=== Train/test fit (temporal holdout, last 4 real months as test) ===")
print(f"Train MAE: {train_mae:.1f} Mn, RMSE: {train_rmse:.1f} Mn, MAPE: {train_mape:.2f}%")
print(f"Test  MAE: {test_mae:.1f} Mn, RMSE: {test_rmse:.1f} Mn, MAPE: {test_mape:.2f}%")
print(f"Slope: {model.coef_[0]:.1f} Mn/month, Intercept: {model.intercept_:.1f}")

# Refit on ALL 19 verified months for the actual forward projection
final_model = LinearRegression().fit(X, y)
last_idx = df['months_since_start'].max()
future_idx = np.array([last_idx+1, last_idx+2, last_idx+3]).reshape(-1,1)
future_dates = [df['month_start'].max() + pd.DateOffset(months=i) for i in (1,2,3)]
future_pred = final_model.predict(future_idx)

# In-sample residual std for a rough prediction interval (small-n, so wide caveat applies)
resid = y - final_model.predict(X)
resid_std = resid.std(ddof=2)

print()
print("=== Next-quarter projection (Nov 2025 - Jan 2026) ===")
for d, p in zip(future_dates, future_pred):
    print(f"{d.strftime('%b-%Y')}: {p:.0f} Mn transactions  (±{1.96*resid_std:.0f} Mn, ~95% band)")

# ---- Chart: actual vs fitted vs projected ----
fig, ax = plt.subplots(figsize=(11,5))
ax.plot(df['month_start'], y, marker='o', color='#2563eb', label='Actual (19 verified months)', linewidth=2)
ax.plot(df['month_start'], final_model.predict(X), color='#94a3b8', linestyle='--', label='Linear fit (all 19 months)')
ax.plot(future_dates, future_pred, marker='D', color='#dc2626', linestyle=':', label='Next-quarter projection', linewidth=2)
ax.fill_between(future_dates, future_pred - 1.96*resid_std, future_pred + 1.96*resid_std, color='#dc2626', alpha=0.15)
for bm in pd.to_datetime(['2023-12-01','2024-02-01','2024-03-01','2024-09-01','2025-07-01']):
    ax.axvline(bm, color='#f59e0b', linestyle=':', alpha=0.3)
ax.set_ylabel('Total UPI volume (Mn transactions)')
ax.set_title('UPI Volume: Actual, Linear Fit, and Next-Quarter Projection')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%y'))
ax.tick_params(axis='x', rotation=45)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('/home/claude/finsight/notebooks/figures/05_projection.png', dpi=150)
plt.close()

# Save projection numbers
proj_df = pd.DataFrame({
    'month': [d.strftime('%Y-%m-01') for d in future_dates],
    'projected_volume_mn': future_pred,
    'lower_95': future_pred - 1.96*resid_std,
    'upper_95': future_pred + 1.96*resid_std,
})
proj_df.to_csv('/home/claude/finsight/data/processed/projection_next_quarter.csv', index=False)
