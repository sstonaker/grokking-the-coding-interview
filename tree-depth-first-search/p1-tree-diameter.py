"""Problem Statement

Given a binary tree, find the length of its diameter. The diameter of a tree is
the number of nodes on the longest path between any two leaf nodes. The
diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given
tree."""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def __init__(self):
        self.tree_diameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.tree_diameter

    def calculate_height(self, current_node):
        if current_node is None:
            return 0

        left_tree_height = self.calculate_height(current_node.left)
        right_tree_height = self.calculate_height(current_node.right)

        if left_tree_height != 0 and right_tree_height != 0:
            diameter = left_tree_height + right_tree_height + 1
            self.tree_diameter = max(self.tree_diameter, diameter)
        return max(left_tree_height, right_tree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
