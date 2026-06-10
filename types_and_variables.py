# #ДЗ: Создание проекта в Pycharm
#
# print("Bears love honey and I'm a Pooh bear")

# # Тема: Типы данных
# # ДЗ: Определение и работа с типами данных
#
# print("ДЗ: Определение и работа с типами данных", '\n')
#
# integer_price = 10
# float_price = 1.59
# my_country = "Russia"
# list_of_fruits = ["apple", "orange", "pear"]
# rating_system = (5, 4, 3)
# product_description = {"name": "pillow", "guarantee": 5}
# rating = {5, 5, 4, 5, 3}
# my_number = "007"
# my_number_code = int(my_number)
# float_price_string = str(float_price)
# list_of_fruits_coords = tuple(list_of_fruits)
# list_of_numbers = [integer_price]
#
# print(type(integer_price), type(float_price), type(my_country),
#       type(list_of_fruits), type(rating_system), type(product_description),
#       type(rating), sep='\n')
#
# print('\n', "Из строки число:", my_number_code, '\n', "Из дробного числа в строку:",
#       float_price_string, '\n', "Из списка в кортеж:", list_of_fruits_coords, '\n',
#       "Из числа в список:", list_of_numbers)
#
# # ДЗ: Строгая и динамическая типизация
#
# print('\n', "ДЗ: Строгая и динамическая типизация", '\n')
#
# number_homework = 2
# difficulty_level = "2"
#
# print("При строгой типизации:", number_homework + int(difficulty_level))
# print("До динамической типизации number_homework имеет тип: ",
#       type(number_homework))
#
# number_homework = "Динамическая типизация в деле"
#
# print("После динамической типизации number_homework имеет тип: ",
#       type(number_homework))
#
# # ДЗ: Работа с изменяемыми типами данных
#
# iphone_version = [10, 20, 11, 12, 13, 14, 15, 16]
# iphone_version.append(17)
# iphone_version[0] = 9
# iphone_version.remove(20)
#
# print('\n', "Линейка iPhone представлена следующая:", iphone_version)

# # Тема: Переменные в Python
# ДЗ: Создание и использование переменных

# name, age, favorite_number = 'Илья', 31 , 1.59
#
# print('\n', "Меня зовут:", name, '\n', "Мой возраст:", age, '\n',
#       "Любимое число:", favorite_number)
#
# age = 32
# favorite_number = 10
#
# print('\n', "Обновлённые данные", '\n', "Меня зовут:", name, '\n',
#       "Мой возраст будет:", age, '\n', "Новое любимое число:",
#       favorite_number)


# # Тема: Простейшие операции
# # ДЗ: Выполнение простейших операций
#
# a, b = 24, 23
# sum_of_numbers = a + b
# number_difference = a - b
#
# print('\n', "Сумма a + b =", sum_of_numbers, '\n', "Разность a - b =", number_difference)
#
# x, y = 126.5, 44.12
# multiplying_numbers = x * y
# dividing_numbers = x / y
#
# print('\n', "Умножение x * y =", multiplying_numbers, '\n', "Деление x / y =", dividing_numbers)
#
# m, n = 4545.87, 86.99
# integer_division = m // n
# division_remainder = m % n
#
# print('\n', "Целочисленное деление m // n =", integer_division, '\n',
#       "Остаток от деления  m % n =", division_remainder)
#
# base, exponent  = 87, 12
# exponentiation = base ** exponent
#
# print('\n', "Возведение в степень base ** exponent =", exponentiation)
#
# q, w, e, r, t, y = 2, 3, 5, 7, 8, 10
# first_expression = (e + w) * q
# second_expression = y / w + r
# third_expression = t ** q - e
#
# print('\n', f"Первое произведение: ({e} + {w}) * {q} =", first_expression)
# print(f"Второе произведение: {y} / {w} + {r} =", second_expression)
# print(f"Третье произведение: {t} ** {q} - {e} =", third_expression)