from unicodedata import category


class Category:
    """Класс для описания продукта"""
    name:str
    description:str
    products: list
    number_of_category = 0
    number_of_products = 0

    def __init__(self, name, description, products:list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name #Задаем имя категории
        self.description = description # Задаем описание категории
        self.products = products # Вносим список продуктов в категории
        Category.number_of_category += 1
        Category.number_of_products += len(products) if products else 0