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


def count_islands_dfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # only if the cell is land
                islands += 1
                visit_islands_dfs(matrix, i, j)
    return islands


def visit_islands_dfs(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return  # return if not a valid cell
    if matrix[x][y] == 0:
        return  # return if a water cell
    matrix[x][y] = 0  # mark visited by making a water cell

    # recursively visit all neighboring cells (horizontally & vertically)
    visit_islands_dfs(matrix, x + 1, y)  # lower cell
    visit_islands_dfs(matrix, x - 1, y)  # upper cell
    visit_islands_dfs(matrix, x, y + 1)  # right cell
    visit_islands_dfs(matrix, x, y - 1)  # left cell


def main():
    print(count_islands_dfs([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(count_islands_dfs([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
