slovo = input('Введите элементы списка через пробел (без пробела получится только 1 элемент списка) - ')
slovo = slovo.split()
print(slovo)
for i in slovo:
    print(f'{slovo.index(i)}-e слово - {i[:10]}')