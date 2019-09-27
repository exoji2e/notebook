from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [defaultdict(int) for _ in range(sz)]
    
    def add_edge(self, i, j, w):
        self.G[i][j] += w
    
    def dfs(self, s, t, FLOW):
        if s in self.V: return 0
        if s == t: return FLOW
        self.V.add(s)
        for u, w in self.G[s].items():
            if w and u not in self.dead:
                F = self.dfs(u, t, min(FLOW, w))
                if F:
                    self.G[s][u] -= F
                    self.G[u][s] += F
                    return F
        self.dead.add(s)
        return 0

    def max_flow(self, s, t):
        flow = 0
        self.dead = set()
        while True:
            pushed = self.bfs(s, t)
            if not pushed: break
            flow += pushed
        return flow
