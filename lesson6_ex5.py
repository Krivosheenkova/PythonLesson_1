"""
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = "title"

    def draw(self):
        print('Start rendering...')

class Pen(Stationery):
    def draw(self):
        print('Pen is writing...')

class Pencil(Stationery):
    def draw(self):
        print('Pencil is drawing...')

class Handle(Stationery):
    def draw(self):
        print('Drawing by handle...')

s = Stationery()
pn = Pen()
pncl = Pencil()
h = Handle()

s.draw()
pn.draw()
pncl.draw()
h.draw()