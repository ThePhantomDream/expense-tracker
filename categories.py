categories = [
    "Food",
    "Transportation",
    "Shopping",
    "Entertainment",
    "Bills",
    "Others"
]

def display_category():
    print("===== Select Category =====")
    print("")
    for i in range(len(categories)):
        print(f"{i+1}. {categories[i]}")
    print("")

def select_category():
    while True:
                try:
                    choice = int(input("Select category: "))
                    if choice < 1 or choice > len(categories):
                        print(f"Please choose between 1-{len(categories)}!")
                        continue
                    else:
                        return choice - 1
                except ValueError:
                    print("Please enter a number!")