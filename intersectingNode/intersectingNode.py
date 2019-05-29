from __future__ import print_function, division


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def length(head):
    if not head:
        return 0
    return 1 + length(head.next)


def intersection(a, b):
    m, n = length(a), length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m - n):
            cur_a = cur_a.next
    else:
        for _ in range(n - m):
            cur_b = cur_b.next

    while cur_a.val != cur_b.val:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a


if __name__ == "__main__":
    headA = Node(3, Node(7, Node(8, Node(10))))
    headB = Node(99, Node(1, Node(8, Node(10))))
    print(intersection(headB, headA))
