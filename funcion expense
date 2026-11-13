def new_expense(expenses: list[list], description: str, cost: float,
                category: str) -> list[list]:
    """
    Add a new expense to the list of expenses.

    Args:
        expenses (list[list]): Current list of expenses. Each expense is
            [description, cost, category].
        description (str): What was bought, e.g. "Pizza". Not empty.
        cost (float): Price in euros, e.g. 8.00. Must be 0 or more.
        category (str): Type of expense, e.g. "Food". Not empty.

    Returns:
        list[list]: The updated list, with the new expense at the end.

    Example:
        >>> new_expense([], "Pizza", 8.00, "Food")
        [['Pizza', 8.0, 'Food']]
    """
    expenses.append([description, cost, category])
    return expenses
