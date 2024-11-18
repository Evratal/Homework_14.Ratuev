
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
        self.__price = price # Задаем цену
        self.quantity = quantity # Задаем количество

    @classmethod
    def new_product(cls,prod_dict):
        #new_instance = product(prod_dict["name"], prod_dict["description"], prod_dict["price"], prod_dict["quantity"])
        return cls(prod_dict["name"], prod_dict["description"], prod_dict["price"], prod_dict["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer_user = ""
            while answer_user not in ["y", "n"]:
                print("Новая цена ниже текущей. Вы действительно хотите понизить цену? ")
                answer_user = input("Введите 'y'(в качестве подтверждения) или 'n'(в случае отказа от изменения): ")

                if answer_user == "y":
                    self.__price = new_price
                    print("Изменения приняты")
                elif answer_user == "n":
                    print("Изменения отменены")
                else:
                    print("Некорректный ввод.Попробуйте ещё раз")
        return self.__price

