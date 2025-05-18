import sqlite3
from datetime import datetime


DB_PATH = "data/balance.db"


def init_db():
    """Initializes the database with the balance table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS balance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_cashflow(entries):
    """Inserts one or multiple cashflow records into the database."""
    if isinstance(entries, dict):
        entries = [entries]

    # Add timestamps
    for entry in entries:
        now = datetime.now()
        entry["timestamp"] = now.isoformat()
        # If not provided (e.g. from CLI), generate date from current time
        entry["date"] = entry.get("date") or now.date().isoformat()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO balance (amount, category, description, date, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (
            float(entry["amount"]),
            entry["category"],
            entry.get("description", entry.get("description", "")),
            entry["date"],
            entry["timestamp"]
        )
        for entry in entries
    ])
    conn.commit()
    conn.close()


def load_cashflow():
    """Loads all cashflow records from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT amount, category, description, timestamp FROM balance"
        )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "amount": row[0],
            "category": row[1],
            "description": row[2],
            "date": row[3],
            "timestamp": row[4]
        }
        for row in rows
    ]


def get_summary(start_date=None, end_date=None, group_by="category"):
    """Returns a summary of cashflow entries in a date range.
    The summary is grouped by the specified field (default: category)."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = f"""
        SELECT {group_by}, SUM(amount)
        FROM balance
        WHERE DATE(timestamp) BETWEEN ? AND ?
        GROUP BY {group_by}
        Order BY {group_by}
    """
    if not start_date:
        start_date = "0001-01-01"
    if not end_date:
        end_date = "9999-12-31"

    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    conn.close()

    return [{group_by: row[0], "total": row[1]} for row in results]

