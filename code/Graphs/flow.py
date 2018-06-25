def class Flow:
    def __init__(self, sz):
        self.G = [[0]*sz for _ in range(sz)]
        self.adj = [[] for i in range(sz)]
    
    def add_edge(self, i, j, w):
        G[i][j] = w
        adj[i].append(j)
        adj[j].append(i)
    
    def dfs(self, s, t, v):
        if s in v: return 0
        v.add(s)
        if s == t: return 10**18 # INF
        for nxt in adj[s]:
            push = min(G[s][nxt], self.dfs(nxt, t, v))
            if push:
                G[s][nxt] -= push
                G[nxt][s] += push
                return push
        return 0

    def max_flow(self, s, t):
        flow = 0
        while 1:
            pushed = self.dfs(s, t, set())
            if not pushed: break
            flow += pushed
