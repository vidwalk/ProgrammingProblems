from __future__ import print_function, division


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head, k):
    slow, fast = head, head
    for i in range(k):
        fast = fast.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(head)
    remove_kth_from_linked_list(head, 3)
    print(head)
