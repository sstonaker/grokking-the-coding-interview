"""Problem Statement

Given a binary tree and a number sequence, find if the sequence is present as a
root-to-leaf path in the given tree."""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, sequence_index):
    if current_node is None:
        return False

    sequence_length = len(sequence)
    if sequence_index >= sequence_length or \
            current_node.val != sequence[sequence_index]:
        return False

    if current_node.left is None and current_node.right is None and \
            sequence_index == sequence_length - 1:
        return True

    return find_path_recursive(current_node.left, sequence,
                               sequence_index + 1) or \
        find_path_recursive(current_node.right, sequence, sequence_index + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
