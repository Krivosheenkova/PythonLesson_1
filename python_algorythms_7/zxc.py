'''
сортировка шелла
'''

import random
size = 100
array = [i for i in range(size)]
random.shuffle(array)
# print(array, '\n')

def shell_sort(array):
    assert len(array) < 4000, 'Massive is too big, choose another sorting method'


    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()
    count = 0
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, - increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1
                # print(array)
    # print(count)
shell_sort(array)

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Happen unexpected')
        print(s_ar, m_ar, l_ar)
        return quick_sort(s_ar) + quick_sort(m_ar) + quick_sort(l_ar)

array_new = quick_sort(array)

def quick_sort_no_memory(array, fst, lst):
    if fst >= lst:
        return
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
            print(array)
    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

# quick_sort_no_memory(array, 0, len(array) - 1)

'''
сортировка сложных структур
'''

from collections import namedtuple
Person = namedtuple('Person', 'name age')
p_1 = Person('Kolya', 25)
p_2 = Person('Nadezhda', 40)
p_3 = Person('Alina', 20)
p_4 = Person('Ilya', 29)
p_5 = Person('Oksana', 38)
p_6 = Person('Andrey', 43)
p_7 = Person('Ludmila', 54)
people = [p_1, p_2, p_3, p_4, p_5, p_6, p_7]

print(people)
# Отдельная функция для получения аргумента key=
def by_age(person):
    return person.age

result = sorted(people, key=by_age)
print(result)

'''
функция реверс
'''
def revers(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

revers(array)
print(array)