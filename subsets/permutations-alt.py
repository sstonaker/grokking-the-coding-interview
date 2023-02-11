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


def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, current_permutation, result):
    if index == len(nums):
        result.append(current_permutation)
    else:
        for i in range(len(current_permutation) + 1):
            new_permutation = list(current_permutation)
            new_permutation.insert(i, nums[index])
            generate_permutations_recursive(nums, index + 1, new_permutation,
                                            result)


def main():
    print(
        f"Here are all the permutations: {str(generate_permutations([1, 3, 5]))}")


main()
