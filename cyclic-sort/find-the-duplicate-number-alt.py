"""Problem Statement

We are given an unsorted array containing `n+1` numbers taken from the range 1
to `n`. The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however,
allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4"""


def find_duplicate(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cycle_length = 1
    while current != arr[slow]:
        current = arr[current]
        cycle_length += 1

    return find_start(arr, cycle_length)


def find_start(arr, cycle_length):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer 2 ahead cycle_length steps
    while cycle_length > 0:
        pointer2 = arr[pointer2]
        cycle_length -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
