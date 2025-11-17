from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Step 1 — Initialize two pointers and max_area
        L = 0                  # Left pointer at start
        R = len(height) - 1    # Right pointer at end
        max_area = 0           # Stores maximum area found

        # Step 2 — Loop until pointers meet
        while L < R:
            # Step 3 — Calculate area with current L and R
            current_area = min(height[L], height[R]) * (R - L)
            max_area = max(max_area, current_area)  # Update max area

            # Step 4 — Move pointer pointing to shorter line
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        # Step 5 — Return the maximum area found
        return max_area
