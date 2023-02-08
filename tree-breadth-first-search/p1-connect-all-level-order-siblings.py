"""Problem Statement

Given a binary tree, connect each node with its level order successor. The last
node of each level should point to the first node of the next level."""


from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end="")
        current = self
        while current:
            print(str(current.value) + " ", end="")
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    q = deque()
    q.append(root)
    current_node, previous_node = None, None

    while q:
        current_node = q.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node

        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
