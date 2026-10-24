import unittest

from algorithms.reorder_logic import (
    calculate_reorder_quantity,
    calculate_urgency,
    needs_replenishment,
)


class TestReorderLogic(unittest.TestCase):

    def test_replenishment_quantity(self):
        quantity = calculate_reorder_quantity(
            stock=5,
            reorder_level=10,
            daily_demand=3,
            planning_horizon=7,
        )

        self.assertEqual(quantity, 21)

    def test_no_replenishment_needed(self):
        quantity = calculate_reorder_quantity(
            stock=20,
            reorder_level=10,
            daily_demand=3,
            planning_horizon=7,
        )

        self.assertEqual(quantity, 0)

    def test_zero_daily_demand(self):
        quantity = calculate_reorder_quantity(
            stock=5,
            reorder_level=10,
            daily_demand=0,
            planning_horizon=7,
        )

        self.assertEqual(quantity, 0)

    def test_needs_replenishment(self):
        self.assertTrue(needs_replenishment(5, 10))

    def test_replenishment_not_needed(self):
        self.assertFalse(needs_replenishment(15, 10))

    def test_stock_at_reorder_level(self):
        self.assertTrue(needs_replenishment(10, 10))

    def test_urgency_for_stockout(self):
        urgency = calculate_urgency(
            stock=0,
            daily_demand=5,
        )

        self.assertEqual(urgency, 100)

    def test_urgency_with_no_demand(self):
        urgency = calculate_urgency(
            stock=10,
            daily_demand=0,
        )

        self.assertEqual(urgency, 0)


if __name__ == "__main__":
    unittest.main()
