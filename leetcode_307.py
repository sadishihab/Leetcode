class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index <= M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)

        self.sum = self.left.sum + self.right.sum

    def rangeQuery(self, L, R):
        if self.L == L and self.R == R:
            return self.sum

        M = (self.L + self.R) // 2

        if R <= M:
            return self.left.rangeQuery(L, R)
        elif L > M:
            return self.right.rangeQuery(L, R)
        else:
            return (self.left.rangeQuery(L, M) +
                    self.right.rangeQuery(M + 1, R))


class NumArray:

    def __init__(self, nums):
        self.root = SegmentTree.build(nums, 0, len(nums) - 1)

    def update(self, index, val):
        self.root.update(index, val)

    def sumRange(self, left, right):
        return self.root.rangeQuery(left, right)
