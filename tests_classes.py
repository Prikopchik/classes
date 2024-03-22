import pytest
from classes import Product
from classes import Category

@pytest.fixture
def sample_category():
    return Category("Electronics", "Electronic gadgets category")

@pytest.fixture
def sample_product():
    return Product("Laptop", "High-performance laptop", 1200.50, 10)

def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Electronic gadgets category"

def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High-performance laptop"
    assert sample_product.price == 1200.50
    assert sample_product.quantity == 10

def test_total_unique_products(sample_category, sample_product):
    assert Category.total_unique_products == set()
    sample_category.add_product(sample_product)
    assert Category.total_unique_products == {"Laptop"}

def test_total_categories(sample_category):
    assert Category.total_categories == 3

def test_category_products():
    category = Category("Electronics", "Electronic gadgets category")
    product1 = Product("Laptop", 1200.50, 10)
    product2 = Product("Smartphone", 800, 15)
    category.add_product(product1)
    category.add_product(product2)
    assert category.products == "Laptop, 1200.5 руб. Остаток: 10 шт.\nSmartphone, 800 руб. Остаток: 15 шт.\n"

def test_product_creation():
    product = Product.create_product("Keyboard", 50, 20)
    assert isinstance(product, Product)
    assert product.name == "Keyboard"
    assert product.price == 50
    assert product.quantity == 20

def test_product_price_setter_valid():
    product = Product("Laptop", "High-performance laptop", 1200.50, 10)
    product.price = 1500
    assert product.price == 1500

def test_product_price_setter_invalid():
    product = Product("Laptop", "High-performance laptop", 1200.50, 10)
    product.price = -500
    assert product.price == 1200.50 
