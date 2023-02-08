"""Problem Statement

Given a binary tree, populate an array to represent its level-by-level
traversal. You should populate the values of all nodes of each level from left
to right in separate sub-arrays."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse(root):
    result = []
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

        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)  # type:ignore
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
