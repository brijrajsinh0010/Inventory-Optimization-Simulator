```python
"""
Inventory Reorder Logic
Project: Smart Inventory Optimization System

Purpose:
    Determine which products require replenishment and
    calculate their required order quantities.

Reorder Formula:
    Required Quantity = max(
        0,
        Reorder Level + Expected Demand - Current Stock
    )

    Expected Demand = Daily Demand * Planning Horizon

Time Complexity: O(1) per product
Space Complexity: O(1) auxiliary space per calculation
"""


def calculate_reorder_quantity(
    stock,
    reorder_level,
    daily_demand,
    planning_horizon=7,
):
    """
    Calculate the required replenishment quantity.

    Parameters:
        stock (int): Current inventory quantity.
        reorder_level (int): Minimum stock threshold.
        daily_demand (float): Expected daily product demand.
        planning_horizon (int): Number of days to plan for.

    Returns:
        int: Required replenishment quantity.
    """

    if stock < 0:
        raise ValueError("Stock cannot be negative.")

    if reorder_level < 0:
        raise ValueError("Reorder level cannot be negative.")

    if daily_demand < 0:
        raise ValueError("Daily demand cannot be negative.")

    if planning_horizon < 1:
        raise ValueError("Planning horizon must be at least 1 day.")

    # Replenishment is unnecessary if stock is above the threshold.
    if stock > reorder_level:
        return 0

    # Estimate the demand over the planning horizon.
    expected_demand = daily_demand * planning_horizon

    # Calculate the required replenishment quantity.
    required_quantity = (
        reorder_level + expected_demand - stock
    )

    # Round upward to ensure the required quantity is a whole number.
    return max(0, int(required_quantity) if required_quantity.is_integer()
               else int(required_quantity) + 1)


def calculate_urgency(stock, daily_demand):
    """
    Calculate a simple inventory urgency score.

    Higher scores indicate greater urgency.

    Formula:
        Daily Demand / (Daily Demand + Current Stock)

    Returns:
        float: Urgency score between 0 and 1.
    """

    if stock < 0 or daily_demand < 0:
        raise ValueError("Stock and demand cannot be negative.")

    denominator = stock + daily_demand

    if denominator == 0:
        return 0.0

    return daily_demand / denominator


def needs_replenishment(stock, reorder_level):
    """
    Check whether the current stock has reached
    or fallen below its reorder level.
    """

    if stock < 0 or reorder_level < 0:
        raise ValueError("Stock and reorder level cannot be negative.")

    return stock <= reorder_level


if __name__ == "__main__":

    # Example product
    product_name = "Cooking Oil"
    current_stock = 0
    reorder_level = 15
    daily_demand = 6
    planning_horizon = 7

    quantity = calculate_reorder_quantity(
        stock=current_stock,
        reorder_level=reorder_level,
        daily_demand=daily_demand,
        planning_horizon=planning_horizon,
    )

    urgency = calculate_urgency(
        stock=current_stock,
        daily_demand=daily_demand,
    )

    print("=" * 45)
    print("INVENTORY REORDER ANALYSIS")
    print("=" * 45)

    print(f"Product          : {product_name}")
    print(f"Current Stock    : {current_stock}")
    print(f"Reorder Level    : {reorder_level}")
    print(f"Daily Demand     : {daily_demand}")
    print(f"Planning Horizon : {planning_horizon} days")
    print(f"Reorder Required : {needs_replenishment(current_stock, reorder_level)}")
    print(f"Required Quantity: {quantity}")
    print(f"Urgency Score    : {urgency:.4f}")

    print("=" * 45)
```
