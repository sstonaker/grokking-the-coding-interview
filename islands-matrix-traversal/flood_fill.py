"""Problem Statement

Any image can be represented by a 2D integer array (i.e., a matrix) where each
cell represents the pixel value of the image.

Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The
given color is applied to all horizontally and vertically connected cells with
the same color as that of the starting cell. Recursively, the algorithm fills
cells with the new color until it encounters a cell with a different color than
the starting cell.

Given a matrix, a starting cell, and a color, flood fill the matrix.

Example 1

Input: matrix =
[ 0, 1, 1, 1, 0 ]
[ 0, 0, 0, 1, 1 ]
[ 0, 1, 1, 1, 0 ]
[ 0, 1, 1, 0, 0 ]
[ 0, 0, 0, 0, 0 ]



    starting cell = (1, 3)
    new color = 2
Output:
[ 0, 2, 2, 2, 0 ]
[ 0, 0, 0, 2, 2 ]
[ 0, 2, 2, 2, 0 ]
[ 0, 2, 2, 0, 0 ]
[ 0, 0, 0, 0, 0 ]

Example 2

Input: matrix =
[ 0, 0, 0, 0, 0 ]
[ 0, 0, 0, 0, 0 ]
[ 0, 0, 1, 1, 0 ]
[ 0, 0, 1, 0, 0 ]
[ 0, 0, 1, 0, 0 ]


    starting cell = (3, 2)
    new color = 5
Output:
[ 0, 0, 0, 0, 0 ]
[ 0, 0, 0, 0, 0 ]
[ 0, 0, 5, 5, 0 ]
[ 0, 0, 5, 0, 0 ]
[ 0, 0, 5, 0, 0 ]
"""


def flood_fill(matrix, x, y, new_color):
    if matrix[x][y] != new_color:
        fill_dfs(matrix, x, y, matrix[x][y], new_color)
    return matrix


def fill_dfs(matrix, x, y, old_color, new_color):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return  # return if not a valid ell
    if matrix[x][y] != old_color:
        return  # return if it is not the required color

    matrix[x][y] = new_color

    # recursively visit all neighboring cells (horizontally & vertically)
    fill_dfs(matrix, x + 1, y, old_color, new_color)  # lower cell
    fill_dfs(matrix, x - 1, y, old_color, new_color)  # upper cell
    fill_dfs(matrix, x, y + 1, old_color, new_color)  # right cell
    fill_dfs(matrix, x, y - 1, old_color, new_color)  # left cell


def main():
    print(flood_fill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))
    print(flood_fill([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


main()
