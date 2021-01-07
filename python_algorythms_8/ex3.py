"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
    a. граф должен храниться в виде списка смежности;
    b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, visited, graph[start])
    # for next in graph[start] - visited:
    #     dfs(graph, next, visited)
    return visited


graph = {'0': ['1', '2'],
         '1': ['0', '3', '4'],
         '2': ['0'],
         '3': ['1'],
         '4': ['2', '3']}

dfs(graph, '0')