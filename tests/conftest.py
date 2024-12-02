import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def grass_1():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


@pytest.fixture
def smartphone_2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

@pytest.fixture
def category_without_product():
    return Category(
        name="Brak",
        description="Брак",
    )