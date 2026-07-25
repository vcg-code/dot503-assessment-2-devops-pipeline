"""Core calculations used by the PQS order calculator.

The application is deliberately small so the project can stay focused on the
DevOps work being assessed: source control, automated testing and a repeatable
build. The validation rules make the example realistic without turning it into
a full retail system.
"""

PROMOTION_BANNER = "PQS Features X, Y and Z promotion message"


def calculate_discount(subtotal: float, discount_rate: float) -> float:
    """Calculate a discount while applying the same rules for every caller.

    The rate is written as a decimal, so 0.10 represents 10%. Invalid pricing
    values are rejected here, and the result is rounded to two decimal places
    because it represents currency.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    return round(subtotal * discount_rate, 2)


def calculate_shipping(subtotal: float, express: bool = False) -> float:
    """Apply the shipping policy used by this example.

    Orders of $100 or more receive free standard shipping, while express
    delivery always uses the fixed $15 charge. A negative subtotal is rejected
    because it cannot represent a valid order.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if express:
        return 15.00

    if subtotal >= 100:
        return 0.00

    return 9.99


def calculate_order_total(subtotal: float, discount_rate: float = 0.0, express: bool = False) -> float:
    """Combine the validated discount and shipping rules into a final total.

    Keeping the calculation in one place gives the tests a clear customer-facing
    result to check and avoids repeating the pricing formula elsewhere.
    """
    discount = calculate_discount(subtotal, discount_rate)
    shipping = calculate_shipping(subtotal, express)
    return round(subtotal - discount + shipping, 2)


def apply_promotion_code(subtotal: float, code: str) -> float:
    """Apply a supported promotion code to the subtotal.

    Codes are normalised so user input is not case-sensitive. SAVE10 gives 10%
    off and SAVE20 gives 20% off. An unknown or empty code leaves the subtotal
    unchanged, which keeps the behaviour predictable.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    normalised_code = code.strip().upper()

    if normalised_code == "SAVE10":
        return round(subtotal - calculate_discount(subtotal, 0.10), 2)

    if normalised_code == "SAVE20":
        return round(subtotal - calculate_discount(subtotal, 0.20), 2)

    return round(subtotal, 2)
