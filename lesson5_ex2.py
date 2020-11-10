"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('test.txt') as f:
    letters = 0
    words = 0
    lines = 0
    for line in f:
        lines += 1
        letters += len(line)
        flag = 'out'
        for letter in line:
            if letter != ' ' and flag == 'out':
                words += 1
                flag = 'in'
            elif letter == ' ':
                flag = 'out'
print('Lines: ', lines)
print('Words: ', words)
print('Letters: ', letters)
