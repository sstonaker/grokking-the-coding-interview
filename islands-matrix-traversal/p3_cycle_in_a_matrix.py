"""Problem Statement

You are given a 2D matrix containing different characters, you need to find if
there exists any cycle consisting of the same character in the matrix.

A cycle is a path in the matrix that starts and ends at the same cell and has
four  or more cells. From a given cell, you can move to one of the cells
adjacent to it - in one of the four directions (up, down, left, or right), if
it has the same character value of the current cell.

Write a function to find if the matrix has a cycle.

Example 1
Input: matrix =
[ a, a, a, a]
[ b, a, c, a]
[ b, a, c, a]
[ b, a, a, a]


Output: true
Explanation: The given matrix has a cycle as shown below:
[ a, a--a--a]
[ b, a, c, a]
[ b, a, c, a]
[ b, a--a--a]


Example 2

Input: matrix =
[ a, a, a, a]
[ a, b, b, a]
[ a, b, a, a]
[ a, a, a, c]



Output: true
Explanation: The given matrix has one cycle as shown below:
[ a--a--a--a]
[ a, b, b, a]
[ a, b, a--a]
[ a--a--a, c]


Example 3

Input: matrix =
[ a, b, e, b]
[ b, b, c, b]
[ b, c, c, d]
[ d, c, d, d]


Output: false
Explanation: The given matrix has no cycle."""


def has_cycle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if contains_cycle_dfs(matrix, visited, matrix[i][j],
                                      i, j, -1, -1):
                    return True
    return False


def contains_cycle_dfs(matrix, visited, start, x, y, prev_x, prev_y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False  # not a valid cell
    if matrix[x][y] != start:
        return False  # different char means a different island
    if visited[x][y]:
        return True  # found a cycle by returning to visited char

    visited[x][y] = True

    if x + 1 != prev_x and contains_cycle_dfs(matrix, visited,
                                              start, x + 1, y, x, y):
        return True
    if x - 1 != prev_x and contains_cycle_dfs(matrix, visited,
                                              start, x - 1, y, x, y):
        return True
    if y + 1 != prev_y and contains_cycle_dfs(matrix, visited,
                                              start, x, y + 1, x, y):
        return True
    if y - 1 != prev_y and contains_cycle_dfs(matrix, visited,
                                              start, x, y - 1, x, y):
        return True

    return False


def main():
    print(has_cycle([['a', 'a', 'a', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'a', 'a']]))

    print(has_cycle([['a', 'a', 'a', 'a'],
                    ['a', 'b', 'b', 'a'],
                    ['a', 'b', 'a', 'a'],
                    ['a', 'a', 'a', 'c']]))

    print(has_cycle([['a', 'b', 'e', 'b'],
                    ['b', 'b', 'b', 'b'],
                    ['b', 'c', 'c', 'd'],
                    ['c', 'c', 'd', 'd']]))


main()
