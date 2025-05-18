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
    return username


def authenticate_user():
    """Authenticates a user based on username and password."""
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return False

    conn = sqlite3.connect(USERS_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM user_data WHERE username=? AND password=?
    """, (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Welcome back, {username}!")
        return True
    else:
        print("❌ Invalid username or password.")
        return False


def login():
    """Handles user login or creation."""
    while True:
        choice = input(
            "Press '1' to login or '2' to create a new user: "
            ).strip()
        if choice == "1":
            if authenticate_user():
                break
        elif choice == "2":
            create_new_user()
            break
        else:
            print("❌ Invalid choice. Please try again.")
