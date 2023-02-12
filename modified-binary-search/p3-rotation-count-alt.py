"""Problem 1

How do we find the rotation count of a sorted and rotated array that has
duplicates too?

The above code will fail on the following example!

Example 1:

Input: [3, 3, 7, 3]
Output: 3
Explanation: The array has been rotated 3 times."""


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1

        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:
                return end
            end -= 1

        elif arr[start] < arr[mid] or arr[start] == arr[mid] and arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


def main():
    print(count_rotations_with_duplicates([10, 15, 1, 3, 8]))
    print(count_rotations_with_duplicates([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations_with_duplicates([1, 3, 8, 10]))


main()
