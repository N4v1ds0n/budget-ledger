import sqlite3

USERS_PATH = ".users/user_data/user_data.db"


def init_user_db():
    """Initializes the database with the balance table if it doesn't exist."""
    conn = sqlite3.connect(USERS_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()