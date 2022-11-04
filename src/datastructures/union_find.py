class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.sz = [1]*N
    def find(self, i):
        path = []
        while i != self.parent[i]:
            path.append(i)
            i = self.parent[i]
        for u in path: self.parent[u] = i
        return i
    def union(self, u, v):
        uR, vR = map(self.find, (u, v))
        if uR == vR: return False
        if self.sz[uR] < self.sz[vR]:
            self.parent[uR] = vR
            self.sz[vR] += self.sz[uR]
        else:
            self.parent[vR] = uR
            self.sz[uR] += self.sz[vR]
        return True