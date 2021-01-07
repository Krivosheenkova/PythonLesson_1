"""
2. Закодируйте любую строку по алгоритму Хаффмана.

"""

import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['ch'])):
    def walk(self, code, acc):
        code[self.ch] = acc or '0'


def huffman_encode(string):
    h = []
    for ch, frq in Counter(string).items():
        h.append((frq, len(h), Leaf(ch)))
    heapq.heapify(h)
    print(h)
    count = len(h)
    while len(h) > 1:
        frq1, _count1, left = heapq.heappop(h)
        frq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (frq1 + frq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_frq, _count, root)] = h
        root.walk(code, '')
    return code

print(huffman_encode('abracadabra'))