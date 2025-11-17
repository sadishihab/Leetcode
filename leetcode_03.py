class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()                                          # store characters in the current window
        L = 0                                                   # left pointer
        max_length = 0

        for R in range(len(s)):  # R is the right pointer
            # If duplicate found, shrink from the left
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # Add current character to the window
            window.add(s[R])

            # Update maximum window size
            max_length = max(max_length, R - L + 1)

        return max_length
