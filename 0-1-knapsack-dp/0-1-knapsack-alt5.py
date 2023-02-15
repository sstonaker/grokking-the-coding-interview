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

The solution above is similar to the previous solution; the only difference is
that we use i%2 instead of i and (i-1)%2 instead of i-1. This solution has a
space complexity of
O(2*C)=O(C), where `C` is the knapsack`s maximum capacity.

This space optimization solution can also be implemented using a single array.
It is a bit tricky, but the intuition is to use the same array for the previous
and the next iteration!

If you see closely, we need two values from the previous iteration: dp[c] and
dp[c-weight[i]]

Since our inner loop is iterating over c:0-->capacity, let`s see how this might
affect our two required values:

When we access dp[c], it has not been overridden yet for the current iteration,
so it should be fine.
dp[c-weight[i]] might be overridden if “weight[i] > 0”. Therefore we can`t use
this value for the current iteration.
To solve the second case, we can change our inner loop to process in the
reverse direction: c:capacity-->0. This will ensure that whenever we change a
value in dp[], we will not need it again in the current iteration.

Can you try writing this algorithm?"""


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for x in range(capacity + 1)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            # exclude the item
            profit2 = dp[c]
            # take maximum
            dp[c] = max(profit1, profit2)

    return dp[capacity]


def main():
    print(
        f"Total knapsack profit: {str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))}")
    print(
        f"Total knapsack profit: {str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))}")


main()
