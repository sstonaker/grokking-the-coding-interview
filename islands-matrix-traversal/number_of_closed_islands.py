"""Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge
or 0s (water). Each cell is considered connected to other cells horizontally or
vertically (not diagonally).

A closed island is an island that is totally surrounded by 0s (i.e., water).
This means all horizontally and vertically connected cells of a closed island
are water. This also means that, by definition, a closed island can't touch an
edge (as then the edge cells are not connected to any water cell).

Write a function to find the number of closed islands in the given matrix.

Example 1

Input: matrix =



Output: 1
Explanation: The given matrix has two islands, but only the highlighted island
is a closed island. The other island is touching the boundary that's why is is
not considered a closed island.

Example 2

Input: matrix =



Output: 2
Explanation: The given matrix has two islands and both of them are closed
islands."""


def closed_island_count_dfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    closed_island_count = 0

    for i in range(rows):
        for j in range(cols):
            # only if the cell is land and not visited
            if matrix[i][j] == 1 and not visited[i][j]:
                if is_closed_island_dfs(matrix, visited, i, j):
                    closed_island_count += 1
    return closed_island_count


def is_closed_island_dfs(matrix, visited, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False  # is touching an edge
    if matrix[x][y] == 0 or visited[x][y]:
        return True  # is surrounded by water

    visited[x][y] = True  # mark as visited
    is_closed = True
    # recursively visit all neighbors horizontally & vertically
    is_closed &= is_closed_island_dfs(matrix, visited, x + 1, y)  # lower cell
    is_closed &= is_closed_island_dfs(matrix, visited, x - 1, y)  # lower cell
    is_closed &= is_closed_island_dfs(matrix, visited, x, y + 1)  # lower cell
    is_closed &= is_closed_island_dfs(matrix, visited, x, y - 1)  # lower cell
    return is_closed


def main():
    print(closed_island_count_dfs([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))

    print(closed_island_count_dfs([[0, 0, 0, 0], [0, 1, 0, 0], [
        0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))


main()
