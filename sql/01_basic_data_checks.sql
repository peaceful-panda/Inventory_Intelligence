-- 1. Count the total number of records
SELECT COUNT(*) AS total_records
FROM inventory;


-- 2. View the first 10 records
SELECT *
FROM inventory
LIMIT 10;


-- 3. Count unique products
SELECT COUNT(DISTINCT SKU_ID) AS total_products
FROM inventory;


-- 4. Count unique warehouses
SELECT COUNT(DISTINCT Warehouse_ID) AS total_warehouses
FROM inventory;


-- 5. Check the date range
SELECT
    MIN(Date) AS first_date,
    MAX(Date) AS last_date
FROM inventory;
