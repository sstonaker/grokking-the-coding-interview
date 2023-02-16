"""Problem Statement

Topological Sort of a directed graph (a graph with unidirectional edges) is a
linear ordering of its vertices such that for every directed edge (U, V) from
vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Example 2:

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Example 3:

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2],
[4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
"""

from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return []

    return sorted_order


def main():
    print(
        f"Topological sort: {str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))}")
    print(
        f"Topological sort: {str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))}")
    print(f"Topological sort: \
        {str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))}")


main()
