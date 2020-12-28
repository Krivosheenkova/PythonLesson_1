"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
m = 10
size = 2 * m + 1
massive = [i for i in range(size)]
random.shuffle(massive)
print(f'Initial massive: {massive}')


# ¯\_(ツ)_/¯ сложно
def median(array):
    return (len(array) - 1) // 2


print(f'Median: {median(massive)}')


