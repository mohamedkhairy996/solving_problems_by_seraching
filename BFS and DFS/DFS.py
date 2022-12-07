visited = set()
def dfs( graph, node):
    if node not in visited:
        print (node , end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs( graph, neighbour)
