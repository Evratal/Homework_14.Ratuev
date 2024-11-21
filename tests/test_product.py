from itertools import product

from src.product import Product
from tests.conftest import carrot


def test_product_init(carrot):
    assert carrot.name == "Carrot"
    assert carrot.description == "Морковка отечественная"
    assert carrot.price == 49.99
    assert carrot.quantity == 500



def test_new_product(smart):
    new_smart = Product.new_product(smart)
    assert new_smart.name == "Samsung Galaxy S23 Ultra"
    assert new_smart.description == "256GB, Серый цвет, 200MP камера"
    assert new_smart.price == 180000.0
    assert new_smart.quantity == 5

