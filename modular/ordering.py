from menu import MENU


def ask_yes_no(question):
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True

        elif answer in ("no", "n"):
            return False

        else:
            print("Invalid input. Please answer with yes or no.\n")


def get_menu_item():
    while True:
        item_name = input("Enter menu item: ").strip().title()

        if item_name in MENU:
            return item_name

        print(
            f"Sorry, '{item_name}' is not on the menu. "
            "Please try again.\n"
        )


def get_quantity():
    while True:
        quantity_input = input("Enter quantity: ").strip()

        if quantity_input.isdigit() and int(quantity_input) > 0:
            return int(quantity_input)

        print(
            "Invalid quantity. Please enter a whole number "
            "greater than 0.\n"
        )


def take_order():
    customer_orders = []

    while True:
        item_name = get_menu_item()
        quantity = get_quantity()

        order_line = {
            "item": item_name,
            "quantity": quantity,
            "price": MENU[item_name]
        }

        customer_orders.append(order_line)

        print(f"Added {quantity} x {item_name} to your order.\n")

        if not ask_yes_no("Do you want to order another item?"):
            break

    return customer_orders
