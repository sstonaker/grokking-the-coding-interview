"""Problem Statement

Given a sorted array, create a new array containing squares of all the numbers
of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]"""


def square_sorted_array(arr):
    left, right = 0, len(arr) - 1
    high = len(arr) - 1
    squares = [0 for x in range(len(arr))]
    while left <= right:
        l_square = arr[left] * arr[left]
        r_square = arr[right] * arr[right]
        if l_square > r_square:
            squares[high] = l_square
            left += 1
        else:
            squares[high] = r_square
            right -= 1
        high -= 1
    return squares


print(square_sorted_array([-2, -1, 0, 2, 3]))
print(square_sorted_array([-3, -1, 0, 1, 2]))
