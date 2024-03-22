import pytest
from classes import Category, Product

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
    assert Category.total_categories == 1