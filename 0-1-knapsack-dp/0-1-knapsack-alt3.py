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

How can we find the selected items?
As we know, the final profit is at the bottom-right corner. Therefore, we will
start from there to find the items that will be going into the knapsack.

As you remember, at every step, we had two options: include an item or skip it.
If we skip an item, we take the profit from the remaining items (i.e., from the
cell right above it); if we include the item, then we jump to the remaining
profit to find more items.

Let`s understand this from the above example:


`22` did not come from the top cell (which is 17); hence we must include the
item at index `3` (which is item `D`).
Subtract the profit of item `D` from `22` to get the remaining profit `6`. We
then jump to profit `6` on the same row.
`6` came from the top cell, so we jump to row `2`.
Again, `6` came from the top cell, so we jump to row `1`.
`6` is different from the top cell, so we must include this item (which is item
`B`).
Subtract the profit of `B` from `6` to get profit `0`. We then jump to profit
`0` on the same row. As soon as we hit zero remaining profit, we can finish our
item search.
Thus, the items going into the knapsack are {B, D}.
Let`s write a function to print the set of items included in the knapsack:
"""


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

    print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


def main():
    print(
        f"Total knapsack profit: {str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))}")
    print(
        f"Total knapsack profit: {str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))}")


main()
