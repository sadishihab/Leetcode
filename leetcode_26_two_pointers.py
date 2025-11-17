from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Step 1 — Handle edge case: if array is empty
        if not nums:
            return 0

        # Step 2 — Initialize slow pointer L
        L = 0  # Points to the last unique element

        # Step 3 — Iterate with fast pointer R from 1 to end
        for R in range(1, len(nums)):
            # Step 4 — Check if current number is different from last unique
            if nums[R] != nums[L]:
                L += 1                # Move slow pointer forward
                nums[L] = nums[R]     # Update position with new unique number

        # Step 5 — Return number of unique elements
        return L + 1  # L is index, so count = L + 1
