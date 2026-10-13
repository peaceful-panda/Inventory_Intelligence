from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parent
DB_PATH = PROJECT_ROOT / "data" / "inventory_intelligence.db"
SQL_PATH = PROJECT_ROOT / "sql" / "06_kpi_summary.sql"

with sqlite3.connect(DB_PATH) as connection:
    sql_text = SQL_PATH.read_text(encoding="utf-8")

    for query in sql_text.split(";"):
        query = query.strip()

        if not query:
            continue


        cursor = connection.execute(query)
        rows = cursor.fetchall()

        if cursor.description:
            print([column[0] for column in cursor.description])

        for row in rows:
            print(row)
