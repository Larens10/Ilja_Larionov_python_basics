# ДЗ: Объявление и вызов функций

def say_hello():
    print('Hello, Python!')


def repeat_message(message):
    print(f"\n{message}" * 3)

    say_hello()
    repeat_message("Хеллоу, Питонище")


# ДЗ: Функции с аргументами и возвращаемыми значениями

def multiply(first_factor, second_factor):
    return first_factor * second_factor


print(multiply(98, 77.6))


# ДЗ: Встроенные функции

def object_description(testee):
    data_type = type(testee).__name__
    try:
        data_length = len(testee)
    except TypeError:
        return data_type, (f'{data_type} не имеет длины '
                           f'и не поддерживает len()')
    else:
        return data_type, data_length


def display_object_description(my_object):
    data_type, data_length = object_description(my_object)
    print(f'\nВведённый объект: {my_object}\nТип данных: {data_type}\n'
          f'Длина объекта: {data_length}')


integer_price = 10
float_price = 1.59
my_country = "Russia"
list_of_fruits = ["apple", "orange", "pear"]
rating_system = (5, 4, 3)
product_description = {"name": "pillow", "guarantee": 5}
rating = {5, 5, 4, 5, 3}

display_object_description(my_country)
display_object_description(list_of_fruits)
display_object_description(rating_system)
display_object_description(product_description)
display_object_description(rating)
display_object_description(integer_price)
display_object_description(float_price)
