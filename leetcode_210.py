class Solution:
    def findOrder(self, numCourses, prerequisites):

        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[b].append(a)

        state = [0] * numCourses
        res = []

        def dfs(course):

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for nei in adj[course]:
                if not dfs(nei):
                    return False

            state[course] = 2
            res.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res[::-1]