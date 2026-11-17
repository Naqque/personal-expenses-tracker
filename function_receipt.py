def receipt(expenses:list[list]) -> str:
    """
    Generates a receipt for the given expenses.Formats and prints a clean,
    easy-to-read overview of all transactions along with the overall total
    (the overrall total is calculated calling the funcion from one of my
    teammates)
    (it can be implementing with some string format)
    Args:
        expenses (list[list]): A list of expenses, where each expense is
        represented as a list containing the name of the item, its cost,
        and its category.
    Returns:
        str: A formatted string representing the receipt, including each
        expense and the overall total.
    """
    total_cost = total(expenses)
    for i in expense:
        print(f"product: {i[0]:10}:{i[1]:5.2f})
        print("------------------------------")
        print(f"Total: {total_cost:5.2f}")
