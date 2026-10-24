```python
"""
Binary Search Algorithm
Project: Smart Inventory Optimization System

Requirement:
    The input list must already be sorted by the search key.

Time Complexity:
    Best Case:    O(1)
    Average Case: O(log n)
    Worst Case:   O(log n)

Auxiliary Space Complexity: O(1)
"""


def binary_search(items, target, key=None):
    """
    Search for a target in a sorted list using Binary Search.

    Args:
        items: A list sorted in ascending order.
        target: The value to find.
        key: Optional function to extract the comparison key.

    Returns:
        The index of the matching item, or -1 if not found.
    """

    if key is None:
        key = lambda item: item

    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2
        current = key(items[middle])

        if current == target:
            return middle

        if current < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


if __name__ == "__main__":

    numbers = [3, 10, 12, 29, 45, 56, 78]

    target = 29
    index = binary_search(numbers, target)

    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} was not found.")

    products = [
        {"product_id": "P101", "name": "Rice"},
        {"product_id": "P102", "name": "Oil"},
        {"product_id": "P103", "name": "Sugar"},
        {"product_id": "P106", "name": "Toothpaste"},
    ]

    target_id = "P106"

    index = binary_search(
        products,
        target_id,
        key=lambda product: product["product_id"]
    )

    if index != -1:
        print("\nProduct found:")
        print(products[index])
    else:
        print(f"\nProduct {target_id} was not found.")
```
