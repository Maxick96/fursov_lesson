"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
 Данные методы должны применяться только к клеткам и выполнять:
  увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Kletka:
    def __init__(self, kolvo: int):
        self._kolvo = kolvo

    def __add__(self, other):
        return f' Сумма двух клеток = {self._kolvo + other._kolvo}'

    def __sub__(self, other):
        sub = self._kolvo - other._kolvo
        if sub > 0:
            return f' Результат вычитания двух клеток = {sub}'
        else:
            return f' Клетка исчезла!'

    def __mul__(self, other):
        return f' Умножение двух клеток = {self._kolvo * other._kolvo}'

    def __truediv__(self, other):
        return f' Деление двух клеток = {self._kolvo // other._kolvo}'

    def make_order(self, row):
        result = ''
        for i in range(int(self._kolvo / row)):
            result += '*' * row + '\n'
        result += '*' * (self._kolvo % row) + '\n'
        return result

cell = Kletka(5)
cell_2 = Kletka(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))