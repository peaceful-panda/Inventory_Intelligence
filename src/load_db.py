from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "supply_chain_cleaned.csv"
)

DB_PATH = PROJECT_ROOT / "data" / "inventory_intelligence.db"


def main():
    print("Loading cleaned dataset...")

    # Read the cleaned CSV
    df = pd.read_csv(CSV_PATH, parse_dates=["Date"])

    print(f"CSV rows: {len(df)}")

    # Connect to SQLite (creates the database if needed)
    with sqlite3.connect(DB_PATH) as connection:

        # Load the DataFrame into a table named 'inventory'
        df.to_sql(
            "inventory",
            connection,
            if_exists="replace",
            index=False
        )

        # Verify the number of rows loaded
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM inventory")
        database_rows = cursor.fetchone()[0]

    print(f"Database saved to: {DB_PATH}")
    print(f"Rows loaded into inventory table: {database_rows}")

    if database_rows == len(df):
        print("SUCCESS: CSV and database row counts match.")
    else:
        print("WARNING: CSV and database row counts do not match.")


if __name__ == "__main__":
    main()