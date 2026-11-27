from categories import categories, display_category
from expense import add_expense,view_expenses,delete_expense,total_expenses
# Main Menu
while True:
    print("======== Expense Tracker ========")
    print("")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")
    print("")

    try:
        choice = int(input("Choose an option: "))

        match choice:
            case 1:
                add_expense()
            case 2:
                view_expenses()
            case 3:
                total_expenses()
            case 4:
                delete_expense()
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")



