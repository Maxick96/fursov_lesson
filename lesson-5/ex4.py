"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
(файл spisok.txt)
+
"""

mass = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_mass = []
with open('spisok.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_mass.append(mass[i[0]] + '  ' + i[1])
    print(new_mass)
f.close()

with open('new_spisok.txt', 'w') as f1:
    f1.writelines(new_mass)
f1.close()