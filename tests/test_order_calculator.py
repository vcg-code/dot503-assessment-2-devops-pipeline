"""
Unit tests for the PQS online retail order calculator.

Assessment requirement:
- Five test cases in total
- Three passing test cases
- Two intentionally failing test cases

The failing assertions demonstrate how a continuous testing stage identifies
incorrect expectations and reports quality issues before deployment.
"""

import unittest

from src.order_calculator import (
    apply_promotion_code,
    calculate_discount,
    calculate_order_total,
    calculate_shipping,
)


class TestOrderCalculator(unittest.TestCase):
    """Validate the main order-calculation behaviours."""

    def setUp(self):
        """Create reusable test data before each test case."""
        self.discount_subtotal = 200.00
        self.shipping_subtotal = 120.00
        self.promotion_subtotal = 150.00

    def test_calculate_discount_passes(self):
        """PASS: A 10% discount on 200 should equal 20."""
        result = calculate_discount(self.discount_subtotal, 0.10)
        self.assertEqual(result, 20.00)

    def test_free_shipping_threshold_passes(self):
        """PASS: Standard shipping is free for orders of 100 or more."""
        result = calculate_shipping(self.shipping_subtotal)
        self.assertEqual(result, 0.00)

    def test_save20_promotion_passes(self):
        """PASS: SAVE20 should reduce a subtotal of 150 to 120."""
        result = apply_promotion_code(self.promotion_subtotal, "SAVE20")
        self.assertEqual(result, 120.00)

    def test_order_total_fails_intentionally(self):
        """FAIL: The deliberately incorrect expected total is 95."""
        result = calculate_order_total(100.00, 0.10, express=False)
        self.assertEqual(result, 95.00)

    def test_shipping_cost_fails_intentionally(self):
        """FAIL: The deliberately incorrect expected shipping cost is 5."""
        result = calculate_shipping(50.00)
        self.assertEqual(result, 5.00)


if __name__ == "__main__":
    unittest.main()
