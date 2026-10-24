```python
"""
Greedy Replenishment Algorithm
Project: Smart Inventory Optimization System

Purpose:
    Prioritize inventory replenishment under a limited budget.

Priority order:
    1. Higher urgency score.
    2. Higher daily demand.
    3. Product ID in alphabetical order.

Time Complexity:
    Sorting: O(n log n)
    Budget allocation: O(n)

Note:
    This is a greedy heuristic. It does not guarantee
    the globally optimal allocation of the budget.
"""

from algorithms.merge_sort import merge_sort


def create_greedy_plan(replenishment_items, budget):
    """
    Allocate a limited budget to replenishment orders.

    Each item must be a dictionary containing:
        product_id
        name
        quantity
        urgency
        daily_demand
        unit_cost

    Returns:
        selected: Orders that fit within the budget.
        deferred: Orders that do not fit within the remaining budget.
        spent: Total budget spent.
        remaining: Budget remaining.
    """

    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    # Sort by urgency, then demand, then product ID.
    ordered_items = merge_sort(
        replenishment_items,
        key=lambda item: (
            -item["urgency"],
            -item["daily_demand"],
            item["product_id"],
        ),
    )

    selected = []
    deferred = []
    remaining = float(budget)

    # Greedily select each affordable order.
    for item in ordered_items:
        quantity = item["quantity"]
        unit_cost = item["unit_cost"]

        if quantity < 0 or unit_cost < 0:
            raise ValueError(
                "Quantity and unit cost cannot be negative."
            )

        order_cost = quantity * unit_cost

        if order_cost <= remaining:
            selected.append({
                **item,
                "total_cost": order_cost,
                "status": "Ordered",
            })

            remaining -= order_cost

        else:
            deferred.append({
                **item,
                "total_cost": order_cost,
                "status": "Deferred",
            })

    spent = float(budget) - remaining

    return selected, deferred, spent, remaining


def display_plan(selected, deferred, spent, remaining):
    """Display the replenishment plan."""

    print("\n" + "=" * 75)
    print("GREEDY REPLENISHMENT PLAN")
    print("=" * 75)

    print("\nSELECTED ORDERS")

    if not selected:
        print("No orders selected.")

    for item in selected:
        print(
            f'{item["product_id"]} | '
            f'{item["name"]} | '
            f'Quantity: {item["quantity"]} | '
            f'Cost: Rs. {item["total_cost"]:.2f} | '
            f'Status: {item["status"]}'
        )

    print("\nDEFERRED ORDERS")

    if not deferred:
        print("No orders deferred.")

    for item in deferred:
        print(
            f'{item["product_id"]} | '
            f'{item["name"]} | '
            f'Quantity: {item["quantity"]} | '
            f'Cost: Rs. {item["total_cost"]:.2f} | '
            f'Status: {item["status"]}'
        )

    print("\nBUDGET SUMMARY")
    print(f"Budget spent     : Rs. {spent:.2f}")
    print(f"Budget remaining : Rs. {remaining:.2f}")
    print("=" * 75)


if __name__ == "__main__":

    sample_orders = [
        {
            "product_id": "P101",
            "name": "Rice",
            "quantity": 20,
            "urgency": 0.25,
            "daily_demand": 4,
            "unit_cost": 250,
        },
        {
            "product_id": "P102",
            "name": "Cooking Oil",
            "quantity": 30,
            "urgency": 1.0,
            "daily_demand": 6,
            "unit_cost": 140,
        },
        {
            "product_id": "P103",
            "name": "Sugar",
            "quantity": 15,
            "urgency": 0.10,
            "daily_demand": 5,
            "unit_cost": 42,
        },
        {
            "product_id": "P106",
            "name": "Toothpaste",
            "quantity": 12,
            "urgency": 0.33,
            "daily_demand": 3,
            "unit_cost": 60,
        },
    ]

    budget = 5000

    selected, deferred, spent, remaining = create_greedy_plan(
        sample_orders,
        budget
    )

    display_plan(selected, deferred, spent, remaining)
```
