"""Problem Statement

Given an
N*N matrix where each row and column is sorted in ascending order, find the Kth
smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
  ],
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7."""


from heapq import heappop, heappush


def find_Kth_smallest(matrix, k):
    min_heap = []
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))
    number_count, number = 0, 0
    while min_heap:
        number, i, row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(row) > i + 1:
            heappush(min_heap, (row[i + 1], i + 1, row))
    return number


def main():
    print(
        f"Kth smallest number is: {str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))}")


main()
