from src.product import Product


class LawnGrass(Product):
    "Класс для описания газонной травы в качестве товара"

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # Дополнительный код
        self.country = country
        self.germination_period = germination_period
        self.color = color
