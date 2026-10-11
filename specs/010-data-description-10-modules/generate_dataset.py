#!/usr/bin/env python3
"""
Generate the Wandering Fork dataset (2 franchises x 120 days = 240 rows)
with designed statistical properties.

Harbour days 1-30 are copied verbatim from the legacy CSV for the 8
original columns. New columns are generated for all 120 days.
"""

import numpy as np
import pandas as pd
from pathlib import Path

SPEC_DIR = Path(__file__).parent
REPO_ROOT = SPEC_DIR.parent.parent
LEGACY_CSV = REPO_ROOT / "specs" / "005-data-description-course" / "wandering-fork-dataset.csv"
OUT_DIR = REPO_ROOT / "teaching" / "data-description" / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CSV_PATH = OUT_DIR / "wandering-fork.csv"
XLSX_PATH = OUT_DIR / "wandering-fork.xlsx"

N_DAYS = 120
SEED = 42
np.random.seed(SEED)

FRANCHISES = ["Harbour", "Campus"]
WEATHER = ["Sunny", "Cloudy", "Rainy"]
DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

legacy = pd.read_csv(LEGACY_CSV)
assert len(legacy) == 30, "Legacy CSV must have 30 rows"
legacy_cols = ["day", "date", "day_of_week", "weather", "temperature_c",
               "customer_count", "items_sold", "daily_revenue_eur"]
for c in legacy_cols:
    assert c in legacy.columns, f"Missing legacy column: {c}"

start_date = pd.Timestamp("2026-04-06")
dates = [start_date + pd.Timedelta(days=i) for i in range(N_DAYS)]

# ─── Build Harbour (franchise A) ────────────────────────────────────────
harbour_rows = []

for i in range(N_DAYS):
    d = dates[i]
    dow = d.day_name()
    month = d.month_name()

    if i < 30:
        # Days 1-30: copy legacy verbatim for the 8 original columns
        base_row = legacy.iloc[i][legacy_cols].to_dict()
        franchise = "Harbour"
    else:
        # Days 31-120: generate new Harbour-like data
        w_probs = [0.45, 0.35, 0.20]
        weather = np.random.choice(WEATHER, p=w_probs)
        day_of_year = d.dayofyear
        seasonal = 15 + 10 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
        temp = round(seasonal + np.random.normal(0, 3), 1)
        base_traffic = 45 if dow in ["Saturday", "Sunday"] else 35
        if weather == "Sunny":
            base_traffic += 10
        elif weather == "Rainy":
            base_traffic -= 10
        foot_traffic = max(10, int(np.random.normal(base_traffic, 8)))
        promo = np.random.choice(["Yes", "No"], p=[0.15, 0.85])
        event = np.random.choice(["Yes", "No"], p=[0.10, 0.90])
        staff = np.random.randint(2, 6)
        cust_base = foot_traffic * 0.6
        if weather == "Sunny":
            cust_base *= 1.15
        elif weather == "Rainy":
            cust_base *= 0.75
        if promo == "Yes":
            cust_base *= 1.25
        customers = max(5, int(np.random.normal(cust_base, 5)))
        # Ensure customers <= foot_traffic
        if customers > foot_traffic:
            customers = foot_traffic
        items_per_cust = np.random.uniform(1.2, 1.6)
        items = int(customers * items_per_cust)
        rev_per_item = np.random.uniform(8, 12)
        revenue = round(items * rev_per_item, 2)
        # Add a couple of high-revenue outlier days (absolute values)
        # Calibrated to keep overall skew <= 0.5
        if i == 44:
            revenue = 1000.00
        elif i == 79:
            revenue = 1050.00
        waste = round(np.random.gamma(2, 1), 2)
        sat_base = 3.5
        if weather == "Sunny":
            sat_base += 0.5
        elif weather == "Rainy":
            sat_base -= 0.5
        if revenue > 700:
            sat_base += 0.3
        satisfaction = int(np.clip(np.random.normal(sat_base, 0.7), 1, 5))

        base_row = {
            "day": i + 1,
            "date": d.strftime("%Y-%m-%d"),
            "day_of_week": dow,
            "weather": weather,
            "temperature_c": temp,
            "customer_count": customers,
            "items_sold": items,
            "daily_revenue_eur": revenue,
        }
        franchise = "Harbour"

    # New columns generated for ALL days (including 1-30)
    if i < 30:
        # For legacy days, generate new columns consistent with the legacy values
        weather = base_row["weather"]
        temp = base_row["temperature_c"]
        customers = base_row["customer_count"]
        items = base_row["items_sold"]
        revenue = base_row["daily_revenue_eur"]
        dow = base_row["day_of_week"]

        # Foot traffic: reverse-engineer from customers (customers ~ 0.6 * foot_traffic)
        foot_traffic = max(customers, int(customers / 0.6 + np.random.normal(0, 5)))
        # Ensure customers <= foot_traffic
        if customers > foot_traffic:
            customers = foot_traffic
        # Promo/event: low probability for legacy period
        promo = np.random.choice(["Yes", "No"], p=[0.10, 0.90])
        event = np.random.choice(["Yes", "No"], p=[0.05, 0.95])
        staff = np.random.randint(2, 6)
        waste = round(np.random.gamma(2, 1), 2)
        sat_base = 3.5
        if weather == "Sunny":
            sat_base += 0.5
        elif weather == "Rainy":
            sat_base -= 0.5
        if revenue > 700:
            sat_base += 0.3
        satisfaction = int(np.clip(np.random.normal(sat_base, 0.7), 1, 5))
    else:
        # Already generated above
        pass

    row = {
        "franchise": franchise,
        "day": i + 1,
        "date": base_row["date"],
        "day_of_week": base_row["day_of_week"],
        "month": month,
        "weather": base_row["weather"],
        "temperature_c": base_row["temperature_c"],
        "event_nearby": event,
        "promo_active": promo,
        "staff_on_duty": staff,
        "foot_traffic": foot_traffic,
        "customer_count": base_row["customer_count"],
        "items_sold": base_row["items_sold"],
        "daily_revenue_eur": base_row["daily_revenue_eur"],
        "waste_kg": waste,
        "satisfaction_rating": satisfaction,
    }
    harbour_rows.append(row)

