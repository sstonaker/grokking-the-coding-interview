"""Problem Statement

Given a number `n`, write a function to return the count of structurally unique
Binary Search Trees (BST) that can store values 1 to `n`.

Example 1:

Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing
numbers from 1-2.
Example 2:

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 3.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_trees(n):
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        count_of_left_subtrees = count_trees(i - 1)
        count_of_right_subtrees = count_trees(n - i)
        count += count_of_left_subtrees * count_of_right_subtrees

    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
