# ДЗ: Калькулятор

result = None
try:
    number_one = float(input("Введите 1-е число: "))
    number_two = float(input("Введите 2-е число: "))
except ValueError:
    print('\n', "Ошибка: Некорректный ввод числа")
else:
    enable_operation = '+-*/'
    operation = input("Доступные действия:\n'+' - сложение\n'-' - вычитание\n"
                      "'*' - умножение\n'/' - деление\nВведите математический символ: ")
    if operation in enable_operation:
        if operation == '+':
            result = number_one + number_two
        elif operation == '-':
            result = number_one - number_two
        elif operation == '*':
            result = number_one * number_two
        else:
            try:
                result = number_one / number_two
            except ZeroDivisionError:
                print('\n', "Ошибка: Попытка деления на ноль")
        if result is not None:
            print('\n', f"{number_one} {operation} {number_two} = {result}")
    else:
        print('\n', "Ошибка: Введён неверный математический символ")