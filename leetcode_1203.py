def topoSort(n, edges):
    adj = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        adj[u].append(v)

    state = [0]*(n+1)   # 0=unvisited, 1=visiting, 2=visited
    res = []

    def dfs(node):
        if state[node] == 1: return False
        if state[node] == 2: return True
        state[node] = 1
        for nei in adj[node]:
            if not dfs(nei): return False
        state[node] = 2
        res.append(node)
        return True

    for i in range(1, n+1):
        if not dfs(i): return []

    return res[::-1]

class Solution:
    def sortItems(self, n, m, group, beforeItems):

        # 1️⃣ Assign unique groups to items with -1
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1

        # 2️⃣ Build graphs
        # item_graph for items, group_graph for groups
        item_edges = []
        group_edges = []
        for curr in range(n):
            for pre in beforeItems[curr]:
                # Item-level dependency
                item_edges.append((pre+1, curr+1))  # +1 for 1-indexed topoSort
                # Group-level dependency if in different groups
                if group[curr] != group[pre]:
                    group_edges.append((group[pre]+1, group[curr]+1))

        # 3️⃣ Topo sort groups and items
        group_order = topoSort(new_group_id, group_edges)
        if not group_order:
            return []

        item_order = topoSort(n, item_edges)
        if not item_order:
            return []

        # 4️⃣ Collect items by groups in order
        from collections import defaultdict
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item-1]].append(item-1)  # convert back to 0-indexed

        # 5️⃣ Merge items by group order
        res = []
        for g in group_order:
            res.extend(group_to_items.get(g-1, []))

        return res