import heapq


class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int           # max projects
        :type w: int           # initial capital
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int            # final maximized capital
        """
        # Step 1️⃣: Min heap for projects by required capital
        capital_heap = []
        for c, p in zip(capital, profits):
            heapq.heappush(capital_heap, (c, p))  # (required capital, profit)

        # Step 2️⃣: Max heap for profits (negate for Python)
        profit_heap = []

        # Step 3️⃣: Repeat up to k projects
        for _ in range(k):
            # Unlock all projects affordable now
            while capital_heap and capital_heap[0][0] <= w:
                c, p = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, -p)  # max-heap by profit

            # If no project is affordable, break early
            if not profit_heap:
                break

            # Pick the most profitable project
            w += -heapq.heappop(profit_heap)

        # Step 4️⃣: Return final capital
        return w
