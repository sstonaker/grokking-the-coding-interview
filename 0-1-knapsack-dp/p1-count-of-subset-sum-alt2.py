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


Bottom-up Dynamic Programming

We will try to find if we can make all possible sums with every subset to populate the array db[TotalNumbers][S+1].

So, at every step we have two options:

Exclude the number. Count all the subsets without the given number up to the
given sum => dp[index-1][sum]
Include the number if its value is not more than the `sum`. In this case, we
will count all the subsets to get the
remaining sum => dp[index-1][sum-num[index]]"""


def count_subsets(num, sum):
    n = len(num)
    dp = [[-1 for x in range(sum + 1)] for y in range(n)]

    # populate the sum = 0 columns, as we will always have an empty set for zero sum
    for i in range(0, n):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for s in range(1, sum + 1):
        dp[0][s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, sum + 1):
            # exclude the number
            dp[i][s] = dp[i - 1][s]
            # include the number, if it does not exceed the sum
            if s >= num[i]:
                dp[i][s] += dp[i - 1][s - num[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
