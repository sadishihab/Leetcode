from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Step 1 — If array has 2 or fewer elements, all are allowed
        if len(nums) <= 2:
            return len(nums)

        # Step 2 — Initialize slow pointer L
        L = 2  # First two elements are always allowed

        # Step 3 — Iterate with fast pointer R starting from index 2
        for R in range(2, len(nums)):
            # Step 4 — Check if current element is allowed (at most 2 duplicates)
            if nums[R] != nums[L - 2]:
                nums[L] = nums[R]  # Write allowed element
                L += 1             # Move slow pointer forward

        # Step 5 — Return the number of allowed elements
        return L
