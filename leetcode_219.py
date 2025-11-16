from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # If the window size exceeds k, remove the leftmost element
            if R - L > k:
                window.remove(nums[L])
                L += 1

            # If the number is already inside the window → duplicate found
            if nums[R] in window:
                return True

            # Add current number to window
            window.add(nums[R])

        return False
