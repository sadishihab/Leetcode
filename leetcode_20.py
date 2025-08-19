# Valid Parentheses
# Push opens to stack. For closes, check top matches. If mismatch/empty → invalid. End: valid if stack empty.
# Time: O(n) (each character processed once)
# Space: O(n) (in worst case, all characters are opens)

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