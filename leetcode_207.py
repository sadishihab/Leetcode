from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        # Step 2: Compute in-degrees
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            indegree[course] += 1

        # Step 3: Initialize queue with courses having 0 in-degree
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        # Step 4: BFS - Topological sort
        while queue:
            curr = queue.popleft()
            taken += 1
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check if all courses can be taken
        return taken == numCourses
