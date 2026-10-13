-- Overall sales and financial metrics
SELECT
    SUM(Units_Sold) AS total_units_sold,
    ROUND(SUM(Units_Sold * Unit_Price), 2) AS estimated_revenue,
    ROUND(
        SUM(Units_Sold * (Unit_Price - Unit_Cost)),
        2
    ) AS estimated_gross_profit
FROM inventory;

-- Top 10 products by estimated revenue
SELECT
    SKU_ID,
    SUM(Units_Sold) AS total_units_sold,
    ROUND(SUM(Units_Sold * Unit_Price), 2) AS estimated_revenue,
    ROUND(
        SUM(Units_Sold * (Unit_Price - Unit_Cost)),
        2
    ) AS estimated_gross_profit
FROM inventory
GROUP BY SKU_ID
ORDER BY estimated_revenue DESC
LIMIT 10;

-- Warehouse-level sales performance
SELECT
    Warehouse_ID,
    SUM(Units_Sold) AS total_units_sold,
    ROUND(SUM(Units_Sold * Unit_Price), 2) AS estimated_revenue,
    ROUND(
        SUM(Units_Sold * (Unit_Price - Unit_Cost)),
        2
    ) AS estimated_gross_profit
FROM inventory
GROUP BY Warehouse_ID
ORDER BY estimated_revenue DESC;
