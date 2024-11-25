def test_lawngrass_init(grass_1):
    assert grass_1.name == "Газонная трава 2"
    assert grass_1.description == "Выносливая трава"
    assert grass_1.price == 450.0
    assert grass_1.quantity == 15
    assert grass_1.country == "США"
    assert grass_1.germination_period == "5 дней"
    assert grass_1.color == "Темно-зеленый"
