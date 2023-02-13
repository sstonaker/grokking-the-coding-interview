"""Problem Statement

Given an unsorted array of numbers, find the top `K` frequently occurring
numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' appeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once."""


from heapq import heappop, heappush


def find_k_frequent_numbers(nums, k):
    num_frequency_map = {}
    for num in nums:
        num_frequency_map[num] = num_frequency_map.get(num, 0) + 1

    min_heap = []

    for num, frequency in num_frequency_map.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)

    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])
    return top_numbers


def main():

    print(
        f"Here are the K frequent numbers: {str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))}")

    print(
        f"Here are the K frequent numbers: {str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2))}")


main()
