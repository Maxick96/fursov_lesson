"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
(файл family.txt)
+
"""

spisok = {}
str1 = 0
summastrok = 0
with open('family.txt', 'r') as f:
    for line in f:
        (val, key) = line.split()
        summastrok += 1
        spisok[val] = float(key)
        str1 += float(key)
        if float(key) < 20000:
            print(val)
    print('Средняя величина дохода сотрудников: ', str1 / summastrok)
f.close()
