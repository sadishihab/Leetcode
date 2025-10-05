import heapq


class Solution:
    def kClosest(self, points, k):
        max_heap = []

        for (x, y) in points:
            dist = x * x + y * y
            heapq.heappush(max_heap, (-dist, x, y))             # store negative for max-heap

            if len(max_heap) > k:
                heapq.heappop(max_heap)                               # remove farthest point

        return [[x, y] for (_, x, y) in max_heap]

