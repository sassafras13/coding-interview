# 01-08-2021
# Emma Benjaminson
# Binary Tree Implementation
# Source: https://www.educative.io/edpresso/binary-trees-in-python

class Node:

    def __init__(self, data):

        # left child
        self.left = None

        # right child
        self.right = None

        # node value
        self.data = data

    def insert(self, data):

        # compare new value with parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not found"
            return self.right.findval(lkpval)
        else:
            return str(self.data)+" is found"

    def PrintTree(self):
        # recursively prints all elements that are children of this node
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

