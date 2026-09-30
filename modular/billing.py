from menu import RESTAURANT_NAME, RESTAURANT_ADDRESS

DISCOUNT_THRESHOLD = 500.00
DISCOUNT_RATE = 0.10
RECEIPT_WIDTH = 40


def calculate_order(customer_orders):
    subtotal = 0.00

    for order_line in customer_orders:
        line_total = (
            order_line["quantity"] *
            order_line["price"]
        )

        order_line["line_total"] = line_total
        subtotal += line_total

    return subtotal


def apply_discount(subtotal):
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE

    return 0.00


def print_receipt(customer_orders, subtotal, discount):
    total = subtotal - discount

    print("\n")
    print("=" * RECEIPT_WIDTH)
    print(RESTAURANT_NAME.center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)

    print(RESTAURANT_ADDRESS.center(RECEIPT_WIDTH))
    print("-" * RECEIPT_WIDTH)

    print(
        f"{'ITEM':<16}"
        f"{'QTY':>5}"
        f"{'PRICE':>9}"
        f"{'TOTAL':>10}"
    )

    print("-" * RECEIPT_WIDTH)

    for order_line in customer_orders:
        item = order_line["item"]
        quantity = order_line["quantity"]
        price = order_line["price"]
        line_total = order_line["line_total"]

        print(
            f"{item:<16}"
            f"{quantity:>5}"
            f"{price:>9.2f}"
            f"{line_total:>10.2f}"
        )

    print("-" * RECEIPT_WIDTH)

    print(f"{'SUBTOTAL':<31}{subtotal:>9.2f}")

    if discount > 0:
        print(
            f"{'DISCOUNT (10%)':<31}"
            f"{-discount:>9.2f}"
        )

    print(f"{'TOTAL':<31}{total:>9.2f}")

    print("=" * RECEIPT_WIDTH)
    print("Thank you for ordering with us!".center(RECEIPT_WIDTH))
    print("Please come again!".center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)
