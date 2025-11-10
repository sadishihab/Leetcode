from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # Base conditions
            if (r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    grid[r][c] == "0" or
                    (r, c) in visit):
                return

            # Mark as visited
            visit.add((r, c))

            # Explore 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                # Found a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
