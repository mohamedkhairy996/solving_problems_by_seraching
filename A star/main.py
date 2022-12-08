file = open('graph.txt')
h = {}
graph = {}


for line in file:
    vals = line.strip().split(' ')
    h[vals[0]] = vals[1]
    graph[vals[0]] = [(vals[2:4]), (vals[4:6])]

file.close()


def path_f_cost(path):
    g_cost=0
    for(node,cost) in path:
        g_cost += int(cost)
    last_node= path[-1][0]
    h_cost = h[last_node]
    f_cost = int(h_cost) + g_cost
    return f_cost,last_node,g_cost

def a_star(graph , start , goal):
    visited = []
    queue = [[(start , 0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal :
            return path
        else:
            neighbour =graph.get(node , [])
            for (node2 , cost) in neighbour:
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)


#Function calling------------------------------
path =a_star(graph,'A','J')
print("The A* path is : ",path)
print("The cost of this path is = ",path_f_cost(path)[2])
