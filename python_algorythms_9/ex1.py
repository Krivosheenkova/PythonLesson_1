"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1()
или любой другой из модуля hashlib задача считается не решённой.
"""
from hashlib import sha1


def sub_count(string):
    assert all(map(lambda c: 97 <= ord(c) <= 122, string)), "You'd better use latin letters"
    subs = set()
    for i in range(len(string)):
        for k in range(len(string) - 1 if i == 0 else len(string), i, -1):
            # print(string[i:k])
            hstr = sha1(string[i:k].encode('utf-8')).hexdigest()
            subs.add(hstr)
    return f'{len(subs) - 1} different substrings were found in string {string}'


s = input('Enter any string using latin letters: ').lower()
print(sub_count(s))
