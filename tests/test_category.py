def test_category_init(food):
    assert food.name == "Food"
    assert food.description == "Продуктовый отдел"
    assert len(food.products) == 3
    assert food.number_of_category == 1
    assert food.number_of_products == 3