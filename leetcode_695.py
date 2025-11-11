from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # Base case — out of bounds, visited, or water
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0

            visit.add((r, c))
            area = 1  # current land cell

            # Explore 4 directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))

        return max_area
