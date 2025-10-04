import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap)  # build heap in O(n)
        while len(self.min_heap) > k:                           # Keep only k largest elements
            heapq.heappop(self.min_heap)

    def add(self, val):
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:                         # If size > k, remove smallest
            heapq.heappop(self.min_heap)

        return self.min_heap[0]                                 # The root is the kth largest
