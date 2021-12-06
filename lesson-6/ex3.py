"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на:
словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
+
"""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': wage, 'Премия': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника и должность (Фамилия, Имя) - {self.name} {self.surname}, {self.position}'

    def get_total_income(self):
        return self._income['Оклад'] + self._income['Премия']

max_f = Position('Фурсов', 'Максим', 'Менеджер', 110, 30)
mik_r = Position('Родионов', 'Михаил', 'Инженер', 150, 10)
elena_t = Position('Митрохина', 'Елена', 'Продавец', 120, 100)
print(f'{max_f.get_full_name()}\nДоход с учётом премии - {max_f.get_total_income()}')
print(f'{mik_r.get_full_name()}\nДоход с учётом премии - {mik_r.get_total_income()}')
print(f'{elena_t.get_full_name()}\nДоход с учётом премии - {elena_t.get_total_income()}')