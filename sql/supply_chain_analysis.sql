-- Supply Chain & Inventory Analytics
-- Import supply_chain_orders.csv into a table named supply_chain_orders.

-- 1. Executive KPIs
SELECT
    SUM("Revenue") AS revenue,
    SUM("Profit") AS profit,
    SUM("UnitsOrdered") AS units_ordered,
    SUM("UnitsShipped") AS units_shipped,
    ROUND(
        SUM("UnitsShipped") / NULLIF(SUM("UnitsOrdered"), 0) * 100,
        2
    ) AS fill_rate_pct,
    ROUND(AVG("StockoutFlag") * 100, 2) AS stockout_rate_pct,
    ROUND(AVG("OnTimeFlag") * 100, 2) AS on_time_rate_pct
FROM supply_chain_orders;

-- 2. Category profitability
SELECT
    "Category",
    SUM("Revenue") AS revenue,
    SUM("Profit") AS profit,
    ROUND(
        SUM("Profit") / NULLIF(SUM("Revenue"), 0) * 100,
        2
    ) AS margin_pct
FROM supply_chain_orders
GROUP BY "Category"
ORDER BY profit DESC;

-- 3. Supplier performance
SELECT
    "Supplier",
    ROUND(AVG("LeadTimeDays"), 2) AS avg_lead_time,
    ROUND(AVG("OnTimeFlag") * 100, 2) AS on_time_rate_pct,
    ROUND(AVG("StockoutFlag") * 100, 2) AS stockout_rate_pct,
    SUM("Profit") AS profit
FROM supply_chain_orders
GROUP BY "Supplier"
ORDER BY on_time_rate_pct DESC;

-- 4. Warehouse fill rate
SELECT
    "Warehouse",
    SUM("UnitsOrdered") AS units_ordered,
    SUM("UnitsShipped") AS units_shipped,
    SUM("BackorderUnits") AS backorder_units,
    ROUND(
        SUM("UnitsShipped") / NULLIF(SUM("UnitsOrdered"), 0) * 100,
        2
    ) AS fill_rate_pct
FROM supply_chain_orders
GROUP BY "Warehouse"
ORDER BY fill_rate_pct;

-- 5. Monthly trend
SELECT
    "OrderMonth",
    SUM("Revenue") AS revenue,
    SUM("Profit") AS profit,
    ROUND(AVG("StockoutFlag") * 100, 2) AS stockout_rate_pct
FROM supply_chain_orders
GROUP BY "OrderMonth"
ORDER BY "OrderMonth";

-- 6. Regional backorder exposure
SELECT
    "Region",
    SUM("BackorderUnits") AS backorder_units,
    SUM("Revenue") AS revenue,
    ROUND(AVG("StockoutFlag") * 100, 2) AS stockout_rate_pct
FROM supply_chain_orders
GROUP BY "Region"
ORDER BY backorder_units DESC;

-- 7. Shipping-mode performance
SELECT
    "ShipMode",
    COUNT(*) AS orders,
    ROUND(AVG("ShippingDays"), 2) AS avg_shipping_days,
    ROUND(AVG("OnTimeFlag") * 100, 2) AS on_time_rate_pct
FROM supply_chain_orders
GROUP BY "ShipMode"
ORDER BY avg_shipping_days;
