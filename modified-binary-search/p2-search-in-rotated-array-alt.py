"""Problem Statement

Given an array of numbers which is sorted in ascending order and also rotated
by some arbitrary number, find if a given `key` is present in it.

Write a function to return the index of the `key` in the rotated array. If the
`key` is not present, return -1.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'."""


def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1
        elif arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def main():
    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()
