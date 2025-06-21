import sqlite3
from datetime import datetime

DB_NAME = "history.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(operations)")
        columns = [col[1] for col in cursor.fetchall()]
        if 'timestamp' not in columns:
            cursor.execute("ALTER TABLE operations ADD COLUMN timestamp TEXT")
        else:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS operations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT,
                    operand1 REAL,
                    operand2 REAL,
                    result REAL,
                    timestamp TEXT
                )
            ''')
        conn.commit()



def save_operation(operation, a, b, result):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO operations (operation, operand1, operand2, result, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (operation, a, b, result, datetime.now().isoformat()))
        conn.commit()
