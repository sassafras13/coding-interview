# 2021-05-20
# Emma Benjaminson
# Adjacency List Implementation

# for Ch04-P01 at least
# need a directed graph implemented as a list
# I suppose I could use a dict too but I think a list is more basic
# a dict is gonna be easier
# define a class

# class
class DirectedGraph(object):

    # initialize the graph list (which itself is a list of lists)
    def __init__(self, graph_list=None):
        '''
        Initialize the graph list. Create one if it doesn't already exist. 
        '''
        
        if graph_list == None:
            graph_list = {} 
        self.graph_list = graph_list 

    # define add vertex method
    def add_vertex(self, v):
        '''
        Check if vertex already exists. Add to list if it does not.
        '''
        if v not in self.graph_list:
            self.graph_list[v] = []
        else:
            print('Vertex already exists in graph.')


    # define add edge method
    def add_edge(self, v1, v2):
        '''
        Check if edge already exists. Add to list if it does not.
        '''
        if v2 not in self.graph_list[v1]:
            self.graph_list[v1].append(v2)
        else:
            print('Edge already exists in graph.')

    # define print graph method 
    def print_graph(self):
        '''
        Print the graph in a human-readable manner.
        '''
        for vertex in self.graph_list:
            print('vertex ', vertex)
            for neighbor in self.graph_list[vertex]:
                print(vertex, " -> ", neighbor)

# direction is implied as running from the first node to the second node in a tuple
# so we only add a connection to the first node's adjacency list
