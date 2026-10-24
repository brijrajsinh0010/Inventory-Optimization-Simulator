"""
Merge Sort Algorithm
Project: Smart Inventory Optimization System

Time Complexity:
    Best Case:    O(n log n)
    Average Case: O(n log n)
    Worst Case:   O(n log n)

Auxiliary Space Complexity: O(n)
"""


def merge_sort(items, key=None):
    """
    Sort a list using the Merge Sort algorithm.

    Args:
        items: List of items to sort.
        key: Optional function used to extract a comparison key.

    Returns:
        A new sorted list. The original list remains unchanged.
    """

    if len(items) <= 1:
        return items.copy()

    if key is None:
        key = lambda item: item

    middle = len(items) // 2

    left = merge_sort(items[:middle], key)
    right = merge_sort(items[middle:], key)

    return merge(left, right, key)


def merge(left, right, key):
    """Merge two sorted lists into one sorted list."""

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":

    sample_data = [45, 12, 78, 3, 29, 10, 56]

    print("Original Data:", sample_data)
    print("Sorted Data:  ", merge_sort(sample_data))

    products = [
        {"product_id": "P103", "name": "Sugar"},
        {"product_id": "P101", "name": "Rice"},
        {"product_id": "P102", "name": "Oil"},
    ]

    sorted_products = merge_sort(
        products,
        key=lambda product: product["product_id"]
    )

    print("\nInventory Sorted by Product ID:")

    for product in sorted_products:
        print(product)
