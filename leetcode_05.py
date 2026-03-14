class Solution:
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1  # return actual start and end indices

        start, end = 0, 0

        for i in range(len(s)):
            l1, r1 = expand(i, i)      # odd-length palindrome
            l2, r2 = expand(i, i + 1)  # even-length palindrome

            # Update the longest palindrome
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

# Example usage
# sol = Solution()
# print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(sol.longestPalindrome("cbbd"))   # Output: "bb"