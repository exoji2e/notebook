from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [defaultdict(int) for _ in range(sz)]
    
    def add_edge(self, i, j, w):
        self.G[i][j] += w
    
    def dfs(self, u, FLOW):
        if u in self.reached: return 0
        if u == self.T: return FLOW
        G = self.G
        self.reached.add(u)
        for v, w in G[u].items():
            if w:
                f = self.dfs(v, min(FLOW, w))
                if f:
                    G[u][v] -= f
                    G[v][u] += f
                    return f
        return 0

    def max_flow(self, S, T):
        flow = 0
        self.T = T
        while True:
            self.reached = set()
            pushed = self.dfs(S, float('inf'))
            if not pushed: break
            flow += pushed
        return flow
