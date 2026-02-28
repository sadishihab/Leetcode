import heapq


class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return time

            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    newTime = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, (newTime, nr, nc))