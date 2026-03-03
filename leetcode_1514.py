import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            adj[a].append((b, prob))
            adj[b].append((a, prob))

        # Probability table
        prob = [0.0] * n
        prob[start] = 1.0

        # Max heap (store negative for Python min-heap)
        maxHeap = [(-1.0, start)]

        while maxHeap:
            currProb, node = heapq.heappop(maxHeap)
            currProb = -currProb

            if node == end:
                return currProb

            if currProb < prob[node]:
                continue

            for nei, edgeProb in adj[node]:
                newProb = currProb * edgeProb
                if newProb > prob[nei]:
                    prob[nei] = newProb
                    heapq.heappush(maxHeap, (-newProb, nei))

        return 0.0