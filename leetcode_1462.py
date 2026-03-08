def topoSort(n, edges):
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)

    state = [0]*n   # 0=unvisited, 1=visiting, 2=visited
    res = []

    def dfs(node):
        if state[node] == 1: return False
        if state[node] == 2: return True

        state[node] = 1
        for nei in adj[node]:
            if not dfs(nei):
                return False

        state[node] = 2
        res.append(node)
        return True

    for i in range(n):
        if not dfs(i):
            return []

    return res[::-1]


class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        # 1️⃣ Build graph edges
        edges = prerequisites

        # 2️⃣ Get topological order
        order = topoSort(numCourses, edges)

        # 3️⃣ Adjacency list
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        # 4️⃣ Store prerequisite sets
        pre = [set() for _ in range(numCourses)]

        # 5️⃣ Process nodes in topo order
        for node in order:
            for nei in adj[node]:
                pre[nei].add(node)
                pre[nei] |= pre[node]

        # 6️⃣ Answer queries
        ans = []
        for u, v in queries:
            ans.append(u in pre[v])

        return ans