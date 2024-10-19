from misc.bootstrap import bootstrap
class Dinitz:
    def __init__(self, sz):
        self.adj = [[] for _ in range(sz)]
        self.sz = sz
        self.INF = 10**18
        # if graph has edges with only small capacities, set to 1
        self.push_start_limit = 2**30
        self.tracked = []
        self.dead = [False]*sz
        self.seen = [False]*sz

    def add_edge(self, i, j, cap, rCap=0):
        self.adj[i].append([j, len(self.adj[j]), cap, 0])
        self.adj[j].append([i, len(self.adj[i])-1, rCap, 0])

    def bfs(self, s, t, MIN):
        level = [0]*self.sz
        q = [s]
        level[s] = 1
        while q:
            q2 = []
            for u in q:
                for v, _, w, used in self.adj[u]:
                    cap = w - used
                    if cap >= MIN and level[v] == 0:
                        level[v] = level[u] + 1
                        q2.append(v)
            q = q2
        self.level = level
        return level[t] != 0

    @bootstrap
    def dfs(self, s, t, FLOW):
        if self.seen[s]: yield 0
        if self.dead[s]: yield 0
        if s == t: yield FLOW
        self.seen[s] = True
        self.tracked.append(s)
        L = self.level[s]
        for e in self.adj[s]:
            u, bId, w, used = e
            cap = w - used
            if self.dead[u]: continue
            if cap > 0 and L+1==self.level[u]:
                F = yield self.dfs(u, t, min(FLOW, cap))
                if F:
                    e[3] += F
                    self.adj[u][bId][3] -= F
                    yield F
        self.dead[s] = True
        yield 0

    def resetV(self):
        for v in self.tracked:
            self.seen[v] = False
        self.tracked = []

    def max_flow(self, s, t):
        flow = 0
        min_edge_cap = self.push_start_limit
        while min_edge_cap > 0:
            while self.bfs(s, t, min_edge_cap):
                self.dead = [False]*self.sz
                while True:
                    self.resetV()
                    pushed = self.dfs(s, t, self.INF)
                    if not pushed: break
                    flow += pushed
            min_edge_cap = min_edge_cap // 2
        return flow