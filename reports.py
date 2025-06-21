import sqlite3
import pandas as pd

def generate_report():
    conn = sqlite3.connect("history.db")
    df = pd.read_sql_query("SELECT * FROM operations", conn)
    df.to_csv("operations_report.csv", index=False)
    conn.close()
