# 2021-01-23
# Emma Benjaminson
# Second implementation of depth-first search
# Source: https://likegeeks.com/depth-first-search-in-python/

graph = {
        'A' : ['D','C','B'],
        'B' : ['E'],
        'C' : ['G','F'],
        'D' : ['H'],
        'E' : ['I'],
        'F' : ['J']
        }

def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]

    while(len(stack) != 0):
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)

DFS_path = dfs_non_recursive(graph, 'A')
print(DFS_path)
