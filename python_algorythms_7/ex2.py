"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random

size = 10
a = [round(random.random()*50, 2) for _ in range(size)]
print(f'Исходный массив: {a}')


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    left = merge_sort(array[:n//2])
    right = merge_sort(array[n//2:n])
    i, j = 0, 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        print(res)
    return res


a = merge_sort(a)
print(f'Отсортированный: {a}')
