from menu import MENU, RESTAURANT_NAME

RECEIPT_WIDTH = 40


def print_header(title):
    print("=" * RECEIPT_WIDTH)
    print(title.center(RECEIPT_WIDTH))
    print("=" * RECEIPT_WIDTH)


def display_menu():
    print_header(RESTAURANT_NAME)

    print(f"{'ITEM':<25}{'PRICE (PHP)':>15}")
    print("-" * RECEIPT_WIDTH)

    for item, price in MENU.items():
        print(f"{item:<25}{price:>15.2f}")

    print("-" * RECEIPT_WIDTH)
