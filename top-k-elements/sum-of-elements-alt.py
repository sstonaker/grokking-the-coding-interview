"""Alternate Solution

We can iterate the array and use a max-heap to keep track of the top K2
numbers. We can, then, add the top K2-K1-1 numbers in the max-heap to find the
sum of all numbers coming between the K1`th and K2`th smallest numbers. Here is
what the algorithm will look like:
"""


from heapq import heappop, heappush


def find_sum_of_elements(nums, k1, k2):
    maxHeap = []
    # keep smallest k2 numbers in the max heap
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(maxHeap, -nums[i])
        elif nums[i] < -maxHeap[0]:
            # as we are interested only in the smallest k2 numbers
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    # get the sum of numbers between k1 and k2 indices
    # these numbers will be at the top of the max heap
    elementSum = 0
    for _ in range(k2 - k1 - 1):
        elementSum += -heappop(maxHeap)

    return elementSum


def main():

    print(f"Sum of all numbers between k1 and k2 smallest numbers: \
        {str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))}")
    print(f"Sum of all numbers between k1 and k2 smallest numbers: \
        {str(find_sum_of_elements([3, 5, 8, 7], 1, 4))}")


main()
