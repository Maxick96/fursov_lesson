my_list = [7, 5, 3, 3, 2]
print(f'Старый список - {my_list}')
chislo = int(input('Введите число - '))
if chislo == 0:
    print(f'{chislo} не является натуральным числом, введите заново!')
else:
    for i in my_list:
        if chislo > max(my_list):              #если число меньше максимального в списке - отправляем число на 0-ую позицию
            my_list.insert(0, chislo)
            break
        if chislo < min(my_list):              #если число меньше минимального в списке - отправляем число на последнюю позицию
            my_list.append(chislo)
            break
        if chislo == i:              #если число ровно одному из элементов - отправляем число после равного элемента
            my_list.insert(my_list.index(i), chislo)
            break
    print(f'Новый список - {my_list}')