from ressources.input_handler import get_cashflow_input
from ressources.summarizer import summarize_cashflow
from users.user_management import login
from ressources.data_manager import (
    save_cashflow,
    load_cashflow_from_csv,
    export_cashflow_to_csv,
)


def menu():
    while True:
        choice = input(
            """
            \nPress '1' to add Cashflow\n
            Press '2' to receive a summary for a specific timeslot\n
            Press '3' to upload a csv file\n
            Press '4' to export your cashflow to a csv file\n
            Press '5' to log out\n
            Choose an option:
            """
            )
        if choice == "1":
            entry = get_cashflow_input()
            save_cashflow(entry)
        elif choice == "2":
            summarize_cashflow()
        elif choice == "3":
            file_path = input("""
                              Enter CSV file path (remember that
                              your csv must have
                              the following columns: date, amount,
                              category and description):
                              """)
            entries = load_cashflow_from_csv(file_path)
            if entries:
                save_cashflow(entries)
                print(f"Imported {len(entries)} cashflow entries from CSV.")
            else:
                print("No valid cashflow entries found in the file.")
        elif choice == "4":
            file_path = input("Enter the path to save the CSV file: ")
            export_cashflow_to_csv(file_path)
            print(f"Cashflow exported to {file_path}.")
        elif choice == "5":
            login()
        else:
            print("❌ Invalid choice.")
