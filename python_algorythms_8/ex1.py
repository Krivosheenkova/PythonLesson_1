"""
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
# kindergarden is wanting me
N = int(input('How many friends will shake hands: '))
graph = [i * [0] + (N - i) * [1] for i in range(1, N + 1)]
print(*graph, sep='\n')
count = 0
for g in graph:
    for i in g:
        if i == 1:
            count += 1
print(f"{N} friends will shake each other's hand for {count} times")