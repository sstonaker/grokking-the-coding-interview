"""Problem Statement

Given a binary tree where each node can only have a digit (0-9) value, each
root-to-leaf path will represent a number. Find the total sum of all the
numbers represented by all paths."""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(current_node, path_sum):
    if current_node is None:
        return 0

    path_sum = 10 * path_sum + current_node.val

    if current_node.left is None and current_node.right is None:
        return path_sum

    return find_root_to_leaf_path_numbers(current_node.left, path_sum) + \
        find_root_to_leaf_path_numbers(current_node.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
