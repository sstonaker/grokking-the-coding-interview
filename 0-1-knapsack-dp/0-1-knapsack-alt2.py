"""Introduction

Given the weights and profits of `N` items, we are asked to put these items in
a knapsack with a capacity `C.` The goal is to get the maximum profit out of
the knapsack items. Each item can only be selected once, as we don`t have
multiple quantities of any item.

Let`s take Merry`s example, who wants to carry some fruits in the knapsack to
get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Le``s try to put various combinations of fruits in the knapsack, such that
their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the
maximum profit, and the total weight does not exceed the capacity.

Problem Statement

Given two integer arrays to represent weights and profits of `N` items, we need
to find a subset of these items which will give us maximum profit such that
their cumulative weight is not more than a given number `C.` Each item can only
be selected once, which means either we put an item in the knapsack or we skip
it.

Bottom-up Dynamic Programming

Let`s try to populate our dp[][] array from the above solution by working in a
bottom-up fashion. Essentially, we want to find the maximum profit for every
sub-array and every possible capacity. This means that dp[i][c] will represent
the maximum knapsack profit for capacity `c` calculated from the first `i`
items.

So, for each item at index `i` (0 <= i < items.length) and capacity `c` (0 <= c
<= capacity), we have two options:

Exclude the item at index `i.` In this case, we will take whatever profit we
get from the sub-array excluding this item => dp[i-1][c]
Include the item at index `i` if its weight is not more than the capacity. In
this case, we include its profit plus whatever profit we get from the remaining
capacity and from remaining items => profit[i] + dp[i-1][c-weight[i]]
Finally, our optimal solution will be maximum of the above two values:

    dp[i][c] = max (dp[i-1][c], profit[i] + dp[i-1][c-weight[i]])"""


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
