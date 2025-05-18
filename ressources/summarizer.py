from ressources.data_manager import get_summary


def summarize_cashflow():
    start = input("Enter start date (YYYY-MM-DD): ").strip()
    end = input("Enter end date (YYYY-MM-DD): ").strip()
    group_by = input("Group by 'category' or 'date'? ").strip().lower()

    if group_by not in {"category", "date"}:
        print("Invalid group_by option. Choose 'category' or 'date'.")
        return None
    try:
        summary = get_summary(start, end, group_by)
        if not summary:
            print("No data found for the given range.")
            return []

        print(f"""\nSummary grouped by {group_by}
              from {start or 'beginning'}
              to {end or 'now'}:\n""")
        print(f"{group_by.capitalize():<20} | Total")
        print("-" * 32)
        for row in summary:
            print(f"{row[group_by]:<20} | €{row['total']:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Something went wrong: {e}")
    return summary
