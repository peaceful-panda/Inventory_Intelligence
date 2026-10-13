-- Consolidated Inventory Intelligence KPI summary
SELECT
    COUNT(*) AS total_records,

    SUM(Units_Sold) AS total_units_sold,

    ROUND(SUM(Units_Sold * Unit_Price), 2)
        AS estimated_revenue,

    ROUND(
        SUM(Units_Sold * (Unit_Price - Unit_Cost)), 2
    ) AS estimated_gross_profit,

    ROUND(AVG(Inventory_Level), 2)
        AS average_inventory_level,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN Inventory_Level <= Reorder_Point THEN 1
                ELSE 0
            END
        ) / COUNT(*), 2
    ) AS pct_records_at_or_below_reorder_point,

    ROUND(AVG(ABS(Demand_Forecast - Units_Sold)), 2)
        AS forecast_mae,

    ROUND(AVG(Demand_Forecast - Units_Sold), 2)
        AS forecast_bias

FROM inventory;
