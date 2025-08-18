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


# 📝 Flashcard Version (for revision)
# “Use two stacks: stack for values, minStack for current mins.
# On push: push val and min(val, last min). On pop: pop both. getMin = top of minStack.”

# 🔑 Full Approach – Min Stack
# Problem Restatement:
# Implement a stack that, besides standard operations (push, pop, top), can return the minimum element in constant time (getMin).

# Observation:
# If we only use one stack, finding the min would require O(n) each time.
# To achieve O(1), we need to track the minimum at each step.

# Two-stack solution:
# Use a normal stack for all elements.
# Use a minStack where each entry keeps the minimum of the stack up to that point.
# Initialize minStack with +∞ to handle the first push gracefully.

# Algorithm:
# push(val):
# Push val to stack.
# Push min(val, minStack[-1]) to minStack.
# pop():
# Pop from both stack and minStack.
# top():
# Return last element from stack.
# getMin():
# Return last element from minStack.
# Return:
# All operations run in O(1).

# ⏱️ Complexity
# Time: O(1) for all operations.
# Space: O(n) for the two stacks.