import ast

def total_expenses(expenses_list):
    total_money = 0
    for expense in expenses_list:
        total_money += expense[1]
    return round(total_money, 2)


def new_expense(expenses: list[list], description: str, cost: float,
                category: str) -> list[list]:
    expenses.append([description, cost, category])
    return expenses


def filter_item(expenses_list, category):
    filtered = []
    for expense in expenses_list:
        if expense[2].lower() == category.lower():
            filtered.append(expense)
    return filtered


def receipt(expenses: list[list]) -> str:
    total_cost = total_expenses(expenses)
    receipt_text = ""
    for i in expenses:
        receipt_text += f"product: {i[0]:10}:{i[1]:5.2f}\n"
        receipt_text += "------------------------------\n"
    receipt_text += f"Total: {total_cost:5.2f}"
    return receipt_text  


expenses = ast.literal_eval(input("Welcome to your personal expense tracker, please introduce a list to start the program: "))

options = int(input("""Now decide which feature would you like to use: 
1 -> get the total amound of expenses 
2 -> return the items of a specific category 
3 -> print a receipt 
4 -> add a new expense to the list. 
Only enter one number between these options: """))

result = None
if options == 1:
    result = total_expenses(expenses)
elif options == 2:
    result = filter_item(expenses, input("Enter the category to filter: "))
elif options == 3:
    result = receipt(expenses)
elif options == 4:
    result = new_expense(expenses, input("Enter the description: "), float(input("Enter the cost: ")), input("Enter the category: "))
else:
    result = "invalid option"

print(result)
