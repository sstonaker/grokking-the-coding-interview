"""Problem Statement

Given a set of numbers that might contain duplicates, find all of its distinct
subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3],
[3,3,5], [1,5,3,3] """


def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    start, end = 0, 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
