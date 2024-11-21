
from src.product import Product


class Category:
    """Класс для описания продукта"""
    name:str
    description:str
    products: list
    number_of_category = 0
    quantity:int

    def __init__(self, name, description, products:list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.product_count = 0
        self.name = name #Задаем имя категории
        self.description = description # Задаем описание категории
        self.__products = products # Вносим список товаров в категории
        Category.number_of_category += 1
        self.product_count += len(self.__products) if products else 0




    def add_product(self,new_product:Product):
        self.__products.append(new_product)
        self.product_count += 1
        return self.__products

    @property
    def products(self):
        new_list_of_products = []
        for product in self.__products:
            new_str_product = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            new_list_of_products.append(new_str_product)
        return new_list_of_products
