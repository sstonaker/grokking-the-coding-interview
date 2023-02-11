"""Problem Statement

Given a number `n`, write a function to return all structurally unique Binary
Search Trees (BST) that can store values 1 to `n`?

Example 1:

Input: 2
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1
to 2:

Example 2:

Input: 3
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1
to 3:"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_recursive(1, n)


def find_unique_trees_recursive(start, end):
    result = []
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_subtrees = find_unique_trees_recursive(start, i - 1)
        right_subtrees = find_unique_trees_recursive(i + 1, end)
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root = TreeNode(i, left_tree, right_tree)
                result.append(root)
    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
