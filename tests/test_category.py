def test_category_init(food_1):
    assert food_1.name == "Food"
    assert food_1.description == "Продуктовый отдел"
    assert food_1.number_of_category == 1
    assert food_1.product_count == 3


def test_add_product(food_1, carrot):
    food_1.add_product(carrot)
    assert food_1.product_count == 4


def test_category_str(food_1):
    assert str(food_1) == "Food, количество продуктов: 1800 шт."
