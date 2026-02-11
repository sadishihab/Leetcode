class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)  # O(n)
        longest = 0

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                # Count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
