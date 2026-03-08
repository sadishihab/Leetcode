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