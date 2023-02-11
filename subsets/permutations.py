"""Problem Statement

Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For
example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has `n` distinct elements it will have
n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]"""


from collections import deque


def find_permutations(nums):
    nums_length = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for current_number in nums:
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, current_number)
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    return result


def main():
    print(
        f"Here are all the permutations: {str(find_permutations([1, 3, 5]))}")


main()
