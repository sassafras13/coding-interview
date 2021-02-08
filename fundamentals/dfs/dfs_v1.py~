# 2021-01-23
# Emma Benjaminson
# Implementation of Depth First Search
# Source: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

# create an adjacency list with a dict
graph = {
        'A' : ['B','C'],
        'B' : ['D','E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
        }

# set collects visited nodes
visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# driver code
dfs(visited, graph, 'A')
