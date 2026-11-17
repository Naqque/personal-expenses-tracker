from function_expense import new_expense
from total_expenses import total_expenses
from function_receipt import receipt


def filter_item(expenses_list, category):
    filtered = []
    for expense in expenses_list:
        if expense[2].lower() == category.lower():
            filtered.append(expense)
    return filtered
"""
example of input:
expenses = [
    ["Supermarket groceries", 45.50, "Food"],
    ["Gasoline", 30.00, "Transport"],
    ["Dinner with friends", 25.80, "Leisure"],
    ["Electricity bill", 65.20, "Utilities"],
    ["Coffee and pastry", 4.50, "Food"],
    ["Monthly subway pass", 55.00, "Transport"],
    ["Movie tickets", 18.00, "Leisure"],
    ["Pharmacy prescription", 12.30, "Health"],
    ["New running shoes", 89.99, "Clothing"],
    ["Internet bill", 40.00, "Utilities"]
]
"""

expenses = input("Welcome to your personal expense tracker, please introduce a list to start the program")
options = int(input("""Now decide which feature would you like to use: 1 -> get the total amound of expenses ; 2 -> return the items of a specific category ;
                    3 -> print a receipt ; 4 -> add a new expense to the list. Only enter one number between these options"""))

result = None
if options == 1:
  result = total(expenses)
if options == 2:
  result = filter_item(expenses)
if options == 3:
  result = receipt(expenses)
if options == 4:
  result = new_expense(expenses)
print(result)
