#!/usr/bin/env python3
"""
Verify the Wandering Fork dataset invariants and recompute all statistics
for module authoring.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats

SPEC_DIR = Path(__file__).parent
REPO_ROOT = SPEC_DIR.parent.parent
DATA_DIR = REPO_ROOT / "teaching" / "data-description" / "data"
LEGACY_CSV = REPO_ROOT / "specs" / "005-data-description-course" / "wandering-fork-dataset.csv"

CSV_PATH = DATA_DIR / "wandering-fork.csv"
XLSX_PATH = DATA_DIR / "wandering-fork.xlsx"
STATS_MD = SPEC_DIR / "dataset-statistics.md"

def quartile_exc(series, q):
    """Excel QUARTILE.EXC equivalent: position (n+1)*q, linear interpolation."""
    s = series.dropna().sort_values().reset_index(drop=True)
    n = len(s)
    pos = (n + 1) * q
    if pos <= 1:
        return s.iloc[0]
    if pos >= n:
        return s.iloc[-1]
    lo = int(np.floor(pos)) - 1
    hi = int(np.ceil(pos)) - 1
    if lo == hi:
        return s.iloc[lo]
    frac = pos - np.floor(pos)
    return s.iloc[lo] * (1 - frac) + s.iloc[hi] * frac

def pearson_median_skew(series):
    """3 * (mean - median) / std (sample)."""
    s = series.dropna()
    return 3 * (s.mean() - s.median()) / s.std(ddof=1)

def verify_invariants(df):
    """Check all 8 invariants from data-model.md §2."""
    errors = []

    # 1. Harbour days 1-30 equal legacy CSV on original columns
    legacy = pd.read_csv(LEGACY_CSV)
    harbour_30 = df[(df["franchise"] == "Harbour") & (df["day"] <= 30)].copy()
    legacy_cols = ["day", "date", "day_of_week", "weather", "temperature_c",
                   "customer_count", "items_sold", "daily_revenue_eur"]
    for c in legacy_cols:
        if not harbour_30[c].reset_index(drop=True).equals(legacy[c].reset_index(drop=True)):
            errors.append(f"Invariant 1 FAIL: Harbour day 1-30 column {c} differs from legacy")

    # 2. No missing values, no duplicate (franchise, day)
    if df.isnull().any().any():
        errors.append("Invariant 2 FAIL: Missing values found")
    dup = df.duplicated(subset=["franchise", "day"]).any()
    if dup:
        errors.append("Invariant 2 FAIL: Duplicate (franchise, day) found")

    # 3. items_sold >= customer_count; customer_count <= foot_traffic; revenue > 0
    if not (df["items_sold"] >= df["customer_count"]).all():
        errors.append("Invariant 3 FAIL: items_sold < customer_count somewhere")
    if not (df["customer_count"] <= df["foot_traffic"]).all():
        errors.append("Invariant 3 FAIL: customer_count > foot_traffic somewhere")
    if not (df["daily_revenue_eur"] > 0).all():
        errors.append("Invariant 3 FAIL: revenue <= 0 somewhere")

    # 4. Campus revenue skewness > +0.5; Harbour revenue skewness within +/-0.5
    harbour_rev = df[df["franchise"] == "Harbour"]["daily_revenue_eur"]
    campus_rev = df[df["franchise"] == "Campus"]["daily_revenue_eur"]
    h_skew = stats.skew(harbour_rev, bias=False)
    c_skew = stats.skew(campus_rev, bias=False)
    if not (abs(h_skew) <= 0.5):
        errors.append(f"Invariant 4 FAIL: Harbour skewness = {h_skew:.3f} (expected |skew| <= 0.5)")
    if not (c_skew > 0.5):
        errors.append(f"Invariant 4 FAIL: Campus skewness = {c_skew:.3f} (expected > 0.5)")

    # 5. r(customers, revenue) >= 0.80 in both; |r|(temp, revenue) <= 0.35
    for name, grp in [("Harbour", harbour_rev), ("Campus", campus_rev)]:
        cust = df[df["franchise"] == name]["customer_count"]
        r_cr = grp.corr(cust)
        if r_cr < 0.80:
            errors.append(f"Invariant 5 FAIL: {name} r(customers, revenue) = {r_cr:.3f} < 0.80")
        temp = df[df["franchise"] == name]["temperature_c"]
        r_tr = grp.corr(temp)
        if abs(r_tr) > 0.35:
            errors.append(f"Invariant 5 FAIL: {name} |r|(temp, revenue) = {abs(r_tr):.3f} > 0.35")

    # 6. Weather x promo row profiles differ by >= 15 pp in at least one franchise
    for name in ["Harbour", "Campus"]:
        sub = df[df["franchise"] == name]
        ct = pd.crosstab(sub["weather"], sub["promo_active"], normalize="index") * 100
        if "Yes" in ct.columns and "No" in ct.columns:
            diff = (ct["Yes"] - ct["No"]).abs().max()
            if diff < 15:
                errors.append(f"Invariant 6 FAIL: {name} weather x promo max diff = {diff:.1f}pp < 15pp")

    # 7. At least one 1.5xIQR outlier per franchise
    for name in ["Harbour", "Campus"]:
        rev = df[df["franchise"] == name]["daily_revenue_eur"]
        q1 = quartile_exc(rev, 0.25)
        q3 = quartile_exc(rev, 0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = rev[(rev < lower) | (rev > upper)]
        if len(outliers) == 0:
            errors.append(f"Invariant 7 FAIL: {name} has no 1.5xIQR outliers")

    # 8. Every category appears at least 5 times
    for col in ["weather", "day_of_week", "month", "event_nearby", "promo_active", "satisfaction_rating"]:
        counts = df[col].value_counts()
        if (counts < 5).any():
            errors.append(f"Invariant 8 FAIL: {col} has categories with <5 occurrences: {counts[counts < 5].to_dict()}")

    return errors

def compute_stats(series, name):
    """Compute all statistics for a numeric series."""
    s = series.dropna()
    n = len(s)
    mean = s.mean()
    median = s.median()
    mode_result = stats.mode(s, keepdims=True)
    mode_val = mode_result.mode[0] if mode_result.count[0] > 1 else "No unique mode"
    min_v = s.min()
    max_v = s.max()
    rng = max_v - min_v
    var_s = s.var(ddof=1)
    std_s = s.std(ddof=1)
    cv = std_s / mean if mean != 0 else np.nan
    q1 = quartile_exc(s, 0.25)
    q3 = quartile_exc(s, 0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    skew_scipy = stats.skew(s, bias=False)
    skew_excel = s.skew()  # pandas uses Fisher-Pearson adjusted (same as Excel SKEW)
    pearson_skew = pearson_median_skew(s)
    return {
        "name": name, "n": n, "mean": mean, "median": median, "mode": mode_val,
        "min": min_v, "max": max_v, "range": rng,
        "var_s": var_s, "std_s": std_s, "cv": cv,
        "q1": q1, "q3": q3, "iqr": iqr,
        "lower_fence": lower_fence, "upper_fence": upper_fence,
        "skew_scipy": skew_scipy, "skew_excel": skew_excel, "pearson_skew": pearson_skew,
    }

def freq_table(series, name):
    """Frequency table for a qualitative series."""
    s = series.dropna()
    counts = s.value_counts().sort_index()
    total = len(s)
    rel = (counts / total * 100).round(2)
    cum = rel.cumsum().round(2)
    return pd.DataFrame({"count": counts, "rel_%": rel, "cum_%": cum}, index=counts.index)

def contingency_table(df, row_var, col_var, franchise):
    """Contingency table with row percentages."""
    sub = df[df["franchise"] == franchise]
    ct = pd.crosstab(sub[row_var], sub[col_var], margins=True)
    ct_pct = pd.crosstab(sub[row_var], sub[col_var], normalize="index", margins=True) * 100
    return ct, ct_pct.round(2)

def regression_stats(x, y):
    """Simple linear regression stats."""
    x = np.asarray(x)
    y = np.asarray(y)
    mask = ~(np.isnan(x) | np.isnan(y))
    x, y = x[mask], y[mask]
    n = len(x)
    if n < 2:
        return {}
    x_mean, y_mean = x.mean(), y.mean()
    sxx = ((x - x_mean) ** 2).sum()
    sxy = ((x - x_mean) * (y - y_mean)).sum()
    slope = sxy / sxx if sxx != 0 else np.nan
    intercept = y_mean - slope * x_mean
    y_pred = intercept + slope * x
    ss_res = ((y - y_pred) ** 2).sum()
    ss_tot = ((y - y_mean) ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else np.nan
    r = np.corrcoef(x, y)[0, 1]
    cov = np.cov(x, y, ddof=1)[0, 1]
    return {
        "n": n, "slope": slope, "intercept": intercept,
        "r": r, "r2": r2, "covariance": cov,
    }

def main():
    print("Loading dataset...")
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded {len(df)} rows")

    # Verify invariants
    print("\n=== Verifying invariants ===")
    errors = verify_invariants(df)
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        return 1
    else:
        print("OK All 8 invariants PASSED")

    # Legacy figures check
    print("\n=== Legacy figures (Harbour days 1-30) ===")
    harbour_30 = df[(df["franchise"] == "Harbour") & (df["day"] <= 30)]["daily_revenue_eur"]
    stats_30 = compute_stats(harbour_30, "Harbour_30d_revenue")
    print(f"Mean: {stats_30['mean']:.2f} (expected 628.34)")
    print(f"Std (sample): {stats_30['std_s']:.2f} (expected 137.09)")
    print(f"Median: {stats_30['median']:.2f} (expected 643.63)")
    print(f"Q1 (EXC): {stats_30['q1']:.2f} (expected 506.60)")
    print(f"Q3 (EXC): {stats_30['q3']:.2f} (expected 729.99)")
    print(f"IQR: {stats_30['iqr']:.2f} (expected 223.39)")

    # Compute all statistics for dataset-statistics.md
    print("\n=== Computing full statistics ===")
    lines = []
    lines.append("# Dataset Statistics for Module Authoring\n")
    lines.append(f"*Generated on {pd.Timestamp.now().strftime('%Y-%m-%d')} from `wandering-fork.csv`*\n")

    for franchise in ["Harbour", "Campus"]:
        sub = df[df["franchise"] == franchise]
        for subset_name, subset_df in [("120d", sub), ("30d", sub[sub["day"] <= 30])]:
            lines.append(f"## {franchise} -- {subset_name}\n")
            rev = subset_df["daily_revenue_eur"]
            stats_rev = compute_stats(rev, f"{franchise}_{subset_name}_revenue")
            lines.append("### Daily Revenue (EUR)")
            for k, v in stats_rev.items():
                if k != "name":
                    lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

            # Customers
            cust = subset_df["customer_count"]
            stats_cust = compute_stats(cust, f"{franchise}_{subset_name}_customers")
            lines.append("### Customer Count")
            for k, v in stats_cust.items():
                if k != "name":
                    lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

            # Temperature
            temp = subset_df["temperature_c"]
            stats_temp = compute_stats(temp, f"{franchise}_{subset_name}_temperature")
            lines.append("### Temperature (degC)")
            for k, v in stats_temp.items():
                if k != "name":
                    lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

            # Foot traffic
            ft = subset_df["foot_traffic"]
            stats_ft = compute_stats(ft, f"{franchise}_{subset_name}_foot_traffic")
            lines.append("### Foot Traffic")
            for k, v in stats_ft.items():
                if k != "name":
                    lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

            # Weather frequency
            lines.append("### Weather Frequency")
            ft_weather = freq_table(subset_df["weather"], "weather")
            lines.append(ft_weather.to_markdown())
            lines.append("")

            # Satisfaction frequency
            lines.append("### Satisfaction Rating Frequency")
            ft_sat = freq_table(subset_df["satisfaction_rating"], "satisfaction")
            lines.append(ft_sat.to_markdown())
            lines.append("")

            # Weather x Promo contingency
            lines.append("### Weather x Promo Contingency (row %)")
            ct, ct_pct = contingency_table(df, "weather", "promo_active", franchise)
            lines.append(ct_pct.to_markdown())
            lines.append("")

            # Regression: customers -> revenue
            lines.append("### Regression: Customers -> Revenue")
            reg = regression_stats(subset_df["customer_count"], subset_df["daily_revenue_eur"])
            for k, v in reg.items():
                lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

            # Regression: temperature -> revenue
            lines.append("### Regression: Temperature -> Revenue")
            reg2 = regression_stats(subset_df["temperature_c"], subset_df["daily_revenue_eur"])
            for k, v in reg2.items():
                lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
            lines.append("")

    # Write statistics markdown
    STATS_MD.write_text("\n".join(lines))
    print(f"\nOK Statistics written to {STATS_MD}")

    # Also verify secondary datasets
    print("\n=== Secondary datasets ===")
    payroll = pd.read_csv(DATA_DIR / "payroll-skew.csv")
    print(f"payroll-skew.csv: {len(payroll)} rows")
    print(f"  Salaries: {payroll['annual_salary_eur'].tolist()}")
    print(f"  Mean: {payroll['annual_salary_eur'].mean():.0f}, Median: {payroll['annual_salary_eur'].median():.0f}")
    print(f"  Skew: {stats.skew(payroll['annual_salary_eur'], bias=False):.3f}")

    bakery = pd.read_csv(DATA_DIR / "lakeside-bakery.csv")
    print(f"lakeside-bakery.csv: {len(bakery)} rows")
    print(f"  Outlets: {bakery['outlet'].unique()}")
    print(f"  Revenue mean: {bakery['daily_revenue_eur'].mean():.2f}")

    return 0

if __name__ == "__main__":
    exit(main())