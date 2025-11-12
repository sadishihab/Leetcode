
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge Case: Empty graph
        if not node:
            return None

        # Step 1: Hash map to store original -> cloned mapping
        clone_map = {}

        # Step 2: Initialize BFS queue
        queue = deque([node])

        # Clone the first node
        clone_map[node] = Node(node.val)

        # Step 3: BFS traversal to clone all nodes and their neighbors
        while queue:
            curr = queue.popleft()

            # Traverse all neighbors
            for neighbor in curr.neighbors:
                # If neighbor not cloned yet → create and add to queue
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Connect the cloned current node to cloned neighbor
                clone_map[curr].neighbors.append(clone_map[neighbor])

        # Step 4: Return the clone of the original starting node
        return clone_map[node]
