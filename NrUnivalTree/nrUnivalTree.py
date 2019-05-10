from __future__ import division, print_function


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_unival_subtrees(root):
    count, _ = helper(root)
    return count


def helper(root):
    """
    Also returns number of unival subtrees, and whether it is itself a unival subtree.
    """
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False


if __name__ == "__main__":
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    """
      0
     / \
    1   0
       / \
      1   0
     / \
    1   1
    """
    print(count_unival_subtrees(node))
