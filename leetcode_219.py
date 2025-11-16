from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # If the window size exceeds k, remove the leftmost element
            if right - left > k:
                window.remove(nums[left])
                left += 1

            # If the number is already inside the window → duplicate found
            if nums[right] in window:
                return True

            # Add current number to window
            window.add(nums[right])

        return False
