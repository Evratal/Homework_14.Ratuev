from itertools import product

from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass
from src.exceptions import ZeroQuantity

class Category:
    """Класс для описания продукта"""

    name: str
    description: str
    products: list
    category_count = 0
    quantity: int
    product_count = 0

    def __init__(self, name, description, products: list = []):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name  # Задаем имя категории
        self.description = description  # Задаем описание категории
        self.__products = products  # Вносим список товаров в категории
        Category.category_count += (
            1  # При создании категории, счётчик будет увеличиваться на 1
        )
        self.product_count += len(
            self.__products
        )  # Количество наименований товаров в категории
    def __repr__(self):
        return print(f"{self.name}")

    def __str__(self):
        summ_of_product = 0
        for prod in self.__products:
            summ_of_product += prod.quantity
        return f"{self.name}, количество продуктов: {summ_of_product} шт."

    def add_product(self, new_product: Product):
        """Функция для добавления товара в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
            print("Товар успешно добавлен")
        else:
            raise TypeError("Данный тип невозможно добавить в категорию")


    @property
    def products(self):
        """Функция для отображения всех товаров в категории по определенному шаблону"""
        new_list_of_products = []
        for product in self.__products:
            new_str_product = (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
            new_list_of_products.append(new_str_product)
        return new_list_of_products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products),2)
        except ZeroDivisionError:
            return 0