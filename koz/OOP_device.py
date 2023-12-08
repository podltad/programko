class device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, device, quantity):
        self.items.append((device, quantity))

    def calculate_total(self):
        total = 0
        for device, quantity in self.items:
            total += device.price * quantity
        return total

    def display_cart(self):
        print("nákupní košík:")
        for device, quantity in self.items:
            print(f"{device} x{quantity}")
        print(f"celkem: {self.calculate_total()} KČ")

device1 = device("mobil", 12000)
device2 = device("notebook", 36000)
device3 = device("tablet", 7000,)
device4 = device("TV",9500,)

cart = ShoppingCart()

cart.add_item(device1, 2)
cart.add_item(device2, 1)
cart.add_item(device3, 3)
cart.add_item(device4, 4)

cart.display_cart()