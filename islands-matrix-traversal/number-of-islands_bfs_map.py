"""Problem Statement

Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
count the number of islands in it.

An island is a connected set of 1s (land) and is surrounded by either an edge
or 0s (water). Each cell is considered connected to other cells horizontally or
vertically (not diagonally).

Example 1

Input: matrix =
[ 0, 1, 1, 1, 0 ]
[ 0, 0, 0, 1, 1 ]
[ 0, 1, 1, 1, 0 ]
[ 0, 1, 1, 0, 0 ]
[ 0, 0, 0, 0, 0 ]


Output: 1
Explanation: The matrix has only one island. See the highlighted cells below.

Example 2

Input: matrix =
[ 1, 1, 1, 0, 0 ]
[ 0, 1, 0, 0, 1 ]
[ 0, 0, 1, 1, 0 ]
[ 0, 0, 1, 0, 0 ]
[ 0, 0, 1, 0, 0 ]

Output: 3
Explanation: The matrix has three islands. See the highlighted cells below.
"""
from collections import deque


def count_islands_bfs_map(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0
    visited = [[False for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # if the cell is land and not visited
            if matrix[i][j] == 1 and not visited[i][j]:
                islands += 1
                visit_islands_bfs(matrix, visited, i, j)
    return islands


def visit_islands_bfs(matrix, visited, x, y):
    neighbors = deque([(x, y)])
    while neighbors:
        row, col = neighbors.popleft()
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue  # continue if it is not a valid cell
        if matrix[row][col] == 0 or visited[row][col]:
            continue  # continue if it is a water cell
        visited[row][col] = True  # mark visited

        # insert all neighboring cells to the queue for BFS
        neighbors.extend([(row + 1, col)])  # lower cell
        neighbors.extend([(row - 1, col)])  # upper cell
        neighbors.extend([(row, col + 1)])  # right cell
        neighbors.extend([(row, col - 1)])  # left cell


def main():
    print(count_islands_bfs_map([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(count_islands_bfs_map([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
