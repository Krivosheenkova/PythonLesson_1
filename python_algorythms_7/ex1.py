"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""


import random

a = [random.randint(-100, 100) for i in range(10)]
random.shuffle(a)
print(f'Initial massive:'
      f'{a}')


def bubble(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    def revers(array):
        for i in range(len(array) // 2):
            array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
    return array


print(f'Sorted and reversed:'
      f'{bubble(a)}')
