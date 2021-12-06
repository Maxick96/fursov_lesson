"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
+
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed: int = speed
        self.color: str = color
        self.name: str = name
        self.is_police: bool = is_police

    def go(self):
        return f'{self.color} {self.name} поехала!'
    def stop(self):
        return f'{self.name} остановилась!'
    def turn(self, direction):
        return f'{self.name} повернула {direction}'
    def policereturn(self):
        if self.is_police == True:
            return 'Это полиция! '
        else:
            return 'Это оБычный водитель!'
    def show_speed(self):
        return f'{self.speed} - текущая скорость!'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышена скорость!'
        else:
            return 'Скорость в норме! '

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышена скорость!'
        else:
            return 'Скорость в норме!'

class PoliceCar(Car):
    pass

work = WorkCar(20, 'Зеленая', 'BMW X5', False)
town = TownCar(130, 'Коричневая', 'BMW X3', False)
police = PoliceCar(150, 'Жёлтая', 'BMW X2', True)
sport = SportCar(110, 'Черная', 'BMW X1', False)

print('1) ' + work.go(), work.show_speed(), work.turn('направо!'), work.turn('налево!'), work.stop())
print('2) ' + town.go(), town.show_speed(), town.turn('направо!'), town.turn('налево!'), town.stop())
print('3) ' + police.go(), police.show_speed(), police.policereturn(), police.turn('направо!'), police.stop())
print('4) ' + sport.go(), sport.show_speed(), sport.turn('направо!'), sport.turn('налево!'), sport.stop())
#print(town.show_speed(), town.skorost())