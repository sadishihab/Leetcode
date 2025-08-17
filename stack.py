# Implementing a stack is trivial using a dynamic array
#The stack follows LIFO


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)    #Adds an element n to the top of the stack.

    def pop(self):
        return self.stack.pop() #Removes and returns the top element from the stack.