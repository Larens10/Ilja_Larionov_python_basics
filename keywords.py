# ДЗ: Ключевые слова

def max_number(number_one, number_two):
    if number_one >= number_two:
        return number_one
    else:
        return number_two


def entering_two_numbers():
    number_one = get_number("Введите 1-е число: ")
    number_two = get_number("Введите 2-е число: ")
    return number_one, number_two


def get_number(input_text):
    while True:
        try:
            return float(input(input_text))
        except ValueError:
            print("\nОшибка: Некорректный ввод числа")


def empty_function():
    pass


def even_numbers(number):
    if number >= 0:
        for i in range(0, int(number) + 1, 2):
            yield i
    else:
        for i in range(0, int(number) - 1, -2):
            yield i


def test_max_number():
    assert max_number(10, 9) == 10, "Ошибка: из чисел (10, 9) большее 10"
    assert max_number(9.9, 9.91) == 9.91, ("Ошибка: из чисел (9.9, 9.91) "
                                           "большее 9.91")
    assert max_number(-9, -9.91) == -9, "Ошибка: из чисел (-9, -9.91) большее -9"
    assert max_number(1, 1) == 1, ("Ошибка: из чисел (1, 1) максимальное"
                                   " любое и равно 1")


for sequence_of_even_numbers in even_numbers(-10.25):
    print(sequence_of_even_numbers)

test_max_number()
print("\nВсе тесты пройдены!\n")

first_number, second_number = entering_two_numbers()
print(f'Наибольшим между {first_number} и {second_number} является:'
      f' {max_number(first_number, second_number)}')
