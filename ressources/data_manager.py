import sqlite3



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