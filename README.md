# 📦 Supply Chain & Inventory Analytics

## Overview

A business analytics project designed to evaluate supply-chain efficiency, inventory fulfillment, supplier reliability, warehouse performance, shipping operations, revenue, and profitability.

The project demonstrates how raw operational data can be transformed into actionable insights using **Python, SQL, Power BI, Excel, and Streamlit**.

---

## 🎯 Business Objective

The objective is to identify operational bottlenecks and understand how supply-chain performance affects revenue, profitability, inventory availability, and customer fulfillment.

### Key Business Questions

1. Which product categories generate the highest revenue and profit?
2. Which suppliers have the best delivery performance?
3. Which suppliers have long lead times or high stockout rates?
4. Which warehouses have the lowest fulfillment rates?
5. Where are backorders concentrated?
6. Which shipping modes provide the best on-time performance?
7. How do revenue and profit change over time?
8. Which operational areas should management prioritize for improvement?

---

## 🛠️ Tools & Technologies

- **Python** — Data preparation, KPI analysis and exploratory analysis
- **Pandas** — Data manipulation and aggregation
- **SQL** — Business-focused analytical queries
- **Power BI** — Interactive supply-chain dashboard
- **Excel** — Supporting data exploration
- **Streamlit** — Interactive analytical dashboard
- **Matplotlib** — Data visualization

---

## 📁 Project Structure

```text
Supply-Chain-Inventory-Analytics/
│
├── data/
│   └── supply_chain_orders.csv
│
├── src/
│   └── 01_analysis.py
│
├── sql/
│   └── supply_chain_analysis.sql
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── kpis.csv
│   ├── category_performance.csv
│   ├── supplier_performance.csv
│   ├── regional_performance.csv
│   ├── monthly_trend.csv
│   ├── warehouse_performance.csv
│   ├── 01_revenue_by_category.png
│   ├── 02_supplier_on_time.png
│   └── 03_monthly_revenue_profit.png
│
├── POWER_BI_SPEC.md
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Analytical Areas

### 1. Executive KPIs

The project tracks:

- Revenue
- Profit
- Units Ordered
- Units Shipped
- Fill Rate
- Stockout Rate
- On-Time Delivery Rate

### 2. Category Performance

Evaluates revenue, profit, units shipped and stockout exposure by product category.

### 3. Supplier Performance

Compares suppliers using:

- Revenue
- Profit
- Average lead time
- On-time delivery rate
- Stockout rate

### 4. Warehouse Performance

Measures:

- Order volume
- Units ordered
- Units shipped
- Fill rate
- Stockout rate
- Average shipping time

### 5. Regional Operations

Compares revenue, profit, fulfillment and backorder exposure across regions.

### 6. Shipping Performance

Analyzes shipping modes and delivery performance using:

- Average shipping days
- On-time delivery rate
- Order volume

### 7. Time-Series Analysis

Tracks monthly:

- Revenue
- Profit
- Units shipped
- Stockout rate

---

## 💡 Business Insights Framework

The analysis is designed to help management identify:

- High-performing product categories
- Suppliers requiring performance improvement
- Warehouses with fulfillment problems
- Regions with high backorder exposure
- Inventory availability issues
- Shipping bottlenecks
- Changes in revenue and profitability over time

---

## 🐍 Python Analysis

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/01_analysis.py
```

The script reads the dataset from `data/` and generates analytical CSV files and charts inside `outputs/`.

---

## 📈 Streamlit Dashboard

Run from the project root:

```bash
streamlit run dashboard/app.py
```

The dashboard provides interactive KPI cards, category performance, supplier analysis, warehouse performance and regional filtering.

---

## 🗄️ SQL Analysis

The `sql/supply_chain_analysis.sql` file contains business queries covering:

- Executive KPIs
- Category profitability
- Supplier performance
- Warehouse fill rate
- Monthly trends
- Regional backorders
- Shipping-mode performance

The SQL is written in a PostgreSQL-style format and can be adapted to other SQL environments.

---

## 📊 Power BI Dashboard

The Power BI specification contains a three-page dashboard design:

### Page 1 — Supply Chain Executive Overview

- Revenue
- Profit
- Fill Rate
- On-Time Rate
- Stockout Rate
- Monthly Revenue & Profit
- Category Performance
- Regional Performance

### Page 2 — Supplier & Warehouse Performance

- Supplier On-Time Rate
- Supplier Lead Time
- Supplier Stockout Rate
- Warehouse Fill Rate
- Warehouse Stockout Rate

### Page 3 — Inventory & Fulfillment

- Backorder Units
- Stockout Rate
- Shipping Performance
- Units Ordered vs Units Shipped
- Fulfillment Performance

---

## 📌 Skills Demonstrated

**Data Analysis:** Python, Pandas, Excel  
**Data Querying:** SQL  
**Business Intelligence:** Power BI  
**Dashboarding:** Power BI, Streamlit  
**Visualization:** Matplotlib  
**Business Analytics:** Supply-chain KPIs, inventory analysis, supplier analysis, warehouse analysis, fulfillment analysis and profitability analysis

---

## 👨‍💻 Portfolio Context

This project is designed as a practical business analytics case study rather than a purely technical exercise. It demonstrates the end-to-end workflow of taking operational data, analyzing business performance, creating KPIs, identifying improvement areas, and presenting findings through dashboards.

---

## ⚠️ Dataset Disclaimer

The included dataset is synthetically generated for educational and portfolio purposes using a fixed random seed. It does not represent a real company, supplier, warehouse, employee, customer, or transaction.
