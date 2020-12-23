"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
    a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
    b. написать 3 варианта кода (один у вас уже есть);
        проанализировать 3 варианта и выбрать оптимальный;
    c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
        комментариев в файл с кодом.
    d. написать общий вывод: какой из трёх вариантов лучше и почему.
Linux Arch 5.4.79-1-lts x86_64 GNU/Linux
Python 3.8.6
"""
import sys
import random


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, obj= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


''' ex9 lesson3 '''
diap = 9
matrix = [[random.randint(0, diap) for _ in range(4)] for _ in range(4)]
print(matrix)
min_out = 0
lst = []
for i in range(len(matrix[0])):
    min_in = diap
    for k in range(len(matrix)):
        if matrix[k][i] < min_in:
            min_in = matrix[k][i]
        print(matrix[k][i], end=' ')
    print(f' | {min_in}')
    lst.append(min_in)

for j in range(len(lst)):
    if lst[j] > min_out:
        min_out = lst[j]

print(f'Максимум из минимумов: {min_out}')

# show_size(matrix)
# type= <class 'list'>, size= 88, obj= [[8, 5, 3, 3], [3, 6, 6, 1], [6, 3, 1, 2], [9, 4, 6, 2]]
# show_size(lst)
# type= <class 'list'>, size= 88, obj= [0, 3, 2, 0]
# 	 type= <class 'int'>, size= 24, obj= 0
# 	 type= <class 'int'>, size= 28, obj= 3
# 	 type= <class 'int'>, size= 28, obj= 2
# 	 type= <class 'int'>, size= 24, obj= 0

# show_size(min_out)
# type= <class 'int'>, size= 24, obj= 0 or type= <class 'int'>, size= 28, obj= 4

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random.random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)

# show_size(b)
# type= <class 'list'>, size= 184, obj= [184, 152, 54, 195, 170, 1, 42, 164, 127, 24]





