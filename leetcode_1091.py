from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # If start or end cell is blocked
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 1  # starting cell counts as 1
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Check if reached destination
                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < n and
                            (nr, nc) not in visit and grid[nr][nc] == 0):
                        queue.append((nr, nc))
                        visit.add((nr, nc))

            length += 1

        return -1
