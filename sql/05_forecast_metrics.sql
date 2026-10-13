-- Additional forecast evaluation metrics
SELECT
    COUNT(*) AS total_records,

    SUM(
        CASE WHEN Units_Sold > 0 THEN 1 ELSE 0 END
    ) AS records_with_positive_sales,

    ROUND(
        AVG(
            CASE
                WHEN Units_Sold > 0
                THEN ABS(Demand_Forecast - Units_Sold) / Units_Sold
            END
        ) * 100,
        2
    ) AS mape_percent_positive_sales_only

FROM inventory;