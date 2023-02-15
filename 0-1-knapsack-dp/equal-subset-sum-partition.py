"""Statement

Given a set of positive numbers, find if we can partition it into two subsets
such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum:
{1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum:
{1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal
sum."""


def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False

    return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, sum, current_index):
    if sum == 0:
        return True

    n = len(num)
    if n == 0 or current_index >= n:
        return False

    if num[current_index] <= sum:
        if can_partition_recursive(num, sum - num[current_index], current_index + 1):
            return True
    return can_partition_recursive(num, sum, current_index + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
