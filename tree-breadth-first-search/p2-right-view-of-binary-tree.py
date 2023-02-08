"""Problem Statement

Given a binary tree, return an array containing nodes in its right view. The
right view of a binary tree is the set of nodes visible when the tree is seen
from the right side."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_right_view(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)

    while q:
        level_size = len(q)
        for i in range(level_size):
            current_node = q.popleft()
            if i == level_size - 1:
                result.append(current_node)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.value) + " ", end='')


main()
