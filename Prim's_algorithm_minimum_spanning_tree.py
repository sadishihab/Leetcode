import heapq

def primMST(edges, n):

    # Step 1: Build adjacency list
    adj = {i: [] for i in range(1, n+1)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    visited = set()
    minHeap = [(0, 1, -1)]   # (weight, node, parent)
    totalCost = 0
    mstEdges = []

    while minHeap and len(visited) < n:

        weight, node, parent = heapq.heappop(minHeap)

        if node in visited:
            continue

        visited.add(node)
        totalCost += weight

        if parent != -1:
            mstEdges.append([parent, node])

        for nei, w in adj[node]:
            if nei not in visited:
                heapq.heappush(minHeap, (w, nei, node))

    return totalCost, mstEdges