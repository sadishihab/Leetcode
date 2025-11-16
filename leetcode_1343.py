from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k  # Minimum sum needed for avg ≥ threshold
        window_sum = sum(arr[:k])  # Sum of the first window
        count = 1 if window_sum >= target_sum else 0

        # Slide the window across the array
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]  # Add new, remove old
            if window_sum >= target_sum:
                count += 1

        return count
