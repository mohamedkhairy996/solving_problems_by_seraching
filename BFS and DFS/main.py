import BFS
import DFS

file = open('graph.txt')
graph = {}

for line in file:
    vals = line.strip().split(' ')
    graph[vals[0]]=vals[2:]

file.close()

print("The Breadth-First Search is : ")
BFS.bfs(graph, '5')
print("\n--------------------------------------------")
print("The Depth-First Search is : ")
DFS.dfs( graph, '5')