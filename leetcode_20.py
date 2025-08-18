class Solution(object):
    def isValid(self, s):
        pairs_paren = {']':'[', '}':'{', ')':'('}
        stack = []
        for char in s:
            if char not in pairs_paren:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs_paren[char]:   # we can also write # if stack.pop() != pairs_paren[char]:#  return False
                    stack.pop()
                else:
                    return False
        return not stack

sol = Solution()
s = "[{()}]"
print(sol.isValid(s))


# 📝Valid Parentheses – Flashcard Approach

# “Push opening symbols to the stack. When encountering a closing symbol, check if it matches the top.
# If not, invalid. In the end, stack must be empty.”

# 🔑 Full Approach – Valid Parentheses
# Use a stack to keep track of opening brackets.
# Create a mapping of closing → opening brackets:
# { ')':'(', ']':'[', '}':'{' }
# Iterate over each character in the string:
# If it’s an opening bracket, push it onto the stack.
# If it’s a closing bracket:
# If the stack is empty → invalid (nothing to match with).
# Otherwise, pop the stack and check if it matches the corresponding opening bracket.
# If mismatch → invalid.
# After processing all characters:
# If the stack is empty → valid.
# If not empty (some opens weren’t matched) → invalid.
# ⏱️ Complexity
# Time: O(n) (each character processed once)
# Space: O(n) (in worst case, all characters are opens)

