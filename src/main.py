```python
"""
Main Application Logic
Project: Smart Inventory Optimization System

Integrates:
    - Inventory CSV loading
    - Merge Sort
    - Binary Search
    - Reorder calculations
    - Greedy replenishment
"""

from algorithms.merge_sort import merge_sort
from algorithms.binary_search import binary_search
from algorithms.reorder_logic import (
    calculate_reorder_quantity,
    calculate_urgency,
)
from algorithms.greedy_replenishment import (
    create_greedy_plan,
    display_plan,
)
from src.inventory import load_inventory_from_csv


def display_inventory(products):
    """Display all products in a formatted table."""

    print("\n" + "=" * 90)
    print("SMART INVENTORY OPTIMIZATION SYSTEM")
    print("=" * 90)

    print(
        f"{'ID':<8}"
        f"{'Product Name':<24}"
        f"{'Stock':>8}"
        f"{'Reorder':>10}"
        f"{'Demand/day':>13}"
        f"{'Unit Cost':>12}"
    )

    print("-" * 90)

    for product in products:
        print(
            f"{product.product_id:<8}"
            f"{product.name:<24}"
            f"{product.stock:>8}"
            f"{product.reorder_level:>10}"
            f"{product.daily_demand:>13.1f}"
            f"{product.unit_cost:>12.2f}"
        )

    print("-" * 90)


def search_product(products, product_id):
    """Search for a product using Binary Search."""

    index = binary_search(
        products,
        product_id,
        key=lambda product: product.product_id,
    )

    if index == -1:
        print(f"\nProduct '{product_id}' was not found.")
        return

    product = products[index]

    print("\nPRODUCT FOUND")
    print("-" * 40)
    print(f"Product ID    : {product.product_id}")
    print(f"Name          : {product.name}")
    print(f"Current Stock : {product.stock}")
    print(f"Reorder Level : {product.reorder_level}")
    print(f"Daily Demand  : {product.daily_demand}")
    print(f"Unit Cost     : Rs. {product.unit_cost:.2f}")


def generate_replenishment_items(products, planning_horizon):
    """Calculate replenishment requirements for each product."""

    replenishment_items = []

    for product in products:
        quantity = calculate_reorder_quantity(
            stock=product.stock,
            reorder_level=product.reorder_level,
            daily_demand=product.daily_demand,
            planning_horizon=planning_horizon,
        )

        if quantity > 0:
            replenishment_items.append({
                "product_id": product.product_id,
                "name": product.name,
                "quantity": quantity,
                "urgency": calculate_urgency(
                    product.stock,
                    product.daily_demand,
                ),
                "daily_demand": product.daily_demand,
                "unit_cost": product.unit_cost,
            })

    return replenishment_items


def run_application(
    csv_file="data/inventory_sample.csv",
    budget=15000,
    planning_horizon=7,
    search_id=None,
):
    """Run the inventory optimization workflow."""

    products = load_inventory_from_csv(csv_file)

    # Merge Sort: arrange products by product ID.
    sorted_products = merge_sort(
        products,
        key=lambda product: product.product_id,
    )

    display_inventory(sorted_products)

    # Binary Search: search for a product if requested.
    if search_id:
        search_product(sorted_products, search_id)

    # Calculate which products require replenishment.
    replenishment_items = generate_replenishment_items(
        sorted_products,
        planning_horizon,
    )

    # Greedy Algorithm: allocate the purchasing budget.
    selected, deferred, spent, remaining = create_greedy_plan(
        replenishment_items,
        budget,
    )

    display_plan(selected, deferred, spent, remaining)


if __name__ == "__main__":
    run_application()
```
