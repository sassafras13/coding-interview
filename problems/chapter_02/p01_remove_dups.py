# 2021-02-02
# Emma Benjaminson
# Chapter 2 Problem 1: Remove Dups

# Problem: write code to remove duplicates from an unsorted linked list

# Emma thinking out loud: 
# what even is a linked list in Python - its a class I'd have to create manually, right? 
# traversing the list is easy, but random access is not possible
# naive approach: scan through the linked list and compare each value to a temp buffer
# if the value already exists in the temp buffer, then remove that node from the list

# the hints suggest using a hash table
# and using two pointers, one to search ahead of the other one
# the two pointer system might work if I didn't have extra storage capacity
# the hash table is a cool idea because if I get a collision, then I know I have a duplicate

# how am I going to implement this in code? Do I have to manually write the linked list myself? 
# I'm gonna peek at the solutions: 
# shoot yeah they implemented linked lists themselves and then imported it as a module
# I didn't look at the rest of the code in detail

# --- okay... ---
# first I need to write a Linked List class in Python
# then I am going to traverse the list
# I'm going to pass every item into a hash table (i.e. a dictionary) 
# if I get a collision, then that is a duplicate
# I then call the "delete node" function written into my linked list class

# --- linked list class ---
# the methods I will need are: 
# init
# delete node
# traverse? or is that just something I'll do myself? 

# I'm going to implement linked list in a separate doc in case I need it again later

import LinkedList as ll

def removeDups(linkList):

    # create a set
    seen = set() 
    
    # while the next node is not None in linkList
    node = linkList.head

    while node.next is not None:

        if node.data in seen:
            linkList.remove_node(node)

        else:
            seen.add(node.data)

        node = node.next

    return seen

if __name__ == "__main__":
    
    linkList = ll.LinkedList(["HI", "OR", "AL", "WA", "OR", "PA"])
    print('original list ', linkList)
    
    seen = removeDups(linkList)
    print('cleaned list ', linkList)
    print('seen set ', seen)
