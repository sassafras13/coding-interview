# 2021-01-18
# Emma Benjaminson
# Implementation of graphs
# Source: https://www.python-course.eu/graphs_python.php

class Graph(object): # here the class will need an input object on creation
    def __init__(self, graph_dict=None):
        """
        Initializes a graph object. If no dictionary, or None is given, an empty dictionary
        will be used.
        """

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        Returns the vertices of a graph.
        """

        return list(self.__graph_dict.keys())

    def edges(self):
        """
        Returns the edges of a graph.
        """

        return self.__generate_edges()



