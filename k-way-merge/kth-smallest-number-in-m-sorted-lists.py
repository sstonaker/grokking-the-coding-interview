"""Problem Statement

Given `M` sorted arrays, find the K`th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be
verified from
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7."""

from heapq import heappop, heappush


def find_Kth_smallest(lists, k):
    min_heap = []

    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    number_count, number = 0, 0
    while min_heap:
        number, i, list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(list) > i + 1:
            heappush(min_heap, (list[i + 1], i + 1, list))
    return number


def main():
    print(
        f"Kth smallest number is: {str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))}")


main()
