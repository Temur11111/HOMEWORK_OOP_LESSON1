import pytest
from src.home_work import Category, Product

def test_category_initialization():
    """Тест правильности инициализации класса категории"""
    category = Category("Test Category", "Description", [])
    assert category.name == "Test Category"
    assert category.descriptions == "Description"
    assert category.products == []


def test_product_initialization():
    """Тест правильности инициализации класса продуктов"""
    name = "Тестовый товар"
    description = "Описание тестового товара"
    price = 100.0
    quantity = 10
    product = Product(name, description, price, quantity)
    assert product.name == name
    assert product.descriptions == description
    assert product.price == price
    assert product.quantity_in_stock == quantity


def test_category_count():
    """Тест подсчет количества категории"""
    category1 = Category("Категория 1", "Описание категории 1", [])
    category2 = Category("Категория 2", "Описание категории 2", [])
    category3 = Category("Категория 3", "Описание категории 3", [])
    assert Category.counter_categories == 3


def test_original_product_count():
    """Тест подсчета оригинальных продуктов"""
    category_1 = Category("Electronics", "Category for electronic products", ["Laptop","Smartphone","Notebooks"])
    assert Category.original_product == 3
    category_2 = Category("Iphone", "Описание", ["12","Smartphone","Notebooks"])

