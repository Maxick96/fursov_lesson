"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
(файл firma.txt)
+
"""
import json

firma = {}
average = {}
srprib = 0
srprib1 = 0
i = 0
with open ('firma.txt', 'r') as f:
    for line in f:
        subject, yourlico, vyr, izd = line.split()
        firma[subject] = int(vyr) - int(izd)
        if firma[subject] >= 0:
            srprib += firma.setdefault(subject)
            i += 1
    if i >= 0:
        srprib1 = srprib / i
        print('Средняя прибыль: ', srprib1)
    else:
        print('Прибыль отсутствует в среднем у всех!')
    average = {'Average - ': srprib1}
    firma.update(average)
    print('Прибыль каждой компании - ', firma)

with open ('data.json', 'w') as f:
    json.dump(firma, f)
f.close()
