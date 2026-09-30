from display import display_menu
from ordering import take_order, ask_yes_no
from billing import calculate_order, apply_discount, print_receipt


def main():
    display_menu()

    if not ask_yes_no("\nWould you like to place an order?"):
        print("\nThank you for visiting RHENZ TAMBAYAN. Goodbye!")
        return

    print()

    customer_orders = take_order()

    subtotal = calculate_order(customer_orders)
    discount = apply_discount(subtotal)

    print_receipt(
        customer_orders,
        subtotal,
        discount
    )


if __name__ == "__main__":
    main()
