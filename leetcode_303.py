class NumArray:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left, right):
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left
