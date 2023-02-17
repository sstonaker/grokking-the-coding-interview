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


import multiprocessing


# definition for a binary search tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = list()
        self.lock = multiprocessing.Lock()
        self.traverseLeft(root)

    # returns whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # returns the next smallest number
    def next(self):
        self.lock.acquire()
        tmpNode = self.stack.pop()
        self.traverseLeft(tmpNode.right)
        self.lock.release()
        return tmpNode.val

    # traverse the left sub-tree to push all nodes on the stack
    def traverseLeft(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


if __name__ == '__main__':

    root = TreeNode(10)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right = TreeNode(15)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(19)
    root.right.right.right = TreeNode(20)

    itr = BSTIterator(root)
    print("hasNext() -> " + str(bool(itr.hasNext())))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("hasNext() -> " + str(bool(itr.hasNext())))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("next() -> " + str(itr.next()))
    print("hasNext() -> " + str(bool(itr.hasNext())))
