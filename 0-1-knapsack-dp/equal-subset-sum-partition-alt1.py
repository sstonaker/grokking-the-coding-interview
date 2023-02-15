"""Statement

Given a set of positive numbers, find if we can partition it into two subsets
such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum:
{1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum:
{1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal
sum.


Top-down Dynamic Programming with Memoization

We can use memoization to overcome the overlapping sub-problems. As stated in
previous lessons, memoization is when we store the results of all the
previously solved sub-problems so we can return the results from memory if we
encounter a problem that has already been solved.

Since we need to store the results for every subset and for every possible sum,
therefore we will be using a two-dimensional array to store the results of the
solved sub-problems. The first dimension of the array will represent different
subsets and the second dimension will represent different `sums` that we can
calculate from each subset. These two dimensions of the array can also be
inferred from the two changing values (sum and currentIndex) in our recursive
function canPartitionRecursive()."""


def can_partition(num):
    s = sum(num)

    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(int(s / 2) + 1)] for y in range(len(num))]
    return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
    # base check
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # if we have not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        if num[currentIndex] <= sum:
            if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) \
                    == 1:
                dp[currentIndex][sum] = 1
                return 1

        # recursive call after excluding the number at the currentIndex
        dp[currentIndex][sum] = can_partition_recursive(
            dp, num, sum, currentIndex + 1)

    return dp[currentIndex][sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
