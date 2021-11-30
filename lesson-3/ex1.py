"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def delitchislo(chislo1, chislo2):
    """Функция реализует деление двух аргументов"""
    return chislo1 / chislo2

def proverkaresult():
    """Функция запрашивает данные, проверяет и выводит"""
    while True:
        chislo1 = input('Введите первое число - ')
        chislo2 = input('Введите второе число - ')
        if chislo1.isdigit() and chislo2.isdigit():
            if float(chislo2) != 0:
                print(f'Результат - {delitchislo(float(chislo1), float(chislo2))}')
                break
            else:
                print('На ноль делить нельзя! Введите число!\n')
        else:
            print('Введены недопустимые символы! Введите число ещё раз!\n')

proverkaresult()