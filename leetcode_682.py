class Solution(object):
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

sol = Solution()
ops = ["5","2","C","D","+"]
print(sol.calPoints(ops))

# 📝 Flashcard Version
# “Use stack for scores. '+': sum last 2, 'D': double last, 'C': pop last, number: push. Return sum of stack.”

# 🔑 Full Approach – Baseball Game

# Initialize a stack to keep track of valid scores.
# Iterate through each operation in operations:
# If the operation is '+':
# Take the sum of the last two scores in the stack and push it.
# If the operation is 'D':
# Double the last score in the stack and push it.
# If the operation is 'C':
# Remove (pop) the last score from the stack.
# Otherwise (a number as a string):
# Convert it to an integer and push it onto the stack.
# Return the sum of all values in the stack after processing all operations.

# Key Insight:
# Use the stack to dynamically keep track of valid scores, handling each operation according to its rule.


