"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
+
"""
with open ('chisla.txt', 'a+') as f:
    summa = 0
    chisla = input('Введите числа через пробел: ')
    f.write(f'{chisla}\n')
    for i in map(int, chisla.split()):
        summa += i
    f.write(f'{summa}\n')
    print('Сумма чисел - ', summa)
f.close()