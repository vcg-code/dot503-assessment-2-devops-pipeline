"""Command-line example used to verify the PQS order calculator."""

try:
    # Package execution uses the relative import available through `python -m src`.
    from .order_calculator import (
        PROMOTION_BANNER,
        apply_promotion_code,
        calculate_order_total,
    )
except ImportError:
    # The zipapp runs this file as its entry point, so it needs a direct import.
    from order_calculator import (
        PROMOTION_BANNER,
        apply_promotion_code,
        calculate_order_total,
    )


def main() -> None:
    """Run one sample order so the source package and zipapp are easy to verify."""
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
