class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # frequency map for characters in the window
        L = 0
        max_freq = 0        # track the count of most frequent character
        max_length = 0

        for R in range(len(s)):
            # Add current character to frequency map
            count[s[R]] = count.get(s[R], 0) + 1

            # Update the most frequent character count
            max_freq = max(max_freq, count[s[R]])

            # If window is invalid, shrink from left
            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1

            # Update maximum valid window size
            max_length = max(max_length, R - L + 1)

        return max_length
