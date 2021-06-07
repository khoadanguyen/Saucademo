class Product:
    def __init__(self, title, description, price, quantity = 1):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = int(quantity)
