from ressources.data_manager import init_db
from users.user_management import init_user_db, get_current_user
import os

os.makedirs("exports", exist_ok=True)


def main():
    init_user_db()  # Ensure the user database is initialized
    get_current_user()  # Prompt for login if not already logged in

    init_db()  # Ensure the database is initialized
    print("Welcome to your personal budget ledger!")


if __name__ == "__main__":
    main()
