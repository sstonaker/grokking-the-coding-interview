"""Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
find the biggest island in it. Write a function to return the area of the
biggest island.

An island is a connected set of 1s (land) and is surrounded by either an edge
or 0s (water). Each cell is considered connected to other cells horizontally
or vertically (not diagonally).

Example 1

Input: matrix =
[ 1, 1, 1, 0, 0 ]
[ 0, 1, 0, 0, 1 ]
[ 0, 0, 1, 1, 0 ]
[ 0, 1, 1, 0, 0 ]
[ 0, 0, 1, 0, 0 ]


Output: 5
Explanation: The matrix has three islands. The biggest island has 5 cells .
"""


def max_island_area_dfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggest_island = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # only if the cell is land
                biggest_island = max(
                    biggest_island, visit_islands_dfs(matrix, i, j))
    return biggest_island


def visit_islands_dfs(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 0  # return if not a valid cell
    if matrix[x][y] == 0:
        return 0  # return if a water cell
    matrix[x][y] = 0  # mark visited by making a water cell

    area = 1  # count the current cell
    # recursively visit all neighboring cells (horizontally & vertically)
    area += visit_islands_dfs(matrix, x + 1, y)  # lower cell
    area += visit_islands_dfs(matrix, x - 1, y)  # upper cell
    area += visit_islands_dfs(matrix, x, y + 1)  # right cell
    area += visit_islands_dfs(matrix, x, y - 1)  # left cell
    return area


def main():
    print(max_island_area_dfs([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
