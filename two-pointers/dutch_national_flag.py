"""Problem Statement

Given an array containing 0s, 1s and 2s, sort the array in-place. You should
treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to
recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and
since our input array also consists of three different numbers that is why it
is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]"""


def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low and < i are 1
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            # decrement high only
            # after the swap, the number at index i could be 0, 1, or 2
            high -= 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
