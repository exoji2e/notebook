from heapq import heappop as pop, heappush as push
# adj: adj-list where edges are tuples (node_id, weight):
# (1) --2-- (0) --3-- (2) has the adj-list:
# adj = [[(1, 2), (2, 3)], [(0, 2)], [0, 3]]
def dijk(adj, S, T):
    N = len(adj)
    INF = 10**18
    dist = [INF]*N
    pq = []
    def add(i, dst):
        if dst < dist[i]:
            dist[i] = dst
            push(pq, (dst, i))
    add(S, 0)

    while pq:
        D, i = pop(pq)
        if i == T: return D
        if D != dist[i]: continue
        for j, w in adj[i]:
            add(j, D + w)
    
    return dist[T]
