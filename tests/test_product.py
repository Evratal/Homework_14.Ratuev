from tests.conftest import carrot


def test_product_init(carrot):
    assert carrot.name == "Carrot"
    assert carrot.description == "Морковка отечественная"
    assert carrot.price == 49.99
    assert carrot.quantity == 500