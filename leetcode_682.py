# Baseball Game
# Split array in half. Interleave: nums[i], nums[i+n]. Replace original array. Return result.
# Time: O(n) — the loop runs n times, and each append is O(1)
# Space: O(n) — result stores 2n elements before copying back to nums

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


