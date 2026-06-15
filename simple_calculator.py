# ДЗ: Калькулятор

class OperationError(Exception):
    pass


try:
    number_one = float(input("Введите 1-е число: "))
    number_two = float(input("Введите 2-е число: "))
    operation = input("Доступные действия:\n'+' - сложение\n'-' - вычитание\n"
                      "'*' - умножение\n'/' - деление\nВведите математический символ: ")

    if operation == '+':
        result = number_one + number_two
    elif operation == '-':
        result = number_one - number_two
    elif operation == '*':
        result = number_one * number_two
    elif operation == '/':
        result = number_one / number_two
    else:
        raise OperationError("\nОшибка: Введён неверный математический символ")

except ValueError:
    print("\nОшибка: Некорректный ввод числа")
except ZeroDivisionError:
    print("\nОшибка: Попытка деления на ноль")
except OperationError as e:
    print(e)
else:
    print(f"\n{number_one} {operation} {number_two} = {result}")