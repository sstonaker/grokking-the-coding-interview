"""Problem Statement

Given the roots of two binary trees 'p' and 'q', write a function to check if they are the same or not.

Two binary trees are considered the same if they met following two conditions:

Both tree are structurally identical.
Each corresponding node on both the trees have the same value.
Example 1:


Given the following two binary trees:

Output: true

Explanation: Both trees are structurally identical and have same values.
Example 2:


Given the following two binary trees:

Output: false

Explanation: Trees are structurally different.
Example 3:


Given the following two binary trees:

Output: false

Explanation: Corresponding nodes have different value ( 4 & 9 )."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = list()
        self.traverse_left(root)

    def has_next(self):
        return self.stack

    def next(self):
        temp_node = self.stack.pop()
        self.traverse_left(temp_node.right)
        return temp_node.val

    def traverse_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


def main():
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(15)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(19)
    root.right.right.right = TreeNode(20)

    itr = BSTIterator(root)
    print("hasNext() -> " + str(bool(itr.has_next())))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("hasNext() -> " + str(bool(itr.has_next())))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("hasNext() -> " + str(bool(itr.has_next())))


main()
