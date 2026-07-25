"""
Command-line entry point for the simple online retail order calculator.
"""

try:
    # Used when running as a package with: python -m src
    from .order_calculator import (
        PROMOTION_BANNER,
        apply_promotion_code,
        calculate_order_total,
    )
except ImportError:
    # Used when running the deployable zipapp package.
    from order_calculator import (
        PROMOTION_BANNER,
        apply_promotion_code,
        calculate_order_total,
    )


def main() -> None:
    """Run a small demonstration of the application."""
    subtotal = 120.00
    promotion_code = "SAVE10"

    discounted_subtotal = apply_promotion_code(subtotal, promotion_code)
    final_total = calculate_order_total(discounted_subtotal, 0.0, express=False)

    print(PROMOTION_BANNER)
    print(f"Original subtotal: ${subtotal:.2f}")
    print(f"Promotion code: {promotion_code}")
    print(f"Discounted subtotal: ${discounted_subtotal:.2f}")
    print(f"Final total: ${final_total:.2f}")


if __name__ == "__main__":
    main()
