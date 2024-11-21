import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def carrot():
    return Product("Carrot", "Морковка отечественная", 49.99, 500)


@pytest.fixture
def apple():
    return Product("Apple", "Яблоки волгоградские", 59.99, 400)


@pytest.fixture
def chocolate():
    return Product("Chocolate", "Шоколад Алёнка", 49.99, 900)


@pytest.fixture
def food_1():
    return Category(
        name="Food",
        description="Продуктовый отдел",
        products=[
            Product("Carrot", "Морковка отечественная", 49.99, 500),
            Product("Apple", "Яблоки волгоградские", 59.99, 400),
            Product("Chocolate", "Шоколад Алёнка", 49.99, 900),
        ],
    )


@pytest.fixture
def smart():
    smart = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    return smart
