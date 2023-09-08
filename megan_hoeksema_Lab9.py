def extractMin(keys, Q):
    minVertex = Q[0]
    for v in Q:
        if keys[v] < keys[minVertex]:
            minVertex = v
    Q.remove(minVertex)
    return minVertex

def neighbors(graph, u):
    listOfNeighbors = []
    for toVertex in range(len(graph)):
        if graph[u][toVertex] != 0:
            listOfNeighbors.append(toVertex)
    return listOfNeighbors

def mst(graph):
    V = []
    for i in range(len(graph)):
        V.append(i)
    key = {}
    P = {}
    s = 0
    for v in V:
        key[v] = float('inf')   # Mark all nodes with infinity
        P[v] = -1
    key[s] = 0                 # Mark the starting node with a 0
    Q = V
    while len(Q) != 0:
        u = extractMin(key, Q)
        for v in neighbors(graph,u):
            if v in Q and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                P[v] = u
    return list(P.items())

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
        [7, 0, 12, 5, 0, 0, 0, 9],
        [0, 12, 0, 6, 0, 0, 0, 0],
        [0, 5, 6, 0, 14, 8, 0, 0],
        [0, 0, 0, 14, 0, 3, 0, 0],
        [10, 0, 0, 8, 3, 0, 0, 0],
        [15, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0]]

print(mst(graph))