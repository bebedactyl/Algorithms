from collections import deque

class MyStack(object):
    def __init__(self, type):
        self.elemType = type
        self.stack = []
    def __str__(self):
        """Displays the contents of the stack"""
        return str(self.stack)
    def push(self, elem):
        """Adds an element to the top of a stack"""
        self.stack.append(elem)
    def empty(self):
        """True if stack is empty"""
        return len(self.stack) == 0
    def pop(self):
        """ Removes the top of a nonempty stack"""
        if not self.empty():
            return self.stack.pop()
    def top(self):
        """ Returns the top of a nonempty stack"""
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.stack[-1]

class MyQueue:
    def __init__(self, type):
        self.elemType = type
        self.queue = deque()
    def __str__(self):
        """Displays the contents of the stack"""
        return str(self.queue)
    def empty(self):
        """True if stack is empty"""
        return len(self.queue) == 0
    def enqueue(self, value):
        """Adds a value to the end of the queue"""
        self.queue.append(value)
    def dequeue(self):
        """Removes value from the front of the queue"""
        if self.empty():
            raise ValueError("Queue is Empty")
        else:
            return self.queue.popleft()
    def front(self):
        """ Returns the front of a nonempty queue"""
        if self.empty():
            raise ValueError("Requested Front of Empty Queue")
        else:
            return self.queue[0]

# Testing code for stack
s = MyStack(int)
print(s.empty())
s.push(5)               # Adds 5 to list [5]
s.push(8)               # Adds 8 to list [5, 8]
print(s)
print(s.pop())          # Removes 8
s.push(3)               # Adds 3 to list [5,3]
print(s)
print(s.empty())        # Returns False, List is not empty
print(s.top())          # Returns the number that was added most recently, which is 3.
print(s.pop())          # Removes 3 from the list
print(s.pop())          # Removes 5 from the list
print(s.top())          # should generate an error

# Testing code for Queue
q = MyQueue(int)
print(q.empty())          # Returns True because the deque is empty
q.enqueue(5)              # Adds 5 to the end of the queue
q.enqueue(8)              # Adds 8 to the end of the queue
print(q)                  # Queue = [5, 8]
print(q.dequeue())        # Removes 5 from the beginning of the queue
q.enqueue(3)              # Adds a 3 to the end of the queue
print(q)                  # Queue = [8, 3]
print(q.empty())          # Returns False because the queue is not empty
print(q.front())          # Returns the first number in the queue which is 8
print(q.dequeue())        # Removes 8 from the queue
print(q.dequeue())        # Removes 3 from the queue
print(q.dequeue())        # should generate an error