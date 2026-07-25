"""
Unit tests for the simple online retail order calculator.

Assessment requirement:
- There must be five test cases.
- Three test cases must pass.
- Two test cases must fail.

The two failing tests are intentionally incorrect to demonstrate how a
continuous testing stage reports failures inside a CI/testing pipeline.
"""

import unittest

from src.order_calculator import (
    apply_promotion_code,
    calculate_discount,
    calculate_order_total,
    calculate_shipping,
)


class TestOrderCalculator(unittest.TestCase):
    """Unit tests for order calculation functions."""

    def test_calculate_discount_passes(self):
        """PASS: 10% discount on 200 should be 20."""
        self.assertEqual(calculate_discount(200.00, 0.10), 20.00)

    def test_calculate_shipping_free_threshold_passes(self):
        """PASS: standard shipping is free for orders of 100 or more."""
        self.assertEqual(calculate_shipping(120.00), 0.00)

    def test_apply_promotion_code_save20_passes(self):
        """PASS: SAVE20 should reduce 150 to 120."""
        self.assertEqual(apply_promotion_code(150.00, "SAVE20"), 120.00)

    def test_calculate_order_total_fails_intentionally(self):
        """FAIL: intentionally expects the wrong total for assessment evidence."""
        self.assertEqual(calculate_order_total(100.00, 0.10, express=False), 95.00)

    def test_shipping_fails_intentionally(self):
        """FAIL: intentionally expects the wrong standard shipping cost."""
        self.assertEqual(calculate_shipping(50.00), 5.00)


if __name__ == "__main__":
    unittest.main()
