from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0                                                                         # Left pointer of the window
        total = 0                                                                     # Current window sum
        min_length = float("inf")                                                     # Store the smallest valid window size

        for R in range(len(nums)):                                           # R is the right pointer
            total += nums[R]                                                 # Expand window by adding nums[R]

            # While the current window meets or exceeds the target
            while total >= target:
                # Update the minimum length
                min_length = min(min_length, R - L + 1)

                # Shrink window from the left
                total -= nums[L]
                L += 1

        # If no valid window found, return 0
        return 0 if min_length == float("inf") else min_length
