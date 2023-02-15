"""Problem Statement

Given two sorted arrays in descending order, find `K` pairs with the largest
sum where each pair consists of numbers from both the arrays.

Example 1:

Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6]
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger
than any of these.
Example 2:

Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]"""


from heapq import heappush, heapreplace


def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heapreplace(min_heap, (nums1[i] + nums2[j], i, j))
    result = []
    for _, i, j in min_heap:
        result.append([nums1[i], nums2[j]])

    return result


def main():
    print(
        f"Pairs with largest sum are: {str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))}")


main()
