from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Step 1 — Initialize pointers and variables
        L, R = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        # Step 2 — Loop until pointers meet
        while L < R:
            if height[L] < height[R]:
                # Step 3 — Process left pointer
                if height[L] >= left_max:
                    left_max = height[L]  # update left_max
                else:
                    water += left_max - height[L]  # water trapped at L
                L += 1  # move left pointer
            else:
                # Step 4 — Process right pointer
                if height[R] >= right_max:
                    right_max = height[R]  # update right_max
                else:
                    water += right_max - height[R]  # water trapped at R
                R -= 1  # move right pointer

        # Step 5 — Return total water trapped
        return water
