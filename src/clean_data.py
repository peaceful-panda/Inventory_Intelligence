
from pathlib import Path

import pandas as pd


# Find the project folder and the raw dataset.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "supply_chain_dataset1.csv"

def check_data_quality(df):
    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    print("\n--- DATE RANGE ---")
    dates = pd.to_datetime(df["Date"], errors="coerce")
    print(f"Earliest date: {dates.min()}")
    print(f"Latest date:   {dates.max()}")
    print(f"Invalid dates: {dates.isna().sum()}")
    print(f"Unique dates:  {dates.nunique()}")

    print("\n--- UNIQUE COUNTS ---")
    for column in ["SKU_ID", "Warehouse_ID", "Supplier_ID", "Region"]:
        print(f"{column}: {df[column].nunique()}")

    print("\n--- NUMERIC RANGES ---")
    numeric_columns = [
        "Units_Sold",
        "Inventory_Level",
        "Supplier_Lead_Time_Days",
        "Reorder_Point",
        "Order_Quantity",
        "Unit_Cost",
        "Unit_Price",
        "Demand_Forecast",
    ]
    print(df[numeric_columns].describe().round(2))

    print("\n--- FLAG VALUES ---")
    for column in ["Promotion_Flag", "Stockout_Flag"]:
        print(f"{column}: {sorted(df[column].unique())}")

    print("\n--- RECORDS PER SKU AND WAREHOUSE ---")
    records = df.groupby(["SKU_ID", "Warehouse_ID"]).size()
    print(records.describe())
    print(f"Unique SKU-warehouse combinations: {len(records)}")
    print(f"Combinations with unexpected record counts: {(records != 365).sum()}")

def validate_data(df):
    print("\n--- BUSINESS RULE VALIDATION ---")

    checks = {
        "Negative units sold": df["Units_Sold"] < 0,
        "Negative inventory": df["Inventory_Level"] < 0,
        "Negative order quantity": df["Order_Quantity"] < 0,
        "Non-positive unit cost": df["Unit_Cost"] <= 0,
        "Non-positive unit price": df["Unit_Price"] <= 0,
        "Negative demand forecast": df["Demand_Forecast"] < 0,
        "Invalid promotion flag": ~df["Promotion_Flag"].isin([0, 1]),
        "Invalid stockout flag": ~df["Stockout_Flag"].isin([0, 1]),
    }

    for check_name, condition in checks.items():
        print(f"{check_name}: {condition.sum()}")

    print(
        "Selling price below unit cost:",
        (df["Unit_Price"] < df["Unit_Cost"]).sum()
    )

    print("\n--- DUPLICATE BUSINESS KEYS ---")
    duplicate_keys = df.duplicated(
        subset=["SKU_ID", "Warehouse_ID", "Date"]
    )
    print(f"Duplicate SKU-warehouse-date records: {duplicate_keys.sum()}")


def main():
    # Load the CSV into a Pandas DataFrame.
    df = pd.read_csv(RAW_DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"], errors="raise")
    # Display basic information about the dataset.
    print("\n--- DATASET SHAPE ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATA TYPES AND NON-NULL COUNTS ---")
    df.info()

    print("\n--- MISSING VALUES PER COLUMN ---")
    print(df.isnull().sum())

    check_data_quality(df)
    validate_data(df)

    output_path = PROJECT_ROOT / "data" / "processed" / "supply_chain_cleaned.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"\nCleaned dataset saved to: {output_path}")
    print(f"Saved rows: {len(df)}")
    print(f"Date data type: {df['Date'].dtype}")

if __name__ == "__main__":
    main()
