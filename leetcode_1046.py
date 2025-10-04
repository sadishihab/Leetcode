import heapq


class Solution:
    def lastStoneWeight(self, stones):

        max_heap = [-s for s in stones]                     # Convert to max-heap by negating
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)                    # heaviest
            x = -heapq.heappop(max_heap)                    # second heaviest

            if x != y:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0
