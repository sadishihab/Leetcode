class Solution(object):
    def searchMatrix(self, matrix, target):
         if not matrix or not matrix[0]:
             return False
         m, n = len(matrix), len(matrix[0])
         left, right = 0, m * n -1

         while left <= right:
             mid = (left + right) // 2
             row, col = mid // n, mid % n
             mid_val = matrix[row][col]
             if target == mid_val:
                 return True
             elif target > mid_val:
                 left  = mid + 1
             else:
                 right = mid - 1
         return False
