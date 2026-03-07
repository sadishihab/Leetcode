class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):

        # attach original index
        edges = [edge + [i] for i, edge in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        # ---------- Union Find ----------
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
            return True

        # ---------- Kruskal helper ----------
        def kruskal(skip_edge=None, force_edge=None):

            for i in range(n):
                parent[i] = i
                rank[i] = 0

            weight = 0
            edges_used = 0

            # force edge first
            if force_edge != None:
                u, v, w, _ = edges[force_edge]
                if union(u, v):
                    weight += w
                    edges_used += 1

            for i, (u, v, w, idx) in enumerate(edges):

                if i == skip_edge:
                    continue

                if union(u, v):
                    weight += w
                    edges_used += 1

                if edges_used == n - 1:
                    break

            if edges_used == n - 1:
                return weight
            return float('inf')

        # ---------- Step 1: Original MST ----------
        base = kruskal()

        critical = []
        pseudo = []

        # ---------- Step 2: Test each edge ----------
        for i in range(len(edges)):

            # test critical
            if kruskal(skip_edge=i) > base:
                critical.append(edges[i][3])

            # test pseudo critical
            elif kruskal(force_edge=i) == base:
                pseudo.append(edges[i][3])

        return [critical, pseudo]