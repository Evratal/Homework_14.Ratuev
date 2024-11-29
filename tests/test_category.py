import pytest


def test_category_init(food_1):
    assert food_1.name == "Food"
    assert food_1.description == "Продуктовый отдел"
    assert food_1.category_count == 1
    assert food_1.product_count == 3


def test_add_product(food_1, carrot):
    food_1.add_product(carrot)
    assert food_1.product_count == 4


def test_category_str(food_1):
    assert str(food_1) == "Food, количество продуктов: 1800 шт."


def test_category_add_product(food_1):
    with pytest.raises(TypeError):
        food_1.add_product("Неизвестный продукт")
