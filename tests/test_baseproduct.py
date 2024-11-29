import pytest

from src.product import Product


def test_baseproduct_init(carrot):
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


def test_baseproduct_str(carrot):
    assert str(carrot) == "Carrot, 49.99 руб. Остаток: 500 шт."


def test_baseproduct_add(carrot, apple, smartphone_1, smartphone_2):
    "Тестирование суммирования объектов"
    assert carrot + apple == 48991.0
    assert smartphone_1 + smartphone_2 == 2580000.0
    with pytest.raises(TypeError):
        smartphone_1 + 1
