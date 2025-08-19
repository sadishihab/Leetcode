# Min Stack
# Two stacks: stack for values, minStack for mins. push → push val & min(val,last). pop → pop both. getMin = top of minStack.
# Time: O(1) for all operations.
# Space: O(n) for the two stacks.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = [float('inf')]

    def push(self, val):
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

minStack = MinStack()
print(minStack.stack)
minStack.push(-2)
print(minStack.stack)
minStack.push(0)
print(minStack.stack)
minStack.push(-3)
print(minStack.stack)
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin())  #return -2