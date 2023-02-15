"""Problem Statement

You are given a set of positive numbers and a target sum `S`. Each number
should be assigned either a `+` or `-` sign. We need to find the total ways to
assign symbols to make the sum of the numbers equal to the target `S`.

Example 1: #
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} &
{-1+1-2+3} & {+1+1+2-3}
Example 2: #
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} &
{-1+2+7+1}"""


def find_target_subsets(num, s):
    totalSum = sum(num)

    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum)/2'
    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0

    return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem
def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to
    # the number
    for s in range(1, sum + 1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]

    return dp[sum]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
