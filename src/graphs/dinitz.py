from collections import defaultdict
from misc.bootstrap import bootstrap
class Dinitz:
    def __init__(self, sz, INF=10**10):
        self.G = [defaultdict(int) for _ in range(sz)]
        self.sz = sz
        self.INF = INF

    def add_edge(self, i, j, w):
        self.G[i][j] += w

    def bfs(self, s, t):
        level = [0]*self.sz
        q = [s]
        level[s] = 1
        while q:
            q2 = []
            for u in q:
                for v, w in self.G[u].items():
                    if w and level[v] == 0:
                        level[v] = level[u] + 1
                        q2.append(v)
            q = q2
        self.level = level
        return level[t] != 0

    @bootstrap
    def dfs(self, s, t, FLOW):
        if s in self.dead: yield 0
        if s == t: yield FLOW

        for idx in range(self.pos[s], len(self.adj[s])):
            u = self.adj[s][idx]
            w = self.G[s][u]
            F = yield self.dfs(u, t, min(FLOW, w))
            if F:
                self.G[s][u] -= F
                self.G[u][s] += F
                if self.G[s][u] == 0:
                    self.pos[s] = idx+1
                    if idx + 1 == len(self.adj[s]):
                        self.dead.add(s)
                yield F
            self.pos[s] = idx+1
        self.dead.add(s)
        yield 0

    def setup_after_bfs(self):
        self.adj = []
        for u in range(self.sz):
            arr = []
            for v, w in self.G[u].items():
                if w and self.level[u] + 1 == self.level[v]:
                    arr.append(v)
            self.adj.append(arr)
        self.pos = [0]*self.sz
        self.dead = set()
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.setup_after_bfs()
            while True:
                pushed = self.dfs(s, t, self.INF)
                if not pushed: break
                flow += pushed
        return flow
