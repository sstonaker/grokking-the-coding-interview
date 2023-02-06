"""Problem Statement

Given an unsorted array containing numbers and a number `k`, find the first `k`
missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2."""


def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()

    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])

    # add remaining missing numbers
    i = 1
    while len(missing_numbers) < k:
        candidate = i + n
        # ignore if th array contains candidate
        if candidate not in extra_numbers:
            missing_numbers.append(candidate)
        i += 1

    return missing_numbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
