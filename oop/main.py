from restaurant import Restaurant


def ask_yes_no(question):
    while True:
        answer = input(
            f"{question} (yes/no): "
        ).strip().lower()

        if answer in ("yes", "y"):
            return True

        if answer in ("no", "n"):
            return False

        print("Invalid input. Please answer yes or no.")


def main():
    restaurant = Restaurant()

    restaurant.display_menu()

    if not ask_yes_no(
        "\nWould you like to place an order?"
    ):
        print("\nThank you for visiting RHENZ TAMBAYAN. Goodbye!")
        return

    while True:
        item = input("Enter menu item: ").strip().title()

        if item in restaurant.menu:
            break

        print("Item not found. Please choose from the menu.")

    while True:
        quantity = input("Enter quantity: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break

        print("Please enter a valid quantity.")

    restaurant.add_order(item, quantity)

    while ask_yes_no("Do you want to order another item?"):

        while True:
            item = input("Enter menu item: ").strip().title()

            if item in restaurant.menu:
                break

            print("Item not found. Please choose from the menu.")

        while True:
            quantity = input("Enter quantity: ").strip()

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                break

            print("Please enter a valid quantity.")

        restaurant.add_order(item, quantity)

    restaurant.print_receipt()


if __name__ == "__main__":
    main()
