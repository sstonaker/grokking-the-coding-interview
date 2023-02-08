"""Problem Statement

Given a binary tree and a node, find the level order successor of the given
node in the tree. The level order successor is the node that appears right
after the given node in the level order traversal."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_successor(root, key):
    if root is None:
        return None

    q = deque()
    q.append(root)

    while q:
        current_node = q.popleft()
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)

        if current_node.value == key:
            break

    return q[0] if q else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.value)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.value)

    result = find_successor(root, 12)
    if result:
        print(result.value)


main()
