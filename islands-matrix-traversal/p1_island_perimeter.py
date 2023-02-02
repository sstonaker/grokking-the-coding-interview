"""Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge
or 0s (water). Each cell is considered connected to other cells horizontally or
vertically (not diagonally).

There are no lakes on the island, so the water inside the island is not
connected to the water around it. A cell is a square with a side length of 1..

The given matrix has only one island, write a function to find the perimeter
of that island.

Example 1

Input: matrix =
[ 1, 1, 0, 0, 0 ]
[ 0, 1, 0, 0, 0 ]
[ 0, 1, 0, 0, 0 ]
[ 0, 1, 1, 0, 0 ]
[ 0, 0, 0, 0, 0 ]


Output: 14
Explanation: The boundary of the island constitute 14 sides.

Example 2

Input: matrix =
[ 0, 0, 0, 0, 0 ]
[ 0, 1, 0, 0, 0 ]
[ 0, 1, 0, 0, 0 ]
[ 0, 1, 1, 0, 0 ]
[ 0, 1, 0, 0, 0 ]


Output: 12
Explanation: The boundary of the island constitute 12 sides."""


def find_island_perimeter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # only if the cell is a land and not visited
            if matrix[i][j] == 1 and not visited[i][j]:
                return island_perimeter_dfs(matrix, visited, i, j)
    return 0


def island_perimeter_dfs(matrix, visited, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 1  # return 1 since this is a boundary cell
    if matrix[x][y] == 0:
        return 1  # return 1 since the boundary is a water cell
    if visited[x][y]:
        return 0  # this cell has already been visited

    visited[x][y] = True

    edges = 0

    edges += island_perimeter_dfs(matrix, visited, x + 1, y)
    edges += island_perimeter_dfs(matrix, visited, x - 1, y)
    edges += island_perimeter_dfs(matrix, visited, x, y + 1)
    edges += island_perimeter_dfs(matrix, visited, x, y - 1)

    return edges


def main():
    print(find_island_perimeter([[1, 1, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0]]))

    print(find_island_perimeter([[0, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 1, 0, 0],
                                [0, 1, 1, 0],
                                [0, 1, 0, 0]]))


main()
