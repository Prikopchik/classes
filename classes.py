class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products.add(product.name)


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
