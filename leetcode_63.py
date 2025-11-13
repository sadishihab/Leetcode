class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If starting or ending cell is blocked → no path possible
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0  # Blocked cell → no paths
                elif r == m - 1 and c == n - 1:
                    curRow[c] = 1  # Destination cell
                else:
                    right = curRow[c + 1] if c + 1 < n else 0
                    down = prevRow[c] if r + 1 < m else 0
                    curRow[c] = right + down
            prevRow = curRow

        return prevRow[0]
