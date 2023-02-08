"""Problem Statement

Given a binary tree, populate an array to represent the averages of all of its
levels."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_level_averages(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)

    while q:
        level_size = len(q)
        level_sum = 0
        for _ in range(level_size):
            current_node = q.popleft()
            level_sum += current_node.value

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

        result.append(level_sum / level_size)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
