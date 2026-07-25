"""
Order calculator module for a simple online retail application.

This module is intentionally small because the assessment focuses on
source control, unit testing and build automation rather than business logic.
"""

PROMOTION_BANNER = "PQS Feature X promotion message"


def calculate_discount(subtotal: float, discount_rate: float) -> float:
    """Return the discount amount for a subtotal and discount rate.

    Args:
        subtotal: Order subtotal before discount.
        discount_rate: Discount percentage expressed as a decimal.
            Example: 0.10 means 10%.

    Returns:
        The calculated discount amount rounded to two decimal places.

    Raises:
        ValueError: If subtotal is negative or discount_rate is outside 0 to 1.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    return round(subtotal * discount_rate, 2)


def calculate_shipping(subtotal: float, express: bool = False) -> float:
    """Return the shipping cost for an order.

    Standard shipping is free for orders of 100 or more.
    Express shipping uses a fixed additional cost.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if express:
        return 15.00

    if subtotal >= 100:
        return 0.00

    return 9.99


def calculate_order_total(subtotal: float, discount_rate: float = 0.0, express: bool = False) -> float:
    """Return the final order total after discount and shipping."""
    discount = calculate_discount(subtotal, discount_rate)
    shipping = calculate_shipping(subtotal, express)
    return round(subtotal - discount + shipping, 2)


def apply_promotion_code(subtotal: float, code: str) -> float:
    """Apply a simple promotion code and return the new subtotal.

    Supported codes:
    - SAVE10: 10% off
    - SAVE20: 20% off
    - NONE or empty code: no discount
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    normalised_code = code.strip().upper()

    if normalised_code == "SAVE10":
        return round(subtotal - calculate_discount(subtotal, 0.10), 2)

    if normalised_code == "SAVE20":
        return round(subtotal - calculate_discount(subtotal, 0.20), 2)

    return round(subtotal, 2)
