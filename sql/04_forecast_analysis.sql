-- Overall demand forecast accuracy
SELECT
    ROUND(AVG(ABS(Demand_Forecast - Units_Sold)), 2)
        AS mean_absolute_error,

    ROUND(AVG(Demand_Forecast - Units_Sold), 2)
        AS average_forecast_bias,

    ROUND(AVG(Units_Sold), 2)
        AS average_actual_units_sold,

    ROUND(AVG(Demand_Forecast), 2)
        AS average_forecast_units
FROM inventory;
