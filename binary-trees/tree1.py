# 01-08-2021
# Emma Benjaminson
# Binary Tree Implementation (v1)
# Source: https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def addNode(self, obj):
        self.children.append(obj)
