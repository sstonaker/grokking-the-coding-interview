"""Problem Statement

Given `M` sorted arrays, find the smallest range that includes at least one
number from each of the `M` lists.

Example 1:

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
Example 2:

Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
"""

import math
from heapq import heappop, heappush


def find_smallest_range(lists):
    min_heap = []
    range_start, range_end = 0, math.inf
    current_max_number = -math.inf

    for arr in lists:
        heappush(min_heap, (arr[0], 0, arr))
        current_max_number = max(current_max_number, arr[0])

    while len(min_heap) == len(lists):
        num, i, arr = heappop(min_heap)
        if range_end - range_start > current_max_number - num:
            range_start = num
            range_end = current_max_number

        if len(arr) > i + 1:
            heappush(min_heap, (arr[i + 1], i + 1, arr))
            current_max_number = max(current_max_number, arr[i + 1])
    return [range_start, range_end]


def main():
    print(
        f"Smallest range is: {str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))}")


main()
