def loadGraph(edgeFilename):
    """Reads in the file of edge data"""

    edgeFilename = open(edgeFilename)

    edges = {}

    for line in edgeFilename.readlines():
        from_vertex = int(line.split()[0])
        to_vertex = int(line.split()[1])

        if from_vertex not in edges:
            edges[from_vertex] = []

        edges[from_vertex].append(to_vertex)

    return edges

class MyQueue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = []

    def __str__(self):
        """Displays the contents of the queue"""
        return str(self.queue)

    def enqueue(self, value):
        """Storing in FIFO order"""
        self.queue.append(value)

    def dequeue(self):
        """Removing in FIFO order"""
        if len(self.queue) == 0:
            raise Exception('Queue is empty!')
        return self.queue.pop(0)

    def empty(self):
        """Empties the list"""
        if len(self.queue) == 0:
            return True
        else:
            return False


def BFS(G,s):
    """Runs breadth-first search algorithm"""
    max(G.keys())

    d = max(G.keys()) + 1  #size of the list
    distance = [float('inf')] * d

    Q = MyQueue()

    distance[s] = 0
    Q.enqueue(s)
    while not Q.empty():
        u = Q.dequeue()
        if u not in G:
            continue
        for v in G[u]:
            if distance[v] == float('inf'):
                distance[v] = distance[u] + 1
                Q.enqueue(v)
    return distance

def distanceDistribution(G):
    """compute the distribution of all distances in G."""
    d = {}
    count = 0
    for node in G:
        Distances = BFS(G, node)
        for i in range(node + 1, len(Distances)):
            distance = Distances[index]
            if distance in d:
                d += 1
            else:
                count += 1
    for key in d:
        d[key] = distance/count


# Test loadGraph Function
print(loadGraph('edges.txt'))

# Test Queue Class
Q = MyQueue()
Q.enqueue(50)
Q.enqueue(100)
print(Q)
print(Q.empty())
Q.dequeue()
print(Q)
Q.dequeue()
print(Q)
print(Q.empty())

# Test BFS Function
G = loadGraph('edges.txt')
result = BFS(G, 200)
print(result)

# Test distanceDistribution Function
G = loadGraph('edges.txt')
print(distanceDistribution(G))

# To what extent does this network satisfy the small world phenomenon?
# Could not get my last function. Assuming that this network satisfies the small world phenomenon
# by the percentages showing that most nodes are connected in 6 degrees or less.
