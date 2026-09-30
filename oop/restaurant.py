class Restaurant:
    def __init__(self):
        self.name = "RHENZ TAMBAYAN"
        self.address = "Calajo-an, Minglanilla, Cebu City"

        self.menu = {
            "Burger": 85.00,
            "Cheeseburger": 95.00,
            "Chicken Sandwich": 105.00,
            "Fries": 45.00,
            "Hotdog": 55.00,
            "Soda": 30.00,
            "Iced Tea": 35.00,
            "Ice Cream": 40.00
        }

        self.orders = []

    def display_menu(self):
        print("=" * 40)
        print(self.name.center(40))
        print("=" * 40)

        print(f"{'ITEM':<25}{'PRICE (PHP)':>15}")
        print("-" * 40)

        for item, price in self.menu.items():
            print(f"{item:<25}{price:>15.2f}")

        print("-" * 40)

    def add_order(self, item, quantity):
        order = {
            "item": item,
            "quantity": quantity,
            "price": self.menu[item]
        }

        self.orders.append(order)

    def calculate_total(self):
        subtotal = 0.00

        for order in self.orders:
            subtotal += (
                order["quantity"] *
                order["price"]
            )

        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_total()

        if subtotal >= 500:
            return subtotal * 0.10

        return 0.00

    def print_receipt(self):
        subtotal = self.calculate_total()
        discount = self.calculate_discount()
        total = subtotal - discount

        print("\n")
        print("=" * 40)
        print(self.name.center(40))
        print(self.address.center(40))
        print("=" * 40)

        for order in self.orders:
            line_total = (
                order["quantity"] *
                order["price"]
            )

            print(
                f"{order['item']:<16}"
                f"{order['quantity']:>5}"
                f"{line_total:>19.2f}"
            )

        print("-" * 40)
        print(f"{'SUBTOTAL':<31}{subtotal:>9.2f}")

        if discount > 0:
            print(
                f"{'DISCOUNT (10%)':<31}"
                f"{-discount:>9.2f}"
            )

        print(f"{'TOTAL':<31}{total:>9.2f}")
        print("=" * 40)
        print("Thank you for ordering with us!".center(40))
        print("=" * 40)
