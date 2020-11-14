"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'The amount of fabric spent: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}m'

    @abstractmethod
    def received(self):
        pass

    def received(self):
        return f'Received parameter: {self.param}'


class Coat(Clothes):
    def received(self):
        return f'Received parameter: {self.param}'

    def coat_f(self):
        return f'It will take {self.param / 6.5 + 0.5 :.2f}m of fabrics to sew a coat'


class Costume(Clothes):
    def received(self):
        return f'Received parameter: {self.param}'

    def costume_f(self):
        return f'It will take {2 * self.param + 0.3 :.2f}m of fabrics to sew a costume'


coat = Coat(20)
print(coat.received() + '\n' + coat.coat_f())
costume = Costume(10)
print(costume.received() + '\n' + costume.costume_f())
clothes = Clothes(5)
print(clothes.received() + '\n' + clothes.consumption)