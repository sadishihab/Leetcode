class NumMatrix:
    def __init__(self, matrix):
        self.prefix = []

        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])

        # Build 2D prefix sum
        for i in range(rows):
            row_prefix = []
            row_sum = 0
            for j in range(cols):
                row_sum += matrix[i][j]
                above = self.prefix[i - 1][j] if i > 0 else 0
                row_prefix.append(row_sum + above)
            self.prefix.append(row_prefix)

    def sumRegion(self, row1, col1, row2, col2):
        total = self.prefix[row2][col2]

        top = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        overlap = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return total - top - left + overlap


