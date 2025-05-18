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


def create_new_user():
    """Creates a new user in the database."""
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    conn = sqlite3.connect(USERS_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_data (username, password, created_at)
        VALUES (?, ?, datetime('now'))
    """, (username, password))
    conn.commit()
    conn.close()
    print(f"User '{username}' created successfully.")
