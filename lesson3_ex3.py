"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return sum(my_list)


print(my_func(1, 2, 3))


# def user_my_func():
#     print(my_func(a=int(input('a = ')), b=int(input('b = ')), c=int(input('c = '))))
#
#
# user_my_func()

