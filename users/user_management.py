import sqlite3
from ressources.data_manager import set_db_path, init_db

USERS_PATH = "users/user_data/user_data.db"

CURRENT_USER = None


def get_current_user():
    """Returns the current user if logged in, otherwise prompts for login."""
    if CURRENT_USER is None:
        login()
    return CURRENT_USER


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
    login()


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
        global CURRENT_USER
        CURRENT_USER = username
        return True
    else:
        return False


def login():
    """Handles user login or creation."""
    while True:
        choice = input(
            "Press '1' to login or '2' to create a new user: "
            ).strip()
        if choice == "1":
            if authenticate_user():
                print("Login successful.")
                user_db = f"data/{CURRENT_USER}.db"
                set_db_path(user_db)
                init_db()  # Initializes user's personal DB if not present
                return True
        elif choice == "2":
            create_new_user()
            break
        else:
            print("❌ Invalid choice. Please try again.")
