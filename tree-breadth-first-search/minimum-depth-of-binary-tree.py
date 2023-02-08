"""Problem Statement

Find the minimum depth of a binary tree. The minimum depth is the number of
nodes along the shortest path from the root node to the nearest leaf node."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_minimum_depth(root):
    if root is None:
        return 0

    q = deque()
    q.append(root)
    min_depth = 0

    while q:
        min_depth += 1
        level_size = len(q)
        for _ in range(level_size):
            current_node = q.popleft()

            if not current_node.left and not current_node.right:
                return min_depth

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
