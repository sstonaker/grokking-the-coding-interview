"""Problem Statement

Given an array of sorted numbers and a target sum, find a pair in the array
whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such
that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11"""


def pair_with_target_sum(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] + array[right] == target:
            return left, right
        elif array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] > target:
            right -= 1


print(pair_with_target_sum([1, 2, 3, 4, 6], target=6))
print(pair_with_target_sum([2, 5, 9, 11], target=11))
