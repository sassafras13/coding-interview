# 01 - 04 - 2021
# Emma Benjaminson
# Linked List Implementation
# Source: https://realpython.com/linked-lists-python/

class LinkedList: 
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0)) #pop(0) pops the 0th element
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next            

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # need this method to make LinkedList iterable
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node # yield creates a generator obj, saves memory
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        # this checks to see if the LinkedList already has a head
        # i.e. if the LinkedList is empty or not
        if not self.head:
            self.head = node
            return
        # iterates through all nodes in LinkedList
        for current_node in self:
            pass
        # adds new node to end
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def get_node(self, target_node_index):
        # check to make sure list is not empty
        if not self.head:
            raise Exception("List is empty")

        # iterate through each node in the list while incrementing a counter
        # if the counter has the same value as target_node_index, return the data in that node
        i = 0
        for node in self:
            if target_node_index == i:
                return node.data
            i += 1

        # if the end of the list is reached and we have not found target_node_index return Exception
        raise Exception("LinkedList does not contain '%0.f' element" % target_node_index)

    def reverse(self):
        # Thanks to https://www.geeksforgeeks.org/reverse-a-linked-list/
        # check to make sure list is not empty
        if not self.head:
            raise Exception("List is empty")

        prev_node = None
        curr_node = self.head
        
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        self.head = prev_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
