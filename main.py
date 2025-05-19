from users.user_management import init_user_db, login
import os

os.makedirs("exports", exist_ok=True)


def main():
    init_user_db()  # Ensure the user database is initialized
    login()  # Prompt for user login
    print("Welcome to your personal budget ledger!")


if __name__ == "__main__":
    main()
