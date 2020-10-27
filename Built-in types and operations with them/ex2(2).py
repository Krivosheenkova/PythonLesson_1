# Ex. 2
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
n = int(input('Enter number of elements: '))
user_list = []
el = 0
i = 0
while i < n:
    user_list.append(input('Enter element: '))
    i += 1
for el in range(int(len(user_list) / 2)):
    user_list[el], user_list[el+1] = user_list[el+1], user_list[el]
    el += 2
print(user_list)


