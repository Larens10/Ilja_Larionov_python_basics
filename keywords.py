# ДЗ: Ключевые слова

def max_number(number_one, number_two):
    if number_one >= number_two:
        return number_one
    else:
        return number_two


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
    assert max_number(9, 10) == 10, "Ошибка: из чисел (9, 10) большее 10"
    assert max_number(9.9, 9.91) == 9.91, ("Ошибка: из чисел (9.9, 9.91) "
                                           "большее 9.91")
    assert max_number(9, 9.91) == 9.91, ("Ошибка: из чисел (9, 9.91) "
                                           "большее 9.91")
    assert max_number(-9.9, -9.91) == -9.9, "Ошибка: из чисел (-9.9, -9.91) большее -9.9"
    assert max_number(-9, -9.91) == -9, "Ошибка: из чисел (-9, -9.91) большее -9"
    assert max_number(0, 0) == 0, ("Ошибка: из одинаковых чисел (0, 0)"
                                   " максимальное любое и равно 0")
    assert max_number(1, 1) == 1, ("Ошибка: из чисел (1, 1) максимальное"
                                   " любое и равно 1")


for sequence_of_even_numbers in even_numbers(-10.25):
    print(sequence_of_even_numbers)

test_max_number()
print("\nВсе тесты пройдены!")