# ─── Build Campus (franchise B) ─────────────────────────────────────────
campus_rows = []

for i in range(N_DAYS):
    d = dates[i]
    dow = d.day_name()
    month = d.month_name()

    w_probs = [0.45, 0.35, 0.20]
    weather = np.random.choice(WEATHER, p=w_probs)
    day_of_year = d.dayofyear
    seasonal = 15 + 10 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
    temp = round(seasonal + np.random.normal(0, 3), 1)

    is_weekend = dow in ["Saturday", "Sunday"]
    is_friday = dow == "Friday"

    if is_weekend:
        base_traffic = 20
    elif is_friday:
        base_traffic = 55
    else:
        base_traffic = 65

    if weather == "Sunny":
        base_traffic += 8
    elif weather == "Rainy":
        base_traffic -= 12

    event = np.random.choice(["Yes", "No"], p=[0.25, 0.75])  # Higher event prob
    if event == "Yes":
        base_traffic *= 2.2  # Stronger event boost for skew

    foot_traffic = max(5, int(np.random.normal(base_traffic, 10)))
    promo = np.random.choice(["Yes", "No"], p=[0.10, 0.90])
    staff = np.random.randint(2, 5)

    cust_base = foot_traffic * 0.55
    if promo == "Yes":
        cust_base *= 1.2
    customers = max(3, int(np.random.normal(cust_base, 6)))

    # Ensure customers <= foot_traffic
    if customers > foot_traffic:
        customers = foot_traffic

    items_per_cust = np.random.uniform(1.1, 1.5)
    items = int(customers * items_per_cust)
    rev_per_item = np.random.uniform(7, 11)
    revenue = round(items * rev_per_item, 2)
    waste = round(np.random.gamma(1.5, 1), 2)

    sat_base = 3.2
    if weather == "Sunny":
        sat_base += 0.4
    elif weather == "Rainy":
        sat_base -= 0.4
    if event == "Yes":
        sat_base += 0.2
    satisfaction = int(np.clip(np.random.normal(sat_base, 0.8), 1, 5))

    row = {
        "franchise": "Campus",
        "day": i + 1,
        "date": d.strftime("%Y-%m-%d"),
        "day_of_week": dow,
        "month": month,
        "weather": weather,
        "temperature_c": temp,
        "event_nearby": event,
        "promo_active": promo,
        "staff_on_duty": staff,
        "foot_traffic": foot_traffic,
        "customer_count": customers,
        "items_sold": items,
        "daily_revenue_eur": revenue,
        "waste_kg": waste,
        "satisfaction_rating": satisfaction,
    }
    campus_rows.append(row)

# ─── Combine and write CSV ──────────────────────────────────────────────
df = pd.DataFrame(harbour_rows + campus_rows)

cols = ["franchise", "day", "date", "day_of_week", "month", "weather",
        "temperature_c", "event_nearby", "promo_active", "staff_on_duty",
        "foot_traffic", "customer_count", "items_sold", "daily_revenue_eur",
        "waste_kg", "satisfaction_rating"]
df = df[cols]

df.to_csv(CSV_PATH, index=False)
print(f"Written {len(df)} rows to {CSV_PATH}")

