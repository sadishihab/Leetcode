import heapq

class DualHeap(object):
    def __init__(self, k):
        self.small = []  # max-heap (left half)
        self.large = []  # min-heap (right half)
        self.delayed = {} # lazy deletions
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def add(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def remove(self, num):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        self.balance()

    def get_median(self):
        if self.k % 2 == 1:
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        dh = DualHeap(k)
        res = []

        for i in range(len(nums)):
            dh.add(nums[i])
            if i >= k - 1:
                res.append(dh.get_median())
                dh.remove(nums[i - k + 1])
        return res
