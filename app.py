import streamlit as st
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "supply_chain_orders.csv"

st.set_page_config(
    page_title="Supply Chain Analytics",
    page_icon="📦",
    layout="wide"
)

df = pd.read_csv(DATA, parse_dates=["OrderDate"])

st.title("📦 Supply Chain & Inventory Analytics")
st.caption("Portfolio project | Synthetic supply-chain dataset")

# Filters
regions = ["All"] + sorted(df["Region"].unique().tolist())
region = st.selectbox("Region", regions)

categories = ["All"] + sorted(df["Category"].unique().tolist())
category = st.selectbox("Category", categories)

view = df.copy()

if region != "All":
    view = view[view["Region"] == region]

if category != "All":
    view = view[view["Category"] == category]

# KPIs
revenue = view["Revenue"].sum()
profit = view["Profit"].sum()
fill_rate = view["UnitsShipped"].sum() / view["UnitsOrdered"].sum()
on_time = view["OnTimeFlag"].mean()
stockout = view["StockoutFlag"].mean()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Revenue", f"${revenue:,.0f}")
c2.metric("Profit", f"${profit:,.0f}")
c3.metric("Fill Rate", f"{fill_rate:.1%}")
c4.metric("On-Time Rate", f"{on_time:.1%}")
c5.metric("Stockout Rate", f"{stockout:.1%}")

# Category
st.subheader("Category Performance")
cat = view.groupby("Category", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum")
)
st.bar_chart(cat.set_index("Category")[["Revenue", "Profit"]])

# Supplier
st.subheader("Supplier Performance")
sup = view.groupby("Supplier", as_index=False).agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum"),
    AvgLeadTime=("LeadTimeDays", "mean"),
    OnTimeRate=("OnTimeFlag", "mean"),
    StockoutRate=("StockoutFlag", "mean")
)
st.dataframe(
    sup.sort_values("OnTimeRate", ascending=False),
    use_container_width=True
)

# Warehouse
st.subheader("Warehouse Performance")
wh = view.groupby("Warehouse", as_index=False).agg(
    Orders=("OrderID", "count"),
    UnitsOrdered=("UnitsOrdered", "sum"),
    UnitsShipped=("UnitsShipped", "sum"),
    BackorderUnits=("BackorderUnits", "sum"),
    StockoutRate=("StockoutFlag", "mean")
)
wh["FillRate"] = wh["UnitsShipped"] / wh["UnitsOrdered"]

st.dataframe(
    wh.sort_values("FillRate"),
    use_container_width=True
)

# Shipping
st.subheader("Shipping Performance")
ship = view.groupby("ShipMode", as_index=False).agg(
    Orders=("OrderID", "count"),
    AvgShippingDays=("ShippingDays", "mean"),
    OnTimeRate=("OnTimeFlag", "mean")
)
st.dataframe(ship, use_container_width=True)