# ─── Write XLSX with multiple sheets ────────────────────────────────────
with pd.ExcelWriter(XLSX_PATH, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="data", index=False)
    ws = writer.sheets["data"]
    from openpyxl.worksheet.table import Table, TableStyleInfo
    tab = Table(displayName="tblFork", ref=f"A1:P{len(df)+1}")
    tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                         showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    ws.add_table(tab)

    harbour_30 = df[(df["franchise"] == "Harbour") & (df["day"] <= 30)].copy()
    harbour_30.to_excel(writer, sheet_name="harbour_30d", index=False)

    campus_30 = df[(df["franchise"] == "Campus") & (df["day"] <= 30)].copy()
    campus_30.to_excel(writer, sheet_name="campus_30d", index=False)

    dict_data = [
        ["franchise", "Qualitative nominal", "", "Franchise name: Harbour or Campus"],
        ["day", "Quantitative discrete", "day number", "Day index within franchise (1-120)"],
        ["date", "Date", "YYYY-MM-DD", "Calendar date"],
        ["day_of_week", "Qualitative nominal", "", "Monday ... Sunday"],
        ["month", "Qualitative ordinal", "", "April ... August (calendar order)"],
        ["weather", "Qualitative nominal", "", "Sunny / Cloudy / Rainy"],
        ["temperature_c", "Quantitative continuous", "degC", "Daily temperature"],
        ["event_nearby", "Qualitative nominal (binary)", "", "Yes / No - event near the truck"],
        ["promo_active", "Qualitative nominal (binary)", "", "Yes / No - promotion running"],
        ["staff_on_duty", "Quantitative discrete", "people", "Staff working that day"],
        ["foot_traffic", "Quantitative discrete", "people", "Passers-by count"],
        ["customer_count", "Quantitative discrete", "customers", "Number of customers served"],
        ["items_sold", "Quantitative discrete", "items", "Total items sold"],
        ["daily_revenue_eur", "Quantitative continuous", "EUR", "Total revenue for the day"],
        ["waste_kg", "Quantitative continuous", "kg", "Food waste (right-skewed)"],
        ["satisfaction_rating", "Qualitative ordinal", "1-5", "Customer satisfaction rating"],
    ]
    dict_df = pd.DataFrame(dict_data, columns=["name", "type", "unit", "meaning"])
    dict_df.to_excel(writer, sheet_name="dictionary", index=False)

print(f"Written XLSX with 4 sheets to {XLSX_PATH}")

# ─── Secondary datasets ─────────────────────────────────────────────────
payroll = pd.DataFrame({
    "role": ["CEO"] + [f"Staff_{i}" for i in range(1, 11)],
    "annual_salary_eur": [180000] + list(np.random.randint(25000, 45000, 10)),
})
payroll_path = OUT_DIR / "payroll-skew.csv"
payroll.to_csv(payroll_path, index=False)
print(f"Written payroll-skew.csv ({len(payroll)} rows)")

bakery_rows = []
outlets = ["Riverside", "Hilltop"]
for outlet in outlets:
    for i in range(60):
        d = start_date + pd.Timedelta(days=i)
        dow = d.day_name()
        month = d.month_name()
        weather = np.random.choice(WEATHER, p=[0.4, 0.35, 0.25])
        temp = round(15 + 10 * np.sin(2 * np.pi * (d.dayofyear - 80) / 365) + np.random.normal(0, 3), 1)
        base_traffic = 40 if dow in ["Saturday", "Sunday"] else 30
        if weather == "Sunny":
            base_traffic += 8
        elif weather == "Rainy":
            base_traffic -= 8
        foot = max(5, int(np.random.normal(base_traffic, 6)))
        customers = max(3, int(foot * np.random.uniform(0.5, 0.7)))
        items = int(customers * np.random.uniform(1.2, 1.8))
        revenue = round(items * np.random.uniform(5, 9), 2)
        waste = round(np.random.gamma(1.5, 0.8), 2)
        sat = int(np.clip(np.random.normal(3.5, 0.7), 1, 5))
        bakery_rows.append({
            "outlet": outlet, "day": i+1, "date": d.strftime("%Y-%m-%d"),
            "day_of_week": dow, "month": month, "weather": weather,
            "temperature_c": temp, "foot_traffic": foot,
            "customer_count": customers, "items_sold": items,
            "daily_revenue_eur": revenue, "waste_kg": waste,
            "satisfaction_rating": sat,
        })
bakery_df = pd.DataFrame(bakery_rows)
bakery_path = OUT_DIR / "lakeside-bakery.csv"
bakery_df.to_csv(bakery_path, index=False)
print(f"Written lakeside-bakery.csv ({len(bakery_df)} rows)")

print("\nAll datasets generated successfully.")