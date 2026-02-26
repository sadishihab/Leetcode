import heapq   # Python's built-in min-heap implementation

def shortestPath(edges, n, src):

    adj = {i: [] for i in range(1, n+1)}                                # Step 1: Build adjacency list | We create a dictionary where: key = node, value = list of (neighbor, weight)

    for s, d, w in edges:                                               # Fill adjacency list using given edges | Each edge: (source, destination, weight)
        adj[s].append((d, w))                                           # add directed edge s -> d

    dist = {i: float("inf") for i in range(1, n+1)}                     # Step 2: Create distance dictionary | Initialize all distances as infinity | Because initially we don't know shortest distance

    dist[src] = 0                                                       # Distance to source is 0 (starting point)

    minHeap = [(0, src)]                                                # Step 3: Min Heap (priority queue) | It always gives the node with smallest distance first | Format: (current_distance, node)

    while minHeap:                                                      # Step 4: Process nodes until heap is empty

        currDist, node = heapq.heappop(minHeap)                         # Pop the node with smallest distance

        if currDist > dist[node]:                                       # IMPORTANT: If this distance is outdated (bigger than stored distance), skip it. This avoids unnecessary work.
            continue

        for nei, weight in adj[node]:                                   # Step 5: Explore neighbors of current node

            newDist = currDist + weight                                 # Calculate new possible distance to neighbor

            if newDist < dist[nei]:                                     # If we found a shorter path, update it

                dist[nei] = newDist                                     # update shortest distance

                heapq.heappush(minHeap, (newDist, nei))            # Push updated distance into heap

    return dist                                                         # Step 6: Return shortest distances to all nodes