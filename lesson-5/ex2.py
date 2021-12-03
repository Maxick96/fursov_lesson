"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
(файл lesson.txt)
+
"""
summastrok = 0
summaslovstrok = 0
with open ('lesson.txt', 'r') as f:
    for line in f:
        summaslovstrok = len(line.split())
        summastrok += 1
        print(f'Кол-во слов в {summastrok} стройке - ', summaslovstrok)
    print('Кол-во строк в файле - ', summastrok)
f.close()
