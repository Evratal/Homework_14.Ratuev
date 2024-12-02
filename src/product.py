from src.baseproduct import BaseProduct
from src.mixinproduct import Mixin


class Product(BaseProduct,Mixin):
    """Класс для описания продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name  # Задаем имя продукта
        self.description = description  # Задаем описание продукта
        self.__price = price  # Задаем цену
        if quantity > 0:
            self.quantity = quantity  # Задаем количество
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        """Магический метод для определения общей стоимости двух видов товаров на складе"""
        if not isinstance(other, self.__class__):
            raise TypeError("Складывать можно только продукты одной категории")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, prod_dict):
        return cls(
            prod_dict["name"],
            prod_dict["description"],
            prod_dict["price"],
            prod_dict["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Функция, дял обновления цены товара"""
        if new_price <= 0:
            """Проверка на отрицательную цену"""
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            """В случае, если новая цена ниже старой, то уточняем замену"""
            answer_user = ""
            """Строка для ввода ответа, если пользователь вводит 'y', то пользователь подтверждает изменения,
             если 'n', то отказывается, если никакой из двух,
            то через цикл запрашиваем ещё раз, пока не получим один из двух ответов"""
            while answer_user not in ["y", "n"]:
                print(
                    "Новая цена ниже текущей. Вы действительно хотите понизить цену? "
                )
                answer_user = input(
                    "Введите 'y'(в качестве подтверждения) или 'n'(в случае отказа от изменения): "
                )

                if answer_user == "y":
                    self.__price = new_price
                    print("Изменения приняты")
                elif answer_user == "n":
                    print("Изменения отменены")
                else:
                    print("Некорректный ввод.Попробуйте ещё раз")
        return self.__price