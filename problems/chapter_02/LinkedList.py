# 2021-02-08
# Emma Benjaminson
# Implementation of Linked List 

# for ch2-p1 (at least) 
# need init, delete methods (possibly traverse?)
# singly linked list for now

# class Node
# this will contain init method
# attribute is next which is pointer to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # this can be replaced later

    def __repr__(self): # the repr is a machine-friendly string representation (__str__ supersedes __repr__ if present)
        return self.data


# class LinkedList
# contain init, delete methods
# internal traverse method?
class LinkedList: 
    def __init__(self, nodes=None): # what parameters do I need here? head? Do I pass in head? or not, for now? 
        self.head = None

        # if nodes is not None, then we have to add them to the list
        # we use pop to remove elements from nodes
        # we assign the first node to the head
        # then we iterate through the remaining nodes and create new nodes that are connected
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self): # this prints a machine-friendly string representing the class object (superseded by __str__ if present)
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self): # this makes the LinkedList class iterable
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        # this node is going to become the head
        # first set node.next equal to current head
        # then make current head equal to node
        node.next = self.head
        self.head = node

    def add_last(self, node):
        # check that the list is not empty
        # if it is, then we just make node the head
        if not self.head:
            self.head = node
            return
        
        # run through the nodes (while node.next is not none)
        # then arrive at the last node
        # assign its next pointer to the new node
        # assign the pointer of this new last node to none
        for curr_node in self:
            pass

        curr_node.next = node
       
    def remove_node(self, target_node):
        # check that the list is not empty
        # otherwise raise an exception
        if not self.head:
            raise Exception('List is empty')

        # check if the target_node is the head
        if self.head == target_node:
            self.head = self.head.next
            return

        # save the head as the previous node
        prev_node = self.head
        # iterate through the nodes
        for node in self: 
            # if node is the target_node then assign prev_node.next = node.next
            if node == target_node:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception('Node with data %s is not in linked list.' % target_node.data)

             
