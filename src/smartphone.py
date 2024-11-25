from src.product import Product


class Smartphone(Product):
    "Класс для описания смартфона в качестве товара"

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # Дополнительный код
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
