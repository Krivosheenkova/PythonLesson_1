"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.weight = 25
        self.thick = 0.05


    def cnt(self):
        mass = self.__length * self.__width * self.weight * self.thick / 1000
        print(f'To cover a road surface of length {self.__length}m and width {self.__width}m, {round(mass)}T ' \
               f'asphalt is required')


r = Road(5000, 20)
r.cnt()