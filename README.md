Программа для работы интернет магазина
Организованы классы: продукты и категории. От класса продукты организованы ещё два класса: смартфоны и трава для газона.
Внутри классов созданы функции. Для класса категории:инизализация, добавление нового товара (с проверкой на соответствии надлежащего класса), 
отоброжения ассортимента
Для класса продуктов:иницализация, показ цены, обновление цены, общая стоимость двух хранящихся товаров(с проверкой на соответствие надлежащего класса).
Новосозданные классы и функции протестированы
29.11.2024. добавлен базовый класс(BaseProduct) и класс-миксин(Mixin), для отображения информации о вновь созданном продукте.
02.11.2024 добавлена обработка ошибки, при добавления нового объекта класса Product с нулевым количеством. 
Также добавлен новый функционал для класса Category, позволяющий получить средний ценик всех товаров в категории.