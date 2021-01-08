"""
2. Закодируйте любую строку по алгоритму Хаффмана.

"""

import heapq
from collections import Counter, namedtuple
from binarytree import build

class Node1(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')



class Leaf(namedtuple('Leaf', ['ch'])):
    def walk(self, code, acc):
        code[self.ch] = acc or '0'


def huffman_encode(string):
    hash_table = []
    for ch, frq in Counter(string).items():
        hash_table.append((frq, len(hash_table), Leaf(ch)))
        # print(hash_table)
    heapq.heapify(hash_table)
    count = len(hash_table)
    while len(hash_table) > 1:
        frq1, _count1, left = heapq.heappop(hash_table)
        frq2, _count2, right = heapq.heappop(hash_table)
        # print(f'frq1 = {frq1}, _count1 = {_count1}, left = {left}')
        # print(f'frq2 = {frq2}, _count2 = {_count2}, right = {right}')
        heapq.heappush(hash_table, (frq1 + frq2, count, Node1(left, right)))
        count += 1
    code = {}
    if hash_table:
        [(_frq, _count, root)] = hash_table
        # print(f'[(_frq, _count, root)] = {[(_frq, _count, root)]}')
        root.walk(code, '')

    encoded_str = ''
    for c in string:
        encoded_str = encoded_str + ' ' + code[c]
    return f'{string}\n{code}\n{encoded_str}'


print(huffman_encode('abracadabra'))
# с бумажки..........
d = build([11, 5, 6, None, None, 2, 4, None, None, None, None, None, None, 2, 2, None, None, None, None, None,
           None, None, None, None, None, None, None, 1, 1, None, None])
print(d)
