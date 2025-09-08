from collections import deque


class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)                               # Step 1: push into q2
        while self.q1:                                  # Step 2: move all from q1 → q2
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1             # Step 3: swap queues

    def pop(self):
        return self.q1.popleft()                        # remove front (top of stack)

    def top(self):
        return self.q1[0]                               # peek front

    def empty(self):
        return not self.q1                              # check if q1 is empty


myStack = MyStack()
myStack.push(1)                     # push 1 → q1 = [1]
myStack.push(2)                     # push 2 → q2 = [2], move q1=[1] → q2 = [2,1], swap → q1=[2,1]
print(myStack.top())                # q1 = [2,1], top = front = 2
print(myStack.pop())                # remove front → 2, now q1 = [1]
print(myStack.empty())              # q1 = [1] → not empty → False
