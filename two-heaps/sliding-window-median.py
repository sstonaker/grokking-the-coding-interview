"""Problem Statement

Given an array of numbers and a number `k`, find the median of all the `k`
sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size `2`:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size `3`:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0"""


from heapq import heapify, heappop, heappush


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for _ in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:  # if we have at least 'k' elements
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = -self.max_heap[0] / \
                        2.0 + self.min_heap[0] / 2.0
                else:
                    result[i - k + 1] = -self.max_heap[0] / 1.0

                element_to_be_removed = nums[i - k + 1]
                if element_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_to_be_removed)
                else:
                    self.remove(self.min_heap, element_to_be_removed)

                self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]

        heapify(heap)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
