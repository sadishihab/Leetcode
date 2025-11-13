class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow[n - 1] = 1  # Only one way from the rightmost column
            for c in range(n - 2, -1, -1):
                curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow

        return prevRow[0]
