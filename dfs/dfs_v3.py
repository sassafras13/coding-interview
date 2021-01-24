# 2021-01-23
# Emma Benjaminson
# Third implementation of depth-first search
# Source: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# uses a dict but incorporates a set because the edges are undirected 
# not sure why making that distinction...
graph = {
        'A' : set(['B','C']),
        'B' : set(['A','D','E']),
        'C' : set(['A','F']),
        'D' : set(['B']),
        'E' : set(['B','F']),
        'F' : set(['C','E'])
        }

# iterative version
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited: 
            visited.add(vertex)
            # minus sign removes visited nodes from set of all adjacent vertices
            stack.extend(graph[vertex] - visited)
    return visited

print('iterative version')
print(dfs(graph, 'A'))

# NOTE: This code does not work as expected, I'm wondering if the minus sign is still 
# operating the same way it did in 2014 when this code was first created...

