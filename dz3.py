class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Ціна: {self.price} грн")
        print(f"Наявність: {self.quantity} шт.")


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            print("Кількість має бути більшою за 0!")
        elif product.quantity < quantity:
            print("Недостатньо товару на складі!")
        else:
            if product in self.items:
                if self.items[product] + quantity > product.quantity:
                    print("Недостатньо товару на складі!")
                    return
                self.items[product] += quantity
            else:
                self.items[product] = quantity

            print(f"{product.name} додано до кошика!")

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]
            print(f"{product.name} видалено з кошика!")
        else:
            print("Товар не знайдено в кошику!")

    def calculate_total(self):
        total = sum(
            product.price * quantity
            for product, quantity in self.items.items()
        )
        return total

    def display_cart(self):
        if not self.items:
            print("Кошик порожній!")
            return

        print("\n--- Ваш кошик ---")
        for product, quantity in self.items.items():
            print(
                f"{product.name} — {quantity} шт. "
                f"× {product.price} грн = "
                f"{product.price * quantity} грн"
            )

        print(f"Загальна вартість: {self.calculate_total()} грн")

laptop = Product("Ноутбук", 25000, 5)
mouse = Product("Мишка", 500, 10)
keyboard = Product("Клавіатура", 1200, 7)
cart = Cart()
cart.add_product(laptop, 1)
cart.add_product(mouse, 2)
cart.add_product(keyboard, 1)
cart.display_cart()
cart.remove_product(mouse)
cart.display_cart()