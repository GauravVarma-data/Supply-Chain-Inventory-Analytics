import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "supply_chain_orders.csv"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["OrderDate"])

# -----------------------------
# Executive KPIs
# -----------------------------
kpis = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Profit",
        "Units Ordered",
        "Units Shipped",
        "Fill Rate",
        "Stockout Rate",
        "On-Time Rate"
    ],
    "Value": [
        df["Revenue"].sum(),
        df["Profit"].sum(),
        df["UnitsOrdered"].sum(),
        df["UnitsShipped"].sum(),
        df["UnitsShipped"].sum() / df["UnitsOrdered"].sum(),
        df["StockoutFlag"].mean(),
        df["OnTimeFlag"].mean()
    ]
})
kpis.to_csv(OUT / "kpis.csv", index=False)

# -----------------------------
# Category performance
# -----------------------------
category = df.groupby("Category", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Units=("UnitsShipped", "sum"),
    Stockouts=("StockoutFlag", "sum")
)
category["ProfitMargin"] = category["Profit"] / category["Revenue"]
category.to_csv(OUT / "category_performance.csv", index=False)

# -----------------------------
# Supplier performance
# -----------------------------
supplier = df.groupby("Supplier", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    AvgLeadTime=("LeadTimeDays", "mean"),
    OnTimeRate=("OnTimeFlag", "mean"),
    StockoutRate=("StockoutFlag", "mean")
)
supplier.to_csv(OUT / "supplier_performance.csv", index=False)

# -----------------------------
# Regional performance
# -----------------------------
region = df.groupby("Region", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    UnitsOrdered=("UnitsOrdered", "sum"),
    UnitsShipped=("UnitsShipped", "sum"),
    BackorderUnits=("BackorderUnits", "sum"),
    StockoutRate=("StockoutFlag", "mean")
)
region["FillRate"] = region["UnitsShipped"] / region["UnitsOrdered"]
region.to_csv(OUT / "regional_performance.csv", index=False)

# -----------------------------
# Monthly trend
# -----------------------------
df["OrderMonth"] = df["OrderDate"].dt.to_period("M").astype(str)

monthly = df.groupby("OrderMonth", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    Units=("UnitsShipped", "sum"),
    StockoutRate=("StockoutFlag", "mean")
)
monthly.to_csv(OUT / "monthly_trend.csv", index=False)

# -----------------------------
# Warehouse performance
# -----------------------------
warehouse = df.groupby("Warehouse", as_index=False).agg(
    Orders=("OrderID", "count"),
    UnitsOrdered=("UnitsOrdered", "sum"),
    UnitsShipped=("UnitsShipped", "sum"),
    BackorderUnits=("BackorderUnits", "sum"),
    StockoutRate=("StockoutFlag", "mean"),
    AvgShippingDays=("ShippingDays", "mean")
)
warehouse["FillRate"] = warehouse["UnitsShipped"] / warehouse["UnitsOrdered"]
warehouse.to_csv(OUT / "warehouse_performance.csv", index=False)

# -----------------------------
# Charts
# -----------------------------
plt.figure(figsize=(8, 5))
category.sort_values("Revenue").plot.barh(
    x="Category", y="Revenue", legend=False
)
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig(OUT / "01_revenue_by_category.png")
plt.close()

plt.figure(figsize=(8, 5))
supplier.sort_values("OnTimeRate").plot.barh(
    x="Supplier", y="OnTimeRate", legend=False
)
plt.title("Supplier On-Time Rate")
plt.tight_layout()
plt.savefig(OUT / "02_supplier_on_time.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(monthly["OrderMonth"], monthly["Revenue"], label="Revenue")
plt.plot(monthly["OrderMonth"], monthly["Profit"], label="Profit")
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Revenue & Profit")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "03_monthly_revenue_profit.png")
plt.close()

print("Supply-chain analysis complete.")
print(f"Outputs saved to: {OUT}")
