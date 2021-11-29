timeyear1 = ['Зима', 'Весна', 'Лето', 'Осень']
timeyear2 = {
    'Зима': (12, 1, 2),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}
month = int(input('Введите месяц в виде числа от 1 до 12 - '))
num = int(input('Выберите способ ввода/вывода данных (1 - list, 2 - dict): '))
if num == 2:
    for i in timeyear2.keys():
        if month in timeyear2[i]:
            print(f'{month}ый месяц это - {i}')
    if month > 12 or month <= 0:
        print('Такого месяца не существует!')
if num == 1:
    if month == 12 or month == 1 or month == 2:
        print(timeyear1[0])
    if month == 3 or month == 4 or month == 5:
        print(timeyear1[1])
    if month == 6 or month == 7 or month == 8:
        print(timeyear1[2])
    if month == 9 or month == 10 or month == 11:
        print(timeyear1[3])
    if month > 12 or month <= 0:
        print('Такого месяца не существует!')