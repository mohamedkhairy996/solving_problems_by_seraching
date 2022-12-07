file = open('graph.txt')
h = {}
graph = {}


for line in file:
    vals = line.strip().split(' ')
    h[vals[0]] = vals[1]
    graph[vals[0]] = [(vals[2:4]), (vals[4:6])]

file.close()


def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        for v in open_set:
            if g[v] + int(heuristic(v)) <= int(heuristic(start_node)):
                n = v
        if n == stop_node or graph[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + int(weight)
                else:
                    if g[m] > g[n] + int( weight):
                        # update g(m)
                        g[m] = g[n] + int(weight)
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('A* Path found: ', path)
            print("Path cost is = " ,g[stop_node])
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        closed_set.add(n)
        open_set.remove(n)

    print('Path does not exist!')

    return None



def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None

def heuristic(n):
    H_dist = {}
    H_dist = h
    return H_dist[n]


#Function calling------------------------------

aStarAlgo('A', 'J')
