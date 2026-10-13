-- 1. Overall inventory summary
SELECT
    ROUND(AVG(Inventory_Level), 2) AS average_inventory_level,
    MIN(Inventory_Level) AS minimum_inventory_level,
    MAX(Inventory_Level) AS maximum_inventory_level,
    ROUND(AVG(Reorder_Point), 2) AS average_reorder_point
FROM inventory;


-- 2. Records at or below the reorder point
SELECT
    COUNT(*) AS total_records,
    SUM(
        CASE
            WHEN Inventory_Level <= Reorder_Point THEN 1
            ELSE 0
        END
    ) AS records_at_or_below_reorder_point,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Inventory_Level <= Reorder_Point THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS percentage_at_or_below_reorder_point
FROM inventory;


-- 3. Average inventory level by product
SELECT
    SKU_ID,
    ROUND(AVG(Inventory_Level), 2) AS average_inventory_level,
    ROUND(AVG(Reorder_Point), 2) AS average_reorder_point
FROM inventory
GROUP BY SKU_ID
ORDER BY average_inventory_level DESC
LIMIT 10;
