from abc import ABC,abstractmethod

class ObjectCreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_object_creation()

    def log_object_creation(self):
        class_name = self.__class__.__name__
        attributes = ", ".join([f"{key}={value}" for key, value in self.__dict__.items()])
        print(f"Создан объект класса {class_name}: {attributes}")


class AbstractProduct(ABC):
    @abstractmethod
    def additional_info(self):
        pass


class Category(ObjectCreationLoggerMixin):
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product или его наследников")
        if product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
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

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class Product(ObjectCreationLoggerMixin, AbstractProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
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

    @abstractmethod
    def additional_info(self):
        pass

class Smartphone(Product):
    def __init__(self, name, price, quantity, performance, model, memory, color):
        super().__init__(name, price, quantity, category="Смартфон")
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
    
    def additional_info(self):
        return f"Производительность: {self.performance}, Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}"

class LawnGrass(Product):
    def __init__(self, name, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, price, quantity, category="Трава газонная")
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def additional_info(self):
        return f"Страна-производитель: {self.country_of_origin}, Срок прорастания: {self.germination_period}, Цвет: {self.color}"
