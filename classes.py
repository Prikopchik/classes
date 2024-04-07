class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return result

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return total_quantity


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."
    
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        total_price_self = self.price * self.quantity
        total_price_other = other.price * other.quantity
        return total_price_self + total_price_other
    
    @classmethod
    def create_product(cls, data):
        return cls(**data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: введена некорректная цена.")
        else:
            self.__price = new_price

class Smartphone(Product):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity, category="Смартфон")
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, price, quantity, category="Трава газонная")
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color