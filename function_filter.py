def filter_item(expenses_list, category):
    filtered = []
    for expense in expenses_list:
        if expense[2].lower() == category.lower():
            filtered.append(expense)
    return filtered
