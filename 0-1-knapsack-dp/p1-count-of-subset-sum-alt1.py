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


Top-down Dynamic Programming with Memoization

We can use memoization to overcome the overlapping sub-problems. We will be
using a two-dimensional array to store the results of solved sub-problems. As
mentioned above, we need to store results for every subset and for every
possible sum."""


def count_subsets(num, sum):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return count_subsets_recursive(dp, num, sum, 0)


def count_subsets_recursive(dp, num, sum, currentIndex):
    # base checks
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # check if we have not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        sum1 = 0
        if num[currentIndex] <= sum:
            sum1 = count_subsets_recursive(
                dp, num, sum - num[currentIndex], currentIndex + 1)

        # recursive call after excluding the number at the currentIndex
        sum2 = count_subsets_recursive(dp, num, sum, currentIndex + 1)

        dp[currentIndex][sum] = sum1 + sum2

    return dp[currentIndex][sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
