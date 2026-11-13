def total_expenses(expenses_list):
    total_money = 0
    for expense in expenses_list:
        total_money += expense[1]
    return round(total_money, 2)