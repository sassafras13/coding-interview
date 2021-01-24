# 2021-01-18
# Emma Benjaminson
# Implementation of graphs
# Source: https://www.educative.io/edpresso/how-to-implement-a-graph-in-python

##################
# ADJACENCY LIST #
##################

# add a vertex to the dictionary
def add_vertex(v):
    global graph # creates a global var that can be modified outside scope of this function
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no += 1
        graph[v] = []

# add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph

    # check if v1 is a valid vertex
    if v1 not in graph:
        print("Vertex ", v1, " does not exist.")

    # check if v2 is a valid vertex
    elif v2 not in graph: 
        print("Vertex ", v2, " does not exist.")
    else: 
        temp = [v2, e]
        graph[v1].append(temp)

# print the graph
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# driver code
print("Adjacency list")
graph = {}

# store the number of vertices in the graph
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

# add the edges between the vertices by specifying
# the start/end vertices and edge weights
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print_graph()
print("Internal representation: ", graph)

####################
# ADJACENCY MATRIX #
####################

# add a vertex to the set of vertices and the graph
def add_vertex(v):
    global graph
    global vertices_no
    global vertices

    if v in vertices:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no += 1
        vertices.append(v)

        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0) # I think this adds another column to the matrix?
        temp = []
        for i in range(vertices_no):
            temp.append(0) # I think this is adding another row to the matrix?
        graph.append(temp)

# add an edge between v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices

    # check if v1 is valid
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")

    # check if v2 is valid
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")

    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# print the graph
def print_graph():
    global graph
    global vertices_no
    
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j], " edge weight: ", graph[i][j])

# driver code
print("Adjacency matrix")
vertices = [] 
vertices_no = 0 
graph = []

add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print_graph()
print("Internal representation: ", graph)
