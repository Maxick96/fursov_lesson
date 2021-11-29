mass = input('Введите элементы списка через пробел (без пробела получится только 1 элемент списка) - ')
mass = mass.split()
print(f'Получившийся список - {mass}')
print(f'Кол-во элементов в списке - {len(mass)}')
i = 0
while i < len(mass)-1:
    mass[i+1], mass[i] = mass[i], mass[i+1]
    i += 2
    print(mass)