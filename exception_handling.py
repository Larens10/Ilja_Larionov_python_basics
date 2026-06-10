# ДЗ: Обработка исключений

try:
    number_one = float(input("Введите числитель (через точку): "))
    number_two = float(input("Введите знаменатель (через точку): "))
    result = number_one / number_two
except ValueError:
    print('\n', "Ошибка: Некорректный ввод числа")
except ZeroDivisionError:
    print('\n', "Ошибка: Попытка деления на ноль")
else:
    print('\n', f"Выражение {number_one} / {number_two} = {result}")
finally:
    print('\n', "Расчёт завершён. Программа закрыта")
