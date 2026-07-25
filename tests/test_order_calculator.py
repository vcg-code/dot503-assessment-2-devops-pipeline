"""Unit tests for the PQS order calculator.

DOT503 requires exactly five cases: three must pass and two must fail
intentionally. The failing cases use plausible but incorrect expectations so
the test output clearly shows how a pipeline reports quality problems.
"""

import unittest

from src.order_calculator import (
    apply_promotion_code,
    calculate_discount,
    calculate_order_total,
    calculate_shipping,
)


class TestOrderCalculator(unittest.TestCase):
    """Check the pricing rules that matter to the sample customer journey."""

    def setUp(self):
        """Keep shared inputs here while leaving each expected result visible."""
        self.discount_subtotal = 200.00
        self.shipping_subtotal = 120.00
        self.promotion_subtotal = 150.00

    def test_calculate_discount_passes(self):
        """Checks the base discount rule used by totals and promotion codes."""
        result = calculate_discount(self.discount_subtotal, 0.10)
        self.assertEqual(result, 20.00)

    def test_free_shipping_threshold_passes(self):
        """Checks the boundary where standard shipping becomes free."""
        result = calculate_shipping(self.shipping_subtotal)
        self.assertEqual(result, 0.00)

    def test_save20_promotion_passes(self):
        """Checks that SAVE20 produces the expected customer subtotal."""
        result = apply_promotion_code(self.promotion_subtotal, "SAVE20")
        self.assertEqual(result, 120.00)

    def test_order_total_fails_intentionally(self):
        """Uses a wrong total so the runner reports the first required failure."""
        result = calculate_order_total(100.00, 0.10, express=False)
        self.assertEqual(result, 95.00)

    def test_shipping_cost_fails_intentionally(self):
        """Uses a wrong charge to provide the second required failure."""
        result = calculate_shipping(50.00)
        self.assertEqual(result, 5.00)


if __name__ == "__main__":
    unittest.main()
