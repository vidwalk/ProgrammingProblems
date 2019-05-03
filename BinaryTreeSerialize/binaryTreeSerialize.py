from __future__ import print_function, division

"""This is your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # String representation of the node

    def __str__(self):
        print(self.val, self.left, self.right)

    def AddLeft(self, left):
        self.left = left

    def AddRight(self, right):
        self.right = right

    def PrintTree(self, stringRep):
        # Print the tree by continously calling on itself the PrintTree method
        # we can use the reference to keep the values in between recursive calls
        stringRep.append(self.val + "\n")
        if self.left:
            self.left.PrintTree(stringRep)
        if self.right:
            self.right.PrintTree(stringRep)


def serialize(node, stringRep):
    node.PrintTree(stringRep)
    # We create our string by joining all the values in the list
    result = ''.join(stringRep)
    return result


def deserialize(nodeText):
    result = Node('root')
    # We are going to read line by line
    for line in nodeText.splitlines():
        aux = result
        # We will append to this multiple values depending on where we go deeper in our tree
        addString = ""
        # we check if there is any value after the '.'
        while("." in line):
            if('left' in line[:4]):
                addString = addString + 'left.'
                aux = aux.left
            if('right' in line[:4]):
                addString = addString + 'right.'
                aux = aux.right
                # We add one to go past the '.' because it would result in '.line' without this
            line = line[line.find(".") + 1:]
        # After we went through all the string, we check if the last thing is a left or a right node
        if('left' == line[:4]):
            aux.AddLeft(Node(addString + 'left'))
        if('right' == line[:4]):
            aux.AddRight(Node(addString + 'right'))

    return result


if __name__ == "__main__":
    # We need to use the reference of an object
    # We are going to use a list so we can make sure that the changes we make are kept
    stringRep = []
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node, stringRep)).left.left.val == 'left.left'
