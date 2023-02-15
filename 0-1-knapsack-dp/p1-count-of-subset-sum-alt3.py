"""Problem Challenge 1: Count of Subset Sum (hard)


Problem Statement

Given a set of positive numbers, find the total number of subsets whose sum is
equal to a given number `S`.

Example 1: #
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our
input.
Example 2: #
Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}


Challenge

Can we improve our bottom-up DP solution even further? Can you find an
algorithm that has
O(S) space complexity?

Similar to the space optimized solution for 0/1 Knapsack!"""


def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal
    # to the number
    for s in range(1, sum + 1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]

    return dp[sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
