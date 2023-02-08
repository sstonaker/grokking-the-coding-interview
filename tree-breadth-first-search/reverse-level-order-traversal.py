"""Problem Statement

Given a binary tree, populate an array to represent its level-by-level
traversal in reverse order, i.e., the lowest level comes first. You should
populate the values of all nodes in each level from left to right in separate
sub-arrays."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse(root):
    result = deque()
    if root is None:
        return result

    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            current_node = q.popleft()
            current_level.append(current_node.value)

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

        result.appendleft(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
