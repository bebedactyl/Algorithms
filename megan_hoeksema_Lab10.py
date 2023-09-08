# Stack ADT with list implementation from Lab 5
class MyStack:
    def __init__(self, type): # Creates an empty list
        self.elemType = type
        self.state = [] # Empty list
    def str (self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds an element to the top of a stack
        assert type(elem) == self.elemType
        self.state.append(elem)
    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()
    def top(self): # Returns the top of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def graphColoring(graph, listOfColors):
    n = len(graph)
    nodesColored = []

    s = MyStack(list)
    s.push(nodesColored)

    while not s.empty():
        currentState = s.pop()
        currentCol = len(currentState)
        if currentCol == n:
            print(currentState)
        else:
            for color in listOfColors:
                feasible = True
                for previousCol in range(currentCol):
                    if graph[previousCol][currentCol] == True and currentState[previousCol] == color:
                        feasible = False
                        break
                if feasible:
                    childState = currentState.copy()
                    childState.append(color)
                    s.push(childState)

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
graph = [[False, True, False, False, False, True],
         [True, False, True, False, False, True],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True],
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']
graphColoring(graph, colors)