"""Problem Statement

Given a binary tree and a number `S`, find all paths in the tree such that the
sum of all the node values of each path equals `S`. Please note that the paths
can start or end at any node but all paths must follow direction from parent to
child (top to bottom)."""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, s):
    return count_paths_recursive(root, s, [])


def count_paths_recursive(current_node, s, current_path):
    if current_node is None:
        return 0

    current_path.append(current_node.val)
    path_count, path_sum = 0, 0
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        if path_sum == s:
            path_count += 1

    path_count += count_paths_recursive(current_node.left, s, current_path)
    path_count += count_paths_recursive(current_node.right, s, current_path)

    del current_path[-1]
    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
