import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        # Step 1: Build adjacency list
        adj = {i: [] for i in range(1, n+1)}
        for s, d, w in times:
            adj[s].append((d, w))

        # Step 2: Initialize distance table
        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0

        # Step 3: Min Heap
        minHeap = [(0, k)]

        while minHeap:

            currDist, node = heapq.heappop(minHeap)

            # Skip outdated distances
            if currDist > dist[node]:
                continue

            # Explore neighbors
            for nei, weight in adj[node]:
                newDist = currDist + weight
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(minHeap, (newDist, nei))

        # Step 4: Check if all nodes are reachable
        maxDist = max(dist.values())
        return maxDist if maxDist < float("inf") else -1