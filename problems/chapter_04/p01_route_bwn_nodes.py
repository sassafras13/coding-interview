# 2021-05-20
# Emma Benjaminson
# Chapter 4 Problem 1: Trees and Graphs

# Problem: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.  

# Emma thinking out loud:
# definitely think that BFS is the answer, and frankly probably two BFS from each of the two nodes that look until they find a node that the other has encountered. 
# do I need to implement the directed graph as well? probably. 
# if I was going to implement the directed graph, I would probably do it as an adjacency list
# I think I need to define a class for the directed graph
# then write an algorithm that does BFS from the two nodes requested by the user

import AdjacencyList as alist
import Queue as q

# algorithm function takes in two nodes that we want to find a connected path between 

# we initiate BFS from the first node

# we run until we find the second node or we have exhausted all the nodes

# to do BFS we want to visit all the child nodes before moving on to the next layer

# use a queue...oh no, I need to implement a queue in Python too...

# start at node 1

# add all child nodes to queue

# go to first child node in queue, add all of its children to the back of the queue

# go to the next child node in queue, add all children to the back

# repeat until we find node 2 or the queue is empty


if __name__ == "__main__":

    mygraph = alist.DirectedGraph()
    mygraph.add_vertex(1)
    mygraph.add_vertex(2)
    mygraph.add_vertex(3)
    mygraph.add_vertex(4)
    mygraph.add_vertex(5)
    mygraph.add_vertex(6)

    mygraph.add_edge(1,2)
    mygraph.add_edge(1,3)
    mygraph.add_edge(1,4)
    mygraph.add_edge(2,5)
    mygraph.add_edge(3,5)
    mygraph.add_edge(3,6)
    mygraph.add_edge(5,3)
    mygraph.add_edge(6,4)
    mygraph.add_edge(3,1)
    mygraph.add_edge(2,1)

    mygraph.print_graph()

    myqueue = q.Queue()
    myqueue.enqueue(5)
    myqueue.enqueue(6)
    myqueue.enqueue(7)
    print(myqueue.dequeue())
