class Product:
    """Класс для описания продукта"""
    name:str
    description:str
    price:float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name #Задаем имя продукта
        self.description = description # Задаем описание продукта
        self.price = price # Задаем цену
        self.quantity = quantity # Задаем количество
