# 2021-01-23
# Emma Benjaminson
# Implementation of breadth-first search
# Source: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

# I guess this must be a directed graph since we are not using sets to list the values
graph = {
        'A' : ['B','C'],
        'B' : ['D','E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
        }

visited = [] # keep track of visited nodes
queue = [] # queue initialized

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# driver code
bfs(visited, graph, 'A')

