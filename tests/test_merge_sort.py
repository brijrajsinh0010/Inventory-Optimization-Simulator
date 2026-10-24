import unittest

from algorithms.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_sort_numbers(self):
        numbers = [45, 12, 78, 3, 29, 10]
        expected = [3, 10, 12, 29, 45, 78]

        self.assertEqual(merge_sort(numbers), expected)

    def test_sort_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_sort_single_element(self):
        self.assertEqual(merge_sort([42]), [42])

    def test_sort_already_sorted_list(self):
        numbers = [1, 2, 3, 4, 5]

        self.assertEqual(merge_sort(numbers), numbers)

    def test_sort_reverse_order(self):
        numbers = [5, 4, 3, 2, 1]

        self.assertEqual(merge_sort(numbers), [1, 2, 3, 4, 5])

    def test_sort_inventory_by_product_id(self):
        products = [
            {"product_id": "P103", "name": "Sugar"},
            {"product_id": "P101", "name": "Rice"},
            {"product_id": "P102", "name": "Oil"},
        ]

        result = merge_sort(
            products,
            key=lambda product: product["product_id"],
        )

        expected_ids = ["P101", "P102", "P103"]
        actual_ids = [product["product_id"] for product in result]

        self.assertEqual(actual_ids, expected_ids)

    def test_original_list_remains_unchanged(self):
        numbers = [5, 2, 4, 1]
        original = numbers.copy()

        merge_sort(numbers)

        self.assertEqual(numbers, original)


if __name__ == "__main__":
    unittest.main()
