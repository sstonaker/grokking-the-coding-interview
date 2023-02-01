"""Problem Statement

Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all
instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be
[2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""


def remove_element(arr, key):
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1
    return next_element


print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], key=3))
print(remove_element([2, 11, 2, 2, 1], key=2))
