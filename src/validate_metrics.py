from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_PATH = PROJECT_ROOT / "data" / "processed" / "supply_chain_cleaned.csv"
DB_PATH = PROJECT_ROOT / "data" / "inventory_intelligence.db"


def main():
    df = pd.read_csv(CSV_PATH)

    # Calculate KPIs using Pandas
    python_metrics = {
        "total_records": len(df),
        "total_units_sold": int(df["Units_Sold"].sum()),
        "estimated_revenue": round(
            (df["Units_Sold"] * df["Unit_Price"]).sum(), 2
        ),
        "estimated_gross_profit": round(
            (
                df["Units_Sold"]
                * (df["Unit_Price"] - df["Unit_Cost"])
            ).sum(),
            2,
        ),
        "average_inventory_level": round(
            df["Inventory_Level"].mean(), 2
        ),
        "pct_records_at_or_below_reorder_point": round(
            (df["Inventory_Level"] <= df["Reorder_Point"]).mean()
            * 100,
            2,
        ),
        "forecast_mae": round(
            (df["Demand_Forecast"] - df["Units_Sold"]).abs().mean(),
            2,
        ),
        "forecast_bias": round(
            (df["Demand_Forecast"] - df["Units_Sold"]).mean(),
            2,
        ),
    }

    # Retrieve the same KPIs from SQLite
    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute("""
            SELECT
                COUNT(*),
                SUM(Units_Sold),
                ROUND(SUM(Units_Sold * Unit_Price), 2),
                ROUND(
                    SUM(Units_Sold * (Unit_Price - Unit_Cost)), 2
                ),
                ROUND(AVG(Inventory_Level), 2),
                ROUND(
                    100.0 * SUM(
                        CASE
                            WHEN Inventory_Level <= Reorder_Point
                            THEN 1 ELSE 0
                        END
                    ) / COUNT(*), 2
                ),
                ROUND(AVG(ABS(Demand_Forecast - Units_Sold)), 2),
                ROUND(AVG(Demand_Forecast - Units_Sold), 2)
            FROM inventory
        """).fetchone()

    sql_metrics = dict(zip(python_metrics.keys(), row))

    print("\n--- PYTHON VS SQL VALIDATION ---")

    all_match = True

    for metric, python_value in python_metrics.items():
        sql_value = sql_metrics[metric]
        matches = abs(python_value - sql_value) < 0.001

        print(
            f"{metric}: Python={python_value}, "
            f"SQL={sql_value}, Match={matches}"
        )

        if not matches:
            all_match = False

    print("\nFINAL RESULT:", "ALL CHECKS PASSED" if all_match
          else "MISMATCH FOUND")


if __name__ == "__main__":
    main()