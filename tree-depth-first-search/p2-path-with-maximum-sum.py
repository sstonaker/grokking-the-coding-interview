"""Problem Statement

Find the path with the maximum sum in a given binary tree. Write a function
that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn't
necessarily pass through the root. The path must contain at least one node."""


import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:

    def find_maximum_path_sum(self, root):
        self.global_maximum_sum = -math.inf
        self.find_maximum_path_sum_recursive(root)
        return self.global_maximum_sum

    def find_maximum_path_sum_recursive(self, current_node):
        if current_node is None:
            return 0

        max_path_sum_from_left = self.find_maximum_path_sum_recursive(
            current_node.left)
        math_path_sum_from_right = self.find_maximum_path_sum_recursive(
            current_node.right)

        # ignore paths with negative sums, since we need to find the maximum
        # sum we should ignore any path which has an overall negative sum.
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        math_path_sum_from_right = max(math_path_sum_from_right, 0)

        # maximum path sum at the current node will be equal to the sum from
        # the left subtree + the sum from right subtree + val of current node
        local_maximum_sum = max_path_sum_from_left + \
            math_path_sum_from_right + current_node.val

        # update the global maximum sum
        self.global_maximum_sum = max(
            self.global_maximum_sum, local_maximum_sum)

        # maximum sum of any path from the current node will be equal to the
        # maximum of the sums from left or right subtrees plus the value of the
        # current node
        return max(max_path_sum_from_left, math_path_sum_from_right) + \
            current_node.val


def main():
    max_path_sum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))


main()
