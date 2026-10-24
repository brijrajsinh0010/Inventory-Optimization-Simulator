import unittest

from algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_find_existing_element(self):
        numbers = [3, 10, 12, 29, 45, 78]

        result = binary_search(numbers, 29)

        self.assertEqual(result, 3)

    def test_element_not_found(self):
        numbers = [3, 10, 12, 29, 45, 78]

        result = binary_search(numbers, 100)

        self.assertEqual(result, -1)

    def test_find_first_element(self):
        numbers = [10, 20, 30, 40]

        self.assertEqual(binary_search(numbers, 10), 0)

    def test_find_last_element(self):
        numbers = [10, 20, 30, 40]

        self.assertEqual(binary_search(numbers, 40), 3)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 10), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([25], 25), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([25], 50), -1)

    def test_search_inventory_by_product_id(self):
        products = [
            {"product_id": "P101", "name": "Rice"},
            {"product_id": "P102", "name": "Oil"},
            {"product_id": "P103", "name": "Sugar"},
        ]

        result = binary_search(
            products,
            "P102",
            key=lambda product: product["product_id"],
        )

        self.assertEqual(result, 1)
        self.assertEqual(products[result]["name"], "Oil")


if __name__ == "__main__":
    unittest.main()
