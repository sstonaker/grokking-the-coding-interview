"""Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge
or 0s (water). Each cell is considered connected to other cells horizontally
or vertically (not diagonally).

Two islands are considered the same if and only if they can be translated (not
rotated or reflected) to equal each other.

Write a function to find the number of distinct islands in the given matrix.

Example 1

Input: matrix =
[ 1, 1, 0, 1, 1 ]
[ 1, 1, 0, 1, 1 ]
[ 0, 0, 0, 0, 0 ]
[ 0, 1, 1, 0, 1 ]
[ 0, 1, 1, 0, 1 ]


Output: 2
Explanation: There are four islands in the given matrix, but three of them are
the same; hence, there are only two distinct islands.

Example 2

Input: matrix =
[ 1, 1, 0, 1]
[ 0, 1, 1, 0]
[ 0, 0, 0, 0]
[ 1, 1, 0, 0]
[ 0, 1, 1, 0]


Output: 2
Explanation: There are three islands in the given matrix, but two of them are
the same; hence, there are only two distinct islands."""


def find_distinct_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    island_set = set()

    for i in range(rows):
        for j in range(cols):
            # only if the cell is land and not visited
            if matrix[i][j] == 1 and not visited[i][j]:
                traversal = traverse_island_dfs(matrix, visited, i, j, "O")
                island_set.add(traversal)

    return len(island_set)


def traverse_island_dfs(matrix, visited, x, y, direction):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return ""  # return if not a valid cell
    if matrix[x][y] == 0 or visited[x][y]:
        return ""  # return if water or is visited

    visited[x][y] = True  # mark the cell as visited

    island_traversal = direction
    island_traversal += traverse_island_dfs(matrix, visited, x + 1, y, "D")
    island_traversal += traverse_island_dfs(matrix, visited, x - 1, y, "U")
    island_traversal += traverse_island_dfs(matrix, visited, x, y + 1, "R")
    island_traversal += traverse_island_dfs(matrix, visited, x, y - 1, "L")
    island_traversal += "B"  # back
    return island_traversal


def main():
    print(find_distinct_islands([[1, 1, 0, 1, 1],
                                [1, 1, 0, 1, 1],
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 1],
                                [0, 1, 1, 0, 1]]))

    print(find_distinct_islands([[1, 1, 0, 1],
                                [0, 1, 1, 0],
                                [0, 0, 0, 0],
                                [1, 1, 0, 0],
                                [0, 1, 1, 0]]))


main()
