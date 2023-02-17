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
        self.stack = multiprocessing.Manager().list()
        self.lock = multiprocessing.Lock()
        self.t1 = None
        self.traverseLeft(self.stack, root)

    # returns whether we have a next smallest number
    def hasNext(self):
        self.checkThread()
        return self.stack

    # returns the next smallest number
    def next(self):
        self.lock.acquire()
        self.checkThread()
        tmpNode = self.stack.pop()
        self.t1 = multiprocessing.Process(
            target=self.traverseLeft, args=(self.stack, tmpNode.right))
        self.t1.start()
        self.lock.release()
        return tmpNode.val

    # traverse the left sub-tree to push all nodes on the stack
    def traverseLeft(self, stack, node):
        while node is not None:
            stack.append(node)
            node = node.left

    # if the previous thread is active, wait before it finishes
    def checkThread(self):
        if self.t1 is not None and self.t1.is_alive():
            self.t1.join()  # wait for the thread traversing the left subtree


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
