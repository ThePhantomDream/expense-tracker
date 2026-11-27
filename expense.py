from categories import display_category,categories,select_category
from datetime import datetime
import pandas as pd

expenses = {
    "Food": [],
    "Transportation": [],
    "Shopping": [],
    "Entertainment": [],
    "Bills": [],
    "Others": []
}

def display_expenses(category):
    displays = pd.DataFrame(
        expenses[category],
        index=range(1, len(expenses[category]) + 1),
        columns=["name", "amount", "date"]
    )

    displays.columns = ["Name", "Amount", "Date"]

    if displays.empty:
        print("No expenses found!")
    else:
        print(f"===== {category} Expenses =====")
        print("")
        print(displays)
        print("")

    return displays

def add_expense():
    display_category()
    category = categories[select_category()]
    name = str(input("Enter expense name: "))

    while True:
        try:
            amount = int(input("Enter expense amount: "))
            if amount == 0:
                print("Enter an acceptable expense amount!")
                continue
            break
        except ValueError:
            print("Enter a valid number!")

    expenses[category].append({
        "name": name,
        "amount": f"${amount:,.2f}",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

def view_expenses():
    display_category()
    choice = select_category()
    category = categories[choice]

    display_expenses(category)

def total_expenses():
    print("===== Total Expenses =====")
    print("")
    for category, expense_list in expenses.items():
        total = 0

        for expense in expense_list:
            total += expense["amount"]

        print(f"{category}: ${total}")
    print("")

def delete_expense():
    display_category()
    choice = select_category()
    category = categories[choice]

    displays = display_expenses(category)

    if displays.empty:
        print("No expenses found!")
        return

    selection = int(input("Enter expense number to delete: "))
    expenses[category].pop(selection - 1)
    