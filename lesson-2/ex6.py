num = int(input('Сколько позиций товаров будем добавлять? '))
spisok1 = []
i = 1
while i <= num:
    spisok1.append(
        (input(f'Введите номер {i}го товара: '), dict({
            'Название': str(input(f'Введите название {i}го товара: ')),
            'Цена': float(input(f'Введите цену {i}го товара: ')),
            'Количество': int(input(f'Введите количество {i}го товара: ')),
            'Единица': str(input(f'Введите единицы измерения {i}го товара: ')),
        }))
    )
    i += 1
print(f'Список товаров:\n{spisok1}\n')
output_dict = dict({})
for prod in spisok1:
    for key, value in prod[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})
print(f'Собрана аналитика:\n {output_dict}')