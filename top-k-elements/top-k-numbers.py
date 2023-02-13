"""Problem Statement

Given an unsorted array of numbers, find the `K` largest numbers in it.

Note: For a detailed discussion about different approaches to solve this
problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]"""


from heapq import heappop, heappush


def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    return min_heap


def main():

    print(
        f"Here are the top K numbers: {str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))}")

    print(
        f"Here are the top K numbers: {str(find_k_largest_numbers([5, 12, 11, -1, 12], 3))}")


main()
