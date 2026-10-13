# Inventory Intelligence — Supply Chain Analytics

An end-to-end data analytics project that transforms supply chain inventory data into actionable descriptive insights using Python, Pandas, SQLite, SQL, and Power BI.

## Project Overview

Inventory Intelligence analyzes sales, inventory levels, reorder thresholds, estimated revenue, gross profit, and demand forecasts using a reproducible data-processing and analytics workflow.

The project demonstrates data cleaning, data-quality validation, SQL-based analysis, KPI calculation, independent metric verification, and dashboard development.

**Dataset:** Simulated supply chain inventory data  
**Observation period:** January 1 – December 30, 2024  
**Records:** 91,250  
**Columns:** 15

## Technology Stack

- **Python:** Data processing and validation
- **Pandas:** Data cleaning and metric calculations
- **SQLite:** Local analytical database
- **SQL:** Aggregations, KPI calculations, and business analysis
- **Power BI Desktop:** Interactive dashboard
- **Git and GitHub:** Version control and project presentation
- **pytest:** Testing support

## Workflow

1. **Data ingestion:** Load the raw CSV dataset.
2. **Data cleaning:** Validate dates, missing values, duplicates, and business rules.
3. **Data export:** Save the cleaned dataset separately from the raw data.
4. **Database loading:** Load cleaned records into SQLite.
5. **SQL analysis:** Calculate sales, inventory, financial, and forecast metrics.
6. **Dashboard development:** Visualize KPIs and comparisons in Power BI.
7. **Metric validation:** Compare selected Pandas and SQLite calculations independently.
8. **Reporting:** Document findings, assumptions, and limitations.

## Dashboard

The Power BI dashboard includes:

- Total units sold
- Estimated revenue
- Estimated gross profit
- Average inventory level
- Estimated revenue by warehouse
- Top 10 products by estimated revenue
- Average inventory vs. reorder point by warehouse
- Actual sales vs. demand forecast over time

**Dashboard screenshot:** Add a screenshot of the completed Power BI report here.

For example, save a screenshot as `reports/dashboard.png` and display it using:

`![Inventory Intelligence Power BI Dashboard](reports/dashboard.png)`

## Key Results

| Metric | Result |
|---|---:|
| Total records | 91,250 |
| Total units sold | 1,829,979 |
| Estimated revenue | 33,426,337.22 |
| Estimated gross profit | 11,088,201.23 |
| Estimated gross profit margin | 33.17% |
| Average inventory level | 471.52 |
| Average reorder point | 300.07 |
| Records at or below reorder point | 5.52% |
| Forecast MAE | 2.38 units |
| Forecast mean bias | +0.03 units |

Revenue and gross profit are expressed in unspecified monetary units because the dataset does not identify a currency. Gross profit is calculated before operating expenses; it is not net profit.

### Validation

Eight key metrics were calculated independently using Pandas and SQLite. All eight matched, including record count, units sold, estimated revenue, estimated gross profit, average inventory, reorder-threshold percentage, forecast MAE, and forecast bias.

## Data Quality

The completed validation checks identified:

- No missing values
- No duplicate rows
- No duplicate SKU–warehouse–date business keys
- No invalid dates detected
- No negative values in the checked sales, inventory, order quantity, and forecast fields
- Positive unit costs and prices
- Binary promotion and stockout flags
- No records where unit price was below unit cost

The raw dataset is preserved separately from the cleaned output.

## Project Structure

```text
Inventory_Intelligence/
├── data/
│   ├── raw/
│   │   └── supply_chain_dataset1.csv
│   ├── processed/
│   │   └── supply_chain_cleaned.csv
│   └── inventory_intelligence.db
├── dashboard/
├── References/
├── reports/
│   ├── findings.md
│   └── dashboard.png
├── sql/
│   ├── 01_basic_data_checks.sql
│   ├── 02_sales_analysis.sql
│   ├── 03_inventory_analysis.sql
│   ├── 04_forecast_analysis.sql
│   ├── 05_forecast_metrics.sql
│   └── 06_kpi_summary.sql
├── src/
│   ├── clean_data.py
│   ├── load_db.py
│   └── validate_metrics.py
├── tests/
├── run_sql.py
└── README.md
```

This structure describes the intended project layout; verify it against the actual files before publishing.

## Setup and Execution

### 1. Create and activate a virtual environment

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install pandas openpyxl pytest
```

### 3. Prepare the data

Place the original dataset at:

`data/raw/supply_chain_dataset1.csv`

Run the cleaning script:

```powershell
python src/clean_data.py
```

### 4. Load the SQLite database

```powershell
python src/load_db.py
```

### 5. Run SQL analysis

For example:

```powershell
python run_sql.py
```

Update `SQL_PATH` in `run_sql.py` to select the SQL file you want to execute.

### 6. Validate metrics

```powershell
python src/validate_metrics.py
```

The completed validation run reported that all eight metric comparisons passed.

### 7. Open the Power BI dashboard

Open the Power BI report file included in the repository, if provided. If the `.pbix` file is not yet saved or included, open Power BI Desktop and connect to the cleaned CSV.

## Limitations

- The dataset is simulated and does not establish real-world business performance.
- The currency is unspecified.
- The stockout flag is zero for every record, so a meaningful stockout rate cannot be calculated from it.
- Forecast evaluation has not yet demonstrated improvement over a baseline method.
- Units sold may differ from true demand if inventory availability constrained sales.
- Average inventory comparisons do not identify every SKU requiring replenishment at a particular moment.
- The observed data runs from January 1 through December 30, 2024; December 31 is absent.

## Future Improvements

- Compare forecasts against simple baseline models.
- Evaluate forecast errors by SKU, warehouse, and time period.
- Investigate replenishment signals at the SKU–warehouse level.
- Add meaningful stockout data and inventory movement history.
- Add automated tests and a repeatable end-to-end execution workflow.

## References

Dataset source: [High Dimensional Supply Chain Inventory Dataset — Kaggle](https://www.kaggle.com/datasets/ziya07/high-dimensional-supply-chain-inventory-dataset?resource=download)

Verify the dataset's license and redistribution conditions before publishing the raw data.

## Author

Developed as a portfolio project to demonstrate practical skills in data analytics, SQL, Python, data validation, and business intelligence.