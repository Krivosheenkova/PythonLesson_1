"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return f'\n{self.name} is moving'

    def stop(self):
        if self.speed == 0:
            return f'\n{self.name} is stopped'

    def turn(self, direction):
        if direction == 'right':
            return f'\n{self.name} terned right'
        if direction == 'left':
            return f'\n{self.name} terned left'

    def show_speed(self):
        return f'\nThe speed of {self.name} is {self.speed}'

    def is_police_func(self):
        if self.is_police == True:
            return f'\n{self.name} is police car.'
        else:
            return f'\n{self.name} is not police car'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n{self.name} is driving too fast: {self.speed}km/h. Slow down!'
        else:
            return f'\nThe speed of {self.name} is {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n{self.name} is driving too fast: {self.speed}km/h. Slow down!'
        else:
            return f'\nThe speed of {self.name} is {self.speed}'


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'yellow', 'toyota', False)
print(town_car.go(), town_car.stop(), town_car.turn('left'), town_car.turn('right'), town_car.show_speed(),
      town_car.is_police_func())
sport_car = SportCar(0, 'blue', 'jaguar', False)
print(sport_car.go(), sport_car.stop(), sport_car.show_speed(),
      sport_car.is_police_func())
work_car = WorkCar(94, 'white', 'bmw', False)
print(work_car.go(), work_car.stop(), work_car.turn('left'), work_car.turn('right'), work_car.show_speed(), work_car.
      is_police_func())
police_car = PoliceCar(276, 'red', 'niva', True)
print(police_car.go(), police_car.stop(), police_car.turn('left'), police_car.turn('right'), police_car.show_speed(),
      police_car.is_police_func())
